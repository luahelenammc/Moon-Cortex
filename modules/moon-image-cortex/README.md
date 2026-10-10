<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Moon Image Cortex

**Visual intelligence and image direction for AI-assisted creative work.**

Moon Image Cortex helps an AI figure out **what an image needs to accomplish**, choose the right visual approach, and check the outcome against the request. It supports creating images, editing existing pictures, translating aesthetic references, working with historical visual languages, and inspecting visual defects.

It is **not an image-generation model or a collection of one-click filters**. Think of it as the *creative direction and quality-control layer* around an image tool: one Visual Director, specialized engines for different kinds of imagery, and reusable components for tasks that cross styles.

**[Start with the Visual Director](VISUAL_DIRECTOR.md#first-use)** · **[Browse all components](docs/COMPONENT_INDEX.md)** · **[Download the complete ZIP](../../downloads/moon-image-cortex.zip)**

| At a glance | What this means |
|---|---|
| **Best for** | Creators, designers, editors, and AI users who need more deliberate visual decisions |
| **What you bring** | An idea, image to edit, reference, visual problem, or a combination |
| **What you get** | A visual brief, direction sheet, optional render-ready prompt or edit instruction, and QA notes where useful |
| **How it works** | A shared director activates only the relevant components, then uses a real image tool **if one is available and authorized** |
| **Included** | 10 active specialist engines, 1 experimental route, 6 cross-cutting components, and 8 optional geographic lenses plus a custom route |
| **Status** | Public pre-release; documented methods and synthetic text checks, **not** measured image-rendering performance |

- **Version:** 0.1.0-pre.3
- **Canonical entry:** [Visual Director](VISUAL_DIRECTOR.md#first-use)
- **Transport surface:** [Complete module package](../../downloads/moon-image-cortex.zip)
- **Documentation license:** CC BY 4.0

## Most common starting points

**Start with the job, not an engine name.** These are the broadest starting points for everyday image work. Their placement reflects **scope and likely usefulness**, not measured adoption or a requirement to activate all six.

| I want to… | Start with | What it helps with |
|---|---|---|
| **Turn an idea into a visual** | [Omnialchemy](components/creative-direction/OMNIALCHEMY.md) | Turns a rough concept into a coherent scene, composition, palette and direction without imposing a house style. |
| **Edit a photo without changing everything else** | [Conservative Photo Edit](components/image-editing/CONSERVATIVE_PHOTO_EDIT.md) | Describes localized changes while protecting people, textures, proportions and untouched regions. |
| **Make a convincing photograph** | [Analogic Photo](engines/photography/ANALOGIC_PHOTO.md) | Coordinates camera perspective, light, focus, film-like material and physically plausible detail. |
| **Make a natural candid snapshot** | [Vernacular Snapshot Realism](engines/photography/VERNACULAR_SNAPSHOT_REALISM.md) | Reconstructs an everyday capture rather than an overly polished studio image. |
| **Recreate the feel of an older family photo** | [Contextual Nostalgic Camera](engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md) | Works from a chosen period and scene, with **no country or decade assumed by default**. |
| **Explore a look, era or visual direction** | [Web Aesthetics](components/creative-direction/WEB_AESTHETICS.md) | Helps compare and combine visual parameters without selecting a fixed style. |
| **Check a result or identify an image defect** | [Visual QA and repair](docs/VISUAL_QA_AND_REPAIR.md) | Inspects actual returned images, legibility, texture, layout and factual graphic details. |

**[Start with the Visual Director](VISUAL_DIRECTOR.md#first-use)** if you are unsure which route fits. It makes the selection for the actual request.

## Getting started

Give the [complete module ZIP](../../downloads/moon-image-cortex.zip) to an AI environment that can read it, or open the [Visual Director's First use](VISUAL_DIRECTOR.md#first-use). Describe the image you want to create, change or inspect in ordinary language. The Director handles routing; **you do not need to load every engine**.

A real image is only produced when an authorized renderer is available. Otherwise the system provides usable direction or edit instructions, explicitly marked **not rendered**.

## How the parts fit together

The [Visual Director](VISUAL_DIRECTOR.md#first-use) is the **sole operational entry**. Other files are selective methods, not separate general-purpose agents.

| Part | Responsibility |
|---|---|
| **Visual Director** | Understand the task, select relevant methods, track reference roles and permissions, and govern the handoff. |
| **Broad starting points** | Handle creation, conservative editing, photography, everyday capture and aesthetic exploration. |
| **Reference and identity tools** | Help with authorized reference use, consent-based likeness preservation and personal preferences. |
| **Specialist engines** | Provide a specific visual grammar only when the creative request calls for it. |
| **QA and renderer gate** | Inspect actual artifacts, distinguish prompts from rendered results, and request a real tool only when available and authorized. |

**Typical path:** request → brief → selected methods → direction / edit instruction → optional render → inspect → bounded repair.

The complete package protects portability. Active attention stays proportional to the task, not the number of available components.

## Reference and identity tools

These three shared methods are broadly reusable **when relevant**, but are not necessary for a simple original image. They do not provide public identity records or assume permission to copy references.

| Component | When it matters |
|---|---|
| [Reference Abstraction Guardrail](components/references-and-identity/REFERENCE_ABSTRACTION_GUARDRAIL.md) | An existing image is a style or composition reference; carry over authorized principles without copying its recognizable scene. |
| [Human Canon Forge](components/references-and-identity/HUMAN_CANON_FORGE.md) | A consenting person's likeness needs continuity; keep the identity profile user-owned and local. |
| [Configurable Visual Profile](components/references-and-identity/CONFIGURABLE_VISUAL_PROFILE.md) | The user explicitly wants optional recurring visual preferences; current instructions always take precedence. |

## Specialized visual families

These are **distinct creative directions**, not mandatory processing steps. They are placed after the everyday routes so uncommon styles do not obscure the module's general usefulness. Each remains available immediately whenever the brief actually calls for it.

### Digital and historical interface imagery

| Engine | Best suited to |
|---|---|
| [Web Retro Image Gen](engines/interfaces-and-retro/WEB_RETRO_IMAGE_GEN.md) | Original web-era pages, early-browser screenshots and historic desktop visual grammar. |
| [Aqua-Skeuo Icon Forge](engines/interfaces-and-retro/AQUA_SKEUO_ICON_FORGE.md) | Tactile, glossy and skeuomorphic icons designed with original marks. |

### Expressive composition and atmosphere

| Engine | Best suited to |
|---|---|
| [Chromatic Dream Logic](engines/expressive-and-editorial/CHROMATIC_DREAM_LOGIC.md) | Color, light, tactile contrast and focal hierarchy with no prescribed subject matter. |
| [Sublime Lyric Still](engines/expressive-and-editorial/SUBLIME_LYRIC_STILL.md) | Vertical atmospheric images, visual scale, negative space and sparse original words. |

### Niche editorial and conceptual art

| Engine | Best suited to |
|---|---|
| [Lived-In Retrofuturism](engines/interfaces-and-retro/LIVED_IN_RETROFUTURISM.md) | A plausible future imagined from a historical period, grounded in human life. |
| [Sentimental Uncanny](engines/expressive-and-editorial/SENTIMENTAL_UNCANNY.md) | Tender, recognizable everyday scenes with one subtle perceptual anomaly. |
| [Vintage Editorial Rubber Hose Poster](engines/expressive-and-editorial/VINTAGE_EDITORIAL_RUBBER_HOSE_POSTER.md) | Original editorial characters, legible metaphors and responsible advocacy posters. |

## Experimental routes

| Engine | Evidence boundary |
|---|---|
| [Pixel-World Camera Translation](engines/experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md) | Reinterprets authorized pixel-world scenes as new physical environments. **Experimental**; transfer beyond the limited source context is unverified. |

## Optional geographic contexts

A regional lens is an **overlay to Contextual Nostalgic Camera**, not a standalone engine and not a nationality filter. Location is never inferred from appearance, ancestry or language. **No country is selected by default.** Use [custom context](engines/photography/regions/CUSTOM_CONTEXT.md) for any other place, period or mixed setting.

| Available research lenses | Explore |
|---|---|
| Brazil, United States, United Kingdom and Japan | [Regional registry](engines/photography/regions/README.md) |
| India, Mexico, France and Germany | [Regional registry](engines/photography/regions/README.md) |
| Any other or mixed location | [Custom geographic context](engines/photography/regions/CUSTOM_CONTEXT.md) |

Regional notes offer contextual research leads, **not** ready-made cultural stereotypes or guaranteed national photographic styles.

## Reference and learning paths

| For more detail | Where to look |
|---|---|
| All routes and their ownership | [Component index](docs/COMPONENT_INDEX.md) · [Capability map](docs/DOMAIN_AND_CAPABILITY_MAP.md) |
| How a visual brief becomes a direction | [Visual state and compilation](docs/VISUAL_STATE_AND_COMPILATION.md) |
| Selecting specialist methods | [Specialist engine registry](docs/SPECIALIST_ENGINES.md) |
| Repairing visual, text, texture, or chart errors | [Visual QA and repair](docs/VISUAL_QA_AND_REPAIR.md) |
| Likeness, source permissions, and privacy | [Identity and consent](docs/IDENTITY_CONSENT_AND_BOUNDARIES.md) |
| Source influence, originality, and proof | [Originality, attribution and claims](docs/ORIGINALITY_ATTRIBUTION_AND_CLAIMS.md) |
| Real tools versus documented instructions | [Tool and renderer contract](docs/TOOL_AND_RENDERER_CONTRACT.md) |
| Relation to the private source system | [Moon Source context bridge](docs/MOON_SOURCE_CONTEXT_BRIDGE.md) |
| Fictional walkthroughs and acceptance checks | [Synthetic examples](examples/) · [22 text-only test intents](docs/IMAGE_CORTEX_REALITY_TEST.md) |
| Release changes | [Module changelog](CHANGELOG.md) |

## Scope and honest limits

- **Not a renderer:** documentation and prompts do not produce an image on their own. Rendering, inspection, and measured fidelity are separate steps and claims.
- **Not a personal identity database:** no private photos, reference collections, identity profiles, or private donor documents are distributed. A subject's consent and the user's authority matter.
- **Not a license to copy:** aesthetic references do not grant rights to reuse third-party logos, source layouts, characters, or an artist's identifiable work.
- **Not a validated benchmark:** the 22 synthetic cases test text-level directions and boundaries, not image-generation quality, identity accuracy, or external adoption.
- **Not every local experiment is public:** some source-dependent concepts remain excluded; Pixel-World Camera Translation is expressly experimental.

See the repository-wide [public boundary](../../PUBLIC_BOUNDARY.md), [licensing](../../LICENSING.md), and [module design contract](../../docs/MODULE_DESIGN_CONTRACT.md).

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
