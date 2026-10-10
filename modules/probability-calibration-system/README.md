<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Probability Calibration System

Structure a forecast around a resolvable outcome, its evidence, and the conditions that would change the estimate. Use qualitative calibration by default; add numbers only when a method and its provenance support them.

The system keeps **fit**, **evidence**, **probability**, **confidence**, and **decision utility** distinct. It supports reference classes, Bayesian updates, structured elicitation, uncertainty propagation, forecast scoring, and empirical recalibration when the data earn those methods.

- **Status:** Public pre-release
- **Version:** 0.2.0-pre.1
- **Canonical entry:** [Probability Calibrator](PROBABILITY_CALIBRATOR.md#first-use)
- **Transport surface:** [Complete module package](../../downloads/probability-calibration-system.zip)
- **License:** CC BY 4.0 for documentation; Apache-2.0 for the dependency-light reference code

## Start here

**Plan A (recommended):** paste this [public GitHub module link](https://github.com/luahelenammc/Moon-Cortex/tree/main/modules/probability-calibration-system) or its [canonical entry](https://github.com/luahelenammc/Moon-Cortex/blob/main/modules/probability-calibration-system/PROBABILITY_CALIBRATOR.md#first-use) into an AI conversation with web/repository retrieval. Ask it to read the First use instructions and only the support files this task needs. **Plan B:** [download the complete module ZIP](../../downloads/probability-calibration-system.zip) if direct retrieval is unavailable, incomplete, or offline use is required. Confirm what the AI actually opened. [Access guide](https://github.com/luahelenammc/Moon-Cortex/blob/main/docs/USE_WITH_AI.md).

Start with the [canonical entry](PROBABILITY_CALIBRATOR.md#first-use), then describe one bounded outcome, its horizon, and how the outcome will be resolved. Share relevant observations, sources, comparable outcomes, constraints, and the decision the estimate will inform.

The default path stays concise and may stop at a qualitative band. A percentage requires a defined event and horizon, a permitted quantitative regime, and traceable provenance. If there is no adequate basis, Q0 qualitative-only remains a complete scientific answer.

Nothing is installed or connected by giving the package to an AI. The reference implementation is optional local code. It does not supply evidence, create a data feed, maintain a forecast history, or establish domain performance.

## Module anatomy

- [Probability Calibrator](PROBABILITY_CALIBRATOR.md) — canonical routing, percentage permission gate, first-use instructions, output contract, and limits.
- [Core invariants](docs/CORE_INVARIANTS.md) — rules every estimate preserves.
- [Calibration model](docs/CALIBRATION_MODEL.md) — field-first estimation and update sequence.
- [Quantitative methods](docs/QUANTITATIVE_METHODS.md) — provenance classes, reference classes, Bayesian methods, dependence, simulation, sensitivity, and decision utility.
- [Structured expert elicitation](docs/STRUCTURED_EXPERT_ELICITATION.md) — elicitation, quantiles, aggregation, and protocol-label limits.
- [Forecast verification](docs/FORECAST_VERIFICATION.md) — ledger schema, resolution, scoring, diagnostics, sufficiency gates, and recalibration.
- [Evidence and claims](docs/EVIDENCE_AND_CLAIMS.md) — evidence quality, validation limits, and public claim ceiling.
- [Scientific references](docs/SCIENTIFIC_REFERENCES.md) — primary and high-authority methods sources.
- [Moon Source context bridge](docs/MOON_SOURCE_CONTEXT_BRIDGE.md) — optional source authority and freshness guidance.
- [Reality test](docs/REALITY_TEST.md) — acceptance checks for a responsible run.
- [Synthetic examples](examples/synthetic_examples.md) — fictional demonstrations, not evidence of performance.
- [Python reference implementation](reference/probability_calibration.py) and [tests](reference/tests/test_quantification.py) — standard-library methods for quantitative transformations, ledger semantics, scoring, diagnostics, and gated isotonic/Platt recalibration.
- [Module changelog](CHANGELOG.md) — release history.

## Cold start

At release, no real resolved forecast history is supplied. Scoring functions and ledger tooling are available, but empirical performance, reliability claims, performance-weighted aggregation, and evidence-backed recalibration remain unavailable until suitable forecasts resolve and pass an explicit data policy. Synthetic fixtures test implementation behavior; they do not fill the historical record.

## Responsibility and limits

The system organizes uncertainty; it does not guarantee accuracy, establish that any estimate is calibrated, replace domain research, or decide for the user. Monte Carlo propagates uncertainty in supplied inputs; it does not create information. A numerical score is not validation.

Medical, legal, financial, safety-critical, self-harm, emergency, regulated, and other high-stakes decisions require current qualified authority. The module may organize questions and uncertainty, but must not provide an unsupported prognosis, regulated advice, or substitute professional judgment.

## Provenance and local sovereignty

Forecast history and relevant source records remain under the user's control. The module itself provides methods and optional local code, not personal forecasts or a live data feed.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
