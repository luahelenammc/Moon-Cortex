<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Probability Calibration System

Structure a forecast around a clearly defined outcome, the evidence that bears on it, and the conditions that would change the estimate.

Use this module when a decision depends on an uncertain future outcome and you need a proportionate, inspectable estimate. It keeps **fit**, **evidence**, **probability**, and **confidence in the estimate** distinct. Qualitative probability bands are valid outputs; a percentage is optional and requires a defensible basis.

- **Status:** Public pre-release
- **Version:** `0.1.0-pre.1`
- **Canonical entry:** [Probability Calibrator](PROBABILITY_CALIBRATOR.md#first-use)
- **Transport surface:** [Complete module package](../../downloads/probability-calibration-system.zip)
- **License:** CC BY 4.0

## Start here

Give the complete package to the AI, or open the [canonical entry](PROBABILITY_CALIBRATOR.md#first-use), and describe one bounded outcome plus its time horizon. Share any relevant observations, source material, comparable outcomes, constraints, and the decision the estimate will inform. The module will ask for missing details when they could change the result.

Nothing is installed. The package provides a reasoning contract and reference material. It does not create a predictive model, data feed, tracker, or professional authority.

## Module anatomy

- [Probability Calibrator](PROBABILITY_CALIBRATOR.md) — canonical operational entry and first-use instructions.
- [Core invariants](docs/CORE_INVARIANTS.md) — rules that every estimate must preserve.
- [Calibration model](docs/CALIBRATION_MODEL.md) — a field-first process for making and updating an estimate.
- [Evidence and claims](docs/EVIDENCE_AND_CLAIMS.md) — evidence quality, evaluation limits, and claim ceilings.
- [Moon Source context bridge](docs/MOON_SOURCE_CONTEXT_BRIDGE.md) — optional guidance for governed sources and freshness.
- [Reality test](docs/REALITY_TEST.md) — acceptance checks for a responsible run.
- [Synthetic examples](examples/synthetic_examples.md) — fictional, low-stakes demonstrations.
- [Module changelog](CHANGELOG.md) — module release history.

## Responsibility and limits

The Probability Calibration System organizes uncertainty. It does not guarantee accuracy, establish that any estimate is calibrated, replace domain research, or decide for the user. It does not infer that a plausible analogy is evidence, convert confidence into probability, or add related signals as if they were independent.

Quantitative forecasts require a defined event and horizon, an appropriate reference class or validated domain model, and enough relevant data to support the precision shown. If that basis is absent, the module can provide a qualitative band, explain why the probability is not estimable, or request evidence.

Medical, legal, financial, safety-critical, self-harm, emergency, regulated, and other high-stakes decisions require current qualified authority. This module may help organize questions and uncertainty, but it must not supply an individual prognosis or regulated advice.

## Provenance

This public module generalizes a probability-protocol mechanism from Local Moon Source. The private source, local context, personal records, and any situational adapters remain outside this package.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
