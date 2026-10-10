#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Validate Moon Image Cortex source, links, claims, and deterministic ZIP."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "modules" / "moon-image-cortex"
PACKAGE = ROOT / "downloads" / "moon-image-cortex.zip"
PACKAGE_PREFIX = "moon-image-cortex/"
MANIFEST_NAME = "PACKAGE_MANIFEST.sha256"
EXPECTED = {
    "README.md",
    "VISUAL_DIRECTOR.md",
    "CHANGELOG.md",
    "docs/DOMAIN_AND_CAPABILITY_MAP.md",
    "docs/VISUAL_STATE_AND_COMPILATION.md",
    "docs/SPECIALIST_ENGINES.md",
    "docs/VISUAL_QA_AND_REPAIR.md",
    "docs/IDENTITY_CONSENT_AND_BOUNDARIES.md",
    "docs/ORIGINALITY_ATTRIBUTION_AND_CLAIMS.md",
    "docs/TOOL_AND_RENDERER_CONTRACT.md",
    "docs/MOON_SOURCE_CONTEXT_BRIDGE.md",
    "docs/IMAGE_CORTEX_REALITY_TEST.md",
    "examples/PHOTO_EDIT_CONSERVATIVE.md",
    "examples/HISTORICAL_WEB_AND_SKEUO.md",
    "examples/RETROFUTURE_EDITORIAL.md",
    "examples/IDENTITY_SAFE_PORTRAIT.md",
    "examples/VISUAL_QA_FAILURES.md",
    "examples/SPECIALIST_GALLERY_SYNTHETIC.md",
    "engines/photography/ANALOGIC_PHOTO.md",
    "engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md",
    "engines/photography/VERNACULAR_SNAPSHOT_REALISM.md",
    "engines/interfaces-and-retro/WEB_RETRO_IMAGE_GEN.md",
    "engines/interfaces-and-retro/AQUA_SKEUO_ICON_FORGE.md",
    "engines/interfaces-and-retro/LIVED_IN_RETROFUTURISM.md",
    "engines/expressive-and-editorial/CHROMATIC_DREAM_LOGIC.md",
    "engines/expressive-and-editorial/SENTIMENTAL_UNCANNY.md",
    "engines/expressive-and-editorial/SUBLIME_LYRIC_STILL.md",
    "engines/expressive-and-editorial/VINTAGE_EDITORIAL_RUBBER_HOSE_POSTER.md",
    "engines/experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md",
    "components/creative-direction/OMNIALCHEMY.md",
    "components/creative-direction/WEB_AESTHETICS.md",
    "components/references-and-identity/HUMAN_CANON_FORGE.md",
    "components/image-editing/CONSERVATIVE_PHOTO_EDIT.md",
    "components/references-and-identity/REFERENCE_ABSTRACTION_GUARDRAIL.md",
    "components/references-and-identity/CONFIGURABLE_VISUAL_PROFILE.md",
    "docs/COMPONENT_INDEX.md",
    "engines/photography/regions/README.md",
    "engines/photography/regions/CUSTOM_CONTEXT.md",
    "engines/photography/regions/BRAZIL.md",
    "engines/photography/regions/UNITED_STATES.md",
    "engines/photography/regions/UNITED_KINGDOM.md",
    "engines/photography/regions/JAPAN.md",
    "engines/photography/regions/INDIA.md",
    "engines/photography/regions/MEXICO.md",
    "engines/photography/regions/FRANCE.md",
    "engines/photography/regions/GERMANY.md",
}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
TEST_INTENTS = [
    "Fragmentary abstract concept",
    "Contemporary documentary photo",
    "Brazilian 1990s family album",
    "US 2000s disposable camera",
    "2000s XP web portal",
    "Aqua-era fictional app icon",
    "1970s future city poster",
    "Non-gothic chromatic image",
    "Late Y2K uncanny bedroom",
    "Vertical atmospheric lyric-style still",
    "Vintage advocacy poster",
    "Game screenshot to embodied scene",
    "Consenting subject identity profile",
    "Real subject without reference",
    "Reference image requests style-only",
    "Simple photo edit",
    "Waxy or tiled result",
    "Infographic on shared temperature axis",
    "No renderer available",
    "Third-party copyrighted or logo reference",
    "Watermark causal diagnosis",
    "Repeated similar outputs",
]
SPECIALISTS = [
    "Analogic Photo",
    "Contextual Nostalgic Camera",
    "Vernacular Snapshot Realism",
    "Web Retro Image Gen",
    "Aqua-Skeuo Icon Forge",
    "Lived-In Retrofuturism",
    "Chromatic Dream Logic",
    "Sentimental Uncanny",
    "Sublime Lyric Still",
    "Vintage Editorial Rubber Hose Poster",
    "Pixel-World Camera Translation",
]


def module_files() -> dict[str, bytes]:
    return {
        path.relative_to(MODULE).as_posix(): path.read_bytes()
        for path in MODULE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }


def slugify_heading(value: str) -> str:
    value = re.sub(r"[*_~]", "", value).lower()
    value = re.sub(r"[^\w -]", "", value)
    return re.sub(r"\s+", "-", value.strip())


def local_links_errors(path: Path, content: str) -> list[str]:
    errors: list[str] = []
    root = ROOT.resolve()
    for raw in LINK_RE.findall(content):
        target = raw.strip().split()[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith("//"):
            continue
        target_path = path if not parsed.path else (path.parent / unquote(parsed.path)).resolve()
        try:
            target_path.relative_to(root)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not target_path.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")
            continue
        if parsed.fragment and target_path.is_file() and target_path.suffix.lower() == ".md":
            headings = re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", target_path.read_text(encoding="utf-8"))
            anchors = {slugify_heading(heading) for heading in headings}
            if unquote(parsed.fragment).lower() not in anchors:
                errors.append(f"{path.relative_to(ROOT)}: missing anchor in {target_path.relative_to(ROOT)}: #{parsed.fragment}")
    return errors


def validation_errors() -> list[str]:
    errors: list[str] = []
    if not MODULE.is_dir():
        return ["missing moon-image-cortex module directory"]

    files = module_files()
    actual = set(files)
    if actual != EXPECTED:
        errors.append(f"module file set mismatch: missing={sorted(EXPECTED - actual)}, unexpected={sorted(actual - EXPECTED)}")

    readme_path = MODULE / "README.md"
    entry_path = MODULE / "VISUAL_DIRECTOR.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        if "# Moon Image Cortex" not in readme.splitlines():
            errors.append("module README has an unexpected title")
        if "- **Version:** 0.1.0-pre.3" not in readme:
            errors.append("module README is missing version 0.1.0-pre.3")
        if "- **Canonical entry:** [Visual Director](VISUAL_DIRECTOR.md#first-use)" not in readme:
            errors.append("module README does not route to the canonical entry")
        if "- **Transport surface:** [Complete module package](../../downloads/moon-image-cortex.zip)" not in readme:
            errors.append("module README does not route to the complete package")
    if entry_path.is_file():
        entry = entry_path.read_text(encoding="utf-8")
        if not re.search(r"(?im)^# Visual Director\s*$", entry):
            errors.append("canonical entry has an unexpected title")
        if "**Version:** 0.1.0-pre.3" not in entry:
            errors.append("canonical entry is missing version 0.1.0-pre.3")
        if "## First use" not in entry:
            errors.append("canonical entry is missing embedded First Use")
        for field in ("visual_brief", "visual_state", "direction_sheet", "prompt_for_renderer", "edit_instruction", "identity_profile", "QA_report", "generated_image"):
            if field not in entry:
                errors.append(f"canonical entry is missing output contract field {field}")
        if "not rendered" not in entry.lower():
            errors.append("canonical entry does not distinguish renderer-absent output")

    specialist_path = MODULE / "docs" / "SPECIALIST_ENGINES.md"
    if specialist_path.is_file():
        specialist_text = specialist_path.read_text(encoding="utf-8")
        for family in SPECIALISTS:
            if family not in specialist_text:
                errors.append(f"specialist registry is missing {family}")
    reality_path = MODULE / "docs" / "IMAGE_CORTEX_REALITY_TEST.md"
    if reality_path.is_file():
        reality_text = reality_path.read_text(encoding="utf-8")
        for intent in TEST_INTENTS:
            if intent not in reality_text:
                errors.append(f"acceptance matrix is missing: {intent}")
        row_count = sum(
            1 for line in reality_text.splitlines()
            if line.startswith("| ") and not line.startswith("| Test intent") and not line.startswith("|---")
        )
        if row_count != len(TEST_INTENTS):
            errors.append(f"acceptance matrix has {row_count} data rows; expected {len(TEST_INTENTS)}")

    for relative, raw in files.items():
        path = MODULE / relative
        if path.suffix.lower() == ".md":
            content = raw.decode("utf-8")
            if "SPDX-License-Identifier: CC-BY-4.0" not in content:
                errors.append(f"{relative}: missing CC-BY-4.0 SPDX header")
            if "MOON-CORTEX-PUBLIC-STAMP" not in content:
                errors.append(f"{relative}: missing public identity stamp")
            errors.extend(local_links_errors(path, content))
            if "![" in content:
                errors.append(f"{relative}: image embeds are not allowed in the text-only package")

    if PACKAGE.is_file():
        try:
            from build_moon_image_cortex_package import archive_bytes, manifest_bytes

            expected_archive = archive_bytes()
            if PACKAGE.read_bytes() != expected_archive:
                errors.append("ZIP differs from deterministic build output")
            with zipfile.ZipFile(PACKAGE) as archive:
                expected_names = {f"{PACKAGE_PREFIX}{name}" for name in EXPECTED | {MANIFEST_NAME}}
                actual_names = set(archive.namelist())
                if actual_names != expected_names:
                    errors.append(f"ZIP file set mismatch: missing={sorted(expected_names - actual_names)}, unexpected={sorted(actual_names - expected_names)}")
                for relative, raw in files.items():
                    name = f"{PACKAGE_PREFIX}{relative}"
                    if name in actual_names and archive.read(name) != raw:
                        errors.append(f"ZIP content differs from source: {relative}")
                manifest_name = f"{PACKAGE_PREFIX}{MANIFEST_NAME}"
                if manifest_name in actual_names and archive.read(manifest_name) != manifest_bytes(files):
                    errors.append("ZIP SHA-256 manifest differs from source files")
        except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
            errors.append(f"cannot validate ZIP: {exc}")
    else:
        errors.append(f"missing package: {PACKAGE.relative_to(ROOT)}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors), file=sys.stderr)
        return 1
    print(f"Moon Image Cortex validation passed: {len(EXPECTED)} source files, 11 specialist routes, 22 synthetic intents, deterministic ZIP.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
