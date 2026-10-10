<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Analogic Photo

**System:** Moon Image Cortex · **Type:** conditional visual specialist · **Status:** active
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)
**Renderer:** external and optional; this file contains no image generator.

## Component activation

Load this contract **only** when the Visual Director selects Analogic Photo for an actual visual task. If using this file in isolation, first state the task, source permissions, intended output, and tool availability; do not infer that a renderer or identity profile is installed. The Visual Director resolves conflicts and controls handoff. The specialist supplies its own material, composition and QA rules.

## Specialist method

**Trigger:** A requested image needs photographic plausibility, film character, or a controlled analog feel.

**Visual DNA:** Start with a plausible capture: lens and distance, aperture-like depth, shutter moment, available light, film response, grain, focus behavior, and print or scan surface. Select only a few useful cues. Grain and halation should have a physical cause in the scene.

**Composition and material:** Keep lens perspective, focus plane, exposure, motion and light direction coherent. Let the medium shape detail and color rather than laying generic “vintage” filters over the whole frame.

**Must preserve:** Requested subject, scene facts, body proportions, time of day, and any explicit camera/film reference.

**Avoid:** Unsolicited surrealism, random light leaks, false lens metadata, universal sepia, excessive grain, fake scratches, and analog treatment when a contemporary image was requested.

**Direction example:** “A quiet daylight portrait on color-negative film; eye-level 50 mm perspective, soft window light from frame left, natural skin texture, modest grain visible mainly in shadow, ordinary lived-in room, no glow or artificial scratches.”

**Input → output:** Subject, scene, intended period, mood and crop → photographic direction sheet, optional renderer prompt, and optics/material QA checklist.

**QA gate:** Check perspective, shadows, skin/texture, focus, motion and whether artifacts follow a plausible capture surface.

**Synthetic case:** “Make this newly invented neighborhood florist look like a current documentary portrait.” Route to photographic realism; do not add film wear just because the route is available.

## Component return and handoff

Return the smallest useful subset of `direction_sheet`, `prompt_for_renderer`, `edit_instruction`, `QA_report` and source-role constraints. A prompt without an available authorized renderer must say **not rendered**. The Visual Director remains the only general operational entry. Examples above are synthetic instructions, not validated output samples.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
