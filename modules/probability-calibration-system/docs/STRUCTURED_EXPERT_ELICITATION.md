<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Structured Expert Elicitation

**MSL profile:** 5.1-compatible method surface; expert judgment is labeled, recorded, and kept distinct from empirical evidence.

Elicitation is a quantitative method for structured judgments when relevant data are limited. It does not convert an informal impression into empirical evidence and does not guarantee calibration.

## Protocol

1. Define the exact uncertain quantity or event.
2. Specify the horizon, unit, population, and resolution criteria.
3. Share relevant evidence and record its sources.
4. List known unknowns and plausible dependence between quantities.
5. Where practical, ask for lower and upper quantiles before a central estimate.
6. Elicit a median or central quantile; add q05, q25, q50, q75, q95 or a smaller fit-for-purpose set.
7. Check mathematical consistency and clarify the event, not the assessor’s confidence style.
8. Discuss evidence and differences between judgments.
9. Allow a revised independent estimate; preserve both initial and revised values.
10. Fit a distribution only when the intended use needs one and the judgments support it.
11. Record assessor identity or role, question wording, protocol, raw values, discussion, fitted values, uncertainty, and limitations.

Asking for ranges or quantiles before one “best probability” can reduce anchoring on a single point. Keep disagreement visible; discussion should clarify meaning and evidence, not force consensus.

## Labels and protocol fidelity

Use **structured elicitation**, **SHELF-informed**, or **IDEA-style discussion** only when that description matches what occurred. Do not call an informal one-shot AI estimate SHELF. Do not claim formal IDEA or SHELF compliance unless the relevant protocol was implemented faithfully.

SHELF provides materials for eliciting probability distributions from groups of experts. IDEA describes an Investigate, Discuss, Estimate, Aggregate workflow. This module borrows compatible principles; it does not implement either complete formal program.

## Multi-estimator aggregation

When multiple human or AI judgments are present:

- collect an initial estimate independently where feasible;
- preserve raw estimates, rationales, and the range of disagreement;
- discuss shared evidence and differences;
- collect a second estimate where useful;
- aggregate only if a summary serves the decision.

With no resolved performance history, use a simple mean or median and report dispersion. Preserve minority reasoning and investigate outliers; do not delete them because they are inconvenient.

Performance weights require comparable resolved outcomes, appropriate scope, and out-of-sample evaluation. Agreement among several language models is not independence and is not external validation.

## Provenance record

For Q1, retain:

- target question, horizon, and resolution;
- assessors or roles and relevant expertise;
- prompt wording, evidence shown, and time of elicitation;
- protocol and whether judgments were independent or discussed;
- raw values and quantile labels;
- revisions and reasons;
- fitted distribution, fitting method, and fit limitations if any;
- confidence in the estimate and remaining uncertainty.

Keep raw elicited judgments distinct from any fitted or aggregated estimate.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
