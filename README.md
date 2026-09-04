<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# 🌙 Moon Cortex

**Domain systems for AI: start from the real field, activate only what belongs there, and leave the result under local ownership.**

AI often reaches for form too early. A financial problem becomes a dashboard. A social-support problem becomes a checklist. A complex field gets forced into whatever schema, workflow or interface is already familiar.

**Moon Cortex takes the opposite route.** It is a public architecture and growing family of domain systems that help AI reconstruct a real situation first, then use a domain-specific method to produce the smallest useful capability, state or handoff that actually fits.

Moon Cortex is not one universal assistant, one mandatory runtime or a shelf of interchangeable templates. Each module has its own domain responsibility, entry interface, invariants, boundaries and output shape.

This repository is the canonical public body of Moon Cortex.

> ## 📦 Start with a module
>
> 💸 **Financial Living System** — organize and reconcile a real personal-finance field as one living, user-owned system.  
> [Read the module](modules/financial-living-system/README.md) · [Download the complete package (.zip)](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip)
>
> 🧭 **Social Support Navigation System** — turn a fragmented support situation into functions, barriers, institutional routes, owners and bounded next steps.  
> [Read the module](modules/social-support-navigation-system/README.md) · [Download the complete package (.zip)](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/social-support-navigation-system.zip)

## Why Moon Cortex exists

A useful AI system needs more than a polished output. It needs the right **domain shape**.

The same architectural form should not be imposed on personal finance, social support, visual work, learning, media or any other field merely because that form is convenient to generate. Different domains contain different kinds of state, risk, evidence, authority, transitions and useful outputs.

Moon Cortex therefore treats a domain system as something that should be **instantiated from the field rather than imposed on it**.

The governing question is not:

> *What template should we build?*

It is:

> **What capability does this real field require, and what is the smallest form that can carry it safely and usefully?**

## The Cortex loop

Every module can have a different internal morphology, but the public architecture follows the same broad movement:

```text
real field
    ↓
domain reconstruction
    ↓
Moon Cortex module
    ↓
domain-shaped routing and capability selection
    ↓
proportional local form
    ↓
user-local operation, ownership and reconfiguration
```

The loop is stable. The shape inside it is not.

A finance module may instantiate an integrated living system. A social-support module may instead produce a direct next step, a Resource Pack, a Living Case State or a bounded Support Handoff. Both belong in Moon Cortex because **the domain determines the morphology**.

## Core laws

A few principles carry most of the architecture:

- **Field before form.** Understand the situation before choosing files, schemas, dashboards or workflows.
- **Domain shape before universal interface.** A module should fit its field rather than imitate another successful module.
- **Capability before decoration.** Activate a mechanism because the situation earns it, not because the package happens to contain it.
- **Access is not activation.** A capability, connector or method being available does not mean it belongs in the current local system.
- **Complete transport, proportional attention.** A module may travel as a complete package while the executing AI loads only what the current task requires.
- **Installation is not permanent dependency.** The useful result should remain operable from the user’s own authoritative sources whenever possible.
- **Local sovereignty is part of the architecture.** Public modules can shape a local capability without owning the person’s resulting state, decisions or records.
- **Claims follow evidence.** Public artifacts, synthetic tests, donor lineage and external adoption are different evidentiary categories.

## Active public modules

| Module | Use it when… | Canonical entry | Typical local result |
|---|---|---|---|
| [Financial Living System](modules/financial-living-system/README.md) | financial reality needs to become legible across timing, obligations, reserves, credit, reconciliation or other material complexity | [Adaptive Finance Bootstrap](modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md) | a living user-local financial system |
| [Social Support Navigation System](modules/social-support-navigation-system/README.md) | a support situation is fragmented across needs, barriers, institutions, informal dependencies or unresolved next steps | [Social Support Navigator](modules/social-support-navigation-system/SOCIAL_SUPPORT_NAVIGATOR.md) | a direct route, Living Case State, Resource Pack or Support Handoff |

These are **active public modules** and the first demonstrated Cortex topologies. They are examples of the architecture’s range, not templates that future modules must copy.

## How to use a module

The normal path is intentionally simple:

1. **Choose the domain module that matches the problem.**
2. **Download its complete package.** Each active module has its own canonical ZIP.
3. **Give the package to the AI as operative context** and state the real situation or goal.
4. **Let the module-specific entry interface route the work.** The user should not need to learn the repository taxonomy first.
5. **Keep the useful result locally sovereign.** Ongoing state should live with the user, project or authorized local system rather than depending on hidden upstream memory.

The package travels whole; attention remains proportional.

## Moon Cortex and Moon Source

Moon Cortex is distinct from [Moon Source](https://github.com/luahelenammc/Moon-Source).

- **Moon Cortex** is the public **domain-system body**: it owns module identity, domain contracts, module-specific routing, boundaries and public lineage.
- **Moon Source** is the public **context-architecture body**: it governs sources, authority, freshness, provenance, transport, mutation, handoffs and related context operations.

A Cortex module may deliberately consult Moon Source during installation or reconfiguration without becoming a Moon Source component and without requiring Moon Source as a permanent runtime dependency.

In shorthand:

> **Cortex by domain identity. Moon Source by context governance. The user by final sovereignty.**

## Public boundary

Moon Cortex publishes generalized mechanisms, module contracts, synthetic examples, bounded tests, implementation guidance and explicit limitations.

It does **not** publish the private donor corpora from which some mechanisms were generalized, real personal records, live case states, private credentials or reconstructible combinations of protected material.

Likewise, the existence of a public module does not by itself prove external adoption, universal correctness, professional validity, regulatory compliance, measured impact or production-scale deployment.

The repository-level boundary is documented in [PUBLIC_BOUNDARY.md](PUBLIC_BOUNDARY.md). Each module also defines the limitations specific to its own domain.

## A growing family, not a frozen taxonomy

Moon Cortex is intentionally multi-module. More domain systems can join the public body when they have a clear responsibility, sufficient generalization, safe public boundaries and a morphology earned by their own field.

[**PREVIEW.md**](PREVIEW.md) shows selected module families still incubating behind the public boundary without exposing their private implementation state.

Incubation is a property of those future modules — **not of Moon Cortex as a whole**.

## Repository map

| Need | Canonical route |
|---|---|
| Understand the shared Cortex architecture | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Use the Financial Living System | [modules/financial-living-system/](modules/financial-living-system/) |
| Use the Social Support Navigation System | [modules/social-support-navigation-system/](modules/social-support-navigation-system/) |
| Preview incubating module families | [PREVIEW.md](PREVIEW.md) |
| Inspect the public/private boundary | [PUBLIC_BOUNDARY.md](PUBLIC_BOUNDARY.md) |
| Reuse or adapt public material | [LICENSING.md](LICENSING.md) + [NOTICE](NOTICE) |
| Follow public change history | [CHANGELOG.md](CHANGELOG.md) |
| Explore the related context architecture | [Moon Source](https://github.com/luahelenammc/Moon-Source) |
| See Moon’s broader AI work | [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en) |

## Current baseline

**Status:** active public architecture  
**Active public modules:** Financial Living System; Social Support Navigation System  
**Canonical transport:** one complete ZIP per module  
**Repository-wide portable:** none  
**Structural grammar:** MSL 4.3

Moon Cortex was created by **Lua Helena Moon Martins Cardoso (Moon)**. Some materials were developed through an AI-assisted coauthorial process with **Áurion**. Moon retains final authority.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en)
