#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Regression tests for the Moon Cortex title/version guard."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_title_version_separation import (  # noqa: E402
    VERSIONED_CURRENT_PATH_EXCEPTIONS,
    contains_version_marker,
    contains_version_marker_in_path,
    current_module_path_errors,
    first_h1,
    normalize_heading,
    validation_errors,
)


def main() -> None:
    assert contains_version_marker("Financial Living System V2")
    assert contains_version_marker("Social Support Navigation System 0.1.0-pre.1")
    assert not contains_version_marker("Financial Living System")
    assert not contains_version_marker("Social Support Navigation System")
    assert contains_version_marker_in_path("modules/finance/BOOTSTRAP_V2.md")
    assert contains_version_marker_in_path("modules/finance/v2/BOOTSTRAP.md")
    assert contains_version_marker_in_path("downloads/finance-0.2.0.zip")
    assert not contains_version_marker_in_path("modules/finance/ADAPTIVE_FINANCE_BOOTSTRAP.md")
    assert first_h1("intro\n# Stable Module\n") == "Stable Module"
    assert normalize_heading("# 🌙 Moon Cortex · Financial Living System") == (
        "Moon Cortex · Financial Living System"
    )
    assert not validation_errors()

    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        module = root / "modules" / "finance"
        downloads = root / "downloads"
        module.mkdir(parents=True)
        downloads.mkdir()
        (module / "README.md").write_text(
            "- **Canonical entry:** [Entry](BOOTSTRAP_V2.md)\n"
            "- **Transport surface:** [ZIP](../../downloads/finance-0.2.0.zip)\n",
            encoding="utf-8",
        )
        (module / "BOOTSTRAP_V2.md").write_text("# Finance\n", encoding="utf-8")
        (downloads / "finance-0.2.0.zip").write_bytes(b"fixture")
        errors = current_module_path_errors(root)
        assert any("canonical entry contains a version marker" in error for error in errors)
        assert any("transport package contains a version marker" in error for error in errors)
        exception_path = "modules/finance/BOOTSTRAP_V2.md"
        VERSIONED_CURRENT_PATH_EXCEPTIONS[exception_path] = "parallel schema compatibility generation"
        errors = current_module_path_errors(root)
        assert not any("canonical entry contains a version marker" in error for error in errors)
        assert any("transport package contains a version marker" in error for error in errors)
        del VERSIONED_CURRENT_PATH_EXCEPTIONS[exception_path]
    print("title/version separation tests passed")


if __name__ == "__main__":
    main()
