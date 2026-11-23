# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.check_ecosystem_links import (
    classify_http_status,
    validate_ecosystem,
    validate_distributions,
    validate_markdown_links,
    validate_packages,
    validate_pending_project_urls,
    validate_routes,
)

ROOT = Path(__file__).resolve().parents[1]


def project(project_id: str, repo: str, entry: str) -> dict:
    return {
        "id": project_id,
        "name": project_id,
        "class": "test",
        "canonical_repo": repo,
        "canonical_entry": entry,
        "summary": "synthetic fixture",
        "status": "active_public",
        "status_verified_at": "2026-11-23",
        "distribution": [],
        "maintainer": "fixture",
        "owned_function": "synthetic fixture",
        "imports": [],
        "references": [],
        "exports": [],
        "privacy_boundary": "synthetic only",
        "legacy_routes": [],
        "validation_ref": "synthetic",
    }


def route(legacy_url: str, target_project_id: str, target_url: str, **overrides) -> dict:
    value = {
        "legacy_url": legacy_url,
        "legacy_repo": "luahelenammc/Moon-Cortex",
        "legacy_path": "README.md",
        "target_project_id": target_project_id,
        "target_canonical_url": target_url,
        "route_class": "markdown",
        "compatibility_behavior": "human_readable_pointer",
        "owner_repo": "luahelenammc/Moon-Cortex",
        "first_known_use": "2026-11-23",
        "old_status": 200,
        "test_method": "offline_path_and_anchor_check",
        "last_checked": "2026-11-23",
        "result": "pass",
        "recovery_ref": "backup/pre-prisma-rearchitecture-2026-11-23",
        "policy_source": ["https://github.com/luahelenammc/Moon-Source/blob/main/docs/SOURCE_OPERATIONS.md"],
    }
    value.update(overrides)
    return value


class CurrentRegistryTests(unittest.TestCase):
    def test_current_ecosystem_and_route_registries_pass(self):
        ecosystem = json.loads((ROOT / "registry/ecosystem.json").read_text())
        routes = json.loads((ROOT / "registry/legacy-routes.json").read_text())
        self.assertEqual([], validate_ecosystem(ecosystem, ROOT))
        self.assertEqual([], validate_routes(routes, ecosystem, ROOT))

    def test_existing_modules_remain_registered(self):
        ecosystem = json.loads((ROOT / "registry/ecosystem.json").read_text())
        ids = {p["id"] for p in ecosystem["projects"]}
        self.assertTrue({
            "financial-living-system", "social-support-navigation-system",
            "probability-calibration-system", "moon-image-cortex", "moon-music-engine",
        }.issubset(ids))

    def test_pending_prisma_has_no_published_route_or_distribution(self):
        ecosystem = json.loads((ROOT / "registry/ecosystem.json").read_text())
        prisma = next(p for p in ecosystem["projects"] if p["id"] == "prisma")
        self.assertEqual("unpublished_pending_verification", prisma["status"])
        self.assertIsNone(prisma["canonical_repo"])
        self.assertIsNone(prisma["canonical_entry"])
        self.assertEqual([], prisma["distribution"])
        self.assertEqual([], validate_pending_project_urls(ecosystem, ROOT))

    def test_pending_prisma_rejects_a_guessed_public_url(self):
        ecosystem = {"projects": [{"id":"prisma", "status":"unpublished_pending_verification"}]}
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "ECOSYSTEM.md").write_text("[PRISMA](https://github.com/luahelenammc/PRISMA)\n")
            errors = validate_pending_project_urls(ecosystem, root)
        self.assertTrue(any("unverified GitHub URL" in e for e in errors))

    def test_package_manifest_matches_all_real_zip_payloads_and_hashes(self):
        manifest = json.loads((ROOT / "registry/distribution-manifest.json").read_text())
        self.assertEqual([], validate_packages(manifest, ROOT))
        ecosystem = json.loads((ROOT / "registry/ecosystem.json").read_text())
        self.assertEqual([], validate_distributions(ecosystem, manifest))
        self.assertEqual([], validate_pending_project_urls(ecosystem, ROOT))
        self.assertEqual(10, len(manifest["packages"]))


class FailureFixtureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "README.md").write_text("# Good\n\nSee [Good](README.md#good).\n")
        (self.root / "present.md").write_text("# Existing Target\n")
        self.source = project("source", "https://github.com/example/Source", "https://github.com/example/Source/blob/main/README.md")
        self.atlas = project("atlas", "https://github.com/luahelenammc/Moon-Cortex", "https://github.com/luahelenammc/Moon-Cortex/blob/main/README.md")
        self.ecosystem = {"projects": [self.source, self.atlas]}

    def tearDown(self):
        self.temp.cleanup()

    def test_missing_local_target_path_fails(self):
        bad = route("https://github.com/luahelenammc/Moon-Cortex/blob/main/old.md", "atlas", "https://github.com/luahelenammc/Moon-Cortex/blob/main/missing.md")
        errors = validate_routes({"routes": [bad]}, self.ecosystem, self.root)
        self.assertTrue(any("target path does not exist" in e for e in errors))

    def test_missing_known_fragment_fails(self):
        errors = validate_markdown_links(self.root, ["README.md"])
        self.assertEqual([], errors)
        (self.root / "README.md").write_text("# Good\n\n[Bad](present.md#not-there)\n")
        errors = validate_markdown_links(self.root, ["README.md"])
        self.assertTrue(any("missing Markdown fragment" in e for e in errors))

    def test_circular_legacy_routes_fail(self):
        a = "https://github.com/luahelenammc/Moon-Cortex/blob/main/old-a.md"
        b = "https://github.com/luahelenammc/Moon-Cortex/blob/main/old-b.md"
        first = route(a, "atlas", b, legacy_path="old-a.md", target_canonical_url=b)
        second = route(b, "atlas", a, legacy_path="old-b.md", target_canonical_url=a)
        errors = validate_routes({"routes": [first, second]}, self.ecosystem, self.root)
        self.assertTrue(any("cycle" in e for e in errors))

    def test_wrong_target_project_is_rejected(self):
        wrong = route(
            "https://github.com/luahelenammc/Moon-Cortex/blob/main/old.md",
            "source",
            "https://github.com/luahelenammc/Moon-Cortex/blob/main/present.md",
            legacy_path="old.md",
        )
        errors = validate_routes({"routes": [wrong]}, self.ecosystem, self.root)
        self.assertTrue(any("does not belong to target_project_id" in e for e in errors))

    def test_unchecked_route_cannot_be_reported_as_success(self):
        bad = route(
            "https://github.com/luahelenammc/Moon-Cortex/blob/main/old.md",
            "atlas",
            "https://github.com/luahelenammc/Moon-Cortex/blob/main/present.md",
            legacy_path="old.md", test_method="unchecked", last_checked=None, result="pass",
        )
        errors = validate_routes({"routes": [bad]}, self.ecosystem, self.root)
        self.assertTrue(any("cannot be reported as pass" in e for e in errors))

    def test_invalid_zip_payload_fails_even_with_matching_hash(self):
        bad_zip = self.root / "bad.zip"
        bad_zip.write_bytes(b"not a zip")
        import hashlib
        manifest = {"packages": [{"path": "bad.zip", "size_bytes": bad_zip.stat().st_size, "sha256": hashlib.sha256(bad_zip.read_bytes()).hexdigest()}]}
        errors = validate_packages(manifest, self.root)
        self.assertTrue(any("invalid ZIP" in e for e in errors))

    def test_false_sha_and_missing_zip_fail(self):
        good_zip = self.root / "good.zip"
        with zipfile.ZipFile(good_zip, "w") as archive:
            archive.writestr("README.md", "synthetic")
        manifest = {"packages": [
            {"path": "good.zip", "size_bytes": good_zip.stat().st_size, "sha256": "0" * 64},
            {"path": "missing.zip", "size_bytes": 0, "sha256": "0" * 64},
        ]}
        errors = validate_packages(manifest, self.root)
        self.assertTrue(any("SHA-256 mismatch" in e for e in errors))
        self.assertTrue(any("file is missing" in e for e in errors))

    def test_live_404_is_failure_and_server_outage_is_unverified(self):
        self.assertEqual("FAIL", classify_http_status(404))
        self.assertEqual("UNVERIFIED", classify_http_status(503))
        self.assertEqual("PASS", classify_http_status(200))


if __name__ == "__main__":
    unittest.main()
