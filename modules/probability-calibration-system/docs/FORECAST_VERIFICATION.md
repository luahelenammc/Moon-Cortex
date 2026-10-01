<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Forecast Verification

**MSL profile:** 5.1-compatible verification contract; issue-time forecasts, outcomes, validation data, and derived model values remain separately traceable.

Empirical verification begins by logging forecasts before their outcomes. At cold start, methods and tooling exist but empirical calibration is unavailable.

## Forecast Ledger schema

The following public-safe schema is reusable. It is a template, not a hosted service. Actual Moon-specific or other private forecasts remain local.

~~~yaml
forecast_id:
created_at:
target_event:
resolution_criteria:
domain:
horizon:
as_of:
quantification_class:
raw_probability:
final_probability:
qualitative_band:
confidence:
reference_class:
method:
evidence_snapshot:
assumptions:
update_triggers:
status: pending
resolution:
resolved_at:
resolution_reason:
revisions: []
~~~

Define resolution criteria at forecast time. Preserve the issued raw probability even when a later model supplies a final recalibrated probability. Version metadata edits and their reasons. Do not revise the original target after seeing the outcome; if the target changes, supersede the forecast and issue a new one.

## Resolution semantics

Supported statuses are:

- **pending** — the event horizon has not resolved;
- **resolved_yes** — predeclared criteria establish the event occurred; outcome is 1;
- **resolved_no** — predeclared criteria establish it did not; outcome is 0;
- **unresolved** — the evidence or criteria do not settle it;
- **invalidated** — the forecast target became unusable under its policy;
- **ambiguous** — available evidence conflicts or the rule cannot classify the event;
- **cancelled** — the target was withdrawn before resolution;
- **superseded** — a new forecast replaced this one.

Retain resolution time and reason. Score only valid resolved yes/no numeric forecasts. Exclude qualitative-only, pending, unresolved, ambiguous, invalidated, cancelled, and superseded records under a declared policy. Never force an ambiguous event into 0 or 1.

## Scores

For N valid resolved binary forecasts, issued probabilities p and outcomes y:

~~~text
Brier = (1/N) × sum((pᵢ - yᵢ)²)
~~~

Lower is better. Report scope and sample size; stratify by domain, horizon, quantification class, or confidence only when the sample supports interpretation.

When a legitimate reference forecast is available:

~~~text
Brier Skill Score = 1 - Brier_model / Brier_reference
~~~

Positive means better than that reference; zero means no improvement; negative means worse. State the reference and do not choose a deliberately weak comparator.

The secondary logarithmic loss is:

~~~text
LogLoss = -(1/N) × sum(yᵢ log(pᵢ) + (1-yᵢ) log(1-pᵢ))
~~~

It penalizes confident errors strongly. The implementation clips exact 0 or 1 only for score calculation, under an explicit clip value; the stored forecast remains unchanged.

## Reliability, resolution, and sharpness

A reliability table or diagram compares mean forecast probability with observed event frequency in each bin. Return counts and uncertainty intervals. Document fixed or adaptive bins. Sparse bins are unstable; do not interpret them as proof of miscalibration.

Calibration is not enough. Describe the spread of forecasts and their ability to separate cases. A system that always returns the base rate may be reliable on average yet uninformative. Seek sharpness subject to calibration; do not reward false extremity.

For binary forecasts the sample Murphy decomposition can be expressed:

~~~text
Brier = Reliability - Resolution + Uncertainty
~~~

The reference implementation computes the exact sample decomposition by identical issued probability values. A binned decomposition is only an approximation and must name its binning.

Resolved numerical performance can also be grouped by declared domain, horizon, quantification class, or confidence band. Each group carries a caller-selected minimum-count status; sparse groups remain exploratory and must not support strong claims.

## Data-sufficiency gates

There is no universal sample-size threshold. A caller selects an explicit policy using:

- total resolved forecasts;
- number of events and non-events;
- distribution across forecast probability ranges;
- domain and horizon strata;
- missing or selected cases;
- whether a disjoint holdout is feasible.

Use states such as **insufficient_data**, **exploratory_only**, **diagnostic_ready**, and **recalibration_candidate**. Large N concentrated in one probability range may not support calibration across the full range. Document policy thresholds as engineering choices for a particular use, not scientific constants.

## Empirical recalibration

The reference implementation supports isotonic regression and Platt/logistic recalibration. Any fit must preserve raw probabilities, record the model identifier and training window, and be validated out of sample using a disjoint holdout, temporal split, or declared cross-validation. A temporal split must place training before validation. Avoid leakage from future outcomes. Fit within the domain and horizon where data justify that scope.

Recalibration should not run unless an explicit sufficiency policy passes its history, event/non-event, probability-coverage, and held-out-data requirements. If those conditions fail, report:

~~~text
recalibration_status: unavailable_insufficient_history
~~~

Beta calibration is a published alternative but is not implemented in this reference code. A method mentioned in research is not a capability claim for this package.

## Cold-start contract

~~~yaml
resolved_forecasts: 0
calibration_status: insufficient_history
available:
  - ledger schema and resolution rules
  - Brier, Brier Skill, log-loss, and diagnostic code
  - synthetic tests of implementation behavior
not_available_yet:
  - evidence-backed empirical recalibration
  - performance-weighted aggregation
  - trustworthy reliability or performance claims
~~~

Never create synthetic history to satisfy a readiness gate. Synthetic records demonstrate mechanics only.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
