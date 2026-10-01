# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Quantitative methods with explicit provenance and dependence gates.

This module performs mathematical transformations of supplied inputs. It does
not supply priors, likelihood ratios, reference classes, or factual evidence.
"""

from __future__ import annotations

import math
import random
import statistics
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Mapping, Sequence


class QuantificationClass(str, Enum):
    QUALITATIVE_ONLY = "Q0_qualitative_only"
    STRUCTURED_EXPERT_ELICITATION = "Q1_structured_expert_elicitation"
    EMPIRICAL_REFERENCE_CLASS = "Q2_empirical_reference_class"
    BAYESIAN_EVIDENCE_UPDATE = "Q3_bayesian_evidence_update"
    SIMULATION = "Q4_simulation_or_predictive_distribution"
    EMPIRICALLY_RECALIBRATED = "Q5_empirically_recalibrated_forecast"


_PROVENANCE_FIELDS: dict[QuantificationClass, tuple[str, ...]] = {
    QuantificationClass.STRUCTURED_EXPERT_ELICITATION: (
        "elicitation_protocol", "elicitation_record", "quantiles_or_ranges", "limitations",
    ),
    QuantificationClass.EMPIRICAL_REFERENCE_CLASS: (
        "reference_class", "reference_class_status", "sample_size", "event_count",
        "inclusion_logic", "comparability_limitations",
    ),
    QuantificationClass.BAYESIAN_EVIDENCE_UPDATE: (
        "prior", "evidence_sources", "likelihood_model", "dependence_handling",
    ),
    QuantificationClass.SIMULATION: (
        "simulation_count", "input_distributions", "parameter_sources", "dependence_handling",
    ),
    QuantificationClass.EMPIRICALLY_RECALIBRATED: (
        "raw_probability", "calibration_model_id", "training_window", "sample_size", "scope", "validation",
    ),
}


@dataclass(frozen=True)
class PercentagePermission:
    allowed: bool
    quantification_class: QuantificationClass
    missing: tuple[str, ...] = ()
    reason: str = ""


def check_percentage_permission(
    *,
    target_event_defined: bool,
    horizon_defined: bool,
    quantification_class: QuantificationClass,
    provenance: Mapping[str, object] | None,
) -> PercentagePermission:
    """Require a resolvable target, horizon, non-Q0 regime, and provenance."""
    if not isinstance(quantification_class, QuantificationClass):
        raise TypeError("quantification_class must be a QuantificationClass")
    missing: list[str] = []
    if not target_event_defined:
        missing.append("target_event")
    if not horizon_defined:
        missing.append("horizon")
    if quantification_class is QuantificationClass.QUALITATIVE_ONLY:
        missing.append("quantitative_basis (Q0 does not permit percentages)")
    else:
        basis = provenance or {}
        missing.extend(key for key in _PROVENANCE_FIELDS[quantification_class] if key not in basis or basis[key] is None)
        if (quantification_class is QuantificationClass.EMPIRICAL_REFERENCE_CLASS and
                basis.get("reference_class_status") != "available"):
            missing.append("reference_class_meets_explicit_policy")
    allowed = not missing
    reason = "percentage is permitted for this documented regime" if allowed else "percentage withheld until every listed prerequisite is supplied"
    return PercentagePermission(allowed, quantification_class, tuple(missing), reason)


def _validate_probability(value: float, name: str = "probability") -> float:
    value = float(value)
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be finite and between 0 and 1")
    return value


def _validate_positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


def _beta_fraction(a: float, b: float, x: float) -> float:
    """Continued fraction for the incomplete beta function (Numerical Recipes)."""
    max_iterations, epsilon, tiny = 300, 3e-14, 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, max_iterations + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < epsilon:
            return h
    raise ArithmeticError("incomplete beta continued fraction did not converge")


def regularized_beta(x: float, a: float, b: float) -> float:
    """Regularized incomplete beta I_x(a,b), using only the standard library."""
    _validate_positive(a, "alpha")
    _validate_positive(b, "beta")
    if not math.isfinite(x) or not 0.0 <= x <= 1.0:
        raise ValueError("x must be between 0 and 1")
    if x == 0.0:
        return 0.0
    if x == 1.0:
        return 1.0
    front = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _beta_fraction(a, b, x) / a
    return 1.0 - front * _beta_fraction(b, a, 1.0 - x) / b


def beta_quantile(probability: float, alpha: float, beta: float) -> float:
    """Numerically invert a Beta CDF by bisection for a central credible interval."""
    probability = _validate_probability(probability, "quantile probability")
    _validate_positive(alpha, "alpha")
    _validate_positive(beta, "beta")
    if probability == 0.0:
        return 0.0
    if probability == 1.0:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if regularized_beta(mid, alpha, beta) < probability:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


@dataclass(frozen=True)
class BetaBinomialPosterior:
    alpha: float
    beta: float
    successes: int
    trials: int
    mean: float
    credible_mass: float
    credible_interval: tuple[float, float]


def beta_binomial_posterior(
    alpha: float,
    beta: float,
    successes: int,
    trials: int,
    *,
    credible_mass: float = 0.95,
) -> BetaBinomialPosterior:
    """Return Beta-Binomial posterior moments and an equal-tailed credible interval."""
    alpha, beta = _validate_positive(alpha, "alpha"), _validate_positive(beta, "beta")
    if isinstance(trials, bool) or isinstance(successes, bool) or not isinstance(trials, int) or not isinstance(successes, int):
        raise TypeError("successes and trials must be integers")
    if trials < 0 or successes < 0 or successes > trials:
        raise ValueError("require 0 <= successes <= trials")
    credible_mass = _validate_probability(credible_mass, "credible_mass")
    if credible_mass <= 0.0:
        raise ValueError("credible_mass must be greater than zero")
    post_a, post_b = alpha + successes, beta + trials - successes
    tail = (1.0 - credible_mass) / 2.0
    interval = (beta_quantile(tail, post_a, post_b), beta_quantile(1.0 - tail, post_a, post_b))
    return BetaBinomialPosterior(
        post_a, post_b, successes, trials,
        post_a / (post_a + post_b), credible_mass, interval,
    )


@dataclass(frozen=True)
class ReferenceClassPolicy:
    minimum_sample_size: int
    heterogeneity_status: str
    interval_level: float = 0.95

    def __post_init__(self) -> None:
        if isinstance(self.minimum_sample_size, bool) or not isinstance(self.minimum_sample_size, int) or self.minimum_sample_size < 1:
            raise ValueError("minimum_sample_size must be an explicit positive integer for this use")
        if self.heterogeneity_status not in ("acceptable", "too_heterogeneous", "unassessed"):
            raise ValueError("heterogeneity_status must be acceptable, too_heterogeneous, or unassessed")
        if not math.isfinite(self.interval_level) or not 0.0 < self.interval_level < 1.0:
            raise ValueError("interval_level must be between 0 and 1")


def _wilson_confidence_interval(events: int, sample_size: int, confidence_level: float) -> tuple[float, float]:
    z = statistics.NormalDist().inv_cdf((1.0 + confidence_level) / 2.0)
    rate = events / sample_size
    denominator = 1.0 + z * z / sample_size
    center = (rate + z * z / (2.0 * sample_size)) / denominator
    margin = z * math.sqrt(rate * (1.0 - rate) / sample_size + z * z / (4.0 * sample_size * sample_size)) / denominator
    return max(0.0, center - margin), min(1.0, center + margin)


@dataclass(frozen=True)
class ReferenceClassSummary:
    status: str
    definition: str | None
    sample_size: int
    event_count: int
    observed_rate: float | None
    empirical_rate: float | None
    uncertainty_interval: tuple[float, float] | None = None
    uncertainty_interval_kind: str | None = None
    posterior: BetaBinomialPosterior | None = None
    limitation: str | None = None


def reference_class_summary(
    *,
    definition: str | None,
    event_count: int,
    sample_size: int,
    inclusion_logic: str,
    comparability_limitations: str,
    policy: ReferenceClassPolicy,
    prior: tuple[float, float] | None = None,
) -> ReferenceClassSummary:
    """Summarize supplied outcomes and gate forecast use on explicit class policy."""
    if (isinstance(sample_size, bool) or isinstance(event_count, bool) or
            not isinstance(sample_size, int) or not isinstance(event_count, int) or
            sample_size < 0 or event_count < 0 or event_count > sample_size):
        raise ValueError("require 0 <= event_count <= sample_size")
    if definition is None or not definition.strip():
        return ReferenceClassSummary(
            "unavailable", None, sample_size, event_count, None, None,
            limitation="no defensible class definition was supplied",
        )
    if not inclusion_logic.strip():
        raise ValueError("inclusion_logic must disclose which cases entered the class")
    if sample_size == 0:
        return ReferenceClassSummary(
            "unavailable", definition, 0, 0, None, None,
            limitation="the defined class has no resolved outcomes",
        )
    observed_rate = event_count / sample_size
    if sample_size < policy.minimum_sample_size:
        return ReferenceClassSummary(
            "too_small", definition, sample_size, event_count, observed_rate, None,
            limitation=f"sample size is below the use-specific threshold of {policy.minimum_sample_size}; observed frequency is descriptive only",
        )
    if policy.heterogeneity_status != "acceptable":
        status = "too_heterogeneous" if policy.heterogeneity_status == "too_heterogeneous" else "unavailable"
        return ReferenceClassSummary(
            status, definition, sample_size, event_count, observed_rate, None,
            limitation="comparability was not accepted under the declared reference-class policy",
        )
    posterior = beta_binomial_posterior(*prior, event_count, sample_size,
                                        credible_mass=policy.interval_level) if prior is not None else None
    uncertainty_interval = (posterior.credible_interval if posterior is not None else
                            _wilson_confidence_interval(event_count, sample_size, policy.interval_level))
    return ReferenceClassSummary(
        "available", definition, sample_size, event_count, observed_rate, observed_rate,
        uncertainty_interval,
        "credible" if posterior is not None else "Wilson_confidence",
        posterior,
        comparability_limitations or "comparability limitations were not supplied",
    )


def _logit(probability: float) -> float:
    probability = _validate_probability(probability)
    if probability == 0.0:
        return -math.inf
    if probability == 1.0:
        return math.inf
    return math.log(probability) - math.log1p(-probability)


def _expit(value: float) -> float:
    if value >= 0:
        exp_value = math.exp(-value) if value < 746 else 0.0
        return 1.0 / (1.0 + exp_value)
    exp_value = math.exp(value) if value > -746 else 0.0
    return exp_value / (1.0 + exp_value)


def bayesian_odds_update(
    prior_probability: float,
    likelihood_ratios: Sequence[float],
    *,
    dependence: str = "single",
) -> float:
    """Update prior odds using supplied likelihood ratios.

    Multiple LRs require an explicit conditional-independence assertion. The
    function intentionally cannot infer or generate an LR from qualitative text.
    """
    prior_probability = _validate_probability(prior_probability, "prior_probability")
    ratios = tuple(_validate_positive(lr, "likelihood ratio") for lr in likelihood_ratios)
    if not ratios:
        raise ValueError("at least one likelihood ratio is required")
    if len(ratios) > 1 and dependence != "conditionally_independent":
        raise ValueError("multiple likelihood ratios require explicit conditional_independence handling")
    if prior_probability in (0.0, 1.0):
        return prior_probability
    posterior_log_odds = _logit(prior_probability) + math.fsum(math.log(lr) for lr in ratios)
    return _expit(posterior_log_odds)


@dataclass(frozen=True)
class EvidenceSignal:
    signal_id: str
    source_family: str | None = None
    causal_origin: str | None = None
    underlying_measure: str | None = None


@dataclass(frozen=True)
class EvidenceDependence:
    clusters: tuple[tuple[str, ...], ...]
    status: str
    shared_basis: tuple[str, ...]


def classify_evidence_dependence(signals: Sequence[EvidenceSignal]) -> EvidenceDependence:
    """Group signals with declared shared sources/origins; absence is unknown."""
    if not signals:
        raise ValueError("at least one evidence signal is required")
    if len({s.signal_id for s in signals}) != len(signals):
        raise ValueError("signal_id values must be unique")
    parents = list(range(len(signals)))

    def root(index: int) -> int:
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index

    def join(left: int, right: int) -> None:
        parents[root(left)] = root(right)

    seen: dict[tuple[str, str], int] = {}
    shared: set[str] = set()
    for index, signal in enumerate(signals):
        for field_name in ("source_family", "causal_origin", "underlying_measure"):
            value = getattr(signal, field_name)
            if value:
                key = (field_name, value)
                if key in seen:
                    join(index, seen[key])
                    shared.add(field_name)
                else:
                    seen[key] = index
    grouped: dict[int, list[str]] = {}
    for index, signal in enumerate(signals):
        grouped.setdefault(root(index), []).append(signal.signal_id)
    clusters = tuple(tuple(ids) for ids in grouped.values())
    complete_provenance = all(s.source_family and s.causal_origin and s.underlying_measure for s in signals)
    unique_provenance = all(
        len({getattr(s, field_name) for s in signals}) == len(signals)
        for field_name in ("source_family", "causal_origin", "underlying_measure")
    ) if complete_provenance else False
    status = "shared_or_overlapping" if len(clusters) < len(signals) else (
        "distinct_sources_still_require_independence_review" if unique_provenance else "unknown_dependence"
    )
    return EvidenceDependence(clusters, status, tuple(sorted(shared)))


@dataclass(frozen=True)
class QuantileElicitation:
    values: Mapping[str, float]
    elicitation_record: str
    protocol_label: str


def validate_quantile_elicitation(
    values: Mapping[str, float],
    *,
    elicitation_record: str,
    protocol_label: str,
    probability_quantity: bool = False,
) -> QuantileElicitation:
    """Validate raw elicited quantiles without fitting or hiding disagreement."""
    order = ("q05", "q25", "q50", "q75", "q95")
    if not values:
        raise ValueError("at least one elicited quantile is required")
    keys = [key for key in order if key in values]
    if len(keys) != len(values):
        raise ValueError("use supported quantile labels q05, q25, q50, q75, q95")
    if any(not math.isfinite(float(values[key])) for key in keys):
        raise ValueError("elicited values must be finite")
    if probability_quantity and any(not 0.0 <= float(values[key]) <= 1.0 for key in keys):
        raise ValueError("elicited event probabilities must lie between 0 and 1")
    if any(float(values[left]) > float(values[right]) for left, right in zip(keys, keys[1:])):
        raise ValueError("elicited quantiles must be nondecreasing")
    if not elicitation_record.strip() or not protocol_label.strip():
        raise ValueError("retain a record and an accurate protocol label")
    return QuantileElicitation(dict(values), elicitation_record, protocol_label)


@dataclass(frozen=True)
class AggregatedEstimate:
    mean: float
    median: float
    minimum: float
    maximum: float
    dispersion: float
    weights: tuple[float, ...]
    estimator_count: int
    preserved_estimates: tuple[float, ...]


def aggregate_estimates(
    estimates: Sequence[float],
    *,
    weights: Sequence[float] | None = None,
    performance_weighted: bool = False,
    comparable_resolved_history: bool = False,
    out_of_sample_evaluation: bool = False,
) -> AggregatedEstimate:
    """Aggregate estimates while preserving their full spread and raw values."""
    values = tuple(_validate_probability(p, "estimate") for p in estimates)
    if not values:
        raise ValueError("at least one estimate is required")
    if performance_weighted and not (comparable_resolved_history and out_of_sample_evaluation):
        raise ValueError("performance weighting requires comparable resolved history and out-of-sample evaluation")
    if weights is None:
        normalized = tuple(1.0 / len(values) for _ in values)
    else:
        supplied = tuple(_validate_positive(w, "weight") for w in weights)
        if len(supplied) != len(values):
            raise ValueError("weights and estimates must have equal length")
        total = math.fsum(supplied)
        normalized = tuple(w / total for w in supplied)
    mean = math.fsum(weight * value for weight, value in zip(normalized, values))
    return AggregatedEstimate(
        mean, statistics.median(values), min(values), max(values), max(values) - min(values),
        normalized, len(values), values,
    )


@dataclass(frozen=True)
class MonteCarloSummary:
    samples: tuple[float, ...]
    mean: float
    median: float
    intervals: Mapping[float, tuple[float, float]]
    simulation_count: int
    seed: int


def monte_carlo_bayesian_update(
    prior_sampler: Callable[[random.Random], float],
    likelihood_ratio_samplers: Sequence[Callable[[random.Random], float]],
    *,
    simulation_count: int,
    seed: int,
    dependence: str = "single",
    interval_masses: Sequence[float] = (0.50, 0.80, 0.95),
) -> MonteCarloSummary:
    """Propagate caller-supplied uncertain inputs with an explicit reproducible seed."""
    if isinstance(simulation_count, bool) or not isinstance(simulation_count, int) or simulation_count < 1:
        raise ValueError("simulation_count must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise TypeError("seed must be an integer when reproducibility is required")
    if not likelihood_ratio_samplers:
        raise ValueError("at least one likelihood-ratio sampler is required")
    if len(likelihood_ratio_samplers) > 1 and dependence != "conditionally_independent":
        raise ValueError("multiple sampled likelihoods require explicit conditional independence")
    masses = tuple(_validate_probability(m, "interval mass") for m in interval_masses)
    if any(m == 0.0 for m in masses):
        raise ValueError("interval masses must be greater than zero")
    rng = random.Random(seed)
    samples: list[float] = []
    for _ in range(simulation_count):
        prior = _validate_probability(prior_sampler(rng), "sampled prior")
        ratios = [_validate_positive(sampler(rng), "sampled likelihood ratio") for sampler in likelihood_ratio_samplers]
        samples.append(bayesian_odds_update(prior, ratios, dependence=dependence if len(ratios) > 1 else "single"))
    ordered = sorted(samples)

    def empirical_quantile(q: float) -> float:
        index = q * (len(ordered) - 1)
        lo = math.floor(index)
        hi = math.ceil(index)
        if lo == hi:
            return ordered[lo]
        return ordered[lo] * (hi - index) + ordered[hi] * (index - lo)

    intervals = {
        mass: (empirical_quantile((1 - mass) / 2), empirical_quantile(1 - (1 - mass) / 2))
        for mass in masses
    }
    return MonteCarloSummary(tuple(samples), statistics.fmean(samples), statistics.median(samples), intervals, simulation_count, seed)


def expected_utility(state_probabilities: Mapping[str, float], utilities: Mapping[str, float]) -> float:
    """Compute expected utility from explicit conditional state probabilities and utilities."""
    if set(state_probabilities) != set(utilities) or not state_probabilities:
        raise ValueError("probability and utility mappings must have the same non-empty states")
    probabilities = {state: _validate_probability(p, f"P({state})") for state, p in state_probabilities.items()}
    if not math.isclose(math.fsum(probabilities.values()), 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValueError("state probabilities must sum to 1")
    if any(not math.isfinite(float(value)) for value in utilities.values()):
        raise ValueError("utilities must be finite and explicitly supplied")
    return math.fsum(probabilities[state] * float(utilities[state]) for state in probabilities)
