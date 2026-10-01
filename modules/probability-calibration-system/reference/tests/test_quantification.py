# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Numerical and boundary tests for quantitative forecast methods."""

from __future__ import annotations

import unittest

from reference.probability_calibration import (
    EvidenceSignal,
    QuantificationClass,
    ReferenceClassPolicy,
    aggregate_estimates,
    bayesian_odds_update,
    beta_binomial_posterior,
    check_percentage_permission,
    classify_evidence_dependence,
    expected_utility,
    monte_carlo_bayesian_update,
    reference_class_summary,
    validate_quantile_elicitation,
)


class PermissionAndReferenceClassTests(unittest.TestCase):
    def test_q0_blocks_percentage_even_with_complete_target(self) -> None:
        result = check_percentage_permission(
            target_event_defined=True, horizon_defined=True,
            quantification_class=QuantificationClass.QUALITATIVE_ONLY, provenance={},
        )
        self.assertFalse(result.allowed)
        self.assertIn("quantitative_basis (Q0 does not permit percentages)", result.missing)

    def test_reference_class_requires_declared_provenance(self) -> None:
        missing = check_percentage_permission(
            target_event_defined=True, horizon_defined=True,
            quantification_class=QuantificationClass.EMPIRICAL_REFERENCE_CLASS,
            provenance={"reference_class": "events with same registration window"},
        )
        self.assertFalse(missing.allowed)
        self.assertEqual(set(missing.missing), {
            "sample_size", "event_count", "inclusion_logic", "comparability_limitations",
            "reference_class_status", "reference_class_meets_explicit_policy",
        })
        permitted = check_percentage_permission(
            target_event_defined=True, horizon_defined=True,
            quantification_class=QuantificationClass.EMPIRICAL_REFERENCE_CLASS,
            provenance={
                "reference_class": "completed sessions with the same lead time",
                "reference_class_status": "available", "sample_size": 10, "event_count": 7,
                "inclusion_logic": "all consecutive resolved sessions",
                "comparability_limitations": "venue capacity varied",
            },
        )
        self.assertTrue(permitted.allowed)
        available = reference_class_summary(
            definition="completed workshops with 3-4 week registration windows",
            event_count=7, sample_size=10, inclusion_logic="all consecutive recorded workshops",
            comparability_limitations="venue capacity varied",
            policy=ReferenceClassPolicy(minimum_sample_size=5, heterogeneity_status="acceptable"),
        )
        self.assertEqual(available.empirical_rate, 0.7)
        self.assertEqual(available.observed_rate, 0.7)
        self.assertEqual(available.uncertainty_interval_kind, "Wilson_confidence")
        self.assertLess(available.uncertainty_interval[0], available.observed_rate)
        self.assertGreater(available.uncertainty_interval[1], available.observed_rate)
        self.assertIsNone(available.posterior)

        posterior = reference_class_summary(
            definition="same workshops", event_count=7, sample_size=10,
            inclusion_logic="all consecutive workshops", comparability_limitations="same venue",
            policy=ReferenceClassPolicy(minimum_sample_size=5, heterogeneity_status="acceptable"),
            prior=(1, 1),
        )
        self.assertEqual(posterior.uncertainty_interval_kind, "credible")
        self.assertEqual(posterior.uncertainty_interval, posterior.posterior.credible_interval)

    def test_reference_class_policy_blocks_tiny_or_heterogeneous_classes(self) -> None:
        tiny = reference_class_summary(
            definition="three selected sessions", event_count=3, sample_size=3,
            inclusion_logic="selected cases only", comparability_limitations="different periods",
            policy=ReferenceClassPolicy(minimum_sample_size=8, heterogeneity_status="acceptable"),
        )
        self.assertEqual(tiny.status, "too_small")
        self.assertEqual(tiny.observed_rate, 1.0)
        self.assertIsNone(tiny.empirical_rate)
        mixed = reference_class_summary(
            definition="sessions across unrelated formats", event_count=4, sample_size=12,
            inclusion_logic="all sessions", comparability_limitations="formats differ",
            policy=ReferenceClassPolicy(minimum_sample_size=8, heterogeneity_status="too_heterogeneous"),
        )
        self.assertEqual(mixed.status, "too_heterogeneous")
        self.assertIsNone(mixed.empirical_rate)

    def test_missing_reference_class_never_returns_an_invented_rate(self) -> None:
        result = reference_class_summary(
            definition=None, event_count=0, sample_size=0, inclusion_logic="",
            comparability_limitations="",
            policy=ReferenceClassPolicy(minimum_sample_size=3, heterogeneity_status="unassessed"),
        )
        self.assertEqual(result.status, "unavailable")
        self.assertIsNone(result.empirical_rate)


class BayesianMethodsTests(unittest.TestCase):
    def test_beta_binomial_shrinks_three_of_three(self) -> None:
        posterior = beta_binomial_posterior(1, 1, 3, 3)
        self.assertAlmostEqual(posterior.mean, 0.8)
        self.assertEqual((posterior.alpha, posterior.beta), (4, 1))
        self.assertLess(posterior.credible_interval[1], 1.0)
        self.assertLess(posterior.credible_interval[0], posterior.credible_interval[1])

    def test_beta_posterior_edge_counts_and_jeffreys_prior(self) -> None:
        zero = beta_binomial_posterior(0.5, 0.5, 0, 5)
        all_yes = beta_binomial_posterior(0.5, 0.5, 5, 5)
        self.assertEqual(zero.mean, 0.5 / 6.0)
        self.assertEqual(all_yes.mean, 5.5 / 6.0)
        self.assertGreater(zero.credible_interval[1], 0)
        self.assertLess(all_yes.credible_interval[0], 1)

    def test_beta_posterior_rejects_invalid_parameters_and_counts(self) -> None:
        for args in ((0, 1, 0, 0), (1, -1, 0, 0), (1, 1, 4, 3)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                beta_binomial_posterior(*args)

    def test_likelihood_ratio_update_behaves_as_odds_expect(self) -> None:
        self.assertAlmostEqual(bayesian_odds_update(0.25, [1]), 0.25)
        self.assertAlmostEqual(bayesian_odds_update(0.25, [3]), 0.5)
        self.assertLess(bayesian_odds_update(0.25, [0.5]), 0.25)
        self.assertEqual(bayesian_odds_update(0, [100]), 0)
        self.assertEqual(bayesian_odds_update(1, [0.01]), 1)

    def test_multiple_likelihood_ratios_require_dependency_declaration(self) -> None:
        with self.assertRaisesRegex(ValueError, "conditional_independence"):
            bayesian_odds_update(0.2, [2, 3])
        self.assertAlmostEqual(bayesian_odds_update(0.2, [2, 3], dependence="conditionally_independent"), 0.6)
        with self.assertRaises(ValueError):
            bayesian_odds_update(0.2, [0])

    def test_dependence_groups_same_source_and_retains_unknowns(self) -> None:
        same_source = classify_evidence_dependence([
            EvidenceSignal("article-a", source_family="press-release-1"),
            EvidenceSignal("repost-b", source_family="press-release-1"),
        ])
        self.assertEqual(same_source.status, "shared_or_overlapping")
        self.assertEqual(same_source.clusters, (("article-a", "repost-b"),))
        unknown = classify_evidence_dependence([EvidenceSignal("a"), EvidenceSignal("b")])
        self.assertEqual(unknown.status, "unknown_dependence")

    def test_quantile_elicitation_keeps_raw_quantiles_and_rejects_order_errors(self) -> None:
        elicitation = validate_quantile_elicitation(
            {"q05": 0.1, "q50": 0.45, "q95": 0.8},
            elicitation_record="panel round 1",
            protocol_label="structured elicitation; not a formal SHELF session",
            probability_quantity=True,
        )
        self.assertEqual(elicitation.values["q50"], 0.45)
        with self.assertRaisesRegex(ValueError, "nondecreasing"):
            validate_quantile_elicitation(
                {"q25": 0.8, "q50": 0.4}, elicitation_record="raw", protocol_label="structured", 
            )

    def test_aggregation_preserves_dispersion_and_gates_performance_weights(self) -> None:
        pooled = aggregate_estimates([0.2, 0.25, 0.9])
        self.assertAlmostEqual(pooled.mean, 0.45)
        self.assertEqual(pooled.median, 0.25)
        self.assertEqual(pooled.maximum, 0.9)
        self.assertEqual(pooled.dispersion, 0.7)
        with self.assertRaisesRegex(ValueError, "out-of-sample"):
            aggregate_estimates([0.2, 0.9], performance_weighted=True)
        weighted = aggregate_estimates([0.2, 0.9], weights=[3, 1], performance_weighted=True,
                                       comparable_resolved_history=True, out_of_sample_evaluation=True)
        self.assertAlmostEqual(weighted.mean, 0.375)

    def test_seeded_monte_carlo_is_reproducible_and_reports_count(self) -> None:
        prior = lambda rng: rng.betavariate(2, 5)
        likelihood = lambda rng: rng.lognormvariate(0.2, 0.1)
        first = monte_carlo_bayesian_update(prior, [likelihood], simulation_count=500, seed=27)
        second = monte_carlo_bayesian_update(prior, [likelihood], simulation_count=500, seed=27)
        self.assertEqual(first.samples, second.samples)
        self.assertEqual(first.simulation_count, 500)
        self.assertLess(first.intervals[0.5][0], first.intervals[0.5][1])
        self.assertTrue(all(0 <= p <= 1 for p in first.samples))

    def test_monte_carlo_rejects_unmodeled_dependence(self) -> None:
        with self.assertRaisesRegex(ValueError, "conditional independence"):
            monte_carlo_bayesian_update(lambda _: 0.5, [lambda _: 2, lambda _: 3], simulation_count=20, seed=1)

    def test_expected_utility_is_explicit_and_checks_normalization(self) -> None:
        value = expected_utility({"success": 0.1, "no_success": 0.9}, {"success": 100, "no_success": -2})
        self.assertAlmostEqual(value, 8.2)
        with self.assertRaisesRegex(ValueError, "sum to 1"):
            expected_utility({"success": 0.2, "no_success": 0.2}, {"success": 1, "no_success": 0})


if __name__ == "__main__":
    unittest.main()
