---
name: moon-music-engine
description: Analyze real songs, artists and bands as creative references, distill transferable sonic features without copying, and compose, preserve or improve original lyrics and AI music directions. Use for sound/style prompts, song prototypes, Suno-friendly handoffs, controlled stylistic variation and debugging of music generations. Audio rendering requires a separately available authorized generator.
---

# Moon Music Engine

Read `references/MUSIC_DIRECTOR.md` first. It is the canonical route and first-use authority. Consult only the needed method files in `references/modes/` and `references/docs/`; the complete public module snapshot travels under `references/`. Current source: https://github.com/luahelenammc/Moon-Cortex/tree/main/modules/moon-music-engine. This skill is documentation and routing, not an audio generator, a Suno plugin or permission to access accounts.

## Procedure

1. Reconstruct the creative goal, supplied lyric/audio, authorship/rights boundaries, musical references, voice, language and non-negotiable constraints; do not require a long brief.
2. When the user supplies an existing song, artist, band, album or playlist as inspiration, **automatically select Reference-to-Feature Translator** (`references/modes/REFERENCE_TO_FEATURE_TRANSLATOR.md`) as the first primary motor. Name the sources in an analysis feature map, separate observed/sourced/user-reported/inferred traits and select an original sonic combination. Otherwise choose Style Architect, Lyric Doctor, Song Prototyper or Generator Debugger according to the task. Invoke controlled variation only when useful or requested.
3. Preserve user-supplied lyric by default and translate mood or references into concrete sound, pulse, instrumentation, vocal behavior and production choices. Never invent that you listened to a recording. Do not copy hooks, riffs, melodies, lyrics, recordings or distinctive close arrangements; removing names alone is insufficient.
4. Provide a concise copy-ready **original** style prompt (without named artist/song references by default), structured lyrics only if warranted, specific negative guidance and suitable titles for new songs. When named references are used, retain a separate reference/feature/provenance map for clarity.
5. Express variation percentages as exploratory controls, not mathematical probabilities or verified acoustic distances. Claim seeded reproducibility only with a real implemented seeded algorithm.
6. Mark what was prepared, generated, actually heard or merely reported. For real results, make targeted corrections rather than assuming output quality from the text prompt.

Created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion. Documentation: CC BY 4.0.
