<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Universal Financial Invariants

**Module:** Moon Cortex · Financial Living System  
**Bootstrap:** Adaptive Finance Bootstrap  
**Version:** `0.1.0-pre.2`  
**MSL:** 4.3  
**Status:** public method specification

This document extracts financial mechanisms that remain useful across jurisdictions, payment systems, currencies and income rhythms. It is an ontology of distinctions, not a country-specific chart of accounts.

## What must remain distinct

### Cash and liability

- A purchase made on credit creates or increases a future liability. It is not an immediate cash outflow.
- Paying a statement is a cash outflow and a liability settlement. It is not a second economic expense.
- A prepayment, credit, refund or charge reversal reduces the amount due, but does not erase the gross transaction history.
- An internal transfer changes the location or ownership view of money. It is not income or spending by itself.
- An expected reimbursement is not cash until the money is actually received.
- A protected reserve is not free cash merely because it is visible in an account.
- One economic obligation must not be counted simultaneously as cash spending, future credit liability, reserve use and reimbursement unless each entry has a different, explicit role.

### Economic authorship

The local system should distinguish, when relevant:

- the person legally or operationally charged by an instrument;
- the person who economically owns the expense;
- a shared expense and its split rule;
- a third-party expense expected to be reimbursed;
- a formal obligation that passes through a payment instrument;
- an unresolved or disputed attribution.

A card can carry another person's purchase. The issuer does not become an accounting philosopher merely because it sends the bill to one name.

### Temporal ownership

Money received now can belong economically to a future period. This applies to advances, bonuses, reimbursements, seasonal income and other irregular inflows.

The system must keep separate:

- when money became visible;
- which period economically owns it;
- which obligations it is protecting;
- how much remains available for current use.

An advance is not automatically recurring income. An uncertain future inflow is not confirmed cash.

### Forecast states

Where a future cycle is still open, distinguish the strength of the ground:

| State | Meaning |
|---|---|
| `observed_ground` | Amount already visible in a statement, account or source snapshot |
| `contractual_ground` | Known future obligations supported by a contract, installment schedule or recurring commitment |
| `expected_pressure` | Likely additions inferred from rhythm or history but not yet posted |
| `closed_truth` | Final amount confirmed after the cycle closes |

An open statement is an observed floor, not an oracle. Successive snapshots of the same open cycle replace the prior photograph; they are not added together.

### Reconciliation

Every material cycle should be able to explain:

> **Opening liquid position + confirmed inflows − confirmed cash outflows ± internal movements and adjustments = closing liquid position.**

The exact presentation may vary by host. The following must remain visible when relevant:

- opening state;
- confirmed inflows;
- confirmed cash outflows;
- transfers and reclassifications;
- credits, refunds and adjustments;
- protected reserves;
- liabilities settled;
- closing state;
- unresolved difference.

If the equation does not close, expose the difference and the best-supported candidate explanations. Never manufacture a balancing transaction.

### Epistemic typing

Financial output should preserve the distinction between:

- `confirmed_fact` — directly evidenced by a statement, account, receipt or explicit user report;
- `calculation` — derived arithmetically from confirmed inputs;
- `inference` — a reasoned interpretation that may be updated;
- `estimate` — a provisional numerical expectation;
- `recommendation` — an action proposed by the system or user;
- `pending_confirmation` — a gap whose resolution may change the model.

Do not use a polished number to disguise a weak source.

## Cycle semantics

The system may use a calendar month, payday cycle, statement cycle, billing cycle or custom period. It must declare the active cycle and avoid confusing:

- purchase date;
- statement closing date;
- due date;
- income date;
- reimbursement date;
- economic competence or ownership period.

The month is a useful container. It is not a law of nature.

## Conditional credit invariants

When credit instruments exist and materially affect decisions, the system may activate:

- gross traffic versus final amount due;
- new current-cycle consumption versus inherited installments;
- installment tail and final competence;
- payment, prepayment, credit and refund effects;
- economic authorship and reimbursable transit;
- microfrequency aggregation;
- replacement analysis when an expiring installment is followed by a new one;
- open-cycle ground and next-cycle anticipation.

These capabilities are conditional. A user without meaningful credit exposure should not receive card machinery as decorative furniture.

## Reserve invariants

A reserve has a purpose, owner, scope and release condition. The system should distinguish:

- protected reserve;
- conditional reserve;
- flexible reserve;
- unassigned savings;
- card or liability coverage;
- future-income replacement;
- emergency liquidity.

Reserve allocation is a reclassification of available money, not a consumption event. Releasing a reserve becomes a cash movement only when it actually changes the position.

## Shared-cost invariants

When money crosses people or households, record enough to prevent ambiguity:

- economic owner;
- relevant cycle or competence;
- source and purpose;
- amount and split rule;
- status: expected, received, offset, disputed or closed;
- destination of reimbursement;
- evidence and confidence;
- duplicate or ambiguity flag.

Third-party obligations do not become current free cash before settlement.

## Behavioral reading invariant

Frequency is a signal, not a moral verdict.

Before suggesting compression, read:

- function;
- need;
- accessibility;
- recurrence;
- replaceability;
- timing;
- economic authorship;
- effect on the user's actual safety.

High-frequency food, transport, healthcare, care, pets, culture or support spending may be structurally necessary. The system exists to make forces legible, not to turn every repeated expense into a confession.

## Public boundary

These invariants are generalized from the private Finanças Moon donor lineage. No personal balance, salary, account, card, family ledger, statement, health cost or private source detail is part of this specification.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex · Financial Living System** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · instantiated through **Adaptive Finance Bootstrap** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Cortex/archive/refs/heads/main.zip)
