<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Evidence and Claims

**MSL profile:** 5.1-compatible Markdown-native evidence contract; provenance, sample limits, domain authority, and claim ceilings remain explicit.

## Evidence is about the target

Review the parts that matter to the defined event:

- **Directness and specificity:** does the source observe the outcome, and does it distinguish that outcome from nearby ones?
- **Reliability and provenance:** how was the information produced, and can the chain be checked?
- **Recency and coverage:** is it current, and which relevant cases or periods are represented?
- **Independence and causal origin:** is it new information or a derivative of the same source or event?
- **Selection and missingness:** which cases were excluded, lost, or more likely to be recorded?
- **Consistency and alternatives:** which contradictions and other explanations remain?

A source may be reliable but weakly related to the target. A signal may fit the story yet provide little evidence about the outcome.

## Keep judgments separate

| Judgment | Question |
|---|---|
| Fit | How closely does the class, analogue, or model match this case? |
| Evidence | How relevant, traceable, independent, current, and complete is the information? |
| Probability | How likely is the defined outcome within the stated horizon? |
| Confidence | How reliable is the estimate under its evidence and assumptions? |
| Utility | What values and consequences attach to possible actions and states? |

Do not collapse these into one score. Make an assumption visible at the point where it affects the estimate.

## Numeric provenance

Every percentage has a quantification class. The public schema in [Quantitative methods](QUANTITATIVE_METHODS.md) captures the target, horizon, as-of time, raw and final values, method, reference class or prior, dependence, uncertainty, sources, assumptions, expiry, and update triggers. Fields may be omitted only when they do not apply; missing values are unknown, not invitations to fabricate.

A reference frequency needs a relevant event definition and denominator. A Bayesian update needs a prior and evidence model. An elicited number needs a documented process. A simulated distribution needs traceable inputs. A recalibrated probability needs preserved raw forecasts and held-out evaluation.

## Evaluation and claim ceiling

Proper scoring rules and calibration diagnostics evaluate a set of probabilistic forecasts against outcomes; they do not validate a method for every domain or individual case. Calibration and sharpness should be read together. Resolution, reliability, sample size, event prevalence, selection, dependence, and subgroup scope affect interpretation.

The module may claim that it supports:

- structured qualitative and evidence-based quantitative forecasts;
- reference-class reasoning and Bayesian updating;
- documented structured expert elicitation;
- uncertainty propagation from supplied inputs;
- scoring and diagnostics for eligible resolved forecasts;
- recalibration when an explicit data policy and out-of-sample evidence permit it.

It may not claim scientifically validated superiority, universal calibration, expert-equivalent performance, measured performance without real resolved records, or clinical, legal, financial, or other domain validity.

## Evidence categories remain distinct

- **Architecture:** a documented design contract.
- **Synthetic example:** a fictional illustration.
- **Software test:** a check of mathematical and control behavior on chosen fixtures.
- **Forecast ledger:** user-local forecasts, assumptions, and outcomes.
- **External evaluation:** a study on real resolved records against a suitable comparator.
- **Professional or regulatory validity:** a separate domain-specific determination.

One category does not prove another. All package examples and tests are synthetic; they are not forecast history.

## High-stakes boundary

Do not provide unsupported individual medical prognoses, legal certainty, regulated financial advice, safety guarantees, psychological diagnoses of other people, or promises about future events. For consequential decisions, organize the uncertainty and route to current qualified or official authority. For imminent danger, use the appropriate emergency channel.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
