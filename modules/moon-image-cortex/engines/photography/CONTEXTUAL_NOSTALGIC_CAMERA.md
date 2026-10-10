<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Contextual Nostalgic Camera

**System:** Moon Image Cortex · **Type:** conditional photographic specialist · **Status:** active
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)
**Regional adapters:** [Geographic Context Registry](regions/README.md)
**Renderer:** external and optional; this file includes no image generator.

## Component activation

Use when a user asks for a period-sensitive personal or everyday camera image, family album, school picture, holiday snapshot or personal memory aesthetic. **No country, nationality, ethnicity, cultural setting or specific decade is selected by default.** Country and region are independent of the subject's nationality or ethnicity.

## Capture-context model

Record only supplied or evidenced fields: calendar period, place at country/region/city granularity if specified, setting (home/public/event), occasion, who took the photograph, consumer capture device/support, lighting, processing/printing history, and the medium being recreated. Keep unknown fields unknown. A place is a **scene context**, not a proxy for people's appearance or identity.

1. Reconstruct the memory or scene with the user-defined period; if absent, use a period-neutral approach rather than silently assuming the 1990s.
2. Select [Vernacular Snapshot Realism](VERNACULAR_SNAPSHOT_REALISM.md) for casual social capture ecology and [Analogic Photo](ANALOGIC_PHOTO.md) for optics/film physical plausibility when needed.
3. Select one country/region adapter **only when explicitly requested or directly established for the source scene**. User instructions override adapter suggestions.
4. If the user asks for a region not in the registry, apply [Custom Geographic Context](regions/CUSTOM_CONTEXT.md). No fixed list restricts the user's choice.
5. Choose era-relevant objects only from supplied images, sourced references or explicit user context. If evidence is absent, avoid culturally distinctive details and disclose uncertainty.
6. Produce an independent direction and scene/capture QA. Texture wear, flash falloff, print aging and aspect ratio require a plausible capture or storage cause.

## Must preserve and avoid

**Preserve:** the user's scene, dates, surroundings when known, human proportions, source image roles, user-specified cultural context, and ordinary imperfections justified by the capture process.

**Avoid:** automatic Brazilian or American backgrounds, flags, costumes, regional stereotypes, nostalgic sepia, fake Polaroid frames, invented localized brands, anachronistic technology, race/ethnicity assumptions, or claiming that one country's archive represents all communities or decades.

## Input → output

Task and reference roles + selected or unspecified place + period and capture context → a context-aware camera direction sheet, optional renderer prompt, provenance/unknowns, and a brief period/culture plausibility QA gate. Without a renderer, return **not rendered**.

## Synthetic case

“An informal 1994 family birthday photograph, no location provided.” Generate a modest everyday setting with an era-appropriate consumer-camera direction. **Do not select a country.** If the user later specifies Recife, activate [Brazil](regions/BRAZIL.md); if Glasgow, use [United Kingdom](regions/UNITED_KINGDOM.md) with Scotland-specific context determined by evidence rather than generic UK props.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
