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

## Photographic material system

The specialty is a **capture grammar**, not a stock subject or a filter. Configure a plausible relationship between observer, lens, light, physical materials and image medium *before* naming any nostalgic styling. A surreal subject does not become physically real just because grain is added; conversely, this engine must never introduce uncanny content by itself.

### Choose a photographic regime

| Regime | Composition and material logic |
|---|---|
| General analog | Natural camera distance, believable light falloff, subtle grain, gentle halation and moderate contrast |
| Vintage editorial | Staged but credible subject placement, restrained direction, period-coherent wardrobe/props only when evidenced |
| Cinematic still | Carefully blocked foreground/middle/background, motivated key light and depth rather than arbitrary haze |
| Consumer photograph | Modest dynamic range, human-eye or casual camera height, non-perfect centering and ordinary surfaces |
| Period print / scan | Device-appropriate print response, possible localized fade and scan artifacts only when the story includes a print or scan |

### Camera, lens and film parameters

Use camera terminology to predict *visible behavior*, not as ornamental namedropping. State observer height, focal-distance category (wide environmental, natural, compressed portrait), subject-to-camera distance, focus plane, depth-of-field intention, light source and scene reflectance. Film-grain size, halation, print fade and exposure softness should be consistent with the intended medium. A direct photographic capture must not automatically include paper folds or scanning dust.

**Color response:** prefer soft but not clipped highlights, blacks with plausible density, measured saturation and white balance appropriate to daylight, tungsten, overcast conditions or older fluorescent interiors. Allow warm light without imposing universal sepia. Limit artificial clarity and hyper-detailed surfaces.

### Compilation order

1. Reconstruct the subject and practical scene.
2. Define who or what operates the camera and why.
3. Choose photographic regime and period only from task context.
4. Resolve perspective and lens behavior.
5. Establish motivated illumination, exposure and film/sensor response.
6. Specify surfaces and scene details with correct depth hierarchy.
7. Layer in small medium-consistent imperfections.
8. Write negative guidance and inspect for CGI polish, implausible physics or generic vintage decoration.

### Output recipe

`subject + setting + camera position + lens behavior + lighting + capture medium + material response + restrained processing + exclusions`

**Example:** A quiet editorial portrait of a bicycle mechanic in a repair shop. Natural 50-mm-equivalent perspective, moderate subject separation, window-side diffuse light, true grease on tools and worn fabric, film-like soft highlight rolloff and very fine grain. Do not replace the shop with a cinematic fantasy set or give the subject glossy synthetic skin.

**QA:** Does the image read as a plausible camera capture? Is the focal plane coherent? Is every proposed “aged” feature justified? Are skin, fabrics and scenery organic rather than tiled? Are identity and any referenced historical period intact?

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
