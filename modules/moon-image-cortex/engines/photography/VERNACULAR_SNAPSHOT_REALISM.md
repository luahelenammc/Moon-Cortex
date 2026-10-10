<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Vernacular Snapshot Realism

**System:** Moon Image Cortex · **Type:** conditional visual specialist · **Status:** active
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)
**Renderer:** external and optional; this file contains no image generator.

## Component activation

Load this contract **only** when the Visual Director selects Vernacular Snapshot Realism for an actual visual task. If using this file in isolation, first state the task, source permissions, intended output, and tool availability; do not infer that a renderer or identity profile is installed. The Visual Director resolves conflicts and controls handoff. The specialist supplies its own material, composition and QA rules.

## Specialist method

**Trigger:** The image should feel like an unplanned photograph made for everyday use rather than commercial or cinematic production.

**Visual DNA:** Reconstruct capture ecology: who took the picture, why, on which kind of device/support, in what era and region, and at what social distance. A smartphone, disposable camera, compact digital camera, and instant camera leave different traces.

**Composition and material:** Accept useful crop mistakes, casual perspective, imperfect timing and available light, but keep image legibility. Texture belongs to the camera, compression, print, or handling history.

**Must preserve:** The user’s chosen place/period and the scene’s lived-in character.

**Avoid:** Applying a “bad photo” filter to every route, nostalgic decay as default, culturally generic props, performative mess, or adding camera faults without a plausible source.

**Direction example:** “A friend’s 2004 disposable-camera snapshot at a suburban US backyard cookout; midday sun, slight flash mismatch in shade, loose framing, ordinary plastic tableware, consumer print color, no Brazilian-specific cues and no cinematic grading.”

**Input → output:** Who/why/where/when/camera and desired informality → capture ecology and specific photographic direction.

**QA gate:** Verify that each imperfection follows from capture, light, medium or social moment instead of being decorative noise.

**Synthetic case:** Compare two fictional scenes: a 1990s Brazilian album photo and a 2000s US disposable-camera picture. Change the capture ecology and local objects rather than just the color cast.

## Component return and handoff

Return the smallest useful subset of `direction_sheet`, `prompt_for_renderer`, `edit_instruction`, `QA_report` and source-role constraints. A prompt without an available authorized renderer must say **not rendered**. The Visual Director remains the only general operational entry. Examples above are synthetic instructions, not validated output samples.

## Capture ecology: the engine's decisive variable

A convincing vernacular photograph is not merely a camera with added imperfections. It implies **who photographed what, in which social situation, using what device and medium, for what ordinary reason**. Those decisions govern framing, posture, flash, clutter, distance and the later appearance of prints or files.

### Social and physical capture model

| Axis | Questions to answer |
|---|---|
| Photographer | Family member, friend, visitor, child or unknown; how practiced were they? |
| Occasion | Informal meal, birthday, backyard gathering, sleepover, school event, ordinary afternoon |
| Camera | Consumer compact film, disposable camera, early compact digital, phone camera or unspecified |
| Shot situation | Candid interruption, one-second posed group, imperfect self-portrait or accidental detail |
| Framing | Human-body geometry, inconvenient crop, horizon tilt, foreground obstruction, subject off-center |
| Light | On-camera flash, indoor tungsten, mixed lighting, open shade, window, night exterior |
| Image medium | Developed minilab print, album scan, consumer JPEG or direct digital file |
| Context | User-specified time/place/material culture; do not substitute generic regional symbolism |

### Realism is causal, not decorative

A cheap direct flash can create hard shadows, uneven close-range exposure and red-eye. A compact digital camera may show hard highlight clipping and simple JPEG artifacts; an old album scan can show print-edge wear and uneven color shifts. Do not combine all of these into one generic “found photograph.” Match defects to the **specific capture path**.

Prefer modest expressions, imperfect timing, ordinary domestic clutter and unremarkable artifacts to glamorous staging. A vernacular image can be happy and beautiful, but it should not look directed by an invisible fashion photographer.

### Camera-to-output variants

- **Film compact / minilab print:** modest grain, small exposure errors, small print fade only if an aged print is actually part of the scene history.
- **Early consumer digital:** limited sensor range, on-camera flash and compression; do not fake film grain as an obligatory layer.
- **Disposable social photograph:** close-range casual framing, inconsistent flash, mundane gestures and slightly awkward group placement.
- **Modern casual snapshot:** contemporary sensor and focal length where requested, but ordinary social timing remains the organizing principle.

### Full direction stack

1. **Style DNA:** amateur, found, socially credible, materially consistent, unposed unless a social occasion warrants posing.
2. **Camera/materiality:** device, focusing limits, flash, exposure, compression/film response and print/scan lineage.
3. **Scene grammar:** what people are doing, where they stand, what remains outside their attention and who is photographing them.
4. **Optional locale:** use the [geographic context registry](regions/README.md) only when the scene place is supplied or credible; it is not a national appearance filter.
5. **Negative guidance:** no studio posing, styled cinematic lighting, immaculate AI symmetry, invented iconic props, repeated texture, plastic faces or cinematic overprocessing.
6. **QA:** Does the moment look like something someone would actually photograph? Is the device plausible for the period? Do all defects have a material cause?

**Synthetic case:** an unplanned birthday kitchen photo at an unspecified location in 1998. Group positions and on-camera flash are plausible; no national cuisine, flag or home decoration is added without evidence.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
