<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Probability Calibrator

**Module:** Probability Calibration System  
**Version:** 0.2.0-pre.1  
**Status:** Public pre-release  
**Canonical path:** modules/probability-calibration-system/PROBABILITY_CALIBRATOR.md  
**Complete package:** downloads/probability-calibration-system.zip  
**Authority:** This entry governs operation; the linked module documents provide supporting methods and limits.

## First use

### What this module does

It helps you reason about one bounded future outcome. It reconstructs the relevant field, distinguishes observations from interpretations, assesses fit and evidence separately, and expresses probability only at the precision the method can support. It may stop at a qualitative band.

### What to give the AI

Provide the complete probability-calibration-system.zip, or this entry with any supporting document relevant to the request. Then describe:

- the outcome to estimate, in terms that later evidence can resolve;
- the time horizon and conditions that count as success, failure, or unresolved;
- what is known, where it came from, and when it was last checked;
- relevant comparison cases, base rates, or a domain model, if available;
- the decision the estimate informs and how much detail is useful.

Do not share private records unless they are needed and you are authorized to share them. A local forecast ledger remains under your control.

### What happens next

The AI should define the target and resolution criteria, reconstruct current evidence and freshness, pass the percentage permission gate, select a suitable regime, and state confidence separately from the outcome probability. It should name important alternatives, assumptions, update triggers, and a proportionate next action.

Nothing is installed or connected by giving this package to an AI. Research, live facts, source access, professional judgment, and external actions require the relevant current source, capability, authorization, or qualified professional.

### Starter prompt

~~~
Use the Probability Calibration System to estimate this outcome:

Outcome and deadline:
Resolution criteria:
Evidence and sources:
Comparable cases or base rate, if any:
Decision this estimate will inform:

Define the event and horizon before estimating. Separate observed facts from interpretation. Assess fit separately from evidence. Keep the output qualitative unless a permitted quantitative method has defensible provenance. State confidence separately from probability. Identify assumptions, dependence, alternatives, uncertainty, freshness, and update triggers. Keep probability separate from action utility. If evidence is insufficient or the domain is high-stakes, say so and route to current qualified authority.
~~~

## Operating contract

### 1. Define the event and horizon

State one resolvable event, the relevant population or case, time horizon, and outcome criteria. Keep a broad intention separate from an observable event. If the target or criteria are ambiguous, ask a focused question or mark the estimate not yet estimable.

### 2. Reconstruct evidence and freshness

Separate direct observations from reports, interpretations, assumptions, and unknowns. Record source, provenance, directness, reliability, specificity, recency, coverage, selection limits, contradictions, and whether evidence is independent or derived from the same origin. State the evidence cutoff.

### 3. Assess fit without turning it into evidence

Explain how well a proposed comparison class or model matches the present case. Compare the event definition, population, period, process, environment, incentives, constraints, and measurement. High fit may coexist with low evidence. An appealing analogy is not a measured base rate.

### 4. Pass the percentage permission gate

Before writing any percentage, verify all of the following:

1. the target event and horizon are defined;
2. the numerical method belongs to an identified quantification class Q1–Q5;
3. the class-specific provenance is present and inspectable;
4. the precision and uncertainty match the evidence;
5. the high-stakes boundary permits the requested use.

If any prerequisite is missing, use Q0 qualitative-only, request evidence, or state that a numeric estimate is unavailable. A request for a percentage does not create a basis for one.

### 5. Route to the least demanding justified regime

| Class | Basis | Route |
|---|---|---|
| Q0 | No defensible quantitative basis | Qualitative band, confidence, unknowns, and update triggers; no percentage or invented interval |
| Q1 | Documented structured expert elicitation | Retain who or what supplied judgments, protocol, raw ranges or quantiles, disagreement, fit, and limits |
| Q2 | Comparable resolved historical outcomes | Define the reference class and inclusion logic; retain denominator, event count, comparability limits, and uncertainty |
| Q3 | Explicit prior and likelihood evidence | Retain prior, evidence, likelihood model, and dependence handling; do not convert adjectives into likelihood ratios |
| Q4 | Stochastic model with uncertain inputs | Retain input distributions and sources, dependence, simulation count, seed policy, and output summaries |
| Q5 | Learned transformation of raw forecasts | Retain raw and adjusted values, model, training window, domain/horizon scope, sample size, and held-out validation |

Do not map a qualitative label, confidence level, signal stage, or agent consensus directly to a probability. No class is a universal formula.

### 6. Compute and audit only when useful

Use reference-class frequencies, a Beta-Binomial posterior, a Bayesian odds update, an elicited distribution, or Monte Carlo only when its assumptions and inputs are stated. Ask what usually happens in genuinely comparable cases before case-specific narrative dominates. Check evidence dependence, sensitivity to priors and likelihoods, and input uncertainty where they could change the result.

The code-backed quantitative details live in [Quantitative methods](docs/QUANTITATIVE_METHODS.md). Expert workflows and labels are bounded in [Structured expert elicitation](docs/STRUCTURED_EXPERT_ELICITATION.md).

### 7. Separate probability, confidence, and utility

Probability concerns the defined outcome under stated evidence and assumptions. Confidence concerns the reliability of that estimate. Utility concerns the value or cost of actions across possible states. None substitutes for another. Expected utility is optional, requires explicit value assumptions, and does not automatically recommend an action.

### 8. Preserve updates and evaluate only resolved forecasts

When useful, register a forecast before its outcome with exact resolution criteria. Preserve the original values and an audit trail. Do not force ambiguous outcomes into yes/no. Evaluation requires resolved, comparable forecasts; recalibration additionally requires an explicit data-sufficiency policy and out-of-sample validation. See [Forecast verification](docs/FORECAST_VERIFICATION.md).

## Probability bands and intervals

Qualitative bands are first-class outputs. Labels such as low, moderate, or high do not encode fixed percentages across domains. When numeric support exists, the qualitative label should faithfully summarize that estimate. When it does not, the band may stand alone.

Prefer uncertainty intervals when parameter uncertainty matters. Call a Bayesian interval a credible interval and a frequentist interval a confidence interval. Do not report more decimal places than the input data and model warrant.

## Default output

~~~
Target and resolution criteria:
Horizon / evidence cutoff:
Quantification class:
Observed facts:
Evidence for / against / unknowns:
Probability reading: qualitative by default; numeric only after permission
Confidence in this estimate:
Interval or predictive summary, if justified:
Key assumptions and dependence:
What changes the estimate:
Proportionate next action:
~~~

Add a quantitative audit or ledger ID only when it materially helps the user. Do not force a technical appendix into every answer.

## Freshness fields

Use the fields that matter for time-sensitive evidence:

- **as_of:** when the input evidence was current;
- **expire_if:** what would make the estimate stale;
- **refresh_if:** what should prompt a source check or update;
- **manual_recalibration_required_if:** what requires deliberate reassessment;
- **safe_fallback_read:** the cautious interpretation when a current check is unavailable.

A stale snapshot is not current evidence.

## High-stakes boundary

For medicine, law, finance, safety-critical systems, self-harm, emergencies, regulated decisions, or other consequential decisions, the system may organize evidence, expose uncertainty, compute a valid transformation of supplied inputs, and compare scenarios. It must not create unsupported prognoses, legal certainty, regulated financial advice, or a substitute for professional authority.

## Scientific maxims

> **A number is not a measurement merely because it has a percent sign.**

> **Every percentage needs provenance.**

> **Monte Carlo propagates uncertainty; it does not create information.**

> **Calibration must be earned by resolved forecasts.**

> **Fit is not evidence. Evidence is not probability. Probability is not confidence. Probability is not utility.**

> **When the data do not earn a number, qualitative calibration is the more scientific answer.**

## Supporting documents

[Core invariants](docs/CORE_INVARIANTS.md) · [Calibration model](docs/CALIBRATION_MODEL.md) · [Quantitative methods](docs/QUANTITATIVE_METHODS.md) · [Structured elicitation](docs/STRUCTURED_EXPERT_ELICITATION.md) · [Forecast verification](docs/FORECAST_VERIFICATION.md) · [Evidence and claims](docs/EVIDENCE_AND_CLAIMS.md) · [Scientific references](docs/SCIENTIFIC_REFERENCES.md) · [Reality test](docs/REALITY_TEST.md) · [Synthetic examples](examples/synthetic_examples.md)

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
