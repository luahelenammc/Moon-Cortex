<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Profile-to-Creation Bridge

Use a personally owned Taste State to influence original music **only when the person explicitly requests it**. This bridge prevents two opposite errors: pretending a profile exists when it does not, and making every new composition sound like a fixed stereotype of its owner.

## Routing

| Intent | Action |
|---|---|
| "Map my music taste" | [Taste Cartographer](../modes/TASTE_CARTOGRAPHER.md), without music generation |
| "Compose for my taste" | select relevant Taste State features, then [Style Architect](../modes/STYLE_ARCHITECT.md) and/or [Song Prototyper](../modes/SONG_PROTOTYPER.md) |
| "Use these bands, but make it fit my taste" | [Reference Translator](../modes/REFERENCE_TO_FEATURE_TRANSLATOR.md) + optional user-authorized taste weighting |
| "Make something unusual for me" | a **Bridge**, Edge or Rift hypothesis, not all favorites averaged |
| "Ignore my musical profile" | no profile use, even if state is available |
| "Why didn't I like that output?" | [Generator Debugger](../modes/GENERATOR_DEBUGGER.md) plus user feedback; optional separate Taste State patch |

## Selective compilation

1. **Gate:** confirm the state was actually supplied or legitimately accessible, and the user wants it considered now. `sharing.use_for_creation = false` blocks profile-fed creation until the owner explicitly revises it.
2. **Scope:** choose 1–2 relevant constellations or one bridge, the stated listening context, user-confirmed likes, relevant conditional negatives and uncertainty. Do not copy the whole profile.
3. **Authority order:** current user instruction → authorship, voice, rights and lyrical invariants → user-confirmed conditional taste → tentative taste hypotheses → creative proposals. The current user may override their past self.
4. **Make an ephemeral creative payload:** `creative_goal`, 3–7 `sonic_features`, `conditional_context`, `negative_guidance`, `exploration_space`, `evidence_status`. Use generalized sound descriptors, not full listening histories or identifying facts.
5. **Build the song:** Style Architect supplies musical direction; Reference Translator supplies source-derived attributes; Song Prototyper drafts original form; Lyric Doctor protects words; Controlled Variation explores unlocked traits.
6. **Listen/learn only when real feedback arrives:** generating an output does **not** count as liking it. Propose an explicit, reversible local state delta.

## Example payload · synthetic

```json
{
  "creative_goal": "Original instrumental for extended focused listening",
  "sonic_features": ["soft hand percussion", "melody emerging gradually", "muted low-end", "plucked-string counterline"],
  "conditional_context": "quiet concentration",
  "negative_guidance": ["no continuous abrasive high-end"],
  "exploration_space": "one new acoustic timbre",
  "evidence_status": "provisional preference, user-stated",
  "profile_mutation": "none"
}
```

**External generator handoff:** transfer the **minimal music features**, not a person's profile file, streaming exports, playlist histories, demographics, contextual autobiography or sensitive associations. Permission to map is distinct from permission to store; permission to create is distinct from permission to transmit data externally. No automatic account or generator access is implied.

If the user requests a deliberately unfamiliar sound, reduce or turn off profile influence. Their new artistic direction wins over the model's historical guess.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
