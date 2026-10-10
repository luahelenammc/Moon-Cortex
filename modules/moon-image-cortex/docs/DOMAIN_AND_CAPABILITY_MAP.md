<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Domain and capability map

Moon Image Cortex is a visual-intelligence layer. It turns an image request into a suitable visual direction, a renderer prompt or edit instruction when useful, and a truthful inspection report when an output exists.

For individually loadable specialist and cross-cutting contracts, see the [component index](COMPONENT_INDEX.md). Load only the file needed for the current task.

## Shared kernel

The kernel owns capabilities that recur across routes:

- **Task router:** separates new image creation, image editing, aesthetic exploration, identity continuity, and visual QA.
- **Reference reconstruction:** identifies each reference’s permitted role and extracts transferable visual invariants without replaying the source.
- **Visual-state compiler:** keeps intent, evidence, constraints, provenance, permission, and unknowns visible.
- **Omnialchemy:** converts an under-specified concept into one concrete visual thesis, medium, scene, composition, light and material. It is a compiler, not a fixed style.
- **Web Aesthetics:** identifies a period’s interface and image grammar while avoiding copied brand identity or exact layouts.
- **Anti-house-style gate:** compares with prior results only when those results are actually present, and routes toward a justified alternative.
- **Renderer gate:** distinguishes direction, prompt, actual generation, inspection, and evidence.
- **Conservative photo-edit gate:** protects unrequested identity, proportions, texture, and scene evidence.
- **Visual QA:** checks repeated tiles, image texture, text, infographic scales and markers, and actual-versus-claimed output.
- **Anti-Echo:** turns a reference toward new content by preserving only its requested aesthetic or structural principle.

## Capability groups

| Group | Routes | Responsibility |
|---|---|---|
| Concept compilation | Omnialchemy; Chromatic Dream Logic | translate an idea into visual grammar without imposing a theme |
| Photographic image | Analogic Photo; Contextual Nostalgic Camera; Vernacular Snapshot Realism | select capture ecology, optics, light and texture; add geographic details **only when selected or sourced** |
| Historical visual systems | Web Retro Image Gen; Aqua-Skeuo Icon Forge; Lived-In Retrofuturism | reconstruct web, icon or future-history grammar from a period |
| Mood-led illustration | Sentimental Uncanny; Sublime Lyric Still; Vintage Editorial Rubber Hose Poster | control tenderness, atmosphere, symbolic force, reading and editorial hierarchy |
| Experimental translation | Pixel-World Camera Translation | reinterpret an authorized pixel-world frame as an embodied scene |
| Identity continuity | Human Canon Forge | create a consent-based local profile for a user-authorized subject |
| Visual inspection | Photo, tile, text, typography, chart and renderer QA | detect a specific failure and repair only the affected dimension |

## Geography-neutral capture model

Country or region is **unknown by default** and independent of subject nationality. In photographic work, the [Contextual Nostalgic Camera](../engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md) may load a user-selected [geographic adapter](../engines/photography/regions/README.md), or an entirely custom one. The optional preset list does not constrain where a user can situate a scene. No source means no national props, no inferred ethnicity and no false local specificity.

## Route selection

Use one primary route. Add a second route only when a distinct constraint demands it: for example a family snapshot may need both Brazilian period context and vernacular capture ecology. Do not activate the whole package.

1. Classify the job and ask what success looks like at intended viewing size.
2. Respect the reference roles and rights boundary.
3. Select one route based on the task trigger, not on familiarity or recent use.
4. Record conflicts and unknowns instead of silently resolving them.
5. Produce a concise direction and tailor QA to likely failure modes.
6. If a renderer is available and authorized, inspect its output before claiming success.

## Route exclusions and status

All eleven specialist families are part of the public registry. Pixel-World Camera Translation is **experimental** because its source testing is narrow. Synthetic examples verify that its boundaries are stated; they do not establish transfer performance across games, renderers, or use cases.

The following source-dependent candidates are not public routes because the donor material supplied no general method body:

- **Original Game Concept Art Engine — excluded, source gap.** The game source offers one project-specific seven-frame bridge, not a reusable art-direction engine. Game mechanics and narrative remain governed by their own project.
- **Cartoon Identity / Fantasy Image Set — excluded, source gap.** The candidate is named in source references, but there is no stable general method to publish without invention.
- **Cat Canon Forge — excluded, source gap.** A predecessor is mentioned, but its full method is absent. Human Canon principles are not silently extended into an animal-identity recipe.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
