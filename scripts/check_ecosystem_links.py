#!/usr/bin/env python3
"""Validate Moon Cortex's non-sovereign public registry and route contracts."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CURRENT_REPO = "luahelenammc/Moon-Cortex"
VALID_STATUSES = {"active_public", "unpublished_pending_verification"}
VALID_BEHAVIORS = {
    "human_readable_pointer",
    "functional_binary_mirror",
    "exact_byte_web_mirror",
    "static_site_301_or_308_if_supported",
    "frozen_archive",
    "git_history_only",
    "not_changed",
}
VALID_ROUTE_RESULTS = {"pass", "fail", "unchecked", "external_unverified", "blocked"}
REQUIRED_PROJECT_FIELDS = {
    "id", "name", "class", "canonical_repo", "canonical_entry", "summary",
    "status", "status_verified_at", "distribution", "maintainer", "owned_function",
    "imports", "exports", "privacy_boundary", "legacy_routes", "validation_ref",
}
REQUIRED_ROUTE_FIELDS = {
    "legacy_url", "legacy_repo", "legacy_path", "target_project_id", "target_canonical_url",
    "route_class", "compatibility_behavior", "owner_repo", "first_known_use", "old_status",
    "test_method", "last_checked", "result", "recovery_ref", "policy_source",
}


def load_json(path: Path) -> tuple[Any | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"{path.relative_to(ROOT)}: {exc}"]


def github_repo_from_url(value: str | None) -> str | None:
    if not isinstance(value, str):
        return None
    parsed = urllib.parse.urlparse(value)
    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
        return None
    parts = [urllib.parse.unquote(part) for part in parsed.path.strip("/").split("/") if part]
    if len(parts) < 2:
        return None
    return f"{parts[0]}/{parts[1]}"


def github_file_path(value: str | None, repo: str) -> tuple[str | None, str | None]:
    """Return (path, fragment) for a GitHub blob/tree URL in the given repo."""
    if not isinstance(value, str):
        return None, None
    parsed = urllib.parse.urlparse(value)
    if github_repo_from_url(value) != repo:
        return None, None
    parts = [urllib.parse.unquote(part) for part in parsed.path.strip("/").split("/") if part]
    if len(parts) >= 5 and parts[2] in {"blob", "tree", "raw"}:
        return "/".join(parts[4:]), urllib.parse.unquote(parsed.fragment) or None
    return None, urllib.parse.unquote(parsed.fragment) or None


def _heading_slug(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.strip().casefold()
    kept = []
    for char in text:
        category = unicodedata.category(char)
        if char.isspace():
            kept.append("-")
        elif char == "-" or category[0] in {"L", "N"}:
            kept.append(char)
    slug = re.sub(r"-+", "-", "".join(kept)).strip("-")
    return slug


def markdown_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return anchors
    for match in re.finditer(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", content):
        base = _heading_slug(match.group(1))
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    for match in re.finditer(r"\bid=[\"']([^\"']+)[\"']|\bname=[\"']([^\"']+)[\"']", content, re.I):
        anchors.add(match.group(1) or match.group(2))
    return anchors


def _local_path_from_link(source: Path, href: str, root: Path) -> tuple[Path | None, str | None]:
    parsed = urllib.parse.urlparse(href)
    if parsed.scheme or parsed.netloc:
        return None, None
    fragment = urllib.parse.unquote(parsed.fragment) or None
    path_text = urllib.parse.unquote(parsed.path)
    target = (source.parent / path_text).resolve() if path_text else source.resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return None, fragment
    return target, fragment


def validate_markdown_links(root: Path, paths: list[str]) -> list[str]:
    errors: list[str] = []
    link_re = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+['\"][^)]*['\"])??\)")
    for rel in paths:
        source = root / rel
        if not source.is_file():
            errors.append(f"Markdown link scan source missing: {rel}")
            continue
        text = source.read_text(encoding="utf-8")
        for match in link_re.finditer(text):
            href = match.group(1).strip("<>")
            parsed = urllib.parse.urlparse(href)
            if parsed.scheme or parsed.netloc:
                continue
            target, fragment = _local_path_from_link(source, href, root)
            if target is None:
                errors.append(f"{rel}: local link escapes repository: {href}")
                continue
            if not target.exists():
                errors.append(f"{rel}: missing local target: {href}")
                continue
            if fragment and target.is_file() and target.suffix.lower() in {".md", ".markdown"}:
                if fragment not in markdown_anchors(target):
                    errors.append(f"{rel}: missing Markdown fragment {fragment!r} in {target.relative_to(root)}")
    return errors


def validate_ecosystem(data: Any, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or not isinstance(data.get("projects"), list):
        return ["registry/ecosystem.json must contain a projects array"]
    projects = data["projects"]
    ids: dict[str, dict[str, Any]] = {}
    for index, project in enumerate(projects):
        if not isinstance(project, dict):
            errors.append(f"projects[{index}] must be an object")
            continue
        missing = REQUIRED_PROJECT_FIELDS - project.keys()
        if missing:
            errors.append(f"projects[{index}] missing fields: {', '.join(sorted(missing))}")
        ident = project.get("id")
        if not isinstance(ident, str) or not ident:
            errors.append(f"projects[{index}].id must be a non-empty string")
        elif ident in ids:
            errors.append(f"duplicate project id: {ident}")
        else:
            ids[ident] = project
        status = project.get("status")
        if status not in VALID_STATUSES:
            errors.append(f"{ident or index}: unsupported status {status!r}")
        if not _is_iso_date(project.get("status_verified_at")):
            errors.append(f"{ident or index}: status_verified_at must be an ISO date")
        repo_url = project.get("canonical_repo")
        entry_url = project.get("canonical_entry")
        if status == "active_public":
            repo = github_repo_from_url(repo_url)
            if repo is None:
                errors.append(f"{ident}: active public project needs a verified HTTPS GitHub canonical_repo")
            if github_repo_from_url(entry_url) != repo or not isinstance(entry_url, str):
                errors.append(f"{ident}: canonical_entry must be a URL inside canonical_repo")
            else:
                local_path, fragment = github_file_path(entry_url, CURRENT_REPO)
                if repo == CURRENT_REPO and local_path:
                    target = root / local_path
                    if not target.is_file():
                        errors.append(f"{ident}: canonical entry path is missing: {local_path}")
                    elif fragment and fragment not in markdown_anchors(target):
                        errors.append(f"{ident}: canonical entry fragment is missing: {fragment}")
        elif status == "unpublished_pending_verification":
            if repo_url is not None or entry_url is not None:
                errors.append(f"{ident}: pending publication must have null canonical_repo and canonical_entry")
            if project.get("distribution") != []:
                errors.append(f"{ident}: pending publication cannot advertise a distribution")
        for field in ("imports", "references", "exports", "legacy_routes", "distribution"):
            if field in project and not isinstance(project[field], list):
                errors.append(f"{ident}: {field} must be an array")
    for project in projects:
        if not isinstance(project, dict):
            continue
        ident = project.get("id", "<unknown>")
        for field in ("imports", "references"):
            for target in project.get(field, []) if isinstance(project.get(field), list) else []:
                if target not in ids:
                    errors.append(f"{ident}: {field} references unknown project id {target!r}")
    required_modules = {
        "financial-living-system", "social-support-navigation-system", "probability-calibration-system",
        "moon-image-cortex", "moon-music-engine",
    }
    missing_modules = required_modules - ids.keys()
    if missing_modules:
        errors.append(f"existing Cortex module entries missing: {', '.join(sorted(missing_modules))}")
    pending = ids.get("prisma")
    if pending and pending.get("status") == "unpublished_pending_verification":
        if pending.get("canonical_repo") is not None or pending.get("canonical_entry") is not None:
            errors.append("PRISMA pending state contains a guessed or unverified URL")
    return errors


def _is_iso_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value))


def _route_target_local_check(url: str, root: Path) -> list[str]:
    path, fragment = github_file_path(url, CURRENT_REPO)
    if not path:
        return []
    target = root / path
    errors: list[str] = []
    if not target.is_file():
        errors.append(f"target path does not exist: {path}")
    elif fragment and target.suffix.lower() in {".md", ".markdown"} and fragment not in markdown_anchors(target):
        errors.append(f"target Markdown fragment does not exist: {path}#{fragment}")
    return errors


def validate_routes(data: Any, ecosystem: Any, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or not isinstance(data.get("routes"), list):
        return ["registry/legacy-routes.json must contain a routes array"]
    projects = {p.get("id"): p for p in ecosystem.get("projects", []) if isinstance(p, dict)} if isinstance(ecosystem, dict) else {}
    routes = data["routes"]
    by_url: dict[str, dict[str, Any]] = {}
    for index, route in enumerate(routes):
        if not isinstance(route, dict):
            errors.append(f"routes[{index}] must be an object")
            continue
        missing = REQUIRED_ROUTE_FIELDS - route.keys()
        if missing:
            errors.append(f"routes[{index}] missing fields: {', '.join(sorted(missing))}")
        legacy_url = route.get("legacy_url")
        if not isinstance(legacy_url, str) or not legacy_url.startswith("https://"):
            errors.append(f"routes[{index}].legacy_url must be an observed HTTPS URL")
            continue
        if legacy_url in by_url:
            errors.append(f"duplicate legacy route: {legacy_url}")
        else:
            by_url[legacy_url] = route
        behavior = route.get("compatibility_behavior")
        if behavior not in VALID_BEHAVIORS:
            errors.append(f"{legacy_url}: unsupported compatibility_behavior {behavior!r}")
        result = route.get("result")
        if result not in VALID_ROUTE_RESULTS:
            errors.append(f"{legacy_url}: unsupported result {result!r}")
        test_method = str(route.get("test_method", "")).casefold()
        last_checked = route.get("last_checked")
        if result == "pass" and ("unchecked" in test_method or "not_run" in test_method or not _is_iso_date(last_checked)):
            errors.append(f"{legacy_url}: unchecked or undated route cannot be reported as pass")
        if last_checked is not None and not _is_iso_date(last_checked):
            errors.append(f"{legacy_url}: last_checked must be an ISO date or null")
        target_project = projects.get(route.get("target_project_id"))
        if not target_project or target_project.get("status") != "active_public":
            errors.append(f"{legacy_url}: target_project_id must name a registered active public project")
        else:
            source_repo = github_repo_from_url(route.get("target_canonical_url"))
            target_repo = github_repo_from_url(target_project.get("canonical_repo"))
            if not source_repo or source_repo != target_repo:
                errors.append(f"{legacy_url}: target URL does not belong to target_project_id {route.get('target_project_id')!r}")
        observed_repo = github_repo_from_url(legacy_url)
        if observed_repo and observed_repo != route.get("legacy_repo"):
            errors.append(f"{legacy_url}: legacy_repo does not match the observed URL")
        if not isinstance(route.get("legacy_repo"), str) or not route.get("legacy_repo"):
            errors.append(f"{legacy_url}: legacy_repo must be recorded")
        legacy_path, _ = github_file_path(legacy_url, route.get("legacy_repo", "")) if observed_repo else (None, None)
        if not isinstance(route.get("legacy_path"), str) or not route.get("legacy_path"):
            errors.append(f"{legacy_url}: legacy_path must be recorded")
        elif legacy_path is not None and legacy_path != route.get("legacy_path"):
            errors.append(f"{legacy_url}: legacy_path does not match the observed GitHub URL")
        if not isinstance(route.get("policy_source"), list) or not route.get("policy_source"):
            errors.append(f"{legacy_url}: policy_source must cite at least one governing source")
        errors.extend(f"{legacy_url}: {e}" for e in _route_target_local_check(str(route.get("target_canonical_url", "")), root))
    # A chain that points back to an old route is circular even if the URLs differ by one hop.
    edges = {url: route.get("target_canonical_url") for url, route in by_url.items()}
    for start in edges:
        seen: set[str] = set()
        current: Any = start
        while current in edges:
            if current in seen:
                errors.append(f"legacy route cycle includes {start}")
                break
            seen.add(current)
            current = edges[current]
    route_urls = set(by_url)
    for project in projects.values():
        for route_id in project.get("legacy_routes", []) if isinstance(project.get("legacy_routes"), list) else []:
            if route_id not in route_urls:
                errors.append(f"{project.get('id')}: legacy_routes references unknown route {route_id!r}")
    return errors


def validate_pending_project_urls(ecosystem: Any, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if not isinstance(ecosystem, dict):
        return errors
    for project in ecosystem.get("projects", []):
        if not isinstance(project, dict) or project.get("status") != "unpublished_pending_verification":
            continue
        repo = project.get("id", "").casefold()
        if repo != "prisma":
            continue
        forbidden = re.compile(r"https?://github\.com/luahelenammc/PRISMA(?:[/#?\s)]|$)", re.I)
        for rel in ("README.md", "ARCHITECTURE.md", "ECOSYSTEM.md", "ECOSYSTEM.pt-BR.md", "registry/ecosystem.json"):
            path = root / rel
            if path.is_file() and forbidden.search(path.read_text(encoding="utf-8")):
                errors.append(f"PRISMA is pending but {rel} publishes an unverified GitHub URL")
    return errors


def validate_packages(data: Any, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or not isinstance(data.get("packages"), list):
        return ["registry/distribution-manifest.json must contain a packages array"]
    seen: set[str] = set()
    for package in data["packages"]:
        if not isinstance(package, dict):
            errors.append("distribution package entries must be objects")
            continue
        rel = package.get("path")
        if not isinstance(rel, str) or rel in seen:
            errors.append(f"duplicate or invalid package path: {rel!r}")
            continue
        seen.add(rel)
        path = (root / rel).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError:
            errors.append(f"package path escapes repository: {rel}")
            continue
        if not path.is_file():
            errors.append(f"package file is missing: {rel}")
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != package.get("sha256"):
            errors.append(f"package SHA-256 mismatch: {rel}")
        if path.stat().st_size != package.get("size_bytes"):
            errors.append(f"package size mismatch: {rel}")
        try:
            with zipfile.ZipFile(path) as archive:
                bad_member = archive.testzip()
                if bad_member:
                    errors.append(f"corrupt ZIP member in {rel}: {bad_member}")
        except (OSError, zipfile.BadZipFile) as exc:
            errors.append(f"invalid ZIP {rel}: {exc}")
    return errors


def validate_distributions(ecosystem: Any, packages: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(ecosystem, dict) or not isinstance(packages, dict):
        return errors
    recorded = {p.get("path"): p for p in packages.get("packages", []) if isinstance(p, dict)}
    for project in ecosystem.get("projects", []):
        if not isinstance(project, dict):
            continue
        for item in project.get("distribution", []) if isinstance(project.get("distribution"), list) else []:
            if not isinstance(item, dict) or item.get("type") not in {"zip", "skill_zip"}:
                continue
            rel = item.get("path")
            package = recorded.get(rel)
            if not package:
                errors.append(f"{project.get('id')}: distribution path is absent from ZIP manifest: {rel}")
                continue
            if item.get("sha256") != package.get("sha256") or item.get("size_bytes") != package.get("size_bytes"):
                errors.append(f"{project.get('id')}: distribution metadata differs from ZIP manifest: {rel}")
    return errors


def classify_http_status(status: int) -> str:
    if status in {404, 410}:
        return "FAIL"
    if status in {403, 429} or status >= 500:
        return "UNVERIFIED"
    if 200 <= status < 400:
        return "PASS"
    return "UNVERIFIED"


class _RedirectRecorder(urllib.request.HTTPRedirectHandler):
    def __init__(self) -> None:
        super().__init__()
        self.visited: list[str] = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.visited.append(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _probe_url(url: str, expected_type: str | None = None) -> dict[str, Any]:
    redirects = _RedirectRecorder()
    opener = urllib.request.build_opener(redirects)
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Moon-Cortex-link-check/1.0"})
    try:
        with opener.open(request, timeout=8) as response:
            status = response.status
            content_type = response.headers.get_content_type()
            result = classify_http_status(status)
            if result == "PASS" and expected_type == "html" and content_type != "text/html":
                result = "FAIL"
            if result == "PASS" and expected_type == "zip" and content_type not in {"application/zip", "application/octet-stream", "application/x-zip-compressed"}:
                result = "FAIL"
            return {
                "url": url, "status": status, "final_url": response.geturl(),
                "redirects": redirects.visited, "content_type": content_type,
                "expected_content_type": expected_type, "result": result,
            }
    except urllib.error.HTTPError as exc:
        return {
            "url": url, "status": exc.code, "final_url": exc.geturl(),
            "redirects": redirects.visited, "content_type": exc.headers.get_content_type() if exc.headers else None,
            "expected_content_type": expected_type, "result": classify_http_status(exc.code),
        }
    except Exception as exc:  # Network and proxy failures do not prove the target is broken.
        return {"url": url, "status": "unchecked", "error": str(exc), "redirects": redirects.visited, "expected_content_type": expected_type, "result": "UNVERIFIED"}


def _external_markdown_urls(root: Path) -> set[str]:
    link_re = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+['\"][^)]*['\"])??\)")
    paths = ["README.md", "ARCHITECTURE.md", "ECOSYSTEM.md", "ECOSYSTEM.pt-BR.md", "docs/ECOSYSTEM_GOVERNANCE.md", "docs/CROSS_REPOSITORY_COMPATIBILITY.md"]
    found: set[str] = set()
    for rel in paths:
        path = root / rel
        if not path.is_file():
            continue
        for match in link_re.finditer(path.read_text(encoding="utf-8")):
            href = match.group(1).strip("<>")
            parsed = urllib.parse.urlparse(href)
            if parsed.scheme in {"http", "https"} and parsed.netloc:
                found.add(href)
    return found


def online_checks(ecosystem: Any, packages: Any, routes: Any, root: Path = ROOT, current_ref: str | None = None) -> list[dict[str, Any]]:
    urls: dict[str, str | None] = {}
    for project in ecosystem.get("projects", []):
        if project.get("status") != "active_public":
            continue
        for field in ("canonical_repo", "canonical_entry"):
            value = project.get(field)
            if not isinstance(value, str):
                continue
            if current_ref and field == "canonical_entry" and github_repo_from_url(value) == CURRENT_REPO:
                parsed = urllib.parse.urlparse(value)
                parts = parsed.path.split("/")
                if len(parts) > 4 and parts[3] == "blob" and parts[4] == "main":
                    parts[4] = current_ref
                    value = urllib.parse.urlunparse(parsed._replace(path="/".join(parts)))
            urls[value] = "html" if field == "canonical_entry" else "html"
    for value in _external_markdown_urls(root):
        urls.setdefault(value, None)
    if isinstance(routes, dict):
        for route in routes.get("routes", []):
            if not isinstance(route, dict):
                continue
            behavior = route.get("compatibility_behavior")
            route_class = route.get("route_class")
            expected = "zip" if behavior == "functional_binary_mirror" or route_class == "binary" else ("html" if route_class in {"markdown", "site"} else None)
            for field in ("legacy_url", "target_canonical_url"):
                value = route.get(field)
                if isinstance(value, str):
                    urls.setdefault(value, expected)
    branch_ref = current_ref or "main"
    if isinstance(packages, dict):
        for package in packages.get("packages", []):
            if isinstance(package, dict) and isinstance(package.get("path"), str):
                quoted = urllib.parse.quote(package["path"], safe="/")
                raw_url = f"https://github.com/{CURRENT_REPO}/raw/refs/heads/{branch_ref}/{quoted}"
                urls[raw_url] = "zip"
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(_probe_url, url, expected) for url, expected in sorted(urls.items())]
        return [future.result() for future in futures]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="probe active public canonical URLs")
    parser.add_argument("--strict-online", action="store_true", help="fail if a live URL is unverified; implies --online")
    parser.add_argument("--ref", help="probe this branch for URLs inside Moon-Cortex; useful before merge")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (defaults to this checkout)")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    ecosystem, e = load_json(root / "registry/ecosystem.json"); errors.extend(e)
    routes, e = load_json(root / "registry/legacy-routes.json"); errors.extend(e)
    packages, e = load_json(root / "registry/distribution-manifest.json"); errors.extend(e)
    if ecosystem is not None:
        errors.extend(validate_ecosystem(ecosystem, root))
        errors.extend(validate_pending_project_urls(ecosystem, root))
    if routes is not None and ecosystem is not None:
        errors.extend(validate_routes(routes, ecosystem, root))
    if packages is not None:
        errors.extend(validate_packages(packages, root))
    if ecosystem is not None and packages is not None:
        errors.extend(validate_distributions(ecosystem, packages))
    link_sources = ["README.md", "ARCHITECTURE.md", "ECOSYSTEM.md", "ECOSYSTEM.pt-BR.md", "docs/ECOSYSTEM_GOVERNANCE.md", "docs/CROSS_REPOSITORY_COMPATIBILITY.md"]
    errors.extend(validate_markdown_links(root, link_sources))
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: ecosystem registry, pending-route discipline, legacy-route schema, local links and ZIP/SHA manifest")
    if args.online or args.strict_online:
        results = online_checks(ecosystem or {}, packages or {}, routes or {}, root, args.ref)
        for result in results:
            status = result.get("status")
            detail = f"HTTP {status}" if isinstance(status, int) else str(status)
            if result.get("final_url") and result["final_url"] != result["url"]:
                detail += f" -> {result['final_url']}"
            if result.get("content_type"):
                detail += f"; Content-Type {result['content_type']}"
            if result.get("redirects"):
                detail += f"; redirects {len(result['redirects'])}"
            print(f"{result['result']}: {result['url']} ({detail})")
        failed = sum(r["result"] == "FAIL" for r in results)
        unverified = sum(r["result"] == "UNVERIFIED" for r in results)
        print(f"Live URL summary: {len(results)} checked, {len(results)-failed-unverified} passing, {failed} broken, {unverified} unverified")
        if failed or (args.strict_online and unverified):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
