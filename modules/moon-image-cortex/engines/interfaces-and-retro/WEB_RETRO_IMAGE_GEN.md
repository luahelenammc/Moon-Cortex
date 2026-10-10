<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Web Retro Image Gen

**System:** Moon Image Cortex · **Type:** conditional visual specialist · **Status:** active
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)
**Renderer:** external and optional; this file contains no image generator.

## Component activation

Load this contract **only** when the Visual Director selects Web Retro Image Gen for an actual visual task. If using this file in isolation, first state the task, source permissions, intended output, and tool availability; do not infer that a renderer or identity profile is installed. The Visual Director resolves conflicts and controls handoff. The specialist supplies its own material, composition and QA rules.

## Specialist method

**Trigger:** A period web page, screenshot, desktop artifact, early social experience, or browser-era image is requested.

**Visual DNA:** Name the period and distinguish native browser screenshot, photograph of a CRT, and recreated interface. Reconstruct information density, typography, color, browser chrome, image compression and interaction cues appropriate to the era.

**Composition and material:** For a screenshot, keep the viewport flat and geometry aligned. For a photographed CRT, add screen curvature, scan pattern, glare, focus falloff and room reflections only where a camera could see them.

**Must preserve:** User-supplied wording and function; period logic; whether the result is a screenshot or photographed object.

**Avoid:** Current SaaS spacing, modern responsive cards in a 2000s page, copied brand colors/layouts, recognizable logos, current interface text disguised as historic, named-service recreation, or CRT artifacts on a native screenshot.

**Direction example:** “Fictional 2002 community-events portal in an early Windows XP browser: compact fixed-width two-column page, blue-gray beveled tabs, bitmap-style small icons, dense links and low-resolution banner; original name and mark, no copied site layout.”

**Input → output:** Period, interface purpose, screenshot-vs-CRT, content and fidelity goal → era sheet, original page prompt, and period/brand QA.

**QA gate:** Check the era cues, screen-medium distinction, legibility, and that layout and marks are newly authored.

**Synthetic case:** Build a fictional 2004 local music portal. Reject a contemporary SaaS dashboard and avoid recreating any named service.

## Component return and handoff

Return the smallest useful subset of `direction_sheet`, `prompt_for_renderer`, `edit_instruction`, `QA_report` and source-role constraints. A prompt without an available authorized renderer must say **not rendered**. The Visual Director remains the only general operational entry. Examples above are synthetic instructions, not validated output samples.

## Era-to-interface translation handbook

This engine creates a **new fictional interface** using historically coherent visual grammar. It does not reproduce a real archive screenshot, real website copy or protected logos. Separate **what the interface does** from **how a period web artifact communicates it**.

### Distinct era regimes

| Chosen visual era | Layout and interface grammar | Medium-specific cues |
|---|---|---|
| Mid-to-late 1990s / Windows 95–98 | Modest browser viewport, beveled gray controls, pixel icons, small system or serif text, link-heavy structure, tables, counters/guestbook when functionally justified | CRT viewing can add curvature, scanlines, mild moiré and screen glare; a clean screenshot should not |
| Early-to-mid 2000s / XP-era web | More rounded containers, gradients, image buttons, forum/community modules, sidebars, badges and portal density | LCD or CRT depends on actual medium; compression may be modest |
| Late 2000s–early 2010s / glossy web | Controlled rounded cards, Web 2.0 gloss, strong hero modules, gradients, skeuomorphic transitions | Do not accidentally turn it into a contemporary flat-design dashboard |
| User-specified niche setting | Era-consistent adaptations for forum, fan page, web game, wiki, personal site or service portal | Local language and culture only when grounded; never assume a US nostalgia template |

### Build a fictitious product as a period interface

1. Write the **function** in plain language: journal, local forum, virtual room directory, photo library, AI assistant or knowledge index.
2. Choose period and platform; decide whether the artifact is a **direct screenshot** or a **photograph of a real monitor**.
3. Define a readable page anatomy: navigation, headline, primary content, side content and one or two actions.
4. Select window chrome, icon style, system font, web graphics, borders, gradients and pixel density coherent with the period.
5. Specify the screen/surface only if photographed: monitor case, phosphor/CRT curvature, viewing angle, glare, camera focus, scanline/moiré behavior.
6. Keep copy short and functionally plausible. For published pages, typeset exact navigation and required copy after generating the visual base.
7. Check originality, layout plausibility, output legibility, title/copy correctness and actual era features.

### Prompt architecture

`original concept → chosen era → OS/browser language → page regions → palette/type/iconography → screenshot/photographed-screen policy → content priorities → negative guidance → QA`.

**Example:** An imaginary neighborhood movie club website in 2002. Left navigation, small guestbook action, framed poster thumbnails and compact forum panel, period-appropriate browser header and functional labels. No cloned GeoCities page, real franchise mark or random QR code.

**Failure diagnostics:** false historical mixing; 1998 interface containing modern phone mockups; synthetic pseudo-text as functional controls; illegible contrast; giant contemporary cards; borrowed website layouts; CRT scanlines added to a clean screenshot; screen hardware and browser UI conflated.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
