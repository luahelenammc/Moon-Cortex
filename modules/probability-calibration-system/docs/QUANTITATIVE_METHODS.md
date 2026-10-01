<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Quantitative Methods

**MSL profile:** 5.1-compatible method surface; quantitative output requires traceable inputs, declared assumptions, and a fallback when its prerequisites fail.

The qualitative regime is a complete first-class method. Quantitative tools activate only when a defined target, horizon, evidence basis, and method-specific provenance exist.

## Quantification classes

| Class | Meaning | Minimum provenance to retain |
|---|---|---|
| Q0 — qualitative only | No defensible numeric basis | Qualitative band, confidence, uncertainty, and reason a number is withheld |
| Q1 — structured expert elicitation | Judgment recorded through a stated process | Who or what supplied estimates, protocol, raw quantiles or ranges, disagreement, fitted distribution if any, and limitations |
| Q2 — empirical reference class | Comparable resolved historical outcomes | Class definition and policy status, sample size, event count, inclusion logic, time period, comparability limits, observed rate, and confidence or credible interval |
| Q3 — Bayesian evidence update | Prior updated through explicit evidence and likelihoods | Prior source, evidence sources, likelihood model, dependence assumptions, and posterior |
| Q4 — simulation | A stochastic model propagates uncertain inputs | Input distributions and sources, dependence structure, model, simulation count, seed policy where useful, and output summaries |
| Q5 — empirically recalibrated | A learned model transforms a raw forecast | Raw and final probabilities, calibration model identifier, training window, sample size, scope, validation method, and out-of-sample result |

These labels identify how a number was produced; they do not certify that its inputs are good. Use the least demanding class that supports the requested precision.

## Percentage permission and provenance

Before any percentage is returned, the target event and horizon must be defined; the method must fit Q1–Q5; class-specific provenance must be present; and the precision must not exceed the evidence. If these checks fail, return Q0 qualitative-only or state what is missing.

A reusable estimate may carry fields such as:

~~~yaml
probability_estimate:
  target_event:
  resolution_criteria:
  horizon:
  as_of:
  raw_probability:
  final_probability:
  qualitative_band:
  confidence:
  quantification_class:
  method:
  reference_class:
  prior:
  likelihood_model:
  dependence_handling:
  uncertainty_interval:
  simulation:
  calibration_status:
  evidence_sources:
  assumptions:
  expiry:
  update_triggers:
~~~

Fields are regime-dependent. Null or omitted values mean unavailable or not applicable; they must not be backfilled by invention.

## Reference-class mode

Ask: **What usually happens in genuinely comparable cases?** Define the outcome and horizon first. Then disclose the class, denominator, event count, inclusion and exclusion rules, time period, source, and differences that may matter. Apply an explicit use-specific minimum-sample policy and an assessed comparability/heterogeneity status; there is no universal threshold. The implementation keeps the observed fraction descriptive and withholds an empirical forecast rate when the class is too small, too heterogeneous, or unassessed. Nested or hierarchical classes may make the similarity/sample-size trade-off visible.

When a class passes its policy, the reference implementation reports a Wilson confidence interval under a binomial sampling assumption, or a Beta posterior credible interval when an explicit prior is supplied. Label the interval accurately and state when dependence, selection, or process drift weakens the assumptions.

If the class is unavailable or too weak for the requested precision, state that status and route to another regime. Never turn an analogy into an empirical rate.

## Beta-Binomial model

For a binary outcome history, with an explicitly justified prior:

~~~text
p ~ Beta(alpha, beta)
X | p ~ Binomial(n, p)
p | X=x ~ Beta(alpha + x, beta + n - x)
E[p | X] = (alpha + x) / (alpha + beta + n)
~~~

The prior may be uniform Beta(1,1), Jeffreys Beta(0.5,0.5), empirical, or expert-specified, but its choice and source must be retained. There is no universal prior. Report a posterior credible interval when uncertainty matters and call it a credible interval.

With three successes in three observations and a uniform prior, the posterior is Beta(4,1), with mean 0.8; it is not silently reported as certainty. That result is conditional on this stated prior and a comparable Bernoulli model.

## Bayesian odds and likelihood ratios

For hypothesis H and evidence E:

~~~text
O(H) = P(H) / (1 - P(H))
LR = P(E | H) / P(E | not H)
O(H | E) = O(H) × LR
P(H | E) = O(H | E) / (1 + O(H | E))
~~~

Multiple likelihood ratios may be multiplied only when conditional independence is defensible and recorded. Otherwise model the dependence, group signals, use a conservative update, widen uncertainty, or remain qualitative. A likelihood ratio must be empirical or explicitly elicited; adjectives do not generate likelihood ratios.

Priors, likelihoods, evidence sources, and sensitivity to plausible alternative values remain visible. A posterior is conditional on them; it does not turn a weak source into strong evidence.

## Evidence dependence gate

Classify signals as independent candidates, conditionally dependent, repeated from the same source, derivative reporting, shared-cause, overlapping, or unknown. Trace articles and metrics back to their origin. Three articles repeating one announcement are one stream unless they add independent observations.

Distinct source labels do not prove statistical independence. When dependence is unknown, state that uncertainty. Correlation or copula models are warranted only when a defensible joint structure and enough information exist.

## Sensitivity and scenario analysis

Identify whether alternative priors, likelihoods, class definitions, or dependence assumptions materially change the result. Show the estimate under named alternatives rather than hiding a dominant assumption inside one number. Scenario labels such as conservative, central, or optimistic are not probabilities unless modeled as such.

## Monte Carlo propagation

Sample the stated input distributions, apply the stated model, repeat an explicit number of times, and report an output distribution or relevant quantiles. Document parameter sources, dependence, sample count, and a reproducibility seed when practical.

> **Monte Carlo propagates uncertainty. It does not create information.**

Do not use simulation to make invented inputs look scientific. More iterations reduce simulation noise, not epistemic uncertainty or model error.

## Multi-estimator aggregation

With no comparable resolved history, use a simple mean or median only if an aggregate is useful; preserve every estimate, the spread, and minority reasoning. Do not treat several AI systems as independent experts because their outputs agree.

Performance-weighted aggregation may activate only when estimators have comparable resolved histories and the weights are evaluated out of sample. Self-description, prestige, and one agreement round are not performance evidence.

## Probability and expected utility

Probability estimation stays separate from action choice. If values are suitable for explicit numbers, an optional decision layer may compute:

~~~text
EU(action) = sum over states [P(state | action) × U(action, state)]
~~~

The utility assumptions are user- or domain-owned, not hidden weights. Qualitative comparison is preferable when numeric utilities would falsely objectify values. A higher expected utility is not automatically a recommendation.

## Uncertainty and confidence

Use posterior credible intervals for Bayesian parameter uncertainty and frequentist confidence intervals only for a frequentist procedure. A predictive interval describes future outcomes under its model. Do not swap these labels.

Confidence in the estimate remains a separate qualitative assessment of evidence, coverage, independence, freshness, fit, parameter uncertainty, missingness, and sensitivity. Do not turn it into the outcome probability or a hidden formula.

## Reference implementation

The dependency-light Python implementation provides percentage permission checks, a Beta-Binomial posterior and credible interval, Bayesian odds updates, dependence clustering, quantile checks, equal/performance-gated aggregation, seeded Monte Carlo, expected utility, scoring, ledger rules, diagnostics, and gated recalibration. It transforms supplied inputs and does not fetch or invent evidence.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
