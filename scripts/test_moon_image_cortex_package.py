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

    def test_child_component_files_are_individually_routable(self) -> None:
        registry = (checks.MODULE / "docs" / "COMPONENT_INDEX.md").read_text(encoding="utf-8")
        import re
        from pathlib import Path
        links = [link for link in re.findall(r"\]\((\.\./(?:engines|components)/[^)]+\.md)\)", registry) if "/regions/" not in link]
        self.assertEqual(17, len(links))
        self.assertEqual(17, len(set(links)))
        for relative in links:
            child = (checks.MODULE / "docs" / relative).resolve()
            self.assertTrue(child.is_file(), relative)
            text = child.read_text(encoding="utf-8")
            self.assertIn("Visual Director", text)
            if "engines" in child.parts:
                self.assertIn("component activation", text.lower())
                self.assertIn("not rendered", text.lower())
            else:
                self.assertIn("first use", text.lower())

    def test_geographic_context_is_opt_in_and_unrestricted(self) -> None:
        parent = (checks.MODULE / "engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md").read_text(encoding="utf-8")
        self.assertIn("No country", parent)
        self.assertIn("CUSTOM_CONTEXT.md", parent)
        custom = (checks.MODULE / "engines/photography/regions/CUSTOM_CONTEXT.md").read_text(encoding="utf-8")
        self.assertIn("country is optional", custom.lower())
        countries = ["BRAZIL", "UNITED_STATES", "UNITED_KINGDOM", "JAPAN", "INDIA", "MEXICO", "FRANCE", "GERMANY"]
        for country in countries:
            child = checks.MODULE / "engines" / "photography" / "regions" / f"{country}.md"
            self.assertTrue(child.is_file(), country)
            data = child.read_text(encoding="utf-8")
            self.assertIn("optional region-specific context adapter", data)
            self.assertIn("not rendered", data.lower())

    def test_english_only_active_engine_names(self) -> None:
        sources = checks.module_files()
        for path, raw in sources.items():
            text = raw.decode("utf-8")
            self.assertNotIn("Retrofuturo Habitável", text, path)
            self.assertNotIn("Nostalgic Camera BR 90s", text, path)
        self.assertIn("Lived-In Retrofuturism", (checks.MODULE / "docs/COMPONENT_INDEX.md").read_text(encoding="utf-8"))

    def test_reorganized_component_paths_are_registered(self) -> None:
        index = (checks.MODULE / "docs/COMPONENT_INDEX.md").read_text(encoding="utf-8")
        for category in ("photography", "interfaces-and-retro", "expressive-and-editorial", "experimental", "creative-direction", "references-and-identity", "image-editing"):
            self.assertIn(category, index)
        self.assertEqual(46, len(checks.EXPECTED))

    def test_public_navigation_prioritizes_broad_use(self) -> None:
        """The public browse order must keep niche routes out of the first-use showcase."""
        cases = (
            (
                checks.MODULE / "README.md",
                [
                    "## Most common starting points",
                    "## Reference and identity tools",
                    "## Specialized visual families",
                    "## Experimental routes",
                    "## Optional geographic contexts",
                ],
            ),
            (
                checks.MODULE / "docs" / "COMPONENT_INDEX.md",
                [
                    "## Most common starting points",
                    "## Reference and identity controls",
                    "## Specialized creative families",
                    "## Experimental",
                    "## Optional geographic overlays",
                ],
            ),
            (
                checks.MODULE / "VISUAL_DIRECTOR.md",
                [
                    "#### Everyday creation, editing and photography",
                    "#### Reference and identity controls",
                    "#### Specialized visual languages",
                    "#### Experimental translation",
                    "#### Optional geographic context",
                ],
            ),
        )
        for path, headings in cases:
            text = path.read_text(encoding="utf-8")
            positions = [text.index(heading) for heading in headings]
            self.assertEqual(sorted(positions), positions, path.name)
            general = text[positions[0]:positions[1]]
            self.assertIn("Omnialchemy", general)
            self.assertIn("Conservative Photo Edit", general)
            self.assertIn("Analogic Photo", general)
            self.assertIn("Vernacular Snapshot Realism", general)
            self.assertIn("Contextual Nostalgic Camera", general)
            self.assertIn("Web Aesthetics", general)
            self.assertNotIn("Pixel-World Camera Translation", general)
            self.assertNotIn("Vintage Editorial Rubber Hose Poster", general)

    def test_catalog_retains_single_entry_and_complete_family(self) -> None:
        """Editorial prioritization does not eliminate access to any public component."""
        index = (checks.MODULE / "docs" / "COMPONENT_INDEX.md").read_text(encoding="utf-8")
        import re
        routes = re.findall(r"\]\((\.\./(?:engines|components)/[^)]+\.md)\)", index)
        routes = [route for route in routes if "/regions/" not in route]
        self.assertEqual(17, len(routes))
        self.assertEqual(17, len(set(routes)))
        self.assertIn("only general operational entry", index.lower())
        self.assertIn("not rendered", index.lower())
        self.assertIn("geography", index.lower())

    def test_specialist_family_registry_is_complete(self) -> None:
        registry = (checks.MODULE / "docs" / "SPECIALIST_ENGINES.md").read_text(encoding="utf-8")
        for family in checks.SPECIALISTS:
            self.assertIn(family, registry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
