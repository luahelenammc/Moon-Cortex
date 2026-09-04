<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# 🌙 Moon Cortex

**Domain capability architecture for AI: start from the real field, compile only what the situation needs, and leave the result under local ownership.**

AI systems can generate impressive artifacts while still getting the underlying responsibility wrong. A polished template can be useless if it assumes the wrong domain shape, activates capabilities the user does not need or leaves the resulting system dependent on the upstream prompt that created it.

Moon Cortex is a public pre-release architecture for a different route: understand a domain field first, instantiate a bounded module through a form that fits that domain and produce a user-local capability that can keep operating on its own sources.

This repository is the canonical public body of Moon Cortex.

> 📦 **Current public module portables**  
> 💸⬇️ [**Financial Living System (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip)  
> 🧭 [**Social Support Navigation System (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/social-support-navigation-system.zip)

## Why Moon Cortex exists

Domain work fails when form arrives before understanding. An AI may see that a user wants help with finances, social support or another domain and immediately reach for a familiar dashboard, file tree, checklist or schema. That can create structure without creating fit.

Moon Cortex treats a domain capability as something that should be **compiled from the field rather than imposed on it**. A module defines a stable responsibility and public semantics. Its entry interface discovers what the user actually has, what is missing, what can be activated, where the result can live and what should remain outside the system.

The goal is not maximal machinery. It is the smallest living capability that is legible, maintainable and locally sovereign.

## Start with the need, not the repository vocabulary

| If you need to… | Start here |
|---|---|
| Build a personal-finance organization and reconciliation system around a real financial situation | [Financial Living System](modules/financial-living-system/README.md) |
| Use the complete Financial Living System with an AI | [Download its complete package (.zip)](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) |
| Navigate a fragmented social-support situation into functions, barriers, institutional routes and owners | [Social Support Navigation System](modules/social-support-navigation-system/README.md) |
| Use the complete Social Support Navigation System with an AI | [Download its complete package (.zip)](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/social-support-navigation-system.zip) |
| Preview module families still incubating behind the public boundary | [Incubated Modules Preview](PREVIEW.md) |
| Understand module identity, installation and user-local sovereignty | [Architecture](ARCHITECTURE.md) |
| Inspect what is public, synthetic or deliberately excluded | [Public Boundary](PUBLIC_BOUNDARY.md) |
| Reuse or adapt public material with correct attribution | [Licensing](LICENSING.md) |
| See what changed across the public pre-release | [Changelog](CHANGELOG.md) |

You do not need to understand the future Cortex taxonomy before using a current module. The public surface is usable before the wider module family is finished.

## The architecture in one minute

Moon Cortex uses a generic loop, but a module may instantiate that loop differently:

**real field → domain module → domain-shaped entry interface → proportional local form → user-local operation → feedback and reconfiguration when needed**

### Financial Living System

```text
user's financial reality
        ↓
Moon Cortex · Financial Living System
        ↓ instantiated through
Adaptive Finance Bootstrap
        ↓ field discovery + capability compilation
user-local living financial system
```

### Social Support Navigation System

```text
person's real situation
        ↓
Moon Cortex · Social Support Navigation System
        ↓ orchestrated through
Social Support Navigator
        ↓ case reconstruction + passage mapping
user-local support route, case state or handoff
```

The difference is intentional. Finance is an integrated financial system with adaptive capability compilation. Social support is a field-shaped navigation system whose useful output may be a direct next step, a Resource Pack, a Living Case State or a bounded Support Handoff. One bootstrap shape does not legislate the whole Cortex.

Principles that carry most of the architecture:

- **Field before form.** Understand the situation before choosing files, schemas or workflows.
- **Capability before decoration.** Activate a mechanism because the field earns it, not because the module happens to contain it.
- **Access is not activation.** A capability, connector or upstream method being available does not mean it belongs in the local system.
- **Domain shape matters.** Modules may have different entrypoints, internal contracts and local outputs.
- **Installation is not permanent dependency.** A generated local system should operate from its own authoritative sources after installation.
- **Claims follow evidence.** Public artifacts, synthetic tests and private donor lineage remain distinct.

## Current public modules

| Module | Public responsibility | Entry / instantiation | Status |
|---|---|---|---|
| [Financial Living System](modules/financial-living-system/README.md) | Personal-finance organization, state and reconciliation shaped around the user’s actual financial field | [Adaptive Finance Bootstrap](modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md) | `0.1.0-pre.4` |
| [Social Support Navigation System](modules/social-support-navigation-system/README.md) | Social-support problem reconstruction, barrier mapping, institutional navigation, ownership and safe handoffs | [Social Support Navigator](modules/social-support-navigation-system/SOCIAL_SUPPORT_NAVIGATOR.md) | `0.1.0-pre.1` |

These are the first demonstrated public modules, not a decree that future Cortex systems must use either topology.

## Financial Living System

The Financial Living System is not a budget template. Its canonical transport unit is the complete module ZIP. The **Adaptive Finance Bootstrap** is the entrypoint inside that package, not a separate installable product.

Its integrated system can remain small for a simple salaried user or compile additional capabilities when the field contains credit tails, reimbursements, irregular income, multiple currencies, protected reserves, shared costs or other material complexity.

📦 [**Download the complete Financial Living System package (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip)

## Social Support Navigation System

The Social Support Navigation System turns a fragmented support situation into a smaller, safer and more institutionally routable passage. It starts with function and dependency mapping, identifies barriers and a first useful door, verifies current resources by jurisdiction, assigns owners and uses event-based checkpoints.

Its canonical transport unit is the complete module ZIP. The **Social Support Navigator** is the entry interface inside that package. A simple request can remain a direct answer; a complex situation may earn a local Living Case State, Resource Pack or Support Handoff.

📦 [**Download the complete Social Support Navigation System package (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/social-support-navigation-system.zip)

The module is not a government office, public defender, law practice, social-work service, clinical service, emergency dispatcher, eligibility authority or substitute decision-maker. Its private donor lineage is identified in the module documentation without exporting private cases or live resources.

## Moon Cortex and Moon Source

Moon Cortex is distinct from [Moon Source](https://github.com/luahelenammc/Moon-Source).

Moon Cortex owns domain-module identity and functional lineage. Moon Source owns its public context architecture and can be deliberately consulted as an installation or context-governance bridge. A module may use those public methods when available, but the resulting user-local system does not become a Moon Source mirror or require routine upstream retrieval.

The short boundary is:

> **Cortex by identity. Module by domain-shaped instantiation. Moon Source by installation governance. The user by final sovereignty.**

## Evidence, boundary and reuse

Moon Cortex is strict about the difference between a public mechanism existing and a larger claim being proven.

- [Public Boundary](PUBLIC_BOUNDARY.md) defines what the public body includes and excludes across both module families.
- [Financial Reality Test](modules/financial-living-system/docs/FINANCIAL_REALITY_TEST.md) defines bounded synthetic validation for the finance module.
- [Social Navigation Reality Test](modules/social-support-navigation-system/docs/SOCIAL_NAVIGATION_REALITY_TEST.md) defines bounded synthetic validation for the social-support module.
- [Licensing](LICENSING.md) governs reuse under **CC BY 4.0** for the current documentation, methods, examples and textual specifications.

A public artifact is not external adoption. A synthetic example is not a case study. A bounded test is not universal correctness.

## Repository map

| Need | Canonical route |
|---|---|
| Moon Cortex architecture and responsibility boundaries | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Financial Living System | [modules/financial-living-system/](modules/financial-living-system/) |
| Social Support Navigation System | [modules/social-support-navigation-system/](modules/social-support-navigation-system/) |
| Preview of incubated module families | [PREVIEW.md](PREVIEW.md) |
| Public/private disclosure boundary | [PUBLIC_BOUNDARY.md](PUBLIC_BOUNDARY.md) |
| Licensing and attribution | [LICENSING.md](LICENSING.md) + [NOTICE](NOTICE) |
| Public change history | [CHANGELOG.md](CHANGELOG.md) |
| Financial Living System portable | [downloads/financial-living-system.zip](downloads/financial-living-system.zip) |
| Social Support Navigation System portable | [downloads/social-support-navigation-system.zip](downloads/social-support-navigation-system.zip) |
| Related context architecture | [Moon Source](https://github.com/luahelenammc/Moon-Source) |
| Moon’s broader professional context | [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en) |

## Current baseline

**Status:** public pre-release  
**Current public modules:** Financial Living System `0.1.0-pre.4`; Social Support Navigation System `0.1.0-pre.1`  
**Current downloadable portables:** one module-specific ZIP for each public module  
**Repository-wide portable:** none  
**Structural grammar:** MSL 4.3

Moon Cortex was created by **Lua Helena Moon Martins Cardoso (Moon)**. Some materials were developed through an AI-assisted coauthorial process with **Áurion**. Moon retains final authority.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en)
