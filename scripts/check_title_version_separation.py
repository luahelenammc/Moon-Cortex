#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Guard active Moon Cortex titles against release-marker coupling."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
VERSION_MARKER_RE = re.compile(
    r"(?i)(?<![A-Za-z])(?:v\d+(?:\.\d+)*|\d+\.\d+(?:\.\d+)*(?:-[a-z0-9.-]+)?|(?:alpha|beta|rc)\d*)(?![A-Za-z])"
)
PATH_VERSION_MARKER_RE = re.compile(
    r"(?i)(?<![A-Za-z0-9])(?:v\d+(?:[._]\d+)*|\d+(?:[._]\d+)+(?:-[a-z0-9][a-z0-9.-]*)?)(?![A-Za-z0-9])"
)
H1_RE = re.compile(r"^\s*#\s+(?!#)(.*?)\s*$", re.MULTILINE)
VERSION_FIELD_RE = re.compile(r"(?im)^\*\*Version:\*\*\s*`?[^`\s]+`?")
CANONICAL_ENTRY_RE = re.compile(
    r"(?im)^\s*-\s*\*\*Canonical entry:\*\*\s*\[[^\]]+\]\(([^)]+)\)"
)
TRANSPORT_SURFACE_RE = re.compile(
    r"(?im)^\s*-\s*\*\*Transport surface:\*\*\s*\[[^\]]+\]\(([^)]+)\)"
)

# A current version-bearing route is exceptional and needs a reason. The
# current repository has no such compatibility/schema route.
VERSIONED_CURRENT_PATH_EXCEPTIONS: dict[str, str] = {}


def contains_version_marker(value: str) -> bool:
    return bool(VERSION_MARKER_RE.search(value))


def contains_version_marker_in_path(value: str) -> bool:
    """Detect release markers in a live route, including parent directories."""

    return bool(PATH_VERSION_MARKER_RE.search(value))


def first_h1(markdown: str) -> str | None:
    match = H1_RE.search(markdown)
    return match.group(1).strip() if match else None


def normalize_heading(value: str) -> str:
    value = re.sub(r"[*_`~]", "", value)
    value = re.sub(r"^[^\w]+(?=[A-Za-z])", "", value)
    return re.sub(r"\s+", " ", value).strip()


def governed_files(root: Path = ROOT) -> list[Path]:
    files = [root / "README.md"]
    for module in sorted((root / "modules").iterdir()):
        if not module.is_dir():
            continue
        files.extend(sorted(module.glob("*BOOTSTRAP*.md")))
        files.extend(sorted(module.glob("*NAVIGATOR*.md")))
    return files


def current_module_path_errors(root: Path = ROOT) -> list[str]:
    """Check current module entry and package routes named by each module README.

    Moon Cortex has no machine-readable capability registry; the active
    modules' READMEs are the repository's current route map.
    """

    errors: list[str] = []
    modules = root / "modules"
    if not modules.is_dir():
        return errors

    root_resolved = root.resolve()
    for module_readme in sorted(modules.glob("*/README.md")):
        content = module_readme.read_text(encoding="utf-8")
        module = module_readme.parent.name
        for coordinate, pattern in (
            ("canonical entry", CANONICAL_ENTRY_RE),
            ("transport package", TRANSPORT_SURFACE_RE),
        ):
            targets = sorted(set(pattern.findall(content)))
            if not targets:
                errors.append(f"{module_readme.relative_to(root)}: missing current {coordinate} route")
                continue
            for target in targets:
                parsed = urlsplit(target.strip())
                if parsed.scheme or parsed.netloc or not parsed.path:
                    errors.append(
                        f"{module_readme.relative_to(root)}: current {coordinate} must use a repository path"
                    )
                    continue
                resolved = (module_readme.parent / parsed.path).resolve()
                try:
                    relative = resolved.relative_to(root_resolved).as_posix()
                except ValueError:
                    errors.append(
                        f"{module_readme.relative_to(root)}: current {coordinate} escapes the repository"
                    )
                    continue
                if not resolved.is_file():
                    errors.append(
                        f"{module_readme.relative_to(root)}: missing current {coordinate}: {relative}"
                    )
                if (
                    contains_version_marker_in_path(relative)
                    and not VERSIONED_CURRENT_PATH_EXCEPTIONS.get(relative, "").strip()
                ):
                    errors.append(
                        f"{module}: current {coordinate} contains a version marker: {relative!r}; "
                        "keep release state in metadata or document a semantic exception"
                    )
    return errors


def validation_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    errors.extend(current_module_path_errors(root))
    files = governed_files(root)
    for path in files:
        if not path.is_file():
            errors.append(f"missing governed file: {path.relative_to(root)}")
            continue
        relative = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8")
        heading = first_h1(content)
        if heading is None:
            errors.append(f"{relative}: no level-one heading")
            continue
        if contains_version_marker(heading):
            errors.append(f"{relative}: heading contains a version marker: {heading!r}")
        if path.parent != root and not VERSION_FIELD_RE.search(content):
            errors.append(f"{relative}: canonical module entry has no dedicated Version field")

    return errors


def main() -> None:
    errors = validation_errors()
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise SystemExit(f"title/version separation validation failed:\n{joined}")
    print(f"validated title/version separation across {len(governed_files())} active Cortex surfaces")


if __name__ == "__main__":
    main()
