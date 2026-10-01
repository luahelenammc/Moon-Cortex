#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Build the stable, deterministic Probability Calibration System ZIP."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_probability_calibration_package import EXPECTED, MODULE, PACKAGE, PACKAGE_PREFIX  # noqa: E402


def build() -> None:
    actual = {
        path.relative_to(MODULE).as_posix()
        for path in MODULE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }
    if actual != EXPECTED:
        missing, unexpected = sorted(EXPECTED - actual), sorted(actual - EXPECTED)
        raise SystemExit(f"refusing to package an unexpected module tree: missing={missing}, unexpected={unexpected}")

    PACKAGE.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(PACKAGE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in sorted(EXPECTED):
            info = zipfile.ZipInfo(f"{PACKAGE_PREFIX}{relative}", date_time=(2026, 10, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (MODULE / relative).read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    print(f"built {PACKAGE.relative_to(ROOT)} with {len(EXPECTED)} source files")


if __name__ == "__main__":
    build()
