<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Conservative Photo Edit

**System:** Moon Image Cortex · **Type:** conditional cross-cutting component
**Parent authority:** [Visual Director](../VISUAL_DIRECTOR.md#first-use) · [Component index](../docs/COMPONENT_INDEX.md)

This file is a subordinate component, **not** another general entry, personal memory, or renderer. Use it only when the task earns it. Public documentation does not install tools or persist identity data.

## Trigger and first use

Use for retouch, restoration, background removal/replacement, resizing, repair and localized edits where preservation outranks reinterpretation. Require the **actual target image** for a concrete visual edit; absent an image, provide instructions only.

## Region and invariance contract

Identify the exact target, permitted modifications, protected areas, original proportions, identity and material/texture constraints. Prefer the smallest changed region. Preserve freckles, natural pores, hair and fabric texture, realistic lens/shadows and original non-target details. Never use unrequested beauty filters, body remodeling, invented accessories or sharpen-everything noise.

## Edit pipeline

1. Record target image identity and requested differences.
2. Mark allowed region(s), protected region(s) and whether changes could spill across seams or lighting.
3. Choose a real authorized image editor or native image-generation editing tool, if available.
4. Implement only the requested delta; preserve the original for comparison.
5. Inspect edited versus source in corresponding crops for unintended alterations. If a problem remains, repair the smallest region and disclose it.
6. If source or tool is missing, output an `edit_instruction` with `not rendered`, never a claim of completed restoration.

## QA

Prioritize identity retention, local boundary consistency, background seams, natural texture, body proportions, text and rights; reject waxiness, tiled patterns, missing details and over-sharpened halos. Diagnoses of invisible watermark causation are **unverified**.

## Synthetic activation

“Remove only the plastic bag on the floor of this family photograph.” Preserve people, furniture, lighting, skin and original framing; do not convert it to an idealized studio photo.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
