# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Scoring, ledger, sufficiency, and recalibration behavior tests."""

from __future__ import annotations

import math
import unittest

from reference.forecast_verification import (
    DataSufficiencyPolicy,
    ForecastRecord,
    ForecastStatus,
    ForecastRevision,
    RecalibrationPolicy,
    assess_data_sufficiency,
    brier_decomposition,
    brier_score,
    brier_skill_score,
    evaluate_recalibration,
    forecast_spread_summary,
    grouped_score_summary,
    log_loss,
    reliability_bins,
    resolve_forecast,
    revise_forecast_metadata,
    scoreable_observations,
)


def pending(forecast_id: str, probability: float | None = 0.6) -> ForecastRecord:
    return ForecastRecord(
        forecast_id=forecast_id, created_at="2026-01-01T00:00:00Z", target_event="event happens",
        resolution_criteria="official count reaches stated threshold by deadline", domain="synthetic",
        horizon="2026-06-30", as_of="2026-01-01", quantification_class="Q2",
        raw_probability=probability, final_probability=probability,
    )


def recalibration_policy(method: str, *, minimum_training: int = 8,
                         minimum_validation: int = 4, occupied_bins: int = 2,
                         validation_strategy: str = "holdout",
                         training_end: str | None = None,
                         validation_start: str | None = None) -> RecalibrationPolicy:
    sufficiency = DataSufficiencyPolicy(
        minimum_resolved=minimum_training, minimum_events=2, minimum_nonevents=2,
        minimum_occupied_probability_bins=occupied_bins, minimum_forecasts_per_occupied_bin=2,
        probability_bin_count=4, minimum_holdout_size=minimum_validation,
    )
    return RecalibrationPolicy(
        minimum_validation, method, "synthetic train", "demo/horizon-1", validation_strategy,
        sufficiency, training_end=training_end, validation_start=validation_start,
    )


class LedgerAndScoreTests(unittest.TestCase):
    def test_resolution_preserves_criteria_and_excludes_ambiguous_records(self) -> None:
        yes = resolve_forecast(pending("yes"), ForecastStatus.RESOLVED_YES,
                               resolved_at="2026-07-01", reason="official count met cutoff")
        ambiguous = resolve_forecast(pending("ambiguous"), ForecastStatus.AMBIGUOUS,
                                     resolved_at="2026-07-01", reason="source records conflict")
        probabilities, outcomes = scoreable_observations([yes, ambiguous])
        self.assertEqual(probabilities, (0.6,))
        self.assertEqual(outcomes, (1,))
        self.assertEqual(yes.resolution_criteria, pending("yes").resolution_criteria)

    def test_pending_forecasts_do_not_enter_score_and_resolution_is_one_time(self) -> None:
        record = pending("pending")
        self.assertEqual(scoreable_observations([record]), ((), ()))
        resolved = resolve_forecast(record, ForecastStatus.RESOLVED_NO,
                                    resolved_at="2026-07-01", reason="deadline passed")
        with self.assertRaisesRegex(ValueError, "only pending"):
            resolve_forecast(resolved, ForecastStatus.RESOLVED_YES,
                             resolved_at="2026-07-02", reason="late edit")

    def test_resolution_criteria_are_immutable_but_other_revisions_are_auditable(self) -> None:
        record = pending("audit")
        metadata = revise_forecast_metadata(record, ForecastRevision(
            "2026-02-01", "evidence_snapshot", "source A", "source A + source B", "additional source found",
        ))
        self.assertEqual(len(metadata.revisions), 1)
        with self.assertRaisesRegex(ValueError, "immutable"):
            revise_forecast_metadata(record, ForecastRevision(
                "2026-02-01", "resolution_criteria", "old", "new", "change outcome definition",
            ))

    def test_brier_bss_and_log_score_known_values(self) -> None:
        self.assertAlmostEqual(brier_score([0.8, 0.2], [1, 0]), 0.04)
        self.assertAlmostEqual(brier_skill_score(0.2, 0.25), 0.2)
        self.assertAlmostEqual(log_loss([0.8, 0.2], [1, 0]), -math.log(0.8))
        with self.assertRaises(ValueError):
            brier_skill_score(0.2, 0.0)

    def test_log_clipping_is_score_only_and_raw_extremes_are_preserved(self) -> None:
        record = pending("extreme", 0.0)
        clipped_loss = log_loss([0.0, 1.0], [1, 0], clip=1e-8)
        self.assertAlmostEqual(clipped_loss, -math.log(1e-8))
        self.assertEqual(record.raw_probability, 0.0)
        with self.assertRaises(ValueError):
            log_loss([0.5], [1], clip=0.5)

    def test_reliability_bins_include_counts_and_uncertainty_intervals(self) -> None:
        table = reliability_bins([0.1, 0.2, 0.8, 0.9], [0, 0, 1, 1], bins=2)
        self.assertEqual(sum(row.count for row in table), 4)
        self.assertEqual([row.count for row in table], [2, 2])
        self.assertLess(table[0].interval[0], table[0].observed_frequency + 0.01)
        adaptive = reliability_bins([0.1, 0.2, 0.8, 0.9], [0, 0, 1, 1], bins=2, adaptive=True)
        self.assertEqual([row.count for row in adaptive], [2, 2])

    def test_exact_brier_decomposition_reconstructs_sample_score(self) -> None:
        probabilities = [0.2, 0.2, 0.8, 0.8, 0.5]
        outcomes = [0, 1, 1, 1, 0]
        result = brier_decomposition(probabilities, outcomes)
        reconstructed = result.reliability - result.resolution + result.uncertainty
        self.assertAlmostEqual(result.brier, brier_score(probabilities, outcomes))
        self.assertAlmostEqual(reconstructed, result.brier)

    def test_spread_is_descriptive_and_entropy_is_bounded(self) -> None:
        result = forecast_spread_summary([0.5, 0.5, 0.5])
        self.assertEqual(result.standard_deviation, 0.0)
        self.assertEqual(result.mean_binary_entropy, 1.0)
        sharp = forecast_spread_summary([0.05, 0.95])
        self.assertLess(sharp.mean_binary_entropy, result.mean_binary_entropy)

    def test_resolved_performance_can_be_grouped_by_domain_or_horizon(self) -> None:
        records = []
        for identifier, domain, horizon, probability, status in (
            ("a", "meetings", "short", 0.8, ForecastStatus.RESOLVED_YES),
            ("b", "meetings", "short", 0.8, ForecastStatus.RESOLVED_NO),
            ("c", "workshops", "long", 0.5, ForecastStatus.RESOLVED_NO),
            ("d", "workshops", "long", 0.5, ForecastStatus.RESOLVED_YES),
        ):
            base = pending(identifier, probability)
            base = ForecastRecord(
                forecast_id=base.forecast_id, created_at=base.created_at, target_event=base.target_event,
                resolution_criteria=base.resolution_criteria, domain=domain, horizon=horizon, as_of=base.as_of,
                quantification_class=base.quantification_class, raw_probability=probability,
                final_probability=probability, status=status,
                resolution=1 if status is ForecastStatus.RESOLVED_YES else 0, resolved_at="2026-07-01",
            )
            records.append(base)
        by_domain = grouped_score_summary(records, dimension="domain", minimum_group_size=2)
        self.assertEqual([item.value for item in by_domain], ["meetings", "workshops"])
        self.assertAlmostEqual(by_domain[0].brier, 0.34)
        self.assertTrue(all(item.status == "diagnostic_ready" for item in by_domain))
        by_horizon = grouped_score_summary(records, dimension="horizon", minimum_group_size=3)
        self.assertTrue(all(item.status == "exploratory_only" for item in by_horizon))


class SufficiencyAndRecalibrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = DataSufficiencyPolicy(
            minimum_resolved=8, minimum_events=2, minimum_nonevents=2,
            minimum_occupied_probability_bins=2, minimum_forecasts_per_occupied_bin=2,
            probability_bin_count=4, minimum_holdout_size=2,
        )

    def test_cold_start_and_distribution_coverage_gate(self) -> None:
        cold = assess_data_sufficiency([], [], self.policy)
        self.assertEqual(cold.status, "insufficient_data")
        narrow = assess_data_sufficiency([0.5] * 8, [0, 1] * 4, self.policy)
        self.assertEqual(narrow.status, "exploratory_only")
        self.assertIn("coverage", " ".join(narrow.limitations))

    def test_recalibration_requires_configured_holdout_and_coverage(self) -> None:
        probabilities = [0.1, 0.12, 0.18, 0.22, 0.7, 0.72, 0.78, 0.82]
        outcomes = [0, 0, 1, 0, 1, 0, 1, 1]
        result = assess_data_sufficiency(probabilities, outcomes, self.policy, holdout_size=2)
        self.assertIn(result.status, ("diagnostic_ready", "recalibration_candidate"))
        self.assertEqual(result.resolved_count, 8)

    def test_insufficient_recalibration_history_returns_named_cold_start_state(self) -> None:
        policy = recalibration_policy("isotonic")
        result = evaluate_recalibration(
            [0.6, 0.7], [1, 0], [0.6, 0.7], [1, 0],
            training_forecast_ids=["a", "b"], validation_forecast_ids=["c", "d"], policy=policy,
        )
        self.assertEqual(result.status, "unavailable_insufficient_history")
        self.assertFalse(result.recalibrated_validation_probabilities)

    def test_recalibration_stays_unavailable_when_training_coverage_collapses(self) -> None:
        policy = recalibration_policy("isotonic", occupied_bins=2)
        result = evaluate_recalibration(
            [0.5] * 8, [0, 1] * 4, [0.2, 0.8, 0.2, 0.8], [0, 1, 0, 1],
            training_forecast_ids=[f"t{i}" for i in range(8)],
            validation_forecast_ids=[f"v{i}" for i in range(4)], policy=policy,
        )
        self.assertEqual(result.status, "unavailable_insufficient_history")
        self.assertIn("coverage", " ".join(result.limitations))
        self.assertFalse(result.recalibrated_validation_probabilities)

    def test_isotonic_fit_uses_disjoint_validation_and_keeps_raw_values(self) -> None:
        train_p = [0.8] * 10
        train_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        valid_p = [0.8] * 4
        valid_y = [1, 0, 1, 0]
        original_raw = tuple(valid_p)
        policy = recalibration_policy("isotonic", occupied_bins=1)
        result = evaluate_recalibration(
            train_p, train_y, valid_p, valid_y,
            training_forecast_ids=[f"t{i}" for i in range(10)],
            validation_forecast_ids=[f"v{i}" for i in range(4)], policy=policy,
        )
        self.assertEqual(result.status, "evaluated_out_of_sample")
        self.assertEqual(tuple(valid_p), original_raw)
        self.assertTrue(all(0 <= p <= 1 for p in result.recalibrated_validation_probabilities))
        self.assertEqual(result.recalibrated_validation_probabilities, (0.5, 0.5, 0.5, 0.5))
        self.assertLess(result.recalibrated_validation_brier, result.raw_validation_brier)

    def test_training_and_validation_forecast_ids_cannot_overlap(self) -> None:
        policy = recalibration_policy("platt", minimum_training=2, minimum_validation=2,
                                      occupied_bins=1)
        with self.assertRaisesRegex(ValueError, "disjoint"):
            evaluate_recalibration(
                [0.2, 0.8], [0, 1], [0.2, 0.8], [0, 1],
                training_forecast_ids=["same", "t2"], validation_forecast_ids=["same", "v2"], policy=policy,
            )

    def test_temporal_validation_must_follow_training_window(self) -> None:
        with self.assertRaisesRegex(ValueError, "before the validation"):
            RecalibrationPolicy(
                4, "isotonic", "w", "demo", "temporal_holdout",
                DataSufficiencyPolicy(10, 2, 2, 1, 2, 4, 4),
                training_end="2026-05-01", validation_start="2026-04-01",
            )

    def test_platt_method_produces_distinct_validation_values(self) -> None:
        train_p = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 0.45, 0.55]
        train_y = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
        valid_p = [0.2, 0.5, 0.8, 0.7]
        valid_y = [0, 1, 1, 0]
        policy = recalibration_policy("platt")
        result = evaluate_recalibration(
            train_p, train_y, valid_p, valid_y,
            training_forecast_ids=[f"t{i}" for i in range(len(train_p))],
            validation_forecast_ids=[f"v{i}" for i in range(len(valid_p))], policy=policy,
        )
        self.assertEqual(result.status, "evaluated_out_of_sample")
        self.assertEqual(len(result.model_parameters), 2)
        self.assertTrue(all(0 <= p <= 1 for p in result.recalibrated_validation_probabilities))


if __name__ == "__main__":
    unittest.main()
