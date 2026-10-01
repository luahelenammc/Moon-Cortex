<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Probability Calibrator

**Module:** Probability Calibration System  
**Version:** `0.1.0-pre.1`  
**Status:** Public pre-release  
**Canonical path:** `modules/probability-calibration-system/PROBABILITY_CALIBRATOR.md`  
**Complete package:** `downloads/probability-calibration-system.zip`  
**Authority:** This entry governs operation; the linked module documents provide supporting rules.

## First use

### What this module does

It helps you reason about one bounded future outcome. It separates what happened from what may happen, assesses how well a reference situation fits, weighs the evidence, and expresses probability at a level of precision the evidence can support. It records uncertainty, relevant assumptions, update triggers, and a proportionate next action.

### What to give the AI

Provide the complete `probability-calibration-system.zip`, or this entry together with any module document relevant to the request. Then describe:

- the outcome you want to estimate, stated so that later evidence can resolve it;
- the time horizon and conditions that count as success or failure;
- what you know, where it came from, and when it was last checked;
- relevant comparison cases, base rates, or a domain model, if available;
- what decision the estimate informs and how much detail is useful.

Do not share private records unless they are needed and you are authorized to share them. A local copy of a forecast log remains under your control.

### What happens next

The AI should clarify the outcome and horizon, separate observations from interpretations, assess fit and evidence independently, decide whether a quantitative probability is justified, and return an estimate with confidence in that estimate. It should name the strongest alternative scenarios, the next evidence that could change the result, and a proportionate action.

Nothing is installed or connected by giving the package to an AI. Current research, live facts, source access, professional judgment, and external actions require the relevant source, capability, authorization, or qualified professional.

### Starter prompt

```text
Use the Probability Calibration System to estimate this outcome:

Outcome and deadline:
Evidence and sources:
Comparable cases or base rate, if any:
Decision this estimate will inform:

Separate observed facts from interpretation. Assess fit separately from evidence. Use a qualitative probability band unless a defensible quantitative basis supports more detail. State confidence in the estimate separately from the probability of the outcome. Identify assumptions, alternatives, update triggers, source freshness, and a proportionate next action. If the evidence is insufficient or the domain is high-stakes, say so and route to the appropriate current authority.
```

## Operating contract

### 1. Define the event before estimating

State one resolvable event, the relevant population or case, the time horizon, and the conditions that count as the outcome. Keep a broad intention separate from an observable event. If the target is ambiguous, ask a focused question or report that it is not yet estimable.

### 2. Separate observation from interpretation

Label direct observations and their sources separately from inferences, assumptions, and unknowns. Note source reliability, directness, recency, specificity, independence, and whether a claim is evidence of the target outcome or merely compatible with it. Record material missing information and contradictions.

### 3. Assess fit and evidence separately

**Fit** describes how closely a comparison case or model matches the present situation. **Evidence** describes how much reliable information supports the present estimate. High fit can coexist with low evidence; a close analogy does not become a measured base rate.

Evaluate similarities and differences that matter to the target: population, setting, time period, process, incentives, constraints, and outcome definition. Do not let an appealing narrative, a familiar pattern, or one vivid example substitute for a relevant reference class.

### 4. Choose a probability expression

Use a qualitative band by default when the evidence is sparse, mixed, non-comparable, or not quantifiable. Use a number only when the target is defined and a relevant empirical base rate, validated model, or other defensible quantitative basis supports it. Explain the reference class, denominator, time window, and major assumptions. Use a range when a point estimate would imply unjustified precision.

If no defensible base rate or model exists, say that a numerical probability is not estimable from the available evidence. A user request for a percentage does not create a quantitative basis. Never present an illustrative number as a measured probability.

Qualitative labels are not universal numeric intervals. Choose and explain the label in the current field. A locally validated scale may define its own thresholds; do not import one silently.

### 5. State confidence in the estimate separately

Probability describes the chance that the defined event occurs within its horizon, given the available evidence and assumptions. **Confidence** describes how reliable the estimate itself is, considering evidence quality, coverage, stability, model or reference-class fit, and unresolved uncertainty.

A moderate probability can have high confidence when a strong, stable reference class supports a broad near-even estimate. A high probability can have low confidence when evidence is thin or the process may have changed. Do not describe confidence as another probability of the event.

### 6. Compare scenarios and identify updates

Include the plausible outcome paths that could materially change the decision. Identify what evidence would move the estimate up, move it down, narrow it, widen it, or leave it unchanged. Recalculate only when new information bears on the defined event or when an assumption, reference class, or process has changed.

Do not count repeated copies, retellings, or dependent observations as independent confirmation. Do not add signal levels or evidence scores into a universal probability formula.

### 7. Match action to uncertainty

Recommend a reversible, proportionate next step when possible. Keep actions distinct from predictions. Do not present a desired outcome as a forecast or a forecast as a reason to take an irreversible action.

## Probability bands

Qualitative descriptions are first-class outputs. The module may use labels such as **very low**, **low**, **low to moderate**, **moderate**, **moderate to high**, **high**, or **very high** when they communicate the evidence faithfully. Explain what the label means in context; the words do not encode fixed percentages across all domains.

## Freshness fields

When facts or rates can change over time, use the fields that matter:

- **as_of:** the date or time at which the evidence was current;
- **expire_if:** a condition that makes the estimate stale;
- **refresh_if:** an event that should prompt a source check or update;
- **manual_recalibration_required_if:** a condition requiring deliberate reassessment;
- **safe_fallback_read:** the cautious interpretation if a current check is unavailable.

A stale snapshot must not be presented as present evidence.

## Forecast evaluation

A single outcome cannot establish whether a forecasting method is calibrated. Evaluation requires a set of resolved, comparable forecasts with well-defined targets, horizons, probabilities, and outcomes. Where the volume and quality of data justify it, suitable scoring and calibration diagnostics may help; the chosen measure, reference class, dependence, selection, and sample uncertainty must be considered. A score or synthetic example does not prove validity, accuracy, or superiority.

Keep any forecast log optional and user-owned. Preserve the forecast as issued, its evidence cutoff, the resolved outcome, and any later revision so that hindsight does not silently rewrite the original estimate.

## High-stakes boundary

For medical, legal, financial, safety-critical, self-harm, emergency, regulated, or other consequential decisions, do not provide an individual prognosis, regulated advice, or a substitute for professional judgment. Help the user state questions, organize known facts, identify uncertainty, and seek current qualified or official sources. If immediate danger or an emergency is present, direct the user to the appropriate emergency service.

## Output contract

```text
Outcome and horizon:
Evidence cutoff:
Observed facts:
Interpretations and assumptions:
Fit:
Evidence quality:
Probability: qualitative band by default; numeric only with a defensible basis
Confidence in this estimate:
Important alternatives:
Unknowns and contradictions:
Update triggers and freshness:
Proportionate next action:
Limits or authority to consult:
```

Use only the fields needed for the current request. Mark missing fields as unknown instead of filling them by invention.

## Tiny example

**Question:** Will a community workshop reach its minimum attendance by the registration deadline?  
**Evidence:** A comparable event series has complete attendance records, but this workshop has a shorter lead time.  
**Read:** The reference class has moderate fit; the current evidence is incomplete. Use a qualitative band, state low confidence, check the current registration count, and revisit after the next reminder. Do not turn a past series average into a guarantee.

## Troubleshooting

- **The target is vague:** make the event and horizon observable before estimating.
- **There are no comparable outcomes:** explain that a numeric probability is unsupported; use a cautious qualitative read or leave it not estimable.
- **The analogy feels exact but records are sparse:** state high fit and low evidence separately.
- **Sources repeat the same claim:** trace the original source and treat dependent copies as one evidence stream.
- **The estimate changed:** identify the new evidence, changed assumption, or freshness trigger that caused the update.
- **The decision is high-stakes:** organize questions and evidence, then route to current qualified authority.

## Supporting documents

[Core invariants](docs/CORE_INVARIANTS.md) · [Calibration model](docs/CALIBRATION_MODEL.md) · [Evidence and claims](docs/EVIDENCE_AND_CLAIMS.md) · [Moon Source context bridge](docs/MOON_SOURCE_CONTEXT_BRIDGE.md) · [Reality test](docs/REALITY_TEST.md) · [Synthetic examples](examples/synthetic_examples.md)

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
