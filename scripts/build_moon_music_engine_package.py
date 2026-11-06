#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Build or check the stable, dependency-free Moon Music Engine portable."""
from __future__ import annotations
import argparse
import io
import zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "modules" / "moon-music-engine"
DEST = ROOT / "downloads" / "moon-music-engine.zip"

def archive_bytes():
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_STORED) as archive:
        for path in sorted(MODULE.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            relative = path.relative_to(MODULE).as_posix()
            info = zipfile.ZipInfo(f"moon-music-engine/{relative}", (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_STORED)
    return out.getvalue()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = archive_bytes()
    if args.check:
        if not DEST.is_file() or DEST.read_bytes() != expected:
            raise SystemExit("Missing or stale Moon Music Engine ZIP")
        print("OK Moon Music Engine ZIP")
    else:
        DEST.parent.mkdir(parents=True, exist_ok=True)
        DEST.write_bytes(expected)
        print(f"built {DEST.relative_to(ROOT)} ({len(expected)} bytes)")
if __name__ == "__main__":
    main()
