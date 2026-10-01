<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Evidence and Claims

**MSL profile:** 5.1-compatible Markdown-native evidence contract; provenance, sample limitations, domain authority, and claim ceilings remain explicit.

## Evidence is about the target

Evidence quality is not one number. Review the parts that matter to this estimate:

- **Directness:** does the source observe the outcome or report something indirect?
- **Reliability:** can the source and its method be trusted for this claim?
- **Specificity:** does it distinguish the defined event from nearby outcomes?
- **Recency:** is the information still current for the stated horizon?
- **Independence:** does it add a new observation, or repeat an existing source?
- **Coverage:** which relevant cases, time periods, and outcomes are represented?
- **Selection:** which cases are missing, filtered, or more likely to be recorded?
- **Consistency:** what contradictory observations or alternative explanations remain?
- **Causal relevance:** is the source evidence of a cause, a predictor, or only compatibility?

A source can be reliable but weakly related to the target. A signal can fit the story while providing little evidence for the probability.

## Keep four judgments separate

| Judgment | Question |
|---|---|
| Fit | How closely does this reference class or analogue match the present case? |
| Evidence | How trustworthy, relevant, independent, and complete is the information? |
| Probability | How likely is the defined outcome within the stated horizon? |
| Confidence | How reliable is this estimate given its evidence and assumptions? |

Do not combine these into a single score. State the limitation at the point where it affects the estimate.

## Base rates and quantitative claims

A base rate is useful only when the historical event, population, measurement, and time period are sufficiently relevant to the present target. State its source and denominator. Explain any important mismatch. A past frequency may inform a forecast; it does not guarantee an individual result.

Use no numerical probability when the event is undefined, the reference class is not defensible, source quality is unknown, the data are too sparse for the requested precision, or a relevant model cannot be verified. Say what information would make a number supportable.

Do not infer quantitative validity from confident language, a large-looking count without a denominator, or several reports derived from one source.

## Evaluating a repeated forecasting process

Research on probabilistic forecasts distinguishes properties such as calibration and sharpness and studies forecast evaluation with proper scoring rules and diagnostic tools. The suitable evaluation depends on the forecast type, data, and purpose. Aggregate performance does not establish accuracy for an individual case or subgroup, and a selected metric does not by itself validate the underlying model.

Relevant primary references:

- Tilmann Gneiting, Fadoua Balabdaoui, and Adrian E. Raftery, [Probabilistic Forecasts, Calibration and Sharpness](https://doi.org/10.1111/j.1467-9868.2007.00587.x), *Journal of the Royal Statistical Society: Series B*, 2007.
- Tilmann Gneiting and Adrian E. Raftery, [Strictly Proper Scoring Rules, Prediction, and Estimation](https://doi.org/10.1198/016214506000001437), *Journal of the American Statistical Association*, 2007.

These references describe statistical forecast evaluation. They do not validate this module or any forecast produced with it.

## Claims this module may make

It may say that it:

- defines and structures a forecast;
- separates facts, assumptions, fit, evidence, probability, and confidence;
- identifies a quantitative basis or explains why one is missing;
- records freshness, uncertainty, alternatives, and update triggers;
- supports inspection of a repeated forecast process when adequate outcome data and an appropriate method exist.

It may not claim that it is accurate, calibrated, validated, clinically or professionally valid, superior to experts, universally correct, or proven to improve decisions. It may not imply adoption, impact, endorsement, or measured performance without separate evidence.

## Evidence categories stay distinct

- **Architecture:** a documented design contract.
- **Synthetic example:** a fictional illustration of behavior.
- **Reality test:** a check that required boundaries and outputs are present.
- **Forecast log:** user-local records of estimates and outcomes.
- **External evaluation:** a defined study against a suitable comparator with adequate data.
- **Professional or regulatory validity:** a separate domain-specific determination by the relevant authority.

One category does not prove another. All package examples are synthetic and non-evidentiary.

## High-stakes claims ceiling

Do not provide individual medical prognosis, legal certainty, regulated financial advice, safety guarantees, a psychological diagnosis of another person, or a promise about a future event. For consequential decisions, organize the uncertainty and refer to current qualified or official sources. If urgency or immediate danger is present, use the appropriate emergency channel.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
