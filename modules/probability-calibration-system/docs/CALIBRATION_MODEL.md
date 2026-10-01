<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Calibration Model

**MSL profile:** 5.1-compatible Markdown-native method surface; each forecast carries its target, evidence basis, uncertainty, provenance, freshness, and update conditions.

This is a field-first decision aid, not a fixed algorithm. It stays concise unless the target earns a quantitative mode.

## Route

1. **Define the event.** State outcome, population or case, horizon, and predeclared resolution rule.
2. **Set the evidence cutoff.** Record sources and what was knowable at forecast time. Mark stale, missing, or unverified facts.
3. **Separate facts and interpretation.** Label observations, reports, assumptions, inferences, unknowns, and contradictions.
4. **Assess fit and reference class.** Compare event definition, population, period, process, setting, incentives, and measurement. If no defensible class exists, record it as unavailable.
5. **Pass the percentage permission gate.** A defined target and horizon are necessary but not sufficient. Identify the quantitative method and its provenance, or stay qualitative.
6. **Choose the least demanding justified regime.** Q0 qualitative; Q1 structured elicitation; Q2 empirical reference class; Q3 Bayesian evidence update; Q4 simulation; Q5 empirically recalibrated forecast.
7. **Compute only from supplied, traceable inputs.** State the prior, likelihood, reference class, elicitation record, or input distributions where applicable. Never create one from a descriptor or narrative alone.
8. **Audit dependence and sensitivity.** Cluster repeated or causally linked evidence. Show if a reasonable prior, likelihood, or dependence choice materially changes the result.
9. **Separate probability, confidence, and action.** Confidence describes reliability of the estimate. Expected utility is optional and requires explicit value assumptions.
10. **Preserve the forecast and update triggers.** Log before outcome only when useful; resolve by the original criteria and evaluate only eligible resolved records.

## Reference-class check

Ask what usually happens in genuinely comparable cases before an engaging case-specific story dominates. Disclose the sample size, event count, inclusion and exclusion logic, time period, and comparability limitations. Check whether the class is too small, heterogeneous, selected, or affected by a process change. A nested class can help expose the trade-off between sample size and similarity.

When a defensible class does not exist, record **reference class unavailable** and route to a different method. Never fabricate a base rate.

## Numeric methods

Use a Beta-Binomial posterior for a binary outcome history only when a prior is justified and its provenance is stated. A small sample such as three successes in three cases must not silently become certainty; the result depends on an explicit prior and retains posterior uncertainty.

Use Bayesian odds updates only with an explicit prior and likelihood ratio whose source or elicitation is recorded. Multiple likelihood ratios may be multiplied only under a defensible conditional-independence model. Unknown dependence requires grouping, conservative aggregation, wider uncertainty, or a qualitative fallback.

Use Monte Carlo only to propagate supplied uncertain distributions through a stated model. Report inputs, their sources, dependence assumptions, sample count, and seed policy when reproducibility matters. More simulation draws reduce computational error; they do not repair missing or invented inputs.

For quantitative details and provenance, see [Quantitative methods](QUANTITATIVE_METHODS.md).

## Confidence

Assess confidence qualitatively from target clarity, evidence quantity and quality, independence, freshness, reference-class fit, missingness, model sensitivity, and domain validity. Do not turn confidence into a hidden weighted score unless a separately validated method exists.

## Update policy

Preserve the prior forecast. On an update, record the new source or event, when it became available, which assumption or class changed, whether probability or confidence moved, and the next trigger. A repeated copy is not a new independent signal.

## Empirical review

Evaluate a repeated forecasting process only after outcomes resolve under the forecast-time criteria. Select metrics and bins for the target use, disclose sample limits, and use a legitimate reference forecast for skill scores. Fit and evaluate any recalibration model on disjoint data or with a declared cross-validation plan. Do not use future outcomes in training.

At cold start, report that empirical calibration is unavailable. This is the correct status until resolved history meets an explicit data policy.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
