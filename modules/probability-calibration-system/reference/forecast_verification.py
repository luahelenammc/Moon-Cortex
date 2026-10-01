# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Forecast records, scoring, diagnostics, sufficiency gates, and recalibration."""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, replace
from datetime import date
from enum import Enum
from typing import Sequence

from .probability_calibration import _validate_probability


class ForecastStatus(str, Enum):
    PENDING = "pending"
    RESOLVED_YES = "resolved_yes"
    RESOLVED_NO = "resolved_no"
    UNRESOLVED = "unresolved"
    INVALIDATED = "invalidated"
    AMBIGUOUS = "ambiguous"
    CANCELLED = "cancelled"
    SUPERSEDED = "superseded"


@dataclass(frozen=True)
class ForecastRevision:
    at: str
    field: str
    old_value: str
    new_value: str
    reason: str


@dataclass(frozen=True)
class ForecastRecord:
    forecast_id: str
    created_at: str
    target_event: str
    resolution_criteria: str
    domain: str
    horizon: str
    as_of: str
    quantification_class: str
    raw_probability: float | None = None
    final_probability: float | None = None
    qualitative_band: str | None = None
    confidence: str | None = None
    reference_class: str | None = None
    method: str | None = None
    evidence_snapshot: str = ""
    assumptions: tuple[str, ...] = ()
    update_triggers: tuple[str, ...] = ()
    status: ForecastStatus = ForecastStatus.PENDING
    resolution: int | None = None
    resolved_at: str | None = None
    resolution_reason: str | None = None
    revisions: tuple[ForecastRevision, ...] = ()

    def __post_init__(self) -> None:
        for name in ("forecast_id", "created_at", "target_event", "resolution_criteria", "domain", "horizon", "as_of", "quantification_class"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} is required")
        if self.raw_probability is not None:
            _validate_probability(self.raw_probability, "raw_probability")
        if self.final_probability is not None:
            _validate_probability(self.final_probability, "final_probability")
        if self.status is ForecastStatus.PENDING and (self.resolution is not None or self.resolved_at is not None):
            raise ValueError("pending forecasts cannot contain a resolution")
        if self.status in (ForecastStatus.RESOLVED_YES, ForecastStatus.RESOLVED_NO):
            expected = 1 if self.status is ForecastStatus.RESOLVED_YES else 0
            if self.resolution != expected or not self.resolved_at:
                raise ValueError("resolved forecasts require a matching outcome and resolved_at")


def resolve_forecast(
    record: ForecastRecord,
    status: ForecastStatus,
    *,
    resolved_at: str,
    reason: str,
) -> ForecastRecord:
    """Resolve once; never rewrite the forecast-time target or criteria."""
    if record.status is not ForecastStatus.PENDING:
        raise ValueError("only pending forecasts may be resolved")
    if status is ForecastStatus.PENDING:
        raise ValueError("resolution status cannot remain pending")
    if not resolved_at.strip() or not reason.strip():
        raise ValueError("resolution time and reason must be retained")
    if status is ForecastStatus.RESOLVED_YES:
        outcome = 1
    elif status is ForecastStatus.RESOLVED_NO:
        outcome = 0
    else:
        outcome = None
    return replace(record, status=status, resolution=outcome, resolved_at=resolved_at, resolution_reason=reason)


def revise_forecast_metadata(record: ForecastRecord, revision: ForecastRevision) -> ForecastRecord:
    """Append an auditable metadata revision; forecast-time criteria remain immutable."""
    if not revision.at.strip() or not revision.reason.strip() or not revision.field.strip():
        raise ValueError("revision time, field, and reason are required")
    if revision.field == "resolution_criteria":
        raise ValueError("resolution criteria are immutable after forecast creation; supersede instead")
    return replace(record, revisions=record.revisions + (revision,))


def scoreable_observations(records: Sequence[ForecastRecord]) -> tuple[tuple[float, ...], tuple[int, ...]]:
    """Return only resolved binary forecasts with a stored pre-resolution probability."""
    probabilities: list[float] = []
    outcomes: list[int] = []
    for record in records:
        if record.status not in (ForecastStatus.RESOLVED_YES, ForecastStatus.RESOLVED_NO):
            continue
        probability = record.final_probability if record.final_probability is not None else record.raw_probability
        if probability is None:
            continue  # qualitative-only records remain valid, but are not numerically scoreable
        probabilities.append(_validate_probability(probability))
        outcomes.append(int(record.resolution))
    return tuple(probabilities), tuple(outcomes)


@dataclass(frozen=True)
class GroupedScore:
    dimension: str
    value: str
    count: int
    brier: float
    log_loss: float
    status: str


def grouped_score_summary(
    records: Sequence[ForecastRecord],
    *,
    dimension: str,
    minimum_group_size: int,
) -> tuple[GroupedScore, ...]:
    """Summarize resolved numerical forecasts by a declared dimension and size policy."""
    allowed = {"domain", "horizon", "quantification_class", "confidence"}
    if dimension not in allowed:
        raise ValueError(f"dimension must be one of {sorted(allowed)}")
    if isinstance(minimum_group_size, bool) or not isinstance(minimum_group_size, int) or minimum_group_size < 1:
        raise ValueError("minimum_group_size must be an explicit positive policy threshold")
    groups: dict[str, list[ForecastRecord]] = {}
    for record in records:
        ps, _ = scoreable_observations([record])
        if not ps:
            continue
        value = getattr(record, dimension)
        key = str(value) if value is not None else "unknown"
        groups.setdefault(key, []).append(record)
    result: list[GroupedScore] = []
    for value, group in sorted(groups.items()):
        probabilities, outcomes = scoreable_observations(group)
        result.append(GroupedScore(
            dimension, value, len(probabilities), brier_score(probabilities, outcomes),
            log_loss(probabilities, outcomes),
            "diagnostic_ready" if len(probabilities) >= minimum_group_size else "exploratory_only",
        ))
    return tuple(result)


def _validate_forecast_arrays(probabilities: Sequence[float], outcomes: Sequence[int]) -> tuple[tuple[float, ...], tuple[int, ...]]:
    ps = tuple(_validate_probability(p, "forecast probability") for p in probabilities)
    ys = tuple(outcomes)
    if not ps or len(ps) != len(ys):
        raise ValueError("probabilities and outcomes must be non-empty and equal length")
    if any(isinstance(y, bool) or y not in (0, 1) for y in ys):
        raise ValueError("outcomes must be binary integers 0 or 1")
    return ps, tuple(int(y) for y in ys)


def brier_score(probabilities: Sequence[float], outcomes: Sequence[int]) -> float:
    """Mean squared probability error; lower is better."""
    ps, ys = _validate_forecast_arrays(probabilities, outcomes)
    return math.fsum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ps)


def brier_skill_score(model_brier: float, reference_brier: float) -> float:
    """Compare a model with a declared reference score; positive means improvement."""
    if not math.isfinite(model_brier) or not 0.0 <= model_brier <= 1.0:
        raise ValueError("model_brier must lie between 0 and 1")
    if not math.isfinite(reference_brier) or not 0.0 < reference_brier <= 1.0:
        raise ValueError("reference_brier must be greater than 0 and at most 1")
    return 1.0 - model_brier / reference_brier


def log_loss(probabilities: Sequence[float], outcomes: Sequence[int], *, clip: float = 1e-15) -> float:
    """Mean negative log score with explicit score-only clipping of exact 0/1."""
    ps, ys = _validate_forecast_arrays(probabilities, outcomes)
    clip = float(clip)
    if not math.isfinite(clip) or not 0.0 < clip < 0.5:
        raise ValueError("clip must be finite and strictly between 0 and 0.5")
    terms = []
    for p, y in zip(ps, ys):
        score_p = min(max(p, clip), 1.0 - clip)
        terms.append(-(y * math.log(score_p) + (1 - y) * math.log1p(-score_p)))
    return math.fsum(terms) / len(terms)


@dataclass(frozen=True)
class ReliabilityBin:
    lower: float
    upper: float
    count: int
    mean_forecast: float
    observed_frequency: float
    interval: tuple[float, float]


def _wilson_interval(events: int, count: int, confidence_level: float) -> tuple[float, float]:
    from statistics import NormalDist

    z = NormalDist().inv_cdf((1.0 + confidence_level) / 2.0)
    rate = events / count
    denominator = 1.0 + z * z / count
    center = (rate + z * z / (2.0 * count)) / denominator
    margin = z * math.sqrt(rate * (1.0 - rate) / count + z * z / (4.0 * count * count)) / denominator
    return max(0.0, center - margin), min(1.0, center + margin)


def reliability_bins(
    probabilities: Sequence[float],
    outcomes: Sequence[int],
    *,
    bins: int = 10,
    adaptive: bool = False,
    confidence_level: float = 0.95,
) -> tuple[ReliabilityBin, ...]:
    """Return plotting-ready reliability data with Wilson intervals per nonempty bin."""
    ps, ys = _validate_forecast_arrays(probabilities, outcomes)
    if isinstance(bins, bool) or not isinstance(bins, int) or bins < 1:
        raise ValueError("bins must be a positive integer")
    if not 0.0 < confidence_level < 1.0:
        raise ValueError("confidence_level must be between 0 and 1")
    pairs = sorted(zip(ps, ys), key=lambda pair: pair[0])
    groups: list[list[tuple[float, int]]] = []
    if adaptive:
        width = math.ceil(len(pairs) / bins)
        groups = [pairs[i:i + width] for i in range(0, len(pairs), width)]
    else:
        groups = [[] for _ in range(bins)]
        for pair in pairs:
            index = min(int(pair[0] * bins), bins - 1)
            groups[index].append(pair)
    result: list[ReliabilityBin] = []
    for index, group in enumerate(groups):
        if not group:
            continue
        forecasts, observations = zip(*group)
        events = sum(observations)
        lower = min(forecasts) if adaptive else index / bins
        upper = max(forecasts) if adaptive else (index + 1) / bins
        result.append(ReliabilityBin(
            lower, upper, len(group), statistics.fmean(forecasts), events / len(group),
            _wilson_interval(events, len(group), confidence_level),
        ))
    return tuple(result)


@dataclass(frozen=True)
class BrierDecomposition:
    brier: float
    reliability: float
    resolution: float
    uncertainty: float
    base_rate: float


def brier_decomposition(probabilities: Sequence[float], outcomes: Sequence[int]) -> BrierDecomposition:
    """Exact sample decomposition by identical issued probability values."""
    ps, ys = _validate_forecast_arrays(probabilities, outcomes)
    base_rate = statistics.fmean(ys)
    groups: dict[float, list[int]] = {}
    for probability, outcome in zip(ps, ys):
        groups.setdefault(probability, []).append(outcome)
    reliability = 0.0
    resolution = 0.0
    for probability, group_outcomes in groups.items():
        weight = len(group_outcomes) / len(ps)
        observed = statistics.fmean(group_outcomes)
        reliability += weight * (probability - observed) ** 2
        resolution += weight * (observed - base_rate) ** 2
    uncertainty = base_rate * (1.0 - base_rate)
    return BrierDecomposition(brier_score(ps, ys), reliability, resolution, uncertainty, base_rate)


@dataclass(frozen=True)
class ForecastSpread:
    count: int
    mean: float
    standard_deviation: float
    minimum: float
    maximum: float
    mean_binary_entropy: float


def forecast_spread_summary(probabilities: Sequence[float]) -> ForecastSpread:
    """Describe spread and entropy; this is not a reward for extreme forecasts."""
    ps = tuple(_validate_probability(p) for p in probabilities)
    if not ps:
        raise ValueError("at least one probability is required")
    entropies = []
    for p in ps:
        if p in (0.0, 1.0):
            entropies.append(0.0)
        else:
            entropies.append(-(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p)))
    stdev = statistics.stdev(ps) if len(ps) > 1 else 0.0
    return ForecastSpread(len(ps), statistics.fmean(ps), stdev, min(ps), max(ps), statistics.fmean(entropies))


@dataclass(frozen=True)
class DataSufficiencyPolicy:
    minimum_resolved: int
    minimum_events: int
    minimum_nonevents: int
    minimum_occupied_probability_bins: int
    minimum_forecasts_per_occupied_bin: int
    probability_bin_count: int
    minimum_holdout_size: int

    def __post_init__(self) -> None:
        values = (self.minimum_resolved, self.minimum_events, self.minimum_nonevents,
                  self.minimum_occupied_probability_bins, self.minimum_forecasts_per_occupied_bin,
                  self.probability_bin_count, self.minimum_holdout_size)
        if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in values):
            raise ValueError("sufficiency policy thresholds must be nonnegative integers")
        if self.probability_bin_count < 1:
            raise ValueError("probability_bin_count must be positive")


@dataclass(frozen=True)
class DataSufficiency:
    status: str
    resolved_count: int
    event_count: int
    nonevent_count: int
    occupied_bins: int
    limitations: tuple[str, ...]


def assess_data_sufficiency(
    probabilities: Sequence[float],
    outcomes: Sequence[int],
    policy: DataSufficiencyPolicy,
    *,
    holdout_size: int = 0,
) -> DataSufficiency:
    """Apply caller-selected thresholds; no universal sample-size default is embedded."""
    if not probabilities and not outcomes:
        return DataSufficiency("insufficient_data", 0, 0, 0, 0, ("no resolved forecast history",))
    ps, ys = _validate_forecast_arrays(probabilities, outcomes)
    if holdout_size < 0 or holdout_size > len(ps):
        raise ValueError("holdout_size must be between zero and the resolved count")
    events, nonevents = sum(ys), len(ys) - sum(ys)
    bin_counts = [0] * policy.probability_bin_count
    for p in ps:
        bin_counts[min(int(p * policy.probability_bin_count), policy.probability_bin_count - 1)] += 1
    occupied = sum(count > 0 for count in bin_counts)
    limitations: list[str] = []
    if len(ps) < policy.minimum_resolved:
        limitations.append("resolved count is below the configured diagnostic threshold")
    if events < policy.minimum_events or nonevents < policy.minimum_nonevents:
        limitations.append("event prevalence is too sparse for the configured policy")
    if occupied < policy.minimum_occupied_probability_bins or any(
        count < policy.minimum_forecasts_per_occupied_bin for count in bin_counts if count > 0
    ):
        limitations.append("probability coverage is too narrow or sparse under the configured bins")
    if limitations:
        status = "exploratory_only" if ps else "insufficient_data"
    elif holdout_size >= policy.minimum_holdout_size and holdout_size > 0:
        status = "recalibration_candidate"
    else:
        status = "diagnostic_ready"
        limitations.append("no policy-sized held-out sample was supplied for recalibration")
    return DataSufficiency(status, len(ps), events, nonevents, occupied, tuple(limitations))


@dataclass(frozen=True)
class RecalibrationPolicy:
    minimum_validation_size: int
    method: str
    training_window: str
    data_scope: str
    validation_strategy: str
    sufficiency_policy: DataSufficiencyPolicy
    training_end: str | None = None
    validation_start: str | None = None

    def __post_init__(self) -> None:
        if isinstance(self.minimum_validation_size, bool) or not isinstance(self.minimum_validation_size, int) or self.minimum_validation_size < 1:
            raise ValueError("minimum_validation_size must be a positive integer selected for the use case")
        if self.method not in ("isotonic", "platt"):
            raise ValueError("supported methods are isotonic and platt")
        if not self.training_window.strip() or not self.data_scope.strip():
            raise ValueError("training window and domain/horizon data scope are required")
        if self.validation_strategy not in ("temporal_holdout", "holdout", "cross_validation"):
            raise ValueError("state temporal_holdout, holdout, or cross_validation validation")
        if self.validation_strategy == "temporal_holdout":
            if not self.training_end or not self.validation_start:
                raise ValueError("temporal validation requires training_end and validation_start")
            if date.fromisoformat(self.training_end) >= date.fromisoformat(self.validation_start):
                raise ValueError("training data must end before the validation window begins")


@dataclass(frozen=True)
class RecalibrationResult:
    status: str
    method: str
    data_scope: str
    training_window: str
    training_size: int
    validation_size: int
    model_parameters: tuple[float, ...] = ()
    raw_validation_probabilities: tuple[float, ...] = ()
    recalibrated_validation_probabilities: tuple[float, ...] = ()
    raw_validation_brier: float | None = None
    recalibrated_validation_brier: float | None = None
    limitations: tuple[str, ...] = ()


def _fit_isotonic(probabilities: Sequence[float], outcomes: Sequence[int]) -> tuple[tuple[float, float], ...]:
    grouped: dict[float, list[int]] = {}
    for probability, outcome in zip(probabilities, outcomes):
        values = grouped.setdefault(float(probability), [0, 0])
        values[0] += int(outcome)
        values[1] += 1
    ordered = [(probability, values[0], values[1]) for probability, values in sorted(grouped.items())]
    blocks: list[list[float]] = []  # [x_max, outcome_sum, count]
    for probability, outcome_sum, count in ordered:
        blocks.append([float(probability), float(outcome_sum), float(count)])
        while len(blocks) > 1 and blocks[-2][1] / blocks[-2][2] > blocks[-1][1] / blocks[-1][2]:
            right = blocks.pop()
            left = blocks.pop()
            blocks.append([right[0], left[1] + right[1], left[2] + right[2]])
    return tuple((block[0], block[1] / block[2]) for block in blocks)


def _apply_isotonic(model: Sequence[tuple[float, float]], probability: float) -> float:
    for upper, fitted in model:
        if probability <= upper:
            return fitted
    return model[-1][1]


def _fit_platt(probabilities: Sequence[float], outcomes: Sequence[int]) -> tuple[float, float]:
    epsilon = 1e-12
    xs = [math.log(p / (1.0 - p)) for p in (min(max(value, epsilon), 1.0 - epsilon) for value in probabilities)]
    prevalence = min(max(statistics.fmean(outcomes), epsilon), 1.0 - epsilon)
    intercept, slope = math.log(prevalence / (1.0 - prevalence)), 1.0

    def loss(a: float, b: float) -> float:
        result = 0.0
        for x, y in zip(xs, outcomes):
            z = a + b * x
            result += max(z, 0.0) - y * z + math.log1p(math.exp(-abs(z)))
        return result

    current_loss = loss(intercept, slope)
    for _ in range(100):
        gradient_a = gradient_b = h_aa = h_ab = h_bb = 0.0
        for x, y in zip(xs, outcomes):
            q = 1.0 / (1.0 + math.exp(-max(min(intercept + slope * x, 700.0), -700.0)))
            weight = q * (1.0 - q)
            error = q - y
            gradient_a += error
            gradient_b += error * x
            h_aa += weight
            h_ab += weight * x
            h_bb += weight * x * x
        damping = 1e-10
        h_aa += damping
        h_bb += damping
        determinant = h_aa * h_bb - h_ab * h_ab
        if determinant <= 1e-20:
            break
        step_a = (h_bb * gradient_a - h_ab * gradient_b) / determinant
        step_b = (-h_ab * gradient_a + h_aa * gradient_b) / determinant
        scale = 1.0
        accepted = False
        while scale >= 1e-8:
            next_a = intercept - scale * step_a
            next_b = slope - scale * step_b
            next_loss = loss(next_a, next_b)
            if next_loss <= current_loss:
                intercept, slope, current_loss = next_a, next_b, next_loss
                accepted = True
                break
            scale /= 2.0
        if not accepted or max(abs(scale * step_a), abs(scale * step_b)) < 1e-8:
            break
    return intercept, slope


def _apply_platt(parameters: tuple[float, float], probability: float) -> float:
    epsilon = 1e-12
    p = min(max(probability, epsilon), 1.0 - epsilon)
    z = parameters[0] + parameters[1] * math.log(p / (1.0 - p))
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-min(z, 746.0)))
    exp_z = math.exp(max(z, -746.0))
    return exp_z / (1.0 + exp_z)


def evaluate_recalibration(
    training_probabilities: Sequence[float],
    training_outcomes: Sequence[int],
    validation_probabilities: Sequence[float],
    validation_outcomes: Sequence[int],
    *,
    training_forecast_ids: Sequence[str],
    validation_forecast_ids: Sequence[str],
    policy: RecalibrationPolicy,
) -> RecalibrationResult:
    """Fit on one forecast set, evaluate only on a disjoint held-out set."""
    if set(training_forecast_ids) & set(validation_forecast_ids):
        raise ValueError("training and validation forecast IDs must be disjoint to prevent leakage")
    if len(training_forecast_ids) != len(training_probabilities) or len(validation_forecast_ids) != len(validation_probabilities):
        raise ValueError("forecast ID arrays must align with their probability arrays")
    train_p, train_y = _validate_forecast_arrays(training_probabilities, training_outcomes)
    valid_p, valid_y = _validate_forecast_arrays(validation_probabilities, validation_outcomes)
    if len(training_forecast_ids) != len(train_p) or len(validation_forecast_ids) != len(valid_p):
        raise ValueError("forecast IDs, probabilities, and outcomes must align")
    readiness = assess_data_sufficiency(
        train_p, train_y, policy.sufficiency_policy, holdout_size=len(valid_p),
    )
    if len(valid_p) < policy.minimum_validation_size or readiness.status != "recalibration_candidate":
        limitations = list(readiness.limitations)
        if len(valid_p) < policy.minimum_validation_size:
            limitations.append("held-out validation count is below the configured threshold")
        return RecalibrationResult(
            "unavailable_insufficient_history", policy.method, policy.data_scope, policy.training_window,
            len(train_p), len(valid_p), raw_validation_probabilities=valid_p,
            limitations=tuple(limitations or ("configured data sufficiency policy was not met",)),
        )
    if policy.method == "isotonic":
        model = _fit_isotonic(train_p, train_y)
        recalibrated = tuple(_apply_isotonic(model, p) for p in valid_p)
        parameters = tuple(value for pair in model for value in pair)
    else:
        model = _fit_platt(train_p, train_y)
        recalibrated = tuple(_apply_platt(model, p) for p in valid_p)
        parameters = model
    return RecalibrationResult(
        "evaluated_out_of_sample", policy.method, policy.data_scope, policy.training_window,
        len(train_p), len(valid_p), parameters, valid_p, recalibrated,
        brier_score(valid_p, valid_y), brier_score(recalibrated, valid_y),
        ("recalibrated probabilities are validation predictions; raw inputs remain unchanged",),
    )
