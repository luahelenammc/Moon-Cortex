<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Synthetic Examples

**MSL profile:** 5.1-compatible examples; every scenario and datum below is fictional, low-stakes, and non-evidentiary.

These examples demonstrate method boundaries. They do not establish base rates, validate a model, or predict any real person or project.

## 1. Qualitative only

**Target:** Will a new neighborhood audio series reach a stated monthly audience within two months?  
**State:** The threshold is defined, but the first episode has not been released and no relevant comparison records exist.

- **Class:** Q0 qualitative-only.
- **Probability:** Not numerically estimable. A cautious qualitative band may be used after direct audience data exist.
- **Confidence:** Low; evidence is sparse.
- **Next step:** Record first-party listening data and revisit after the next episode.

Do not invent a percentage to complete the format.

## 2. Empirical reference class

**Target:** Will a fictional workshop series fill at least 12 places by its registration deadline?  
**Synthetic record:** Seven of ten prior workshops with the same registration window met the threshold. All ten consecutive records are included; venue capacity varied and is a comparability limitation.

- **Class:** Q2 empirical reference class.
- **Observed rate:** 7/10 = 0.70 for the described record.
- **Uncertainty:** With an explicitly chosen Beta(1,1) prior, the posterior mean is 8/12 ≈ 0.67; this is conditional on the prior and comparability assumptions.
- **Confidence:** Moderate at most; ten cases are limited.
- **Update trigger:** Review after current registrations or a change in promotion or venue.

The fraction describes a synthetic history. It does not guarantee the next outcome.

## 3. Beta-Binomial shrinkage with three successes in three cases

**Synthetic record:** Three comparable one-off sessions all met the attendance threshold. Use a stated uniform Beta(1,1) prior only for illustration.

- **Class:** Q2 with a Bayesian Beta-Binomial summary.
- **Posterior:** Beta(4,1), mean 0.80, with a broad upper-tail uncertainty interval.
- **Confidence:** Limited by the small record and the assumed class stability.

The naive 3/3 fraction is not a certainty estimate. Choosing a different justified prior changes the posterior and must be reported.

## 4. Bayesian likelihood-ratio update

**Synthetic target:** A fictional event occurs within one month. Start from prior probability 0.20. One documented synthetic evidence item has likelihood ratio 3.

~~~text
prior odds = 0.20 / 0.80 = 0.25
posterior odds = 0.25 × 3 = 0.75
posterior probability = 0.75 / 1.75 ≈ 0.43
~~~

- **Class:** Q3.
- **Provenance:** The prior and likelihood ratio each have an explicit synthetic source in this example.
- **Limit:** The calculation is conditional on those inputs; it does not validate them.

## 5. Correlated reports

**Target:** Do three articles independently confirm that a fictional venue is reserved?

**Evidence:** All three articles quote the same organizer announcement. There is one common source family and no direct venue confirmation.

- **Dependence:** Shared source / derivative reporting.
- **Update:** Do not multiply three likelihood ratios.
- **Next evidence:** A direct confirmation from the venue would add a distinct source, though independence still requires review.

## 6. Structured expert elicitation

Three fictional assessors independently estimate a defined event before discussion: 0.20, 0.45, and 0.75. Each records q05, q50, and q95 plus a rationale. After an IDEA-style discussion, they submit revised quantiles; both rounds remain in the record.

- **Class:** Q1 structured elicitation.
- **Aggregation:** A simple median may summarize the second round if useful.
- **Required display:** Preserve the range, individual rationales, disagreement, and limitations.
- **Label:** “IDEA-style discussion” is not a claim of formal protocol compliance.

Consensus is not required and does not create independent evidence.

## 7. Monte Carlo with uncertain parameters

Use a fictional prior distribution Beta(2,8) and one explicitly elicited synthetic likelihood-ratio distribution Lognormal(log(2), 0.3). Simulate 5,000 draws with seed 2026, applying one likelihood ratio to each sampled prior.

- **Class:** Q4.
- **Report:** Median posterior, central 50% and 90% intervals, simulation count, seed, and input provenance.
- **Limit:** The output only propagates these assumed distributions. It does not make them empirically grounded.

## 8. Low-probability, high-impact decision

**Synthetic values:** An adverse event has probability 0.02. Doing nothing has utility −100 if it occurs and 0 otherwise. A protective action costs 1 in all states and reduces the adverse-state utility loss to −20.

- **Expected utility of inaction:** 0.02 × (−100) + 0.98 × 0 = −2.
- **Expected utility of protection:** 0.02 × (−20) + 0.98 × (−1) = −1.38.
- **Reading:** Under these explicitly supplied values, protection has higher expected utility.

These fictional values do not determine what a real person should value or do. Probability and utility remain separate.

## 9. Forecast Ledger resolution

**Synthetic forecast:** Before a deadline, record “the fictional room reservation is confirmed by the venue,” the exact confirmation criterion, horizon, evidence cutoff, and probability. At the deadline, the venue archive is unavailable and the user cannot verify whether confirmation arrived.

- **Status:** Ambiguous or unresolved, with reason retained.
- **Scoring:** Exclude from binary scoring under the declared resolution policy.
- **Integrity:** Do not revise the original criterion after the deadline.

## 10. Brier and logarithmic scores

Two resolved synthetic cases receive probabilities 0.80 and 0.20; outcomes are yes and no:

~~~text
Brier = ((0.80 - 1)^2 + (0.20 - 0)^2) / 2 = 0.04
LogLoss = (-log(0.80) - log(0.80)) / 2 ≈ 0.223
~~~

This tiny fixture proves only that the formulas operate on these values. It is not a performance claim.

## 11. Recalibration with insufficient history

A fictional system has zero resolved forecasts. It may define a ledger, calculate scores after outcomes resolve, and test the implementation with synthetic fixtures.

- **Calibration status:** Insufficient history.
- **Recalibration:** Unavailable; no evidence-backed model can be fit.
- **Claims:** No measured reliability or performance claim is permitted.

## 12. Synthetic out-of-sample recalibration demonstration

For a deliberately small fictional demonstration, ten training forecasts all issue 0.80; five resolve yes and five no. Isotonic regression maps this training level to 0.50. A separate validation set contains four forecasts of 0.80 with outcomes yes, no, yes, no.

- **Raw validation Brier:** 0.34.
- **Recalibrated validation Brier:** 0.25.
- **Status:** A synthetic code-path demonstration with disjoint IDs only.
- **Limit:** These tiny generated records do not imply robustness, real calibration, or generalization. A production policy would require a use-specific sufficiency gate and much stronger validation.

## 13. High fit, low evidence

A fictional past workshop had a similar topic and venue, but only three selected events are recorded and the current registration window is shorter.

- **Fit:** High on topic and venue; incomplete on timing and audience.
- **Evidence:** Low; the selected record is too sparse for a stable base rate.
- **Probability:** Qualitative low-to-moderate reading, with low confidence.
- **Next step:** Check current registrations and compare consecutive like-for-like records.

Strong resemblance supports fit. It does not make sparse evidence strong.

## 14. Moderate probability, high confidence in the broad band

In a fictional, stable series, 96 of 200 consecutive comparable first-time registrations attended. Records are complete and each person appears once.

- **Fit:** High for the next session under the stated stability assumption.
- **Probability:** Moderate; 96/200 = 0.48 describes this synthetic record, not a guarantee for one event.
- **Confidence:** High in the broad moderate band; lower in any exact forecast for a particular session.
- **Update trigger:** A change in audience, schedule, location, or registration rules.

Confidence concerns the broad estimate, not whether a specific future event will occur.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
