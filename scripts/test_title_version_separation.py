#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Regression tests for the Moon Cortex title/version guard."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_title_version_separation import (  # noqa: E402
    contains_version_marker,
    first_h1,
    normalize_heading,
    validation_errors,
)


def main() -> None:
    assert contains_version_marker("Financial Living System V2")
    assert contains_version_marker("Social Support Navigation System 0.1.0-pre.1")
    assert not contains_version_marker("Financial Living System")
    assert not contains_version_marker("Social Support Navigation System")
    assert first_h1("intro\n# Stable Module\n") == "Stable Module"
    assert normalize_heading("# 🌙 Moon Cortex · Financial Living System") == (
        "Moon Cortex · Financial Living System"
    )
    assert not validation_errors()
    print("title/version separation tests passed")


if __name__ == "__main__":
    main()

