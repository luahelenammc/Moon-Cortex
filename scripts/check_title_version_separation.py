#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Guard active Moon Cortex titles against release-marker coupling."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_MARKER_RE = re.compile(
    r"(?i)(?<![A-Za-z])(?:v\d+(?:\.\d+)*|\d+\.\d+(?:\.\d+)*(?:-[a-z0-9.-]+)?|(?:alpha|beta|rc)\d*)(?![A-Za-z])"
)
H1_RE = re.compile(r"^\s*#\s+(?!#)(.*?)\s*$", re.MULTILINE)
VERSION_FIELD_RE = re.compile(r"(?im)^\*\*Version:\*\*\s*`?[^`\s]+`?")


def contains_version_marker(value: str) -> bool:
    return bool(VERSION_MARKER_RE.search(value))


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


def validation_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
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
