#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate the Probability Calibration System source unit and complete ZIP."""

from __future__ import annotations

import re
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "modules" / "probability-calibration-system"
PACKAGE = ROOT / "downloads" / "probability-calibration-system.zip"
PACKAGE_PREFIX = "probability-calibration-system/"
EXPECTED = {
    "README.md",
    "PROBABILITY_CALIBRATOR.md",
    "docs/CORE_INVARIANTS.md",
    "docs/CALIBRATION_MODEL.md",
    "docs/EVIDENCE_AND_CLAIMS.md",
    "docs/FORECAST_VERIFICATION.md",
    "docs/MOON_SOURCE_CONTEXT_BRIDGE.md",
    "docs/QUANTITATIVE_METHODS.md",
    "docs/REALITY_TEST.md",
    "docs/SCIENTIFIC_REFERENCES.md",
    "docs/STRUCTURED_EXPERT_ELICITATION.md",
    "examples/synthetic_examples.md",
    "CHANGELOG.md",
    "reference/__init__.py",
    "reference/probability_calibration.py",
    "reference/forecast_verification.py",
    "reference/tests/__init__.py",
    "reference/tests/test_quantification.py",
    "reference/tests/test_forecast_verification.py",
}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

def validation_errors() -> list[str]:
    errors: list[str] = []
    if not MODULE.is_dir():
        return ["missing probability-calibration-system module directory"]

    actual = {
        path.relative_to(MODULE).as_posix()
        for path in MODULE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }
    if actual != EXPECTED:
        errors.append(f"module file set mismatch: missing={sorted(EXPECTED - actual)}, unexpected={sorted(actual - EXPECTED)}")

    entry = MODULE / "PROBABILITY_CALIBRATOR.md"
    if entry.is_file():
        entry_text = entry.read_text(encoding="utf-8")
        if not re.search(r"(?im)^# Probability Calibrator\s*$", entry_text):
            errors.append("canonical entry has an unexpected title")
        if "**Version:** 0.2.0-pre.1" not in entry_text:
            errors.append("canonical entry is missing version 0.2.0-pre.1")
        if "## First use" not in entry_text:
            errors.append("canonical entry is missing embedded first-use instructions")
        for field in ("as_of", "expire_if", "refresh_if", "manual_recalibration_required_if", "safe_fallback_read"):
            if field not in entry_text:
                errors.append(f"canonical entry is missing freshness field {field}")

    readme = MODULE / "README.md"
    if readme.is_file():
        readme_text = readme.read_text(encoding="utf-8")
        if "[Probability Calibrator](PROBABILITY_CALIBRATOR.md#first-use)" not in readme_text:
            errors.append("module README does not route to the canonical entry")
        if "[Complete module package](../../downloads/probability-calibration-system.zip)" not in readme_text:
            errors.append("module README does not route to the stable package path")

    markdown_files = [MODULE / rel for rel in EXPECTED if rel.endswith(".md") and (MODULE / rel).is_file()]
    for source in markdown_files:
        for raw_target in LINK_RE.findall(source.read_text(encoding="utf-8")):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            relative = unquote(parsed.path)
            candidate = (source.parent / relative).resolve() if relative else source.resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not candidate.is_file():
                errors.append(f"{source.relative_to(ROOT)}: missing local link target: {target}")

    combined = "\n".join(path.read_text(encoding="utf-8") for path in markdown_files).lower()
    required = (
        "fit", "evidence", "probability", "confidence", "no universal probability formula",
        "qualitative", "high-stakes", "synthetic", "local moon source",
    )
    for marker in required:
        if marker not in combined:
            errors.append(f"module is missing required contract marker: {marker}")
    if "capela" in combined:
        errors.append("module package contains a private situational adapter name")
    example_text = (MODULE / "examples" / "synthetic_examples.md").read_text(encoding="utf-8").lower() if (MODULE / "examples" / "synthetic_examples.md").is_file() else ""
    for marker in ("high fit, low evidence", "moderate probability, high confidence", "correlated", "qualitative only", "recalibration"):
        if marker not in example_text:
            errors.append(f"synthetic examples are missing required case: {marker}")

    stale_version = "0.1.0-pre.1"
    for source in markdown_files:
        if source.name != "CHANGELOG.md" and stale_version in source.read_text(encoding="utf-8"):
            errors.append(f"{source.relative_to(ROOT)} retains stale current-state version {stale_version}")

    if not PACKAGE.is_file():
        errors.append("missing complete package downloads/probability-calibration-system.zip")
    else:
        try:
            with zipfile.ZipFile(PACKAGE) as archive:
                names = archive.namelist()
                expected_names = {PACKAGE_PREFIX + rel for rel in EXPECTED}
                if set(names) != expected_names:
                    errors.append(f"package member set mismatch: missing={sorted(expected_names - set(names))}, unexpected={sorted(set(names) - expected_names)}")
                for rel in EXPECTED:
                    member = PACKAGE_PREFIX + rel
                    if member not in names:
                        continue
                    source = MODULE / rel
                    if source.is_file() and archive.read(member) != source.read_bytes():
                        errors.append(f"package content differs from source: {rel}")
        except (OSError, zipfile.BadZipFile) as exc:
            errors.append(f"package cannot be opened: {exc}")

    return errors

def main() -> None:
    errors = validation_errors()
    if errors:
        raise SystemExit("probability package validation failed:\n- " + "\n- ".join(errors))
    print(f"validated Probability Calibration System module and {len(EXPECTED)} package files")

if __name__ == "__main__":
    main()
