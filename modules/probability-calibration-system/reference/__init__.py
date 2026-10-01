# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Dependency-light reference implementation for Probability Calibration System."""

from .probability_calibration import (
    EvidenceSignal,
    QuantificationClass,
    ReferenceClassPolicy,
    aggregate_estimates,
    bayesian_odds_update,
    beta_binomial_posterior,
    classify_evidence_dependence,
    check_percentage_permission,
    expected_utility,
    monte_carlo_bayesian_update,
    reference_class_summary,
    validate_quantile_elicitation,
)
from .forecast_verification import (
    DataSufficiencyPolicy,
    ForecastRecord,
    ForecastRevision,
    ForecastStatus,
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

__all__ = [
    "EvidenceSignal", "QuantificationClass", "ReferenceClassPolicy", "aggregate_estimates", "bayesian_odds_update",
    "beta_binomial_posterior", "classify_evidence_dependence", "check_percentage_permission",
    "expected_utility", "monte_carlo_bayesian_update", "reference_class_summary",
    "validate_quantile_elicitation", "DataSufficiencyPolicy", "ForecastRecord", "ForecastRevision",
    "ForecastStatus", "RecalibrationPolicy",
    "assess_data_sufficiency", "brier_decomposition", "brier_score", "brier_skill_score",
    "evaluate_recalibration", "forecast_spread_summary", "grouped_score_summary", "log_loss", "reliability_bins",
    "resolve_forecast", "revise_forecast_metadata", "scoreable_observations",
]
