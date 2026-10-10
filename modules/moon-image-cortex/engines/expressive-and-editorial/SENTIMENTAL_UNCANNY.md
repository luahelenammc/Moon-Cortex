<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Sentimental Uncanny

**System:** Moon Image Cortex · **Type:** conditional visual specialist · **Status:** active
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)
**Renderer:** external and optional; this file contains no image generator.

## Component activation

Load this contract **only** when the Visual Director selects Sentimental Uncanny for an actual visual task. If using this file in isolation, first state the task, source permissions, intended output, and tool availability; do not infer that a renderer or identity profile is installed. The Visual Director resolves conflicts and controls handoff. The specialist supplies its own material, composition and QA rules.

## Specialist method

**Trigger:** A tender, familiar or nostalgic everyday scene should contain a slight unease that remains emotionally restrained.

**Visual DNA:** Preserve an inviting ordinary base, then introduce one small perceptual mismatch: a reflection, empty space, timing, scale, or object position. Keep uncertainty unresolved rather than escalating to a threat.

**Composition and material:** Familiar domestic light and tactility carry most of the frame. Let one detail hold attention just long enough to feel off. Avoid stacking uncanny devices.

**Must preserve:** Tenderness, ordinary setting, smallness of disturbance, and the user’s intended emotional balance.

**Avoid:** Horror by default, gore, jump-scare lighting, monster reveal, exaggerated distortion, or treating a vulnerable person as a prop.

**Direction example:** “Late-Y2K bedroom in soft peach lamp light, a neatly made bed and a small stack of CDs; in the wardrobe mirror, the chair appears slightly farther back than it is, subtle enough to question, no figure, no threat, no horror grading.”

**Input → output:** Everyday place, intended warmth, allowed uncanny degree and any excluded fears → one restrained anomaly, prompt and emotional QA.

**QA gate:** Does the scene still feel tender? Is there only one anomaly? Does it create ambiguity without converting the image into horror?

**Synthetic case:** A cozy 2001 bedroom should feel faintly wrong. Use a misaligned reflection; do not add a ghost or make a frightening claim.

## Component return and handoff

Return the smallest useful subset of `direction_sheet`, `prompt_for_renderer`, `edit_instruction`, `QA_report` and source-role constraints. A prompt without an available authorized renderer must say **not rendered**. The Visual Director remains the only general operational entry. Examples above are synthetic instructions, not validated output samples.

## Tenderness-first uncanny grammar

The engine sits between familiar decorative beauty and a **single subtle disruption**. The effect depends on affection and recognition remaining intact. It should not turn a gentle request into horror, violent surprise or surreal clutter.

### Three structural layers

| Layer | Visual role | Example |
|---|---|---|
| **Recognizable domestic or everyday world** | A room, patio, shelf, beach, party, night road or remembered object is immediately plausible | A softly lit birthday living room |
| **Sentimental surface** | Color, small treasured objects, familiar ornament, warm light and gentle imperfections give emotional credibility | Ribbon, paper decorations, flowers, lamps or a handmade card |
| **Disquieting mismatch** | One element feels subtly out of place in time, scale, absence, reflection or spatial expectation | A hallway that extends farther than it should |

### Intensity control

**Low:** melancholy, unexpected stillness, one ambiguous empty chair or a slightly delayed reflection. **Medium:** a clearly odd spatial relationship or repeated object that the camera treats casually. **High:** user-requested uncanny, still grounded in recognizable material; if the request is explicit horror, route accordingly rather than pretending it is the same gentle mode.

### Operators

Colorful late-1990s or early-2000s decorative memory is one possible *selected* treatment, not a mandatory date. Interiors, windows, seaside light, flowers, animal figures, toys, mirrored surfaces and quiet doorways can carry emotional dissonance when they have a scene function. Avoid using all of them together, or turning the image into random symbolic mythology.

### Prompt architecture

`ordinary moment + familiar tactile detail + emotional temperature + single deviation + credible camera/medium + perceptual restraint + QA`.

**Synthetic direction:** “An old neighborhood community hall after a children's craft evening: colorful paper garlands, ordinary folding chairs, gentle fluorescent light. At the back, one door seems to lead to the same decorated room at a slightly different hour. Everything else remains physically commonplace.”

### Failure checks

- Would the picture still be emotionally recognizable if the unusual detail were removed?
- Is there **one** meaningful disturbance rather than a collection of supernatural props?
- Does the composition evoke a memory rather than generic fantasy?
- Is any nostalgia culturally/temporally supplied, not imposed?
- Has the result unintentionally become horror, kitsch, a branded childhood world or glossy AI illustration?

For a strictly natural photograph, hand off to Analogic Photo or Vernacular Snapshot Realism. For a quiet atmospheric landscape with sparse text, Sublime Lyric Still is the more specific route.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
