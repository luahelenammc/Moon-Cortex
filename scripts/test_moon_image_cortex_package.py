#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Regression tests for the Moon Image Cortex public package contract."""

from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import build_moon_image_cortex_package
import check_moon_image_cortex_package as checks


class MoonImageCortexPackageTests(unittest.TestCase):
    def test_public_package_validation_passes(self) -> None:
        self.assertEqual([], checks.validation_errors())

    def test_deterministic_archive_rebuilds_byte_for_byte(self) -> None:
        first = build_moon_image_cortex_package.archive_bytes()
        second = build_moon_image_cortex_package.archive_bytes()
        self.assertEqual(first, second)

    def test_stale_but_valid_zip_is_rejected(self) -> None:
        """A valid ZIP with bytes unlike the committed reproducible build must fail."""
        with tempfile.TemporaryDirectory() as directory:
            stale_package = Path(directory) / "moon-image-cortex.zip"
            stale_package.write_bytes(build_moon_image_cortex_package.archive_bytes())
            with zipfile.ZipFile(stale_package, "a") as archive:
                archive.comment = b"stale-public-artifact"
            with patch.object(checks, "PACKAGE", stale_package):
                errors = checks.validation_errors()
        self.assertIn("ZIP differs from deterministic build output", errors)

    def test_acceptance_matrix_covers_all_intents_once(self) -> None:
        matrix = checks.MODULE / "docs" / "IMAGE_CORTEX_REALITY_TEST.md"
        rows = [
            line for line in matrix.read_text(encoding="utf-8").splitlines()
            if line.startswith("| ") and not line.startswith("| Test intent") and not line.startswith("|---")
        ]
        self.assertEqual(22, len(rows))
        for intent in checks.TEST_INTENTS:
            self.assertEqual(1, sum(intent in row for row in rows), intent)

    def test_specialist_family_registry_is_complete(self) -> None:
        registry = (checks.MODULE / "docs" / "SPECIALIST_ENGINES.md").read_text(encoding="utf-8")
        for family in checks.SPECIALISTS:
            self.assertIn(family, registry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
