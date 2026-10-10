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
| **Native pixel and game art** | [Authored Pixel Art](../engines/pixel-and-game-art/AUTHORED_PIXEL_ART.md) | choose a true pixel grid, silhouette and clusters, palette, tile or animation behavior and native-size inspection |
| Mood-led illustration | Sentimental Uncanny; Sublime Lyric Still; Vintage Editorial Rubber Hose Poster | control tenderness, atmosphere, symbolic force, reading and editorial hierarchy |
| Experimental translation | Pixel-World Camera Translation | reinterpret an authorized pixel-world frame as an embodied **non-pixel** physical scene; this is not the authored-pixel route |
| Identity continuity | Human Canon Forge | create a consent-based local profile for a user-authorized subject |
| Visual inspection | Photo, tile, text, typography, chart and renderer QA | detect a specific failure and repair only the affected dimension |

## Vista-specific conditional route

[Windows Vista Ultimate Black](../engines/interfaces-and-retro/web-retro/WINDOWS_VISTA_ULTIMATE_BLACK.md) is selectively loaded *within* Web Retro Image Gen. Distinguish the predominantly black Vista Ultimate retail packaging from the Aero Glass window system, whose color and transparency could be personalized. A dark Aero Vista screen is a historical configuration choice, not an edition-exclusive operating-system skin. The lens governs historical period facts, palette/material logic, screenshots versus monitor/box photography and rights-aware original UI composition.

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

## Experimental status

[Pixel-World Camera Translation](../engines/experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md) is an experimental visual direction method. Its current written examples do not establish performance across games or image-generation tools.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
