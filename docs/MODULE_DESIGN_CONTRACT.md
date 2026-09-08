<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Moon Cortex Module Design Contract

A public Cortex module must be understandable, enterable and safely usable without requiring the newcomer to learn the repository taxonomy first.

## Domain identity before copied morphology

A module earns its shape from its domain. Do not copy the file tree, bootstrap, state model, output family or runtime assumptions of another Cortex module merely because that module already works.

Every module must identify:

- the real field it serves;
- its domain responsibility;
- its canonical operational entry;
- the boundaries it must not cross;
- what local state or output the user should own after use;
- what evidence supports its public claims;
- what remains hypothetical, synthetic, unvalidated or jurisdiction-dependent.

A new module should add a domain capability, not a renamed template.

## Human entry and embedded first use

The module `README.md` is the primary human-facing entry surface. It should explain how to begin from inside the component instead of sending the newcomer to a detached onboarding file by default.

A new public module, and an existing module when it receives a material documentation or package revision, should make first use discoverable near the beginning of its README. The exact heading may follow the module's voice, but the content must answer plainly:

- what the module is for;
- whether anything is actually installed;
- what package or canonical entry should be given to the AI;
- what the human should say or provide first;
- what should happen next;
- which actions still depend on a real connector, tool, permission, professional authority or manual step;
- what the module does not claim or do.

The README may include a starter prompt, tiny example and troubleshooting path where useful. The goal is not identical prose across modules; the goal is that each module teaches its own first run.

Do not create a separate `FIRST_USE.md` merely because onboarding grows. A detached onboarding surface is justified only when it has a genuinely independent audience, lifecycle, transport contract or responsibility that cannot remain coherent in the README.

## Human entry is not operational authority

The README teaches the human how to enter. The module's canonical operational entry governs AI-side execution.

```text
README.md
= identity + orientation + first use

canonical module entry
= operational routing / instantiation authority

module package
= complete transport surface
```

These roles may coexist in one module without becoming competing semantic bodies.

A README must not silently change the operational contract. If the README and canonical entry disagree, the disagreement must be resolved explicitly rather than letting onboarding prose become a hidden second specification.

## Transport, attention, installation and runtime are different states

Cortex modules may travel as complete packages, but complete transport does not mean complete active context.

- **Transport** says what moves together.
- **Attention** says what the executing AI needs to load now.
- **Entry** says which interface begins the module's operation.
- **Installation or setup** says what local capability is created or configured, if any.
- **Runtime** says what keeps operating after the initial use.

Documentation alone does not create a connector, account permission, model capability, background service, professional authority or persistent runtime.

If an external capability is required, the module must distinguish:

```text
instruction to use a capability
≠
capability actually available and authorized
```

If the interface cannot perform a step, say what the user must do manually or what must be verified first.

## Complete transport, proportional attention

A canonical module ZIP may include several cooperating files because the module itself is the portable unit. That does not require the AI to ingest every file for every request.

Package completeness protects portability and recoverability. Active attention remains proportional to the field.

A module should therefore expose enough package anatomy for routing without making the user coordinate the internal architecture by hand.

## Local sovereignty

The public module shapes a capability; it does not own the user's resulting local state.

Whenever ongoing state is created, prefer a design where it can remain with the user, project or authorized local system and continue without hidden dependency on Moon Cortex, private donor material or invisible upstream memory.

The public package may provide structure, routing and reconfiguration rules. It should not become the sole place where a person's own current facts, decisions or records can be resumed unless that dependency is explicit and justified.

## Evidence and claim boundary

Keep these categories distinct:

- public architecture;
- synthetic test;
- fictional example;
- donor lineage;
- user-local result;
- external adoption;
- measured impact;
- professional or regulatory validity.

One category does not silently prove another.

A module-specific README and canonical entry must preserve the repository's `PUBLIC_BOUNDARY.md` and any stronger domain boundary required by the module.

## Versioning and onboarding changes

A documentation or first-use clarification does not by itself earn a semantic version bump.

When feedback reveals confusion, classify the delta first:

```text
misunderstood first step / installation / integration / manual action
→ README or interface clarification

wrong domain rule / wrong routing contract / wrong operational behavior
→ semantic module change
```

Only the second category normally changes the module's behavioral contract and may require a release-state decision.

Human-facing titles remain stable according to [Repository Naming and Versioning](REPOSITORY_NAMING_AND_VERSIONING.md).

## Feedback as interface evidence

A newcomer misunderstanding the module is useful evidence about the entry surface. Do not dismiss it as user error, but do not automatically rewrite the domain method either.

The preferred response is:

1. identify the exact mental model the public surface created;
2. separate documentation/interface failure from semantic failure;
3. fix the smallest owning surface;
4. preserve the canonical operational body when its behavior remains correct;
5. promote the lesson into this contract only when it generalizes across modules.

## Promotion gate for a public module

Before a new module is treated as public-ready, confirm that:

- domain responsibility is distinct;
- public/private boundary is safe;
- canonical operational entry is explicit;
- README teaches the first run without requiring repository archaeology;
- installation/integration claims match actual capability;
- complete package transport is defined;
- active attention can remain proportional;
- local sovereignty is preserved;
- synthetic evidence is not described as external validation;
- title and version are separated;
- relevant validation and package checks pass.

The contract is intentionally shared at the repository level, while each module remains free to earn a different internal morphology.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en)
