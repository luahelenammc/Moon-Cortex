<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Core Invariants

**MSL profile:** 5.1-compatible Markdown-native module contract; uncertainty, evidence, freshness, and authority boundaries remain explicit.

These invariants govern every use of the Probability Calibration System.

## 1. Define the target

A forecast is about a specified event, population or case, and horizon. If the outcome cannot later be resolved, clarify it or say that the request is not yet estimable.

## 2. Keep fit, evidence, probability, and confidence distinct

- **Fit:** resemblance between the present case and a proposed reference class, analogue, or model.
- **Evidence:** information that bears on the target, with its reliability, directness, independence, recency, specificity, and coverage.
- **Probability:** the estimated chance of the defined outcome within the stated horizon.
- **Confidence:** the reliability of the probability estimate, given evidence, fit, assumptions, and stability.

None of these terms substitutes for another. High fit is not proof. Confidence is not the probability of the outcome.

## 3. Precision must be earned

Use qualitative bands when evidence does not support numerical detail. Use a quantitative probability only when a defensible data source or domain model supports it. State the basis and uncertainty. Never create precision to satisfy the form of a request.

## 4. There is no universal probability formula

Do not impose one equation, score, signal ladder, Bayesian prior, or weighting scheme on every field. Use a quantitative method only when the event, data, assumptions, and domain justify that method.

## 5. Evidence remains traceable

Separate observations from interpretation. Preserve source, date, provenance, contradictions, missing information, and the relation between each observation and the target. Repeated or dependent claims do not become independent evidence through repetition.

## 6. Forecasts can change

Every time-sensitive estimate has an evidence cutoff. Record assumptions and triggers that require refresh or manual recalibration. A changed estimate should identify what changed; it should not silently rewrite a prior forecast.

## 7. Actions are proportionate

State uncertainty and alternatives. Prefer reversible actions when uncertainty is material. A forecast is not a promise, an instruction, or a substitute for the user decision.

## 8. The domain keeps its authority

High-stakes, regulated, professional, or emergency matters require current qualified authority. The module may organize questions and evidence but does not claim professional or regulatory validity.

## 9. Local state remains local

Forecast logs, sensitive context, and user records remain under user control. Public examples and test cases are synthetic and do not demonstrate predictive performance.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
