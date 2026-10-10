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
        self.assertEqual(18, len(links))
        self.assertEqual(18, len(set(links)))
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
        self.assertEqual(47, len(checks.EXPECTED))

    def test_every_public_child_has_substantive_method_content(self) -> None:
        """A public child needs an operational manual, not a two-paragraph stub."""
        specs = {
            "components/creative-direction/OMNIALCHEMY.md": "## Extended operating method",
            "components/creative-direction/WEB_AESTHETICS.md": "## Parametric aesthetic workbench",
            "components/image-editing/CONSERVATIVE_PHOTO_EDIT.md": "## Preservation-first editing handbook",
            "components/references-and-identity/HUMAN_CANON_FORGE.md": "## Consent-based likeness workflow",
            "components/references-and-identity/REFERENCE_ABSTRACTION_GUARDRAIL.md": "## Reference-to-originality extraction protocol",
            "components/references-and-identity/CONFIGURABLE_VISUAL_PROFILE.md": "## User-owned configuration model",
            "engines/photography/ANALOGIC_PHOTO.md": "## Photographic material system",
            "engines/photography/VERNACULAR_SNAPSHOT_REALISM.md": "## Capture ecology: the engine's decisive variable",
            "engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md": "## Period reconstruction without a nationality filter",
            "engines/interfaces-and-retro/WEB_RETRO_IMAGE_GEN.md": "## Era-to-interface translation handbook",
            "engines/interfaces-and-retro/AQUA_SKEUO_ICON_FORGE.md": "## Visual systems handbook",
            "engines/interfaces-and-retro/LIVED_IN_RETROFUTURISM.md": "## Counterfactual editorial-worldbuilding system",
            "engines/expressive-and-editorial/CHROMATIC_DREAM_LOGIC.md": "## Chromatic and compositional compiler",
            "engines/expressive-and-editorial/SENTIMENTAL_UNCANNY.md": "## Tenderness-first uncanny grammar",
            "engines/expressive-and-editorial/SUBLIME_LYRIC_STILL.md": "## Cinematic atmospheric still production",
            "engines/expressive-and-editorial/VINTAGE_EDITORIAL_RUBBER_HOSE_POSTER.md": "## Editorial message-to-image pipeline",
            "engines/pixel-and-game-art/AUTHORED_PIXEL_ART.md": "## Visual DNA: deliberate discrete construction",
            "engines/experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md": "## Isometric-source to physical-space conversion",
        }
        self.assertEqual(18, len(specs))
        for relative, heading in specs.items():
            path = checks.MODULE / relative
            self.assertTrue(path.is_file(), relative)
            content = path.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(content.encode("utf-8")), 5400, relative)
            self.assertIn(heading, content, relative)
            self.assertTrue("qa" in content.lower() or "audit" in content.lower(), relative)

    def test_authored_pixel_art_is_native_and_active(self) -> None:
        relative = "engines/pixel-and-game-art/AUTHORED_PIXEL_ART.md"
        manual = (checks.MODULE / relative).read_text(encoding="utf-8")
        self.assertIn("**Status:** active", manual)
        self.assertIn("## Component activation", manual)
        for contract in (
            "native canvas", "clusters", "silhouette", "palette", "tileset",
            "animation", "1×", "not rendered", "Visual Director",
        ):
            self.assertIn(contract.lower(), manual.lower(), contract)
        director = (checks.MODULE / "VISUAL_DIRECTOR.md").read_text(encoding="utf-8")
        self.assertIn("Authored Pixel Art", director)
        self.assertIn("Pixel-World Camera Translation", director)
        registry = (checks.MODULE / "docs/SPECIALIST_ENGINES.md").read_text(encoding="utf-8")
        self.assertIn("Pixel and game art", registry)
        self.assertEqual(12, len(checks.SPECIALISTS))
        self.assertEqual(47, len(checks.EXPECTED))

    def test_pixel_art_vs_physical_translation_routing(self) -> None:
        director = (checks.MODULE / "VISUAL_DIRECTOR.md").read_text(encoding="utf-8")
        self.assertIn("actual pixel-native sprites", director)
        self.assertIn("physical environment", director)
        manual = (checks.MODULE / "engines/pixel-and-game-art/AUTHORED_PIXEL_ART.md").read_text(encoding="utf-8")
        self.assertIn("Pixel-World Camera Translation", manual)
        index = (checks.MODULE / "docs/COMPONENT_INDEX.md").read_text(encoding="utf-8")
        self.assertIn("pixel-native", index.lower())

    def test_shared_compilation_and_diagnostic_depth(self) -> None:
        visual_state = (checks.MODULE / "docs/VISUAL_STATE_AND_COMPILATION.md").read_text(encoding="utf-8")
        visual_qa = (checks.MODULE / "docs/VISUAL_QA_AND_REPAIR.md").read_text(encoding="utf-8")
        self.assertIn("## Visual-frame resolution across multiple specialists", visual_state)
        self.assertIn("## Diagnostic taxonomy for real output", visual_qa)
        self.assertIn("provenance", visual_state.lower())
        self.assertIn("unverified", visual_qa.lower())

    def test_specialist_family_registry_is_complete(self) -> None:
        registry = (checks.MODULE / "docs" / "SPECIALIST_ENGINES.md").read_text(encoding="utf-8")
        for family in checks.SPECIALISTS:
            self.assertIn(family, registry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
