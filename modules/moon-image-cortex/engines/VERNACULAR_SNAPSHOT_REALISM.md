<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Vernacular Snapshot Realism

**System:** Moon Image Cortex · **Type:** conditional visual specialist · **Status:** active
**Parent authority:** [Visual Director](../VISUAL_DIRECTOR.md#first-use) · [Component index](../docs/COMPONENT_INDEX.md)
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

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
