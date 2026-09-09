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

## Human facade and embedded first use

A composite public module should normally expose two clearly different surfaces:

```text
module README
= human browse + presentation + directory navigation

canonical entry
= operational + semantic + embedded First use authority
```

The README should let a visitor understand what the module is, when it is relevant, where to start, where to download it, what major children exist and where authority lives. It must stay lightweight: it should route to the canonical entry rather than reproducing its starter prompt, troubleshooting path, operational laws or domain method.

The canonical entry remains the primary human-and-AI **operative** entry surface. A new public module, and an existing module when it receives a material documentation or package revision, should make first use discoverable near the beginning of that canonical entry. The exact heading may follow the module's voice, but the content must answer plainly:

- what the module is for;
- whether anything is actually installed;
- what package or canonical entry should be given to the AI;
- what the human should say or provide first;
- what should happen next;
- which actions still depend on a real connector, tool, permission, professional authority or manual step;
- what the module does not claim or do.

The entry must also include a starter prompt, tiny example and troubleshooting path where useful. The goal is not identical prose across modules; the goal is that each canonical entry teaches its own first run.

Do not create a separate `FIRST_USE.md` merely because onboarding grows. A module `README.md` is different: when the module directory has several meaningful children, the README legitimately owns human presentation and navigation. It must never become a competing operational entry or hidden second specification.

## One authoritative entry, not necessarily one file

The module's canonical entry carries operational authority and embedded first use. Internal docs, examples and a human-facing README remain valid when they own real responsibilities, but they are subordinate routes rather than competing authorities.

```text
README facade
= identity + concise orientation + navigation + Start / Download routes

canonical entry artifact
= semantic + operational + First use + routing / instantiation authority

module package
= complete transport surface
```

One authoritative entry does not mean one file. Composite modules should remain multi-file when docs, examples, changelog or adapters own real responsibilities, and a readable README is often desirable precisely because those children exist.

If a README and canonical entry disagree, the canonical entry governs. Repair the README unless the disagreement reveals that the operational contract itself is wrong.

## Transport, attention, installation and runtime are different states

Cortex modules may travel as complete packages, but complete transport does not mean complete active context.

- **Presentation** says how a human browses and understands the module before operation.
- **Transport** says what moves together.
- **Attention** says what the executing AI needs to load now.
- **Entry** says which authoritative interface begins the module's operation.
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

A module should therefore expose enough package anatomy for routing without making the user coordinate the internal architecture by hand. The repository README facade may describe that anatomy; the package contract decides what actually travels.

A presentation-only README does not by itself change package semantics. Do not add it to an established module ZIP merely because it exists in the GitHub directory unless the transport contract intentionally earns that change.

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

The canonical entry and module README must preserve the repository's `PUBLIC_BOUNDARY.md` and any stronger domain boundary required by the module.

## Versioning and presentation changes

A README restoration, presentation clarification or discoverability improvement does not by itself earn a semantic version bump. It does not change the canonical entry identity or operational contract.

A first-use clarification inside the canonical entry also does not automatically earn a semantic version bump, even when it changes the canonical entry hash or complete package bytes.

When feedback reveals confusion, classify the delta first:

```text
unclear module identity / discoverability / browse path
→ README presentation delta

misunderstood first step / installation / integration / manual action
→ canonical-entry onboarding or interface clarification

wrong domain rule / wrong routing contract / wrong operational behavior
→ semantic module change
```

Only the third category normally changes the module's behavioral contract and may require a release-state decision.

Human-facing titles remain stable according to [Repository Naming and Versioning](REPOSITORY_NAMING_AND_VERSIONING.md).

## Feedback as interface evidence

A newcomer misunderstanding the module is useful evidence about the public surface. Do not dismiss it as user error, but do not automatically rewrite the domain method either.

The preferred response is:

1. identify the exact mental model the public surface created;
2. separate presentation, onboarding and semantic failure;
3. fix the smallest owning surface;
4. preserve the canonical operational body when its behavior remains correct;
5. promote the lesson into this contract only when it generalizes across modules.

## Promotion gate for a public module

Before a new module is treated as public-ready, confirm that:

- domain responsibility is distinct;
- public/private boundary is safe;
- a composite module has a legible human browse surface when that materially improves navigation;
- canonical operational entry is explicit;
- canonical entry teaches the first run without requiring repository archaeology;
- README and canonical entry roles are visibly distinct;
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

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).