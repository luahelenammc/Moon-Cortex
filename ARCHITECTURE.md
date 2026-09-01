<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Moon Cortex Architecture

**Status:** public pre-release

**Structural grammar:** MSL 4.3

Moon Cortex is a lineage for domain modules that help AI systems produce situated, user-owned capabilities. It is intentionally smaller than a complete platform or product specification. The repository currently exists to make one coherent module inspectable.

## The first demonstrated topology

```text
field / user's reality
        ↓
Finance Bootstrap Seed
        ↓ adaptive setup
Financial Field Model
        ↓ capability compilation
Personal Finance Engine specification
        ↓ optional installation bridge
user-local living finance system
```

The form comes from the field. A module may be a bootstrap seed when a fixed template would be too blunt for the domain. This release demonstrates that pattern for personal finance; it does not make a universal packaging rule for every future Cortex module.

## Responsibility boundaries

| Layer | Owns | Does not own |
|---|---|---|
| Moon Cortex | module identity, domain lineage and public module boundaries | the user's private runtime or Moon Source's public method body |
| Finance Bootstrap Seed | financial discovery, localization, capability routing and installation contract | a pre-filled personal finance system or financial advice |
| Moon Source | public context architecture and installation methods when deliberately consulted | ownership of the Finance module or perpetual runtime execution |
| User-local Finance Engine | current balances, obligations, decisions, sources, ledgers and updates after installation | Moon Cortex's public semantics |

The short contract is:

> **Cortex by identity. Moon Source by installation. The user by final sovereignty.**

## Transport, installation and runtime

These are separate states:

- **Transport:** the Finance Bootstrap Seed is self-contained and can begin setup without Moon Source.
- **Installation:** a canonical installation consults the current public Moon Source repository, reads its Kernel first and uses only the methods needed for that installation.
- **Runtime:** the generated Finance Engine operates from its own local sources. Routine transactions do not require Moon Source retrieval.

If the Moon Source bridge is unavailable, discovery and compilation may still finish. The result must say `ready_for_installation`, not pretend that canonical installation happened.

## MSL 4.3 posture

This repository uses Markdown-native, proportionate materialization:

- a source has a current role, scope, authority, freshness and update contract;
- a ledger tracks comparable events without becoming the whole history;
- a bridge translates between sovereign systems without silently transferring authority;
- a test documents what was actually validated;
- historical or superseded material is not allowed to govern the present by accident.

The repository deliberately does not create a machine-readable module registry, package manager, website mirror, runtime service or skill adapter in `0.1.0-pre.1`.

## Public/private boundary

Public files contain generalized mechanisms, synthetic examples, public claims and installation guidance. They do not contain the private donor system, personal transactions, account details, balances, family ledgers, statements or private Moon Source corpus.

The donor lineage is named so the extraction remains honest. Naming lineage does not publish the donor.

## What this pre-release establishes

It establishes a bounded public module with:

- adaptive setup rather than a fixed finance template;
- jurisdiction-neutral financial ontology;
- capability activation by observed need;
- explicit cash, liability, reserve, receivable and temporal-ownership distinctions;
- optional full, compact, minimal and existing-system installation profiles;
- a current Moon Source installation bridge;
- a synthetic Financial Reality Test and public claim ceiling.

It does not establish a stable Moon Cortex product, universal financial correctness, bank integration, autonomous transactions, regulatory compliance, external adoption or measured impact.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · first module: **Finance Bootstrap Seed 0.1.0-pre.1** · [Moon Source](https://github.com/luahelenammc/Moon-Source)
