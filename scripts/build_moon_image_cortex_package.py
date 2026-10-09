#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Build the stable, deterministic Moon Image Cortex ZIP."""

from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_moon_image_cortex_package import EXPECTED, MODULE, PACKAGE, PACKAGE_PREFIX, MANIFEST_NAME  # noqa: E402


def source_files() -> dict[str, bytes]:
    actual = {
        path.relative_to(MODULE).as_posix(): path.read_bytes()
        for path in MODULE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }
    if set(actual) != EXPECTED:
        missing = sorted(EXPECTED - set(actual))
        unexpected = sorted(set(actual) - EXPECTED)
        raise SystemExit(f"refusing to package unexpected module tree: missing={missing}, unexpected={unexpected}")
    return actual


def manifest_bytes(files: dict[str, bytes]) -> bytes:
    lines = [
        f"{hashlib.sha256(files[name]).hexdigest()}  {name}"
        for name in sorted(files)
    ]
    return ("\n".join(lines) + "\n").encode("utf-8")


def archive_bytes() -> bytes:
    files = source_files()
    files[MANIFEST_NAME] = manifest_bytes(files)
    import io

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in sorted(files):
            info = zipfile.ZipInfo(f"{PACKAGE_PREFIX}{relative}", date_time=(2026, 10, 8, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[relative], compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buffer.getvalue()


def build() -> None:
    PACKAGE.parent.mkdir(parents=True, exist_ok=True)
    PACKAGE.write_bytes(archive_bytes())
    print(f"built {PACKAGE.relative_to(ROOT)} with {len(EXPECTED)} source files and a SHA-256 manifest")


if __name__ == "__main__":
    build()
