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

## Period reconstruction without a nationality filter

The parent route is a **temporal and capture-ecology engine**. Its optional geographic lenses can constrain real material culture, but country is never inferred from who appears in the image, and it remains empty unless requested or established by source evidence. “1990s” is likewise not a default decade: the user chooses the time range or supplies clues that genuinely establish one.

### Reconstruction matrix

| Dimension | User-provided or source-supported input | Visual consequence |
|---|---|---|
| Date | Year, decade or period range | Consumer camera format, processing, wardrobe and devices may vary |
| Setting | Domestic, school, workplace, travel or public event | Ordinary spatial relationships and prop families |
| Photographer / relationship | Relative, friend, event participant | Casual or formal distance, framing and social timing |
| Camera | Compact film, disposable, early digital or unknown | Flash behavior, focal characteristics, noise/grain and image ratio |
| Recording history | Direct file, print, album page, later scan | Only justified color aging, dust, physical wear or JPEG artifacts |
| Place | Unknown or user-selected locality | Locale-sensitive cues when evidenced; never a person's ethnicity |
| Retained details | Actual reference objects, number of subjects, pose or key objects | Protect source-specific details while varying the visual treatment |

### Capture regimes and distinct evidence

**Compact film photograph:** believable grain and lens softness, inconsistent direct flash and modest consumer-camera dynamic range. A later print might bear localized fading, but new photo output should not falsely show album wear.

**Disposable social camera:** plausible short-range flash, casual body placement, moments that look taken by a peer rather than an editorial director.

**Early 2000s digital:** modest JPEG compression, limited dynamic range, on-camera flash and sensor-era color response. It must not automatically look like a scanned 1990s print.

**Album rediscovery:** only when the user actually asks for a found or scanned album artifact: print borders, handling traces, modest paper discoloration and scan geometry become part of the output medium.

### Direction-writing protocol

Construct the scene at three distinct levels: **human event**, **capture device** and **subsequent medium history**. First identify the ordinary activity. Next make the photographer's viewpoint and visible imperfections causally plausible. Only then add optional archival aging. Determine locale independently from scene behavior using the [custom context](regions/CUSTOM_CONTEXT.md) or one chosen regional lens.

**Avoid:** one country's generic suburban motifs, stereotyped costumes, random old brands, indiscriminate sepia, exaggerated date stamps, implausible mixture of print scratches and smartphone capture, sanitized AI interiors and centered advertising poses.

### Verification questions

- Does the result look like an actual remembered snapshot rather than an advertisement for nostalgia?
- Could this camera and medium plausibly exist at the specified time?
- Are visual imperfections connected to a photographic process?
- Are scene-specific cultural details grounded, and have unknown locations remained unknown?
- Is the photographed subject treated as a person, rather than a generic “national type”?

**Example direction:** “A slightly awkward 1995 school celebration photographed by a relative with a consumer compact camera; available light mixed with a near-axis flash. Preserve the number of people and event details from the authorized reference. If the location is unspecified, do not invent national decorations.”

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
