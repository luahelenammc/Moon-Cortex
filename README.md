<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# 🌙 Moon Cortex

**AI domain systems that adapt to the situation, not the other way around.**

A budget is not always a spreadsheet. A difficult support situation is not just a checklist. An uncertain outcome is not automatically a percentage. An image request is not always solved by adding adjectives to a prompt.

**Moon Cortex starts with the real problem.** It is an open public family of domain-specific methods that help AI reconstruct what matters, select useful capabilities, and produce an appropriate result under the user's control.

Each module has its own job, entry point, boundaries, and output. **Moon Cortex is not one universal chatbot, a compulsory runtime, or a collection of interchangeable prompt templates.**

**[Choose a module](#choose-a-module)** · **[How to start](#getting-started)** · **[Explore the architecture](ARCHITECTURE.md)** · **[Public boundary](PUBLIC_BOUNDARY.md)**

## Choose a module

You don't need to understand the architecture first. Start with what you want to accomplish.

| Your situation | Domain module | What you can get | Start / download |
|---|---|---|---|
| **My finances are scattered** across paydays, bills, cards, obligations, reserves, or statements. | 💸 **[Financial Living System](modules/financial-living-system/README.md)** | A proportionate, user-owned living financial system for tracking timing, commitments, and reconciliation. | [First use](modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md#first-use) · [ZIP](downloads/financial-living-system.zip) |
| **I need to navigate support**, services, institutions, family dependencies, or overlapping practical barriers. | 🧭 **[Social Support Navigation System](modules/social-support-navigation-system/README.md)** | A clear first route, owners and checkpoints, or a bounded case state, Resource Pack, or Support Handoff when warranted. | [First use](modules/social-support-navigation-system/SOCIAL_SUPPORT_NAVIGATOR.md#first-use) · [ZIP](downloads/social-support-navigation-system.zip) |
| **I need to reason about an uncertain outcome** without confusing a hunch, evidence, confidence, and probability. | 📊 **[Probability Calibration System](modules/probability-calibration-system/README.md)** | A bounded forecast and update conditions; quantitative estimates only when the evidence and method justify them. | [First use](modules/probability-calibration-system/PROBABILITY_CALIBRATOR.md#first-use) · [ZIP](downloads/probability-calibration-system.zip) |
| **I want to create, edit, or assess an image**, work from aesthetic references, or choose a distinct visual language. | 🎨 **[Moon Image Cortex](modules/moon-image-cortex/README.md)** | A visual brief, direction sheet, edit instruction, renderer handoff, or evidence-bounded QA report. | [First use](modules/moon-image-cortex/VISUAL_DIRECTOR.md#first-use) · [ZIP](downloads/moon-image-cortex.zip) |

**Each module is independently usable.** Its README explains the field; its **canonical entry** teaches operative first use; its own ZIP carries the complete portable module. There is no mandatory repository-wide installation or universal Cortex package.

## What makes it a Cortex system?

The common idea is **field before form**: discover the actual situation before deciding what format, procedure, or capability it needs.

**Real situation → domain reconstruction → selective capability → appropriate local result → feedback and revision**

That shared movement can yield very different systems:

| Module shape | Why it is different |
|---|---|
| **Living system** · Finance | Obligations, timing, reserves, credit, and reconciliation may require interconnected ongoing state rather than a one-time budget. |
| **Navigation system** · Social support | A fragmented situation may need a first useful institutional door, functional support map, owner, checkpoint, or safe handoff rather than a large database. |
| **Calibration method** · Probability | An estimate needs a defined outcome, evidence, provenance, uncertainty, and revision criteria. Sometimes a qualitative answer is the correct result. |
| **Visual direction system** · Images | A visual goal requires choosing a medium, composition, reference role, specialist method, and QA. Actual image rendering depends on an external tool. |

The architecture provides a common discipline, **not a requirement that every module copy the same file tree, data model, workflow, or runtime**.

## Getting started

1. **Pick the domain above.** You can start from a practical problem rather than a module name.
2. **Open its First use link**, or give its complete ZIP to an AI environment capable of reading the package. The canonical entry is the operational authority; the README is for understanding and navigation.
3. **Describe the real situation and your goal.** Share only the information and source material you are authorized and comfortable using. The module determines what additional context is actually needed.
4. **Use the output in your own context.** Keep continuing records, decisions, and generated local state with you or your authorized workspace. Revise when the situation changes.

A downloaded module is documentation and, where included, optional reference code. **It does not automatically install an AI model, connect accounts, grant permissions, run in the background, or validate its own results.** Any real tool operation needs the capability and authorization to exist.

## Shared design commitments

| Principle | What it means in practice |
|---|---|
| **Field before form** | Understand the real problem before deciding on a dashboard, list, score, image, or system. |
| **Domain identity matters** | Every module has its own responsibility and limits; one successful module is not a template forced onto another field. |
| **One authoritative entry** | A human-friendly README can explain the module, but the canonical entry owns its operational method and First use. |
| **Complete transport, selective attention** | Carry the whole module in its ZIP; load only the parts that matter for the current task. |
| **Access is not activation** | A documented method or available connector is not automatically required, enabled, or authorized. |
| **Local sovereignty** | The resulting state and decisions should remain under the user's or authorized project's control. |
| **Claims follow evidence** | A specification, a synthetic example, a passing test, a rendered result, and measured external impact are different kinds of evidence. |

See the [architecture](ARCHITECTURE.md) and [module design contract](docs/MODULE_DESIGN_CONTRACT.md) for the detailed public rules.

## Moon Cortex, Moon Source, and you

These are related, but they do different jobs.

| Layer | Responsibility |
|---|---|
| **Moon Cortex** | The **domain-system body**: what a finance, social-support, probability, or visual module is allowed to do and what useful local output it creates. |
| **[Moon Source](https://github.com/luahelenammc/Moon-Source)** | The **context-governance body**: source authority, freshness, provenance, transport, mutation, and handoff methods when intentionally applied. |
| **The user or authorized project** | The final owner of local facts, state, permissions, choices, and continuing operation. |

Moon Source is an optional public method bridge for these modules, **not** the owner of Moon Cortex and not a required permanent runtime.

## What's public, and what isn't?

The public repository contains generalized domain methods, module contracts, portable packages, fictional examples, limited validation materials, and explicit restrictions. Some methods were generalized from private donor systems, but **the donor corpora are not distributed here**.

It does **not** publish identifiable private records, real support cases, personal financial data, private forecasts, image reference packs, personal identity profiles, or credentials. It does not claim universal validity, professional authority, measured impact, external adoption, or image-model performance without supporting evidence.

| Publication state | Meaning |
|---|---|
| **Active public modules: 4** | The four modules in [Choose a module](#choose-a-module) have public entry points and individual ZIP packages. |
| **Public pre-release** | Methods, scope, evidence limits, and packaging remain open to responsible revision. |
| **Incubating families** | Selected future directions appear in [Module Preview](PREVIEW.md), but are not active public modules or promises of release. |
| **Transport** | One complete, module-specific ZIP per active module; no all-in-one repository-wide ZIP. |
| **Structural grammar** | MSL 5.1-compatible Markdown-native public surfaces. |

Read the full [public boundary](PUBLIC_BOUNDARY.md) before reusing sensitive workflows or making deployment claims.

## Explore the repository

| Looking for… | Open |
|---|---|
| **The four modules and their files** | [modules/](modules/) |
| **Portable downloads** | [downloads/](downloads/) |
| **Overall architecture** | [ARCHITECTURE.md](ARCHITECTURE.md) |
| **How to design or revise a module** | [Module Design Contract](docs/MODULE_DESIGN_CONTRACT.md) |
| **Which names and paths remain stable** | [Repository Naming and Versioning](docs/REPOSITORY_NAMING_AND_VERSIONING.md) |
| **What is excluded from public release** | [PUBLIC_BOUNDARY.md](PUBLIC_BOUNDARY.md) |
| **Future and incubating module directions** | [PREVIEW.md](PREVIEW.md) |
| **Licenses, attribution, and reuse terms** | [LICENSING.md](LICENSING.md) · [NOTICE](NOTICE) |
| **Release and repository history** | [CHANGELOG.md](CHANGELOG.md) |
| **Related context architecture and creator's work** | [Moon Source](https://github.com/luahelenammc/Moon-Source) · [Professional site](https://www.luahelena.com.br/ia/?lang=en) |

**Moon Cortex was created by Lua Helena Moon Martins Cardoso (Moon).** Some public materials were developed through AI-assisted coauthorial work with **Áurion**; Moon retains final human authority.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
