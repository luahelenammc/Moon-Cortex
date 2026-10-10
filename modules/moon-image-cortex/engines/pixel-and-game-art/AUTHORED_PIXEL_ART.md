<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Authored Pixel Art

**System:** Moon Image Cortex · **Type:** conditional visual specialist · **Status:** active
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)
**Related methods:** [Omnialchemy](../../components/creative-direction/OMNIALCHEMY.md) · [Web Aesthetics](../../components/creative-direction/WEB_AESTHETICS.md) · [Reference Abstraction Guardrail](../../components/references-and-identity/REFERENCE_ABSTRACTION_GUARDRAIL.md)
**Different route:** [Pixel-World Camera Translation](../experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md) translates authorized game-like scenes **out of** pixel art into physical-space imagery.
**Renderer:** separate and optional; this method does not generate image pixels by itself.

## Component activation

Activate for an output whose **native discrete pixel structure** is part of the deliverable: characters, portraits, item icons, tilesets, environment scenes, mock game screenshots, pixel UI assets, key poses, animation-ready sprite sheets, or pixel-native editorial stills.

Use this route when individual pixel placement, clusters, palette economy and readability at the native grid matter. For a photo with a retro filter, a fuzzy downscaled illustration, a CRT photograph, or a physically reconstructed pixel-world environment, select a more appropriate route instead.

**First-use inputs:** intended artifact class; target use/platform; requested content and references; constraints on native pixels, palette or tile scale if supplied; whether the result must be editable, tileable, animated or immediately recognizable at 1×. Ask only for critical missing constraints. Do not invent a hardware limitation or claim a particular console's original limitations without a source.

## Visual DNA: deliberate discrete construction

Pixel art is **authored on a grid**, not defined by a blocky final appearance. Start with composition and semantic clarity, select a coherent native canvas and scale, design dominant silhouettes and clusters, then allocate colors and detail to those forms.

Five interlocking laws govern the method:

1. **Cluster economy.** Neighboring pixels form meaningful shapes for volume, boundary, texture, light or semantic cue. Random singleton noise is not substitute detail.
2. **Silhouette priority.** The major object or action must remain identifiable without its internal material rendering.
3. **Palette relationships.** Colors serve ramps, material distinction, light direction, depth and narrative priority; a low color count alone does not create coherence.
4. **Material shorthand.** Discrete contrasts and cluster shapes imply glass, metal, cloth, water, soil, foliage and skin without imitating continuous photo shading.
5. **Readability at the real native scale.** Check 1× and the intended final display size. Attractive zoomed pixels can fail as a working sprite or icon.

### Native pixels are not display pixels

Keep three things separate:

| Parameter | Meaning | Example, not a universal default |
|---|---|---|
| Native canvas | Actual authored pixel grid | 16×16 icon, 32×48 sprite, 160×144 scene |
| Presentation scale | How each authored pixel appears on the destination screen | 4× or 6× integer scaling |
| Density policy | Allowable cluster detail relative to intended reading distance | Sparse silhouette-first icon versus dense authored environment |
| Grid discipline | How outlines, pixels and subshapes align across assets | Consistent 1-pixel contour behavior at native scale |
| Delivery format | Transparency, tile sheet, individual frames, mock screenshot or visual brief | Transparent PNG for an icon when a tool supports it |

Use crisp nearest-neighbor enlargement when integer presentation scaling is appropriate. Avoid accidentally introducing bilinear smoothing, anti-aliased contours or mixed subpixel geometry. If a specific destination requests noninteger responsive resizing, specify how the image will be displayed without claiming universal perfect crispness.

A nominal 640×360 export may contain a deliberately authored 160×90 grid magnified 4×; it is not automatically 640×360-native pixel art.

## Choose the artifact class first

| Class | Primary constraint | Distinct QA obligation |
|---|---|---|
| Character sprite | Proportion system, pose, expression and silhouette | Readable facing/action and stable dimensions across variants |
| Character portrait | Identity cues in a small grid | Expression without false likeness precision |
| Item icon | Function recognition at 1× | Silhouette and contrast before decorative sparkle |
| Tileset | Repeatable seams, neighbor transitions, consistent scale | Validate adjacency in several assembled arrangements |
| Scene / background | Depth grouping, walkable versus decorative space | Foreground hierarchy, spatial coherence and no texture spam |
| Pixel UI asset | States, alignment, accessible contrast, icon/function clarity | Active/disabled/hover states distinguishable at output size |
| Mock game screenshot | World, view, HUD and period/game grammar | No cloned game interface, inconsistent pixel density or accidental photo effects |
| Isometric pixel room | Projection consistency, topology and object occlusion | Pixel-based isometry remains intentional rather than accidentally photographic |
| Animation / sprite sheet | Key poses, registration, frames and loop policy | Stable silhouette, baseline and volume from frame to frame |
| Pixel promotional still | Grid-authored focal hierarchy and art direction | Image remains pixel-authored, not blurred or downsampled illustration |

**Routing distinction:** If the user asks to *preserve* the block/pixel construction, select **Authored Pixel Art**. If the user asks to turn an isometric sprite room into a human-scale photographed room, select **Pixel-World Camera Translation**. The latter is experimental; neither implies rights in third-party game assets.

## Seven design stages

### 1. Reconstruct the semantic nucleus

Clarify the essential action, feeling and information that the asset must communicate. For a game item, ask what it does. For a character, record the gesture and identifying cues. For an environment, identify the main circulation path and focal event. Avoid generic nostalgia assumptions like automatic fantasy villages or cyberpunk alleys.

### 2. Establish native grid and perspective

Choose the artifact class and, if not supplied, propose a *task-suitable* working grid and explain why. State camera grammar: side view, top-down, fixed perspective, isometric or a one-shot editorial composition. For a multiasset set, lock intended tile units and consistent proportions before drawing unique items.

### 3. Design silhouette and value hierarchy

Make the main shape readable in 1-bit silhouette or a very small number of value groups. Fix overlap and visual mass before texture. In a scene, outline primary foreground/subject/background groups. For tiny sprites, allocate pixels to action and distinctiveness rather than anatomically impossible detail.

### 4. Build a coherent palette

Define shared neutrals, light-to-dark ramps, hue shifts, and one or two focal accents where useful. Record light direction and material identity. Decide whether the scene uses strict hardware-inspired limits, flexible contemporary pixel-art color, or a user-specified exact palette. **Do not claim historical hardware authenticity solely from a color count.**

### 5. Allocate clusters and shorthand materials

Cluster shapes must reveal volume, direction and surface. Material examples:

| Material | Economical pixel treatment | Common failure |
|---|---|---|
| Metal | Abrupt value jump and small coherent specular cluster | Random white sparkle on every surface |
| Cloth | Larger soft ramps, folds with intentional direction | Pillow shading or glossy plastic |
| Stone | Weight, chipped silhouette, limited stratified marks | Uniform noise over every tile |
| Foliage | Readable masses and controlled silhouette variation | Isolated leaf-pixel confetti |
| Glass | Sparse edge contrast and reflected environment shapes | Full-frame opaque cyan fill |
| Skin | Deliberate warm/cool relationships, simple planes | Smeared photographic gradients |
| Water | Cluster rhythm aligned with surface and light | Arbitrary repeating stripes |

Use dithering when a transitional surface, material or deliberate retro grammar calls for it. Do not fill all surfaces with checkerboard dithering to imply effort.

### 6. Resolve functional constraints

For a tileset, specify tile size, edge families, interior/outer corners, transitions, walkable paths and collision relevance when applicable. For animation, specify baseline, anchor points, sprite-box dimensions, directional facings, key poses, optional timing and what must remain stable. For UI, distinguish states and minimum readable labels. For a screenshot, explicitly separate world pixels from the HUD and any optional postprocessing, and keep the pixel density coherent.

### 7. Inspect and repair

Test at 1×, at destination display scale and, where relevant, inside neighboring tiles or sequential animation frames. Inspect silhouette confusion, contour stair-stepping, palette bloat, tile seams, uneven pixel sizes, over-dithering, accidental anti-aliasing, cloned assets and text legibility. Repair the failed dimension, not the entire scene by default.

## Style regimes, not franchise presets

| Regime | Useful decisions |
|---|---|
| Clean console-era logic | Strong silhouette, restrained color ramps, economical and consistent clusters |
| Painterly pixel art | Richer color ramps and material transitions while retaining unambiguous discrete structure |
| Decorative indie scene | More atmospheric color and environment depth, still subordinate to native-scale readability |
| Tactical / systems UI | Icon function, state distinction and repeated-unit alignment before mood |
| Isometric pixel world | Topology, occlusion, tile perspective and controlled sprite/environment scale |
| Narrative screenshot | Staged action and readable world/UI hierarchy within a fictional original game |
| Pixel illustration / poster | Grid-authored artistic hierarchy at a planned export size |

Choose one primary regime or a clearly documented combination. The engine never defaults to an identifiable game, developer, artist or protected character style.

## Identity and continuity at low resolution

When depicting a consenting real person or recurring original character, compress identity into a few stable, *authorized* markers: silhouette, head/body proportions, hairstyle shape, dominant wardrobe hues, posture and a limited accessory. At a tiny grid, exact facial identity is not a reliable deliverable.

For repeated variants or animations, lock the proportion system, palette family, contour treatment, facing, registration points and any subject-designated distinctive cues. The user may override these intentionally. Do not infer a person's nationality, health, age or sensitive identity from the sprite.

## Reference abstraction and originality

With a permitted reference, extract **transferable design variables**: palette relationships, cluster density, texture grammar, contour logic, object scale, animation economy, tile topology, or UI density. Do not reuse protected sprite poses, exact tile arrangements, characters, logos, map layouts, distinctive character silhouettes or proprietary HUD composition.

Use [Reference Abstraction Guardrail](../../components/references-and-identity/REFERENCE_ABSTRACTION_GUARDRAIL.md) when external visual examples materially influence a result. If a generated asset resembles a reference's distinctive composition, change the scene geometry rather than merely renaming objects.

## Compiler and handoff contract

`artifact_class` · `semantic_nucleus` · `native_resolution` · `presentation_scale` · `pixel_density` · `camera_or_projection` · `palette_and_ramps` · `silhouette_priorities` · `cluster_logic` · `material_shorthand` · `tile_or_animation_constraints` · `reference_scope` · `identity_permissions` · `negative_guidance` · `QA_targets`.

A direction sheet should explain the design decisions without pretending they have been rendered. A renderer prompt must not promise access to pixel-exact drawing, frame generation, transparent assets, sprite packing, palette-index controls or programmatic tileset validation unless a real authorized tool supports the action.

### Synthetic examples

**Character sprite:** An original 32×48 pixel botanist, calm forward-facing pose, apron and satchel as identity cues, controlled green-and-brown ramps, animation-compatible foot placement, economical cluster shading. No borrowed role-playing-game character silhouette.

**Item icon:** An original 32×32 magnetic field notebook with a legible rectangular mass and clasp, restrained cool-gray highlights, a shared paper ramp, transparent background if tool-supported. It must still read at 1×.

**Mock screenshot:** An original top-down night-market scene on a planned native grid, dark-indigo environment blocks and warm lantern accents, clear walkable path and restrained independent HUD. No cloned game UI or photographed CRT effect unless requested.

**Tileset:** A 16×16 grass-to-stone tile family with center, edge, inner/outer corners and transition tiles. Assemble adjacency tests in multiple directions before adding tiny detail.

**Animation:** An original six-frame walking loop with a fixed character box, planted-foot contact, clear left/right weight transfer, controlled cluster updates and consistent registration. If animation cannot actually be exported, provide key-pose and frame constraints rather than a fake sprite-sheet deliverable.

## QA gate and repair table

| Failure | Observable symptom | Bounded correction |
|---|---|---|
| Downsampled illustration | Blurred contour and no coherent native clusters | Rebuild the major forms on an explicit native grid |
| Noise masquerading as detail | Random single-pixel speckles and unclear material | Simplify clusters, silhouette and palette |
| Palette bloat | Unmotivated near-duplicate colors | Consolidate ramps and preserve contrast anchors |
| Pillow shading | Uniform middle highlight unrelated to a light source | Resolve geometry and choose a consistent light direction |
| Over-dithering | Checkerboard pattern obscures volume | Confine dithering to materials that need it |
| Tile seams | Edge patterns visibly break when repeated | Repair adjacency and transition logic first |
| Pixel-size drift | Mixed source scales, fuzzy enlargement, anti-aliased shapes | Restore grid discipline and crisp display handling |
| Sprite continuity drift | Proportions/anchors/palette change between poses | Lock baseline, scale, cue set and frame registration |
| Imitation risk | Recognizable proprietary sprite or level layout | Author new silhouettes, topology and story geometry |

**Acceptance questions:** Is the native grid explicit? Is the asset recognizable at 1×? Do clusters serve form rather than noise? Are palette and material coherent? Does the object have the requested function? Does tiling or frame continuity work when applicable? Is it structurally original and permission-aware? Did an actual supported tool create the expected artifact?

## Component return and handoff

Return the smallest justified result: pixel-art direction brief, native-resolution and palette sheet, icon/sprite specification, tileset adjacency plan, frame constraints, renderer prompt or QA report on an actual asset.

**Without an available authorized renderer, output a direction only and state _not rendered_.** Visual Director alone governs task state, source roles, renderer permission, inspection and final acceptance.


<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
