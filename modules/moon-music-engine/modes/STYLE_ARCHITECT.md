<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Style Architect

Build a generator-usable **sonic identity**, not an adjective salad. When the user explicitly wants music based on their taste and provides a valid Taste State, accept only a task-sized [Profile-to-Creation Bridge](../docs/PROFILE_TO_CREATION_BRIDGE.md) payload, not their entire profile. **When real songs, artists, albums, bands or playlists are supplied as references, route first through the [Reference-to-Feature Translator](REFERENCE_TO_FEATURE_TRANSLATOR.md).** It is a primary engine, not an optional footnote.

## Inputs
Use intent, emotional trajectory, musical references, language, vocals, any existing lyrics, and protected constraints. If the user supplies named real-music references, use the Translator's provenance-tagged feature map as input; never imply audio playback if it was not available. Extract generalized sonic behavior rather than writing an imitation command.

## Procedure
1. If real references are present, distill them using the [primary reference engine](REFERENCE_TO_FEATURE_TRANSLATOR.md), retaining their names on the analysis side and synthesizing original, uncopied attributes.
2. Identify 2–4 audible anchors: primary rhythmic behavior, lead instrument or voice, harmonic texture and production space.
3. Specify the arc: opening density, verse/refrain contrast, turning point, final landing. Don't force a verse/chorus on ambient or instrumental material.
4. Balance specific and flexible instructions. Prefer "dry snare under a slow pulsing bass with widening synth pads at the refrain" over "cinematic sad epic magical".
5. Write a compact Style prompt (and useful negative guidance). Proposed BPM may be a range if actual tempo is unknown.
6. If the user requests variations, apply [Controlled Variation](../docs/CONTROLLED_VARIATION.md) to eligible sonic variables only.
7. Check with [Musical QA](../docs/MUSICAL_QA.md). Mark anything not actually rendered as a proposed musical instruction.

## Output
Sonic DNA, concise copy-ready style prompt, optional arrangement notes, negative constraints where useful. Never infer a permanent user taste identity from one request.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
