<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Moon Music Engine

**AI-assisted songwriting, sonic direction, controlled variation and generator repair.**

Moon Music Engine turns a human musical intention, original lyric, reference or disappointing generation into a useful, tool-aware music production brief. It works with generative-music tools such as Suno through explicit adapters, but does not require a Suno account to prepare a creative direction.

It is **not** a music synthesis model, automatic Suno connection, artist imitation service, or replacement for the author's choices. Audio generation requires a separately available, authorized tool.

**[Start with Music Director](MUSIC_DIRECTOR.md#first-use)** · **[Modes](#capabilities)** · **[Complete module ZIP](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/moon-music-engine.zip)** · **[Agent Skill ZIP](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/skills/moon-music-engine.zip)**

- **Version:** 0.1.0-pre.1
- **Status:** public pre-release / documentary method
- **Canonical entry:** [Music Director](MUSIC_DIRECTOR.md#first-use)
- **Transport surface:** [Complete module ZIP](../../downloads/moon-music-engine.zip)
- **Documentation license:** CC BY 4.0

## First steps

**Plan A:** give an AI with repository retrieval the [canonical Music Director link](https://github.com/luahelenammc/Moon-Cortex/blob/main/modules/moon-music-engine/MUSIC_DIRECTOR.md#first-use); ask it to retrieve only supporting mode or adapter files needed. **Plan B:** if GitHub cannot be read, provide the complete module ZIP and begin with `MUSIC_DIRECTOR.md`. A URL alone is not evidence that the AI read the file.

Tell the AI what you want to make or improve, any existing original lyrics, the desired sound or creative constraints, and the output format you need. Sparse input is allowed; the Director should propose a useful first version rather than interrogating you with a production questionnaire.

## Capabilities

| Real need | Selective method |
|---|---|
| Translate mood or references into specific sound | [Style Architect](modes/STYLE_ARCHITECT.md) |
| Preserve and improve a human-written lyric | [Lyric Doctor](modes/LYRIC_DOCTOR.md) |
| Develop a song from an idea | [Song Prototyper](modes/SONG_PROTOTYPER.md) |
| Diagnose a generated result and correct instructions | [Generator Debugger](modes/GENERATOR_DEBUGGER.md) |
| Explore unusual but bounded sonic alternatives | [Controlled Variation](docs/CONTROLLED_VARIATION.md) |
| Check composition and prompt quality | [Musical QA](docs/MUSICAL_QA.md) |

The [Lyric Sovereignty](docs/LYRIC_SOVEREIGNTY.md) contract protects user-written material and explicit narrative boundaries. [Tool adapters](docs/TOOL_ADAPTERS.md) keep provider-specific syntax separate from composition.

## Output you can expect

By default: a compact direction, a practical generator style prompt, structured lyric when appropriate, negative guidance, and a clear note about what has *not* been generated or heard. Suggest a main title and alternatives when a **new song** is being created. Provide variations only when useful or requested.

The user retains ownership and control over their own project files, recordings, lyrics, feedback and iterations. No private musical taste profile is bundled or automatically inferred.

## Evidence and boundaries

This is a documented, reusable method, not a measured evaluation of musical output. Synthetic examples illustrate routing and boundaries; they do not establish listening quality, adoption or generator reproducibility. Actual music output, platform rules, commercial rights and availability are external to this package. See [Synthetic Cases](examples/SYNTHETIC_CASES.md) and [Changelog](CHANGELOG.md).

Created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by Áurion.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
