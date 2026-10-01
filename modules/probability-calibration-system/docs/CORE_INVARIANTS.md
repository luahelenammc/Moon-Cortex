<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Core Invariants

**MSL profile:** 5.1-compatible Markdown-native module contract; uncertainty, provenance, freshness, and authority boundaries remain explicit.

These invariants govern every use of the Probability Calibration System.

## 1. Define the target

A forecast has a specified event, population or case, horizon, and resolution criteria. If a future reader could not determine what counts as yes, no, or unresolved, clarify the target or abstain.

## 2. Keep fit, evidence, probability, confidence, and utility distinct

- **Fit:** resemblance between the present case and a reference class, analogue, or model.
- **Evidence:** information bearing on the target, with source quality, dependence, coverage, recency, and selection limits.
- **Probability:** the estimated chance of the defined event.
- **Confidence:** the reliability of the probability estimate.
- **Utility:** the value or cost of an action in possible states.

No one judgment substitutes for another. Probability does not recommend an action by itself.

## 3. Qualitative output remains complete

When evidence is sparse, unstable, non-comparable, or unquantified, Q0 qualitative-only is a valid result. Confidence may be stated qualitatively. Do not add arbitrary exact percentages or fake intervals.

## 4. Every percentage passes a provenance gate

A numeric probability requires a defined event and horizon, an identified Q1–Q5 method, class-specific provenance, and precision justified by the evidence. A user request, confident phrasing, or convenient formula cannot waive that gate.

## 5. There is no universal probability formula

Do not map signal stages, confidence, qualitative labels, or arbitrary scores to a universal probability. Choose a method only when its assumptions, data, and domain justify it.

## 6. Evidence remains traceable and dependent signals remain dependent

Preserve the source, cutoff, inclusion logic, contradictions, missing information, and relation to the target. Reposts, derivatives, or several measurements of one origin do not become independent by multiplication.

## 7. Forecasts and outcomes keep their own history

Define resolution criteria when issuing a forecast. Preserve raw forecasts, later recalibrated values, revisions, and reasons. Ambiguous, invalidated, unresolved, cancelled, or superseded cases are not silently forced into binary scores.

## 8. Calibration is earned by resolved forecasts

A single forecast, synthetic example, or internal test cannot establish performance. Use comparable resolved records, honest reference forecasts, uncertainty-aware diagnostics, and out-of-sample evaluation before any empirical recalibration claim.

## 9. Domain authority and local ownership remain intact

High-stakes matters require current qualified authority. Private forecasts, sensitive context, and user records remain local. Public examples are synthetic and demonstrate no predictive performance.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
