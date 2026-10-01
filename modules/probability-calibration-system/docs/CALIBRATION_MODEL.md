<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Calibration Model

**MSL profile:** 5.1-compatible Markdown-native method surface; each estimate carries its target, evidence basis, uncertainty, freshness, and update conditions.

This model is a decision aid, not a fixed algorithm. It may stop at any step when the target, evidence, or authority boundary is unresolved.

## Sequence

### 1. Bound the question

Write the outcome, relevant case or population, time horizon, and resolution rule. Include any important conditions. Separate the outcome the user wants from the outcome that can actually be observed.

### 2. Set the evidence cutoff

Record the date, sources, and information available at the moment of the estimate. Mark any facts that are stale or unverified. If a current fact could change the answer, verify it when a suitable authorized source is available; otherwise state the limitation.

### 3. Map facts, claims, and unknowns

Separate direct observations from reports, interpretations, assumptions, and speculation. For every material signal, note:

- source and provenance;
- directness and reliability;
- specificity to the defined outcome;
- recency and freshness;
- independence from other signals;
- coverage of the relevant cases or process;
- material omissions, selection effects, contradictions, and alternative explanations;
- whether the signal is causal, predictive, or merely compatible with the outcome.

### 4. Assess the reference class and fit

Choose a reference class only when its event definition and relevant context resemble the present case. Explain material mismatches in population, period, process, environment, incentives, constraints, or measurement. Keep an analogy separate from a measured frequency. If a defensible reference class is absent, say so.

### 5. Choose the probability form

- **Qualitative band:** preferred for sparse, mixed, evolving, or non-comparable evidence.
- **Numeric range:** useful when quantitative evidence exists but a single point would overstate certainty.
- **Point probability or predictive distribution:** use only when an appropriate base rate, validated model, or defensible quantitative method supports it.

State the denominator, period, model or method, assumptions, and main uncertainty when they apply. Explain what the estimate does and does not cover. Do not present historical frequency as a guarantee for an individual case.

### 6. Rate confidence in the estimate

Confidence is a separate statement about the estimate. Consider target clarity, evidence quality and quantity, reference-class fit, stability, source independence, unresolved contradictions, and model limitations. A strong broad reference class may support high confidence in a broad moderate probability band, while leaving confidence in an exact point low.

Do not output a numeric confidence score unless a field-specific, validated method supports it. Plain language is sufficient.

### 7. Compare alternatives and specify updates

Name the alternative scenarios that materially affect the decision. For each important one, state which observation would change the read and how. Distinguish an event that changes the outcome likelihood from an event that only changes confidence or narrows uncertainty.

### 8. Select a proportionate action

Choose an action based on the user goal, consequences, reversibility, and remaining uncertainty. If the cost of being wrong is high, use qualified current authority and avoid relying on an informal forecast.

## Optional signal progression

Some fields involve a sequence of observable steps. In those cases, a local signal ladder may describe progression from ambiguous attention, to recognition, to specific engagement, to a concrete commitment, to an observed outcome. Define the stages from the field and the target event.

A ladder describes what kind of signal occurred. It is not a universal measure of signal strength, evidence independence, or event probability. Do not sum its levels, treat adjacent steps as equal intervals, or infer that a later stage guarantees the target.

## Quantitative calibration and review

Calibration is a property evaluated across a set of forecasts and resolved outcomes, not a certificate earned by one correct prediction. A quantitative review needs comparable targets, explicit probabilities, aligned horizons, reliable outcomes, and enough data for useful uncertainty bounds. Dependencies, shifting populations, missing cases, and selection into the record can make apparent calibration misleading.

Suitable scoring rules or graphical diagnostics can help evaluate a repeated forecast process when their assumptions fit the task. Select the evaluation method for the forecast type and intended use. Do not infer that a better aggregate score proves causal understanding, professional validity, or success on every subgroup.

Do not calibrate a local scale from too few, selectively retained, or shifting cases. If a stable reference class cannot be established, preserve the uncertainty instead of fitting thresholds to noise.

## Update policy

An update should preserve the former estimate and document:

1. the new source or event and when it became available;
2. whether it changes the target, the probability, confidence, freshness, or only the narrative;
3. the assumption or reference-class match that changed;
4. the revised estimate and remaining uncertainty;
5. the next trigger or expiry condition.

A repeated copy of an existing source is not a new independent signal. A direct observation can materially change an estimate without proving the causal mechanism behind it.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
