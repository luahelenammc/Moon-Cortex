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

## What can I use it for?

You don't need to know an engine's name first. Start with the job you actually want to accomplish.

| I want to… | How Moon Image Cortex can help |
|---|---|
| **Turn a rough concept into a picture** | [Omnialchemy](components/OMNIALCHEMY.md) develops a visual thesis, scene, palette, material, light, and composition without forcing a default aesthetic. |
| **Plan a convincing photograph** | [Analogic Photo](engines/ANALOGIC_PHOTO.md) works with plausible light, optics, focus, and surface texture; [Vernacular Snapshot Realism](engines/VERNACULAR_SNAPSHOT_REALISM.md) helps when the image should feel candid rather than staged. |
| **Create a period-specific, location-aware family photograph** | [Contextual Nostalgic Camera](engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md) is **country-neutral by default**. Opt into [regional context lenses](engines/photography/regions/README.md), or define any other place; geography never determines ethnicity or appearance. |
| **Edit or restore an existing image carefully** | [Conservative Photo Edit](components/CONSERVATIVE_PHOTO_EDIT.md) specifies the requested change while protecting unrelated areas, identity, proportions, and texture. |
| **Keep a consenting subject recognizable across images** | [Human Canon Forge](components/HUMAN_CANON_FORGE.md) structures a private, user-owned likeness profile and preservation constraints. |
| **Explore styles or work from visual references** | [Web Aesthetics](components/WEB_AESTHETICS.md) organizes aesthetic parameters; [Reference Abstraction Guardrail](components/REFERENCE_ABSTRACTION_GUARDRAIL.md) extracts permitted visual principles without copying a source scene. |
| **Design a fictional retro website or tactile icon** | [Web Retro Image Gen](engines/WEB_RETRO_IMAGE_GEN.md) reconstructs period-appropriate web imagery; [Aqua-Skeuo Icon Forge](engines/AQUA_SKEUO_ICON_FORGE.md) guides original, material-rich desktop or mobile icons. |
| **Imagine the future through the past** | [Lived-In Retrofuturism](engines/RETROFUTURO_HABITAVEL.md) builds historically situated, human-scale retrofuture scenes and editorial images. |
| **Find an expressive visual mood** | [Chromatic Dream Logic](engines/CHROMATIC_DREAM_LOGIC.md) explores color and material; [Sentimental Uncanny](engines/SENTIMENTAL_UNCANNY.md) adds restrained unease; [Sublime Lyric Still](engines/SUBLIME_LYRIC_STILL.md) develops atmospheric vertical stills. |
| **Make an editorial or advocacy poster** | [Vintage Editorial Rubber Hose Poster](engines/VINTAGE_EDITORIAL_RUBBER_HOSE_POSTER.md) builds an original visual metaphor and readable poster hierarchy. |
| **Translate a pixel-art environment into a new physical scene** | [Pixel-World Camera Translation](engines/PIXEL_WORLD_CAMERA_TRANSLATION.md) offers an **experimental** route for authorized scenes, not sprite replication. |
| **Check or repair a visual result** | [Visual QA and repair](docs/VISUAL_QA_AND_REPAIR.md) checks texture, tiled artifacts, composition, legibility, and factual graphics such as shared measurement scales. |
| **Use my own recurring visual preferences** | [Configurable Visual Profile](components/CONFIGURABLE_VISUAL_PROFILE.md) keeps optional, user-owned preferences separate from the public module and subordinate to the current request. |

## How the system is organized

**One director, selective components.** The [Visual Director](VISUAL_DIRECTOR.md#first-use) is the sole general operational entry. It understands the request, picks a route, assembles a direction, and checks results. Each specialist is an addressable child contract, **not** another assistant competing for control.

| Layer | Responsibility | Explore |
|---|---|---|
| **Visual Director** | Reconstruct the task; decide which components matter; manage source roles, permissions, output, and QA | [Canonical entry](VISUAL_DIRECTOR.md#first-use) |
| **Shared components** | Handle concept synthesis, aesthetic exploration, references, consent-based identity, conservative edits, and optional preferences | [Six components](docs/COMPONENT_INDEX.md#shared-components) |
| **Specialist engines** | Apply a distinct photographic, historical, illustrative, cinematic, or experimental visual grammar | [Engine catalog](#specialist-engines) |
| **Visual QA** | Inspect an actual returned artifact and identify bounded fixes; distinguish observation from untested claims | [QA and repair](docs/VISUAL_QA_AND_REPAIR.md) |
| **Renderer, when available** | A separate, authorized tool actually creates or edits image pixels; this package alone does not | [Tool and renderer contract](docs/TOOL_AND_RENDERER_CONTRACT.md) |

**Typical path:** request → visual brief → selected components → direction / edit instruction → optional rendering → image inspection → bounded repair or handoff.

Only the pieces relevant to a task need active attention. The complete ZIP is for portability, not an instruction to load all 17 core/specialist components or every regional lens every time.

## Specialist engines by category

Engines are separated by **what they make**, not by an arbitrary aesthetic taxonomy. Each engine has its own activation contract, examples and QA; each remains subordinate to the [Visual Director](VISUAL_DIRECTOR.md#first-use).

### Photography and personal memories

| Engine | Use |
|---|---|
| [Analogic Photo](engines/photography/ANALOGIC_PHOTO.md) | Physically plausible lens, film, grain, exposure and lighting choices. |
| [Vernacular Snapshot Realism](engines/photography/VERNACULAR_SNAPSHOT_REALISM.md) | Everyday, candid photographs with socially and materially plausible imperfections. |
| [Contextual Nostalgic Camera](engines/photography/CONTEXTUAL_NOSTALGIC_CAMERA.md) | Time- and context-sensitive consumer photos with **no nationality or decade imposed**. [Choose an optional regional lens](engines/photography/regions/README.md). |

### Interfaces, objects and historical futures

| Engine | Use |
|---|---|
| [Web Retro Image Gen](engines/interfaces-and-retro/WEB_RETRO_IMAGE_GEN.md) | Original web-era pages and desktop visual artifacts. |
| [Aqua-Skeuo Icon Forge](engines/interfaces-and-retro/AQUA_SKEUO_ICON_FORGE.md) | Original tactile, glossy, material-rich interface icons. |
| [Lived-In Retrofuturism](engines/interfaces-and-retro/LIVED_IN_RETROFUTURISM.md) | Historically situated imagined futures with believable human life and infrastructure. |

### Expressive, atmospheric and editorial images

| Engine | Use |
|---|---|
| [Chromatic Dream Logic](engines/expressive-and-editorial/CHROMATIC_DREAM_LOGIC.md) | Color-led composition, material and focal hierarchy without mandatory symbolism. |
| [Sentimental Uncanny](engines/expressive-and-editorial/SENTIMENTAL_UNCANNY.md) | Tender everyday imagery with one restrained perceptual mismatch. |
| [Sublime Lyric Still](engines/expressive-and-editorial/SUBLIME_LYRIC_STILL.md) | Atmospheric vertical images, scale and minimal original text. |
| [Vintage Editorial Rubber Hose Poster](engines/expressive-and-editorial/VINTAGE_EDITORIAL_RUBBER_HOSE_POSTER.md) | Original editorial illustration, clear visual metaphors and responsible advocacy posters. |

### Experimental image translation

| Engine | Scope |
|---|---|
| [Pixel-World Camera Translation](engines/experimental/PIXEL_WORLD_CAMERA_TRANSLATION.md) | Experimental: reinterprets authorized pixel-world scenes as independently composed physical environments; cross-game performance is unverified. |

## Optional geographic camera contexts

Location is **never inferred from a person's face, ancestry or language**. The nostalgic camera route works with location unspecified; these lenses merely help research a place and period *when requested*.

| Available examples | Open choice |
|---|---|
| [Brazil](engines/photography/regions/BRAZIL.md) · [United States](engines/photography/regions/UNITED_STATES.md) · [United Kingdom](engines/photography/regions/UNITED_KINGDOM.md) · [Japan](engines/photography/regions/JAPAN.md) | [Any country, region or mixed context](engines/photography/regions/CUSTOM_CONTEXT.md) |
| [India](engines/photography/regions/INDIA.md) · [Mexico](engines/photography/regions/MEXICO.md) · [France](engines/photography/regions/FRANCE.md) · [Germany](engines/photography/regions/GERMANY.md) | [Region registry and evidence limits](engines/photography/regions/README.md) |

These are **research scaffolds**, not cultural costume presets, national style models or photo assets.

## Reusable components by responsibility

These six cross-cutting components may combine with multiple engines. They are **not six more image styles**.

| Functional layer | Component | Purpose |
|---|---|---|
| **Creative direction** | [Omnialchemy](components/creative-direction/OMNIALCHEMY.md) | Converts abstract intent into a coherent visual thesis without a default house style. |
| **Creative direction** | [Web Aesthetics](components/creative-direction/WEB_AESTHETICS.md) | Explores era, medium, composition and aesthetic parameters. |
| **References and identity** | [Human Canon Forge](components/references-and-identity/HUMAN_CANON_FORGE.md) | Consent-based local likeness preservation, not a public profile database. |
| **References and identity** | [Reference Abstraction Guardrail](components/references-and-identity/REFERENCE_ABSTRACTION_GUARDRAIL.md) | Transfers permitted visual principles while preventing reference echoes. |
| **References and identity** | [Configurable Visual Profile](components/references-and-identity/CONFIGURABLE_VISUAL_PROFILE.md) | Applies optional, user-owned visual preferences. |
| **Image editing** | [Conservative Photo Edit](components/image-editing/CONSERVATIVE_PHOTO_EDIT.md) | Changes only an authorized region while protecting unrelated image detail. |

## Getting started

Open the **[Visual Director: First use](VISUAL_DIRECTOR.md#first-use)** or provide the **[complete ZIP](../../downloads/moon-image-cortex.zip)** to an AI environment that can read the documents. Describe what you want in ordinary language: a new image, an edit, a look, or a defect to inspect. The Director chooses a suitable route; you do **not** need to select or install individual engines first.

The result can be a direction sheet, an edit instruction, a usable prompt, or a QA report. **An image is generated only if a real renderer is available and authorized.** Otherwise the outcome is explicitly marked **not rendered**.

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
