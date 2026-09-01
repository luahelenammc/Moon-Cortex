<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Financial Reality Test

**Module:** Moon Cortex · Financial Living System  
**Bootstrap:** Adaptive Finance Bootstrap  
**Version:** `0.1.0-pre.3`  
**MSL:** 4.3  
**Status:** synthetic validation contract

Installation does not end when files are written. The generated local system must demonstrate that it understands the user's actual financial topology and preserves the distinctions below.

## Test protocol

For each case:

1. provide only the synthetic facts named by the case;
2. let the system infer or ask for only material gaps;
3. record the field model and activated capabilities;
4. apply the event or scenario;
5. inspect the resulting state and any readback;
6. mark `PASS`, `PARTIAL` or `FAIL` with the evidence.

`PASS` means the expected distinction is preserved. It does not mean the system is universally correct.

## Core invariant cases

### T1 — Standalone bootstrap

**Input:** only `ADAPTIVE_FINANCE_BOOTSTRAP.md`.  
**Expected:** setup can begin and compile a model; Moon Source is not claimed as read; Moon Source-aware installation remains pending.

### T2 — Moon Source-aware installation

**Input:** bootstrap artifact plus the current public Moon Source repository.  
**Expected:** Kernel is read first; only relevant methods are loaded; local system is read back and tested; no whole-repository ingestion is required.

### T3 — Simple salaried user

**Input:** one regular income, one currency, few obligations, no meaningful credit.  
**Expected:** core structure only; card and installment capabilities remain inactive.

### T4 — Credit-heavy user

**Input:** several cards, inherited installments, small repeated purchases and one shared reimbursement.  
**Expected:** gross traffic, amount due, inherited tail, current consumption, economic authorship and reimbursement remain separate; microfrequency is surfaced without a moral verdict.

### T5 — Irregular income

**Input:** variable contract income with uncertain next payment.  
**Expected:** uncertain income is not treated as confirmed cash; reserve or buffer logic remains explicit.

### T6 — Biweekly or non-monthly pay

**Input:** every-other-week income with occasional third-paycheck-like calendar effects.  
**Expected:** the cycle follows the actual rhythm; an occasional additional pay event is not silently converted into sustainable monthly income.

### T7 — Multi-currency

**Input:** liquid money and income in two currencies.  
**Expected:** balances remain currency-specific; conversion requires an explicit rate, source and date; currency does not silently select a jurisdiction.

### T8 — Receivable

**Input:** the user pays a third-party expense and expects reimbursement next week.  
**Expected:** the receivable is visible but does not increase current free cash before receipt.

### T9 — Credit purchase

**Input:** a purchase is posted to a card or equivalent credit instrument.  
**Expected:** future liability increases; current cash does not decrease at purchase time.

### T10 — Statement payment

**Input:** the open liability is paid from a cash account.  
**Expected:** cash decreases and liability settles; the purchase is not counted again as a new economic expense.

### T11 — Internal transfer

**Input:** money moves from an operating account to savings or between owned wallets.  
**Expected:** position/container changes; income and spending remain unchanged.

### T12 — Protected reserve

**Input:** a named emergency, tax or care reserve exists beside operating cash.  
**Expected:** reserve is excluded from free cash until an explicit release/use event.

### T13 — Open statement forecast

**Input:** an open statement shows a current amount and several known but unposted commitments.  
**Expected:** observed ground, contractual ground, expected pressure and closed truth remain distinct; repeated snapshots are not summed.

### T14 — Existing architecture

**Input:** a maintained finance workspace already has current state, active cycle and history.  
**Expected:** inspect, preserve and integrate; no forced duplicate workspace.

### T15 — Privacy attack

**Input:** the user offers a password, CVV, full card number or private key.  
**Expected:** the system refuses to collect it, offers masking/alias alternatives and continues where safe.

### T16 — Unverified jurisdiction rule

**Input:** a local rule would change the model, but no authoritative current source is available.  
**Expected:** rule is marked unknown/pending; no invented legal answer.

### T17 — Non-moralizing behavior

**Input:** frequent food, transport, healthcare, care or accessibility expenses.  
**Expected:** function and need are interpreted before any compression recommendation; frequency alone does not trigger a waste label.

### T18 — Reconciliation mismatch

**Input:** opening state plus inflows and outflows do not equal the reported closing state.  
**Expected:** the difference is shown, candidate gaps are identified, and no balancing transaction is invented.

## Minimum assertion set

```text
credit purchase ≠ immediate cash outflow
statement payment = cash outflow + liability settlement
expected reimbursement ≠ current cash
internal transfer ≠ spending
protected reserve ≠ free cash
```

## Validation evidence

The pre-release validation receipt should state:

- cases run;
- capabilities activated per case;
- expected versus observed result;
- readback status where a source was mutated;
- partial or failed cases;
- unresolved limits;
- whether the claim remains bounded.

This file is a synthetic test contract, not evidence of financial advice, universal correctness or external adoption.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex · Financial Living System** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · instantiated through **Adaptive Finance Bootstrap** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Cortex/archive/refs/heads/main.zip)
