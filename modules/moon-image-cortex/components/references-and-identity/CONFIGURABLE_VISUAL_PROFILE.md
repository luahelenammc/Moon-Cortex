<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Configurable Visual Profile

**System:** Moon Image Cortex · **Type:** conditional cross-cutting component
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)

This file is a subordinate component, **not** another general entry, personal memory, or renderer. Use it only when the task earns it. Public documentation does not install tools or persist identity data.

## Trigger and first use

This optional component manages user-chosen visual preferences and explicitly scoped local state. Activate only when someone explicitly wants the system to use, define or refine **their own** aesthetic defaults across authorized tasks.

## Local state contract

The user can specify: recurring preferences, disallowed motifs, favored/avoided palettes, typical output formats, photo-edit preservation priorities, sensitivity to synthetic artifacts, how strongly to apply symbolic cues, and whether the profile is ephemeral or retained by their own workspace. Include provenance, consent, uncertainty, refresh conditions and a clear opt-out. **No Moon-specific physical appearance, source photos, signature tastes or private prompts are published here.**

## Override and routing

Current instructions beat profile defaults. A newly created visual request starts independently unless the user explicitly applies the profile or their authorized environment passes it in. Never treat a project or creator identity as a requirement to produce moons, purple palettes, cosmic maps or a recognizable house style. Omnialchemy and chosen specialists operate on the **current visual brief**, with this profile only as an optional constraint.

## Output and QA

Produce an inspectable user-owned `visual_preferences` record, optional application notes, conflict warnings and a reset procedure. If profile access or retention is unavailable, ask for relevant preferences in the current request and do not pretend they persist.

## Synthetic activation

A fictional artist opts for matte daylight, warm gray paper and editorial simplicity for their own posters. A later user request for saturated retrofuturism overrides those defaults without changing the stored profile.

## User-owned configuration model

A visual preference profile should accelerate familiar workflows **without claiming ownership over the person or the current request**. It is an optional set of defaults, not a personality inference, private biometric dossier, automatic aesthetic signature or universal style imposed by the engine.

### Configuration fields

| Category | Examples | Override |
|---|---|---|
| Default working media | Photography, illustration, editorial artifact, mobile-oriented image | Current task can select any other medium |
| Color preferences | Favored or excluded relationships, saturation, contrast and tone | Current explicit palette wins |
| Composition | More breathing room, strong focal hierarchy, typical aspect ratios | Required platform dimensions and task content win |
| Surface and defects | Natural film grain, paper, painting texture, dislike of plastic skin | Must remain consistent with actual medium |
| Symbolic motifs | Symbols the user likes, avoids or never wants applied automatically | Silence is **not** permission to insert recurring motifs |
| Image edit constraints | Preserve skin texture, identity, lens response and untouched regions | Target-image facts and explicit edit request govern |
| Accessibility | Legibility, caption placement, contrast and reduced decorative clutter | Applicable accessibility needs take priority |
| Retention and revision | Ephemeral session, user-managed reusable profile, opt-out and version history | No persistence claimed without actual authorized storage |

### Default hierarchy

1. Applicable law, consent, confidentiality and task-specific safety limits.
2. Current user instruction and supplied sources.
3. Observed facts in the actual image or reference, with uncertainty marked.
4. Opt-in preferences explicitly supplied for the current task.
5. Optional persistent preferences when an authorized environment actually provides them.
6. Generic engine defaults only where no conflict exists.

A profile is never allowed to rewrite the user's identity, declare a photographic observation certain, infer a sensitive trait or override a current style change. Even strongly preferred motifs remain *available*, not automatic.

### Update discipline

Treat `visual_preferences` as a user-readable object with `scope`, `confirmed_preferences`, `exclusions`, `source`, `last_revision`, `override_log` and `storage_authority`. If the user wants one-off experimentation, create a task-local override and do not silently mutate reusable preferences. Provide a simple reset path in systems where storage actually exists.

**Example:** Someone commonly prefers matte documentary daylight and minimal ornament, but requests a richly saturated 2008 skeuomorphic interface today. The current request routes to Web Retro or Aqua-Skeuo; the profile does not flatten it into documentary photography.

**Audit:** Did any profile preference appear without being opted in? Did current instructions override it? Were irrelevant biography, private photos or identity assumptions kept out of the directions?

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
