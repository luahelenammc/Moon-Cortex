<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# 🌙 Moon Cortex

**Domain capability architecture for AI: start from the real field, compile only what the situation needs, and leave the result under local ownership.**

AI systems can generate impressive artifacts while still getting the underlying responsibility wrong. A polished template can be useless if it assumes the wrong domain shape, activates capabilities the user does not need, or leaves the resulting system dependent on the upstream prompt that created it.

Moon Cortex is a public pre-release architecture for a different route: understand a domain field first, instantiate a bounded module through an adaptive mechanism, and produce a user-local capability that can keep operating on its own sources.

This repository is the canonical public body of Moon Cortex.

> 📦 **Want the public source at once?**  
> 🌙⬇️ [**Download the complete Moon Cortex repository (.zip)**](https://github.com/luahelenammc/Moon-Cortex/archive/refs/heads/main.zip)  
> 💸⬇️ [**Download the complete Financial Living System module (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip)

## Why Moon Cortex exists

Domain work fails when form arrives before understanding. An AI may see that a user wants help with finances, projects, research or another domain and immediately reach for a familiar dashboard, file tree, checklist or schema. That can create structure without creating fit.

Moon Cortex treats a domain capability as something that should be **compiled from the field rather than imposed on it**. The module defines the stable responsibility and public semantics. Its instantiation mechanism discovers what the user actually has, what is missing, what can be activated, where the result can live and what should remain outside the system.

The goal is not maximal machinery. The goal is the smallest living capability that is legible, maintainable and locally sovereign.

## Start with the need, not the repository vocabulary

| If you need to… | Start here |
|---|---|
| Build a personal finance organization and reconciliation system around a real financial situation | [Financial Living System](modules/financial-living-system/README.md) |
| Use the Financial Living System with an AI | [Download the complete Financial Living System package (.zip)](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) and keep the full package together |
| Preview the module families currently incubating behind the public boundary | [Incubated Modules Preview](PREVIEW.md) |
| Understand what Moon Cortex owns versus the bootstrap, Moon Source and the user-local runtime | [Architecture](ARCHITECTURE.md) |
| Inspect what is public, synthetic or deliberately excluded | [Public Boundary](PUBLIC_BOUNDARY.md) |
| Reuse or adapt public material with correct attribution | [Licensing](LICENSING.md) |
| See what changed across the public pre-release | [Changelog](CHANGELOG.md) |

You do not need to understand the future Cortex taxonomy before using the current module. The public surface is deliberately usable before the wider module family is finished.

## The architecture in one minute

Moon Cortex currently demonstrates this loop:

**real field → domain module → adaptive instantiation → proportional local form → user-local operation → feedback and reconfiguration when needed**

For the first public module:

```text
user's financial reality
        ↓
Moon Cortex · Financial Living System
        ↓ instantiated through
Adaptive Finance Bootstrap
        ↓ field discovery + capability compilation
user-local living financial system
```

A few principles carry most of the architecture:

- **Field before form.** Understand the situation before choosing files, schemas or workflows.
- **Capability before decoration.** Activate a mechanism because the field earns it, not because the module happens to contain it.
- **Access is not activation.** A capability, connector or upstream method being available does not mean it belongs in the local system.
- **The bootstrap is not the product.** It is the adaptive instantiation mechanism for the module.
- **Installation is not permanent dependency.** A generated local system should operate from its own authoritative sources after installation.
- **Claims follow evidence.** Public artifacts, synthetic tests and private donor lineage are kept distinct.

## Current public modules

| Module | Public responsibility | Instantiation | Status |
|---|---|---|---|
| [Financial Living System](modules/financial-living-system/README.md) | Personal-finance organization, state and reconciliation shaped around the user's actual financial field | [Adaptive Finance Bootstrap](modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md) | `0.1.0-pre.4` |

Finance is the first demonstrated domain, not a decree that every future Cortex module must use the same packaging or bootstrap pattern.

For a deliberately low-detail glimpse of directions that are real enough to name but **not yet public releases**, see [Incubated Modules Preview](PREVIEW.md).

## Financial Living System

The Financial Living System is not a budget template and does not require the user to know Moon Cortex vocabulary. Its canonical transport unit is the complete module ZIP. The Adaptive Finance Bootstrap is the entrypoint inside that package, not a separate installable product.

It can remain small for a simple salaried user or compile additional capabilities when the field actually contains credit tails, reimbursements, irregular income, multiple currencies, protected reserves, shared costs or other material complexity.

📦 [**Download the complete Financial Living System module (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) — this is the default transport and use surface.

📘 [**Open the module README**](modules/financial-living-system/README.md) for package-first usage, installation states, examples and internal anatomy.

## Moon Cortex and Moon Source

Moon Cortex is distinct from [Moon Source](https://github.com/luahelenammc/Moon-Source).

Moon Cortex owns domain-module identity and functional lineage. Moon Source owns its own public context architecture and can be deliberately consulted as an installation/context-governance bridge. The Adaptive Finance Bootstrap may use those current public methods when available, but the generated user-local financial system does not become a Moon Source mirror or require routine upstream retrieval.

The short boundary is:

> **Cortex by identity. Bootstrap by instantiation. Moon Source by installation governance. The user by final sovereignty.**

## Evidence, boundary and reuse

Moon Cortex is deliberately strict about the difference between a public mechanism existing and a larger claim being proven.

- [Public Boundary](PUBLIC_BOUNDARY.md) defines what the public body includes and what remains private or excluded.
- [Financial Reality Test](modules/financial-living-system/docs/FINANCIAL_REALITY_TEST.md) defines bounded synthetic validation for the current module.
- [Privacy, Claims and Attribution](modules/financial-living-system/docs/PRIVACY_AND_CLAIMS.md) defines the module's public claim ceiling and safe-input boundary.
- [Licensing](LICENSING.md) governs reuse under **CC BY 4.0** for the current documentation, methods, examples and textual specifications.

A public artifact is not external adoption. A synthetic example is not a case study. A bounded test is not universal financial correctness.

## Repository map

Use this README for orientation; use deeper files only when the responsibility belongs there.

| Need | Canonical route |
|---|---|
| Moon Cortex architecture and responsibility boundaries | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Current finance module | [modules/financial-living-system/](modules/financial-living-system/) |
| Preview of incubated module families | [PREVIEW.md](PREVIEW.md) |
| Canonical adaptive finance instantiation interface | [ADAPTIVE_FINANCE_BOOTSTRAP.md](modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md) |
| Public/private disclosure boundary | [PUBLIC_BOUNDARY.md](PUBLIC_BOUNDARY.md) |
| Licensing and attribution | [LICENSING.md](LICENSING.md) + [NOTICE](NOTICE) |
| Public change history | [CHANGELOG.md](CHANGELOG.md) |
| Complete Financial Living System archive | [downloads/financial-living-system.zip](downloads/financial-living-system.zip) |
| Related context architecture | [Moon Source](https://github.com/luahelenammc/Moon-Source) |
| Moon's broader professional context | [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en) |

## Current baseline

**Status:** public pre-release / pre-inauguration  
**Current public module:** Financial Living System `0.1.0-pre.4`  
**Current instantiation mechanism:** Adaptive Finance Bootstrap  
**Structural grammar:** MSL 4.3

Moon Cortex was created by **Lua Helena Moon Martins Cardoso (Moon)**. Some materials were developed through an AI-assisted coauthorial process with **Áurion**. Moon retains final authority.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex · Financial Living System** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · instantiated through **Adaptive Finance Bootstrap** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Cortex/archive/refs/heads/main.zip)
