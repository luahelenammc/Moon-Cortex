<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Moon Image Cortex

**Visual intelligence and image direction for AI-assisted creative work.**

Moon Image Cortex helps an AI understand what an image needs to accomplish, choose a fitting visual approach, prepare a direction or edit instruction, and evaluate a result against the brief. It supports everyday image creation, careful photo editing, photographic realism, style exploration, reference use, and more specialized visual languages.

**It is not an image generator or a collection of fixed filters.** The [Visual Director](VISUAL_DIRECTOR.md#first-use) coordinates the work; individual components contribute methods only when relevant. Actual image generation or editing needs a separate, available and authorized tool.

**[Start with the Visual Director](VISUAL_DIRECTOR.md#first-use)** · **[Browse the component index](docs/COMPONENT_INDEX.md)** · **[Download the complete ZIP](../../downloads/moon-image-cortex.zip)**

| At a glance | What this means |
|---|---|
| **Most useful for** | Developing an image idea, editing a photo, directing realistic or candid photography, exploring an aesthetic, or checking a visual result |
| **You provide** | A short brief, image to edit, allowed references, or a specific visual problem |
| **You receive** | A visual brief, direction sheet, optional image-tool prompt or edit instruction, and QA notes as needed |
| **Optional depth** | Specialist aesthetics, identity/reference methods, experimental translation and regional context research |
| **Public status** | 11 active visual engines, 1 experimental engine, 6 reusable components, and 8 optional regional research lenses plus custom geography |
| **Evidence** | Synthetic textual tests establish route and package checks, not image-rendering quality or external adoption |

- **Version:** 0.1.0-pre.5
- **Canonical entry:** [Visual Director](VISUAL_DIRECTOR.md#first-use)
- **Transport surface:** [Complete module package](../../downloads/moon-image-cortex.zip)
- **Documentation license:** CC BY 4.0

## Start here

Describe the visual problem in ordinary language. You do **not** need to recognize an engine name or browse every component first. Open [Visual Director · First use](VISUAL_DIRECTOR.md#first-use) or give the [complete ZIP](../../downloads/moon-image-cortex.zip) to an AI environment that can read the documents.

The Director selects only the method the task earns. A prompt or direction is **not a rendered image**; if no suitable tool is actually available, the output is marked **not rendered**.

## Most common starting points

These are the broadest entry routes for everyday visual work. **They are presented first for discoverability, not automatically activated or privileged over the user's actual request.**

| I want to… | Best starting point | Typical help |
|---|---|---|
| **Turn an idea into an image concept** | [Omnialchemy](components/creative-direction/OMNIALCHEMY.md) · shared creative direction | Translate a rough idea into medium, scene, composition, color and light without forcing a house style |
| **Edit or restore a photo without changing everything else** | [Conservative Photo Edit](components/image-editing/CONSERVATIVE_PHOTO_EDIT.md) · shared image editing | Define a minimal change and protect other regions, facial features, proportions and textures |
| **Plan a convincing photographic image** | [Analogic Photo](engines/photography/ANALOGIC_PHOTO.md) · photography engine | Direct plausible lens behavior, exposure, natural light, grain, focus and capture material |
| **Get a natural, everyday snapshot** | [Vernacular Snapshot Realism](engines/photography/VERNACULAR_SNAPSHOT_REALISM.md) · photography engine | Reproduce the logic of an informal real-world camera moment rather than a polished commercial shoot |
| **Create a family-album or period camera aesthetic** | [Contextual Nostalgic Camera](engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md) · photography engine | Build a period-sensitive personal snapshot without assuming a nationality, location or decade |
| **Explore aesthetic directions and variations** | [Web Aesthetics](components/creative-direction/WEB_AESTHETICS.md) · shared creative direction | Compare eras, visual media, density, composition and aesthetic parameters |

**Checking or repairing a real image:** [Visual QA and repair](docs/VISUAL_QA_AND_REPAIR.md) is a cross-cutting quality process, available for *any* of the routes above, not a niche engine.

## Reference and identity tools

Useful across many workflows, but **activated only when the request involves references, consented likeness, or user-selected persistent preferences**. These are methods, not visual styles.

| Component | When it helps |
|---|---|
| [Reference Abstraction Guardrail](components/references-and-identity/REFERENCE_ABSTRACTION_GUARDRAIL.md) | Extract permissible light, palette, material and other principles from a style reference without echoing its protected scene or distinctive layout |
| [Human Canon Forge](components/references-and-identity/HUMAN_CANON_FORGE.md) | Prepare consent-based, user-owned likeness constraints for a subject; no public identity profiles or exact likeness guarantees |
| [Configurable Visual Profile](components/references-and-identity/CONFIGURABLE_VISUAL_PROFILE.md) | Apply visual preferences the user explicitly chooses for their own projects, without treating them as permanent or universal defaults |

## Specialized visual families

These engines are useful when the user already has a more specific medium or visual language in mind. They are **not required** for ordinary image creation or editing.

| Creative family | Engine | Best for |
|---|---|---|
| Historical interfaces | [Web Retro Image Gen](engines/interfaces-and-retro/WEB_RETRO_IMAGE_GEN.md) | Original period web pages, early browser experiences and desktop artifacts |
| Tactile icon design | [Aqua-Skeuo Icon Forge](engines/interfaces-and-retro/AQUA_SKEUO_ICON_FORGE.md) | Original glossy, beveled, material-rich desktop or mobile icons |
| **Native pixel art and game assets** | [Authored Pixel Art](engines/pixel-and-game-art/AUTHORED_PIXEL_ART.md) | Purposeful pixel clusters, palette discipline, sprites, tilesets, original mock game screenshots and pixel-native interfaces |
| Color-led imagery | [Chromatic Dream Logic](engines/expressive-and-editorial/CHROMATIC_DREAM_LOGIC.md) | Coherent palette, material, light and focal logic without mandatory themes |
| Atmospheric stills | [Sublime Lyric Still](engines/expressive-and-editorial/SUBLIME_LYRIC_STILL.md) | Vertical atmospheric images, negative space, spatial scale and minimal original text |

Pixel art is a **native construction method**, not a retro filter. [Authored Pixel Art](engines/pixel-and-game-art/AUTHORED_PIXEL_ART.md) preserves discrete pixels; the [experimental Pixel-World Camera Translation](engines/experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md) does the opposite by reconstructing a pixel-world scene as a physical space.

### More specific artistic languages

These three creative routes have narrow stylistic intentions. They are intentionally separated from the broad entry points above.

| Engine | Specific creative intention |
|---|---|
| [Lived-In Retrofuturism](engines/interfaces-and-retro/LIVED_IN_RETROFUTURISM.md) | Historical visions of future living, infrastructure and public life |
| [Sentimental Uncanny](engines/expressive-and-editorial/SENTIMENTAL_UNCANNY.md) | An ordinary tender scene containing one subtle unsettling detail |
| [Vintage Editorial Rubber Hose Poster](engines/expressive-and-editorial/VINTAGE_EDITORIAL_RUBBER_HOSE_POSTER.md) | Original simplified editorial characters, visual arguments and advocacy-poster hierarchy |

## Experimental routes

| Route | What is and isn't established |
|---|---|
| [Pixel-World Camera Translation](engines/experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md) | Experimental reinterpretation of an authorized pixel-world scene as a newly composed physical environment. Transfer breadth and renderer performance are **unverified**; no game affiliation or asset rights are implied. |

## Optional geographic camera contexts

For [Contextual Nostalgic Camera](engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md), a place can be supplied by the user or established by the source scene. **No country, ethnicity, or region is inferred by default.** These are context and research overlays, not independent engines or one-click national styles.

| Example lenses | Open choice |
|---|---|
| [Brazil](engines/photography/regions/BRAZIL.md) · [United States](engines/photography/regions/UNITED_STATES.md) · [United Kingdom](engines/photography/regions/UNITED_KINGDOM.md) · [Japan](engines/photography/regions/JAPAN.md) | [Any country, region or mixed context](engines/photography/regions/CUSTOM_CONTEXT.md) |
| [India](engines/photography/regions/INDIA.md) · [Mexico](engines/photography/regions/MEXICO.md) · [France](engines/photography/regions/FRANCE.md) · [Germany](engines/photography/regions/GERMANY.md) | [Geographic research registry](engines/photography/regions/README.md) |

An archive or geographic lens can guide research, but cannot establish a universal national photographic look.

## How the system fits together

The [Visual Director](VISUAL_DIRECTOR.md#first-use) remains the **only general operational entry**. A component's position on this page reflects likely visitor interest, **not authority or compulsory execution order**.

| Layer | Responsibility | Where to look |
|---|---|---|
| Director | Reconstruct brief, select routes, record provenance and permissions, coordinate handoff | [Visual Director](VISUAL_DIRECTOR.md#first-use) |
| Broad cross-cutting methods | Concept synthesis, conservative editing, aesthetic exploration and optional reference/identity controls | [Component index](docs/COMPONENT_INDEX.md) |
| Specialist engines | Supply photographic, interface, editorial or experimental visual grammar when requested | [Specialist registry](docs/SPECIALIST_ENGINES.md) |
| Quality assurance | Inspect actual results for visual, text, chart or image-edit defects | [QA and repair](docs/VISUAL_QA_AND_REPAIR.md) |
| External renderer (optional) | Actually generate or modify image pixels when a permitted tool exists | [Tool and renderer contract](docs/TOOL_AND_RENDERER_CONTRACT.md) |

**Flow:** visual need → brief → relevant component(s) → direction or edit instruction → authorized rendering when possible → QA → bounded repair.

The ZIP carries the whole system for transport. **The AI should load only the parts needed for the current task**, not all 18 core components or the geographic lenses by default.

## Reference and learning paths

| To explore… | Open |
|---|---|
| Every route, ordered for use | [Component index](docs/COMPONENT_INDEX.md) |
| Visual capabilities and route selection | [Domain and capability map](docs/DOMAIN_AND_CAPABILITY_MAP.md) |
| Turning an idea into a direction | [Visual state and compilation](docs/VISUAL_STATE_AND_COMPILATION.md) |
| Detailed specialist contracts | [Specialist registry](docs/SPECIALIST_ENGINES.md) |
| Image, typography, texture and chart errors | [Visual QA and repair](docs/VISUAL_QA_AND_REPAIR.md) |
| Likeness and informed consent | [Identity and consent](docs/IDENTITY_CONSENT_AND_BOUNDARIES.md) |
| Reference originality and evidence limits | [Originality, attribution and claims](docs/ORIGINALITY_ATTRIBUTION_AND_CLAIMS.md) |
| What software can actually run | [Tool and renderer contract](docs/TOOL_AND_RENDERER_CONTRACT.md) |
| Relation to Moon Source and source boundaries | [Moon Source context bridge](docs/MOON_SOURCE_CONTEXT_BRIDGE.md) |
| Fictional demonstrations and acceptance checks | [Synthetic examples](examples/) · [22 textual test intents](docs/IMAGE_CORTEX_REALITY_TEST.md) |
| Public release history | [Module changelog](CHANGELOG.md) |

## Scope and honest limits

- **Not a renderer:** prompts and instructions do not generate pixels on their own. Image performance requires actual rendering and inspection.
- **Identity and consent:** source photographs and likeness profiles require permission and remain user-controlled; no identity database is provided.
- **Not permission to copy:** aesthetic sources do not automatically authorize reuse of logos, layouts, characters or copyrighted images.
- **Not a validated image benchmark:** synthetic texts test contracts and routing, not exact likeness, measured visual quality or external adoption.
- **Not a national preset library:** optional location lenses aid research; geography does not dictate a person's identity or imagery.

See the [public boundary](../../PUBLIC_BOUNDARY.md), [licensing](../../LICENSING.md), and [module design contract](../../docs/MODULE_DESIGN_CONTRACT.md).

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
