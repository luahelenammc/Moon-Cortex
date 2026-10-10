<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Nostalgic Camera BR 90s

**System:** Moon Image Cortex · **Type:** conditional visual specialist · **Status:** active
**Parent authority:** [Visual Director](../VISUAL_DIRECTOR.md#first-use) · [Component index](../docs/COMPONENT_INDEX.md)
**Renderer:** external and optional; this file contains no image generator.

## Component activation

Load this contract **only** when the Visual Director selects Nostalgic Camera BR 90s for an actual visual task. If using this file in isolation, first state the task, source permissions, intended output, and tool availability; do not infer that a renderer or identity profile is installed. The Visual Director resolves conflicts and controls handoff. The specialist supplies its own material, composition and QA rules.

## Specialist method

**Trigger:** Brazilian 1990s family album, school, birthday, outing, or ordinary home photo.

**Visual DNA:** Select period-plausible consumer capture: compact point-and-shoot flash when scene distance and room explain it, direct snapshots, household print/album handling, imperfect framing, local light and color. Specific regional objects come from the user’s scene, not a stock “Brazil” checklist.

**Composition and material:** Allow a candid crop, casual horizon, close flash falloff, modest print aging only when the image’s history warrants it, and era-consistent domestic setting. Preserve the feeling of a photograph someone took to remember a moment.

**Must preserve:** Brazilian time and place supplied by the user, family event, relationships described, natural body proportions, and ordinary imperfections.

**Avoid:** Default American props and interiors, flags or tropical motifs as shorthand, modern phones, cinematic teal-orange grading, staged studio polish, invented identities, and exaggerated damage.

**Direction example:** “A fictional family birthday in a modest 1990s Brazilian apartment, compact point-and-shoot with direct flash, close candid crop, paper decorations and simple cake, warm household bulbs, plausible local details only, ordinary consumer print.”

**Input → output:** Time, Brazilian region if known, event, capture role and any allowed source image → contextual camera direction and period-plausibility checks.

**QA gate:** Ask whether the objects and capture ecology fit the stated place and period; remove items that rely on a US-default memory.

**Synthetic case:** A 1994 birthday in Recife with no decor details supplied. Use ordinary home celebration cues and disclose that exact local objects are unspecified.

## Component return and handoff

Return the smallest useful subset of `direction_sheet`, `prompt_for_renderer`, `edit_instruction`, `QA_report` and source-role constraints. A prompt without an available authorized renderer must say **not rendered**. The Visual Director remains the only general operational entry. Examples above are synthetic instructions, not validated output samples.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
