<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Tool Adapters

Keep musical intelligence independent of any one generation service. Platform-specific field semantics and policies may change and must be confirmed when the exact current interface matters.

## Generic musical handoff
- **Style:** compact description of genre family, pulse, lead/vocal, instruments, production and dynamic progression.
- **Lyrics:** supplied original text or new original text only when requested, with simple section tags if compatible.
- **Exclusions:** a few high-value negative constraints.
- **Variant metadata:** optional exploration percentage, declared seed only if an actual seeded selector is used.
- **Execution:** text prepared / not rendered unless a real generator result is confirmed.

## Suno-oriented text layout

```text
STYLE
Restrained electronic pop, 94 BPM proposal, female lead with intimate low register,
rounded analog bass, dry percussion, airy keys, gradual opening of the refrain,
warm close vocal mix and spacious but controlled outro.

LYRICS
[Verse 1]
(Insert the user's original authorized lyrics, or a newly requested original lyric.)

EXCLUDE / NEGATIVE GUIDANCE
No male lead, no shouted ad-libs, no orchestral climax.
```

Field names, character limits, "exclude" availability and generator behavior must be adapted to the current user interface; the example does not certify present Suno controls.

**Instrumental-only:** omit the lyric block entirely rather than inserting placeholder words that could be sung. Use instrumental/no vocal instructions where supported.

**Other generators:** translate the same musical direction into fields actually supported by the tool. Do not pretend a generic textual instruction is a documented API call, and do not claim an integration that is not connected.

## Platform and rights boundary
No Suno affiliation or endorsement is implied. Commercial rights and third-party audio-use permissions are provider- and context-dependent; check current terms before asserting them.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
