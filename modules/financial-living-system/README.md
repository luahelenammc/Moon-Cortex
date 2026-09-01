<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# 🌙 Moon Cortex · Financial Living System

**Adaptive personal-finance organization for AI: map financial reality before choosing structure.**

A budget template starts with categories. A dashboard starts with widgets. A finance app starts with whatever its database already knows how to store. Real financial life often starts somewhere messier: several pay rhythms, money that belongs to another period, credit purchases that are not current cash outflows, protected reserves that look spendable, reimbursements that have not arrived, or a perfectly usable spreadsheet that should not be replaced.

The Financial Living System is the Moon Cortex finance module for organizing that field into a living, user-owned financial system. It is instantiated through the **Adaptive Finance Bootstrap**, which discovers the situation before deciding what capabilities or local form are warranted.

> 📦 **Want the whole Financial Living System at once?**  
> 💸⬇️ [**Download the complete module (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) — bootstrap, methods, tests and fictional examples in one file.

## Why the Financial Living System exists

Personal-finance systems commonly fail in two opposite ways: they are too thin to preserve real distinctions, or so elaborate that the user ends up maintaining the system instead of using it.

The Financial Living System takes a field-first route. It separates the stable financial distinctions that matter from the optional capabilities that should appear only when the user's situation earns them. The result can therefore stay compact for a simple case and become richer only when credit, installments, irregular income, shared money, multiple currencies, protected reserves or other material complexity actually exists.

Its job is not to moralize spending or prescribe one ideal budget. Its job is to make financial state, obligations, timing and uncertainty **legible enough to reconcile and act on**.

## Start with reality, not the template

| If the situation contains… | Start with… |
|---|---|
| A simple salary, one currency and a few recurring obligations | Core state, reconciliation and reserve semantics |
| Credit cards, inherited installments or open statements | Credit, installment-tail and next-cycle capabilities |
| Reimbursements or shared costs | Economic authorship and receivable/shared-money ledgers |
| Irregular income or advances | Temporal ownership and irregular-income handling |
| Multiple currencies | Currency-specific state and explicit conversion evidence |
| An existing spreadsheet or finance workspace | Existing-system integration instead of replacement |
| Unclear jurisdiction-specific rules | Jurisdiction discovery and explicit verification boundaries |

The full routing surface lives in the [Capability Map](docs/CAPABILITY_MAP.md). The user does not need to choose these technical names during setup.

## The architecture in one minute

The module follows this loop:

```text
user's financial reality
        ↓
Financial Living System
        ↓ instantiated through
Adaptive Finance Bootstrap
        ↓
inspect → infer → ask only material gaps
        ↓
Financial Field Model
        ↓
activate only earned capabilities
        ↓
choose the smallest maintainable local form
        ↓
user-local living financial system
        ↓
readback + Financial Reality Test
```

The central law is:

> **Map the user's financial reality first, then generate the smallest local finance system that actually fits it.**

A few distinctions carry most of the system:

- credit purchase ≠ immediate cash outflow;
- statement payment = cash outflow + liability settlement;
- expected reimbursement ≠ current cash;
- internal transfer ≠ spending;
- protected reserve ≠ free cash;
- observed future pressure ≠ closed truth;
- available capability ≠ activated capability.

## Start here

Provide [`ADAPTIVE_FINANCE_BOOTSTRAP.md`](ADAPTIVE_FINANCE_BOOTSTRAP.md) to an AI as operative context.

**No command phrase is required.** The bootstrap is self-activating by default: the AI should begin adaptive setup automatically unless the user explicitly asks only to read, review or analyze the artifact without execution.

The AI should inspect any supplied financial material before asking the user to repeat it, discover only material gaps, preserve a sound existing system when one already exists, protect sensitive information and explain where the generated local system should live.

## What can be compiled

The Financial Living System has a small core and a conditional capability layer.

| Layer | Examples |
|---|---|
| Core | Current Financial State, Cycle Reconciliation, Temporal Ownership, Reserve Semantics, Double-Count Guards, Cycle Closing, Epistemic Typing |
| Conditional | Credit Card Intelligence, Installment Tail, Microfrequency, Next-Cycle Anticipation, Reimbursements, Shared Costs, Debt Schedule, Irregular Income, Multi-Currency, Tax Reserve, Subscriptions |

> **Access ≠ activation.**

A user without meaningful credit should not receive decorative card machinery. A user with an existing maintained spreadsheet should not receive a parallel five-file empire because folders happen to look serious.

## Installation states

The module distinguishes setup, installation and ordinary runtime.

### Standalone setup

With only the canonical bootstrap, an AI can discover the field, compile the Financial Field Model, map local terminology, select capabilities and produce an installation-ready plan.

### Moon Source-aware installation

When the current public [Moon Source](https://github.com/luahelenammc/Moon-Source) repository is deliberately available, the installer can use the [Moon Source Installation Bridge](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md). The Moon Source Kernel is read first, only the smallest relevant methods are loaded, the local system is materialized and read back, and the Financial Reality Test is run proportionately.

### User-local runtime

After installation, ordinary finance work should operate from the user's own local sources. Moon Source remains a justified reconfiguration or repair dependency, not a permanent upstream API.

In shorthand:

```text
self-contained in transport
Moon Source-aware at installation
locally sovereign at runtime
```

## Examples

The examples are fictional, didactic and non-evidentiary. They show how the same module compiles differently when the field changes.

- [Simple Salaried User](examples/SIMPLE_SALARIED_USER.md) — a deliberately small installation without credit machinery.
- [Credit and Non-Monthly Pay User](examples/CREDIT_AND_NONMONTHLY_PAY_USER.md) — biweekly income, credit tails, microfrequency and reimbursement.
- [Irregular Multi-Currency User](examples/IRREGULAR_MULTICURRENCY_USER.md) — uncertain income, multiple currencies, protected tax reserve and integration into an existing spreadsheet.

The examples are not case studies and do not contain private Finanças Moon data.

## Evidence, boundary and reuse

The module is deliberately conservative about what its public artifacts prove.

- [Financial Reality Test](docs/FINANCIAL_REALITY_TEST.md) defines bounded synthetic validation.
- [Privacy, Claims and Attribution](docs/PRIVACY_AND_CLAIMS.md) defines safe-input rules and the public claim ceiling.
- [Universal Financial Invariants](docs/UNIVERSAL_FINANCIAL_INVARIANTS.md) defines the financial distinctions intended to survive across jurisdictions and payment systems.
- [Moon Source Installation Bridge](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md) defines the optional installation/context-governance relationship.
- [Moon Cortex Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) governs reuse under **CC BY 4.0** for the current public textual body.

The financial architecture was generalized from the private donor system **Finanças Moon**. Naming that lineage does not publish the donor corpus or turn private financial facts into evidence.

## Module map

Use this README for orientation; use deeper files when the responsibility actually belongs there.

| Need | Canonical route |
|---|---|
| Run adaptive setup | [ADAPTIVE_FINANCE_BOOTSTRAP.md](ADAPTIVE_FINANCE_BOOTSTRAP.md) |
| See capability activation rules | [docs/CAPABILITY_MAP.md](docs/CAPABILITY_MAP.md) |
| Inspect cross-jurisdiction financial distinctions | [docs/UNIVERSAL_FINANCIAL_INVARIANTS.md](docs/UNIVERSAL_FINANCIAL_INVARIANTS.md) |
| Install with current public Moon Source methods | [docs/MOON_SOURCE_INSTALLATION_BRIDGE.md](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md) |
| Validate an installed local system | [docs/FINANCIAL_REALITY_TEST.md](docs/FINANCIAL_REALITY_TEST.md) |
| Inspect privacy, claims and attribution | [docs/PRIVACY_AND_CLAIMS.md](docs/PRIVACY_AND_CLAIMS.md) |
| Browse fictional scenarios | [examples/](examples/) |
| Follow module changes | [CHANGELOG.md](CHANGELOG.md) |
| Download the whole module | [financial-living-system.zip](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) |

## Current baseline

**Version:** `0.1.0-pre.3`  
**Status:** public pre-release  
**Structural grammar:** MSL 4.3  
**Canonical module path:** `modules/financial-living-system/`  
**Canonical instantiation artifact:** `modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md`

The executing AI should follow the user's language after activation. The public portable is English-first, model-agnostic and does not require a primary `SKILL.md`, bank connector, hosted UI or autonomous transaction layer.

Created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion**. Moon retains final authority.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex · Financial Living System** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · instantiated through **Adaptive Finance Bootstrap** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Cortex/archive/refs/heads/main.zip)
