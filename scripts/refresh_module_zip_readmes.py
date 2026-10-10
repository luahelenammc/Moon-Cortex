#!/usr/bin/env python3
"""Keep fallback ZIP README copies in sync without changing module content or ZIP layout."""
from __future__ import annotations

from pathlib import Path
from tempfile import NamedTemporaryFile
import os
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MODULES = ("financial-living-system", "social-support-navigation-system")

def refresh(slug: str) -> None:
    archive_path = ROOT / "downloads" / f"{slug}.zip"
    source = ROOT / "modules" / slug / "README.md"
    target = f"{slug}/README.md"
    with zipfile.ZipFile(archive_path, "r") as original:
        records = [(info, original.read(info.filename)) for info in original.infolist()]
    matches = [info.filename for info, _ in records if info.filename == "README.md" or info.filename.endswith("/README.md")]
    if len(matches) != 1:
        raise SystemExit(f"expected one root README in {archive_path}, found={matches}; members={[x.filename for x, _ in records][:20]}")
    target = matches[0]
    with NamedTemporaryFile(dir=archive_path.parent, suffix=".zip", delete=False) as tmp:
        path = Path(tmp.name)
    try:
        with zipfile.ZipFile(path, "w") as dest:
            for info, data in records:
                dest.writestr(info, source.read_bytes() if info.filename == target else data)
        os.replace(path, archive_path)
    finally:
        path.unlink(missing_ok=True)
    with zipfile.ZipFile(archive_path, "r") as check:
        assert check.read(target) == source.read_bytes()
    print(f"synchronized {archive_path.name}: {target}")

if __name__ == "__main__":
    for module in MODULES:
        refresh(module)
