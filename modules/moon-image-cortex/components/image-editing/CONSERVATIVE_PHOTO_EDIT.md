<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Conservative Photo Edit

**System:** Moon Image Cortex · **Type:** conditional cross-cutting component
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)

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

## Preservation-first editing handbook

### Specify exactly what may change

The unit of work is a **bounded visual delta**, not a reinterpretation of the photograph. Record the original file and an explicit edit boundary. Separate (a) target area, (b) protected subjects/objects, (c) permitted illumination or edge harmonization around the change and (d) forbidden changes. For people, protect recognizable facial geometry, skin tone and natural texture, expression, hairline, body proportions and unrequested identifying details.

| Edit class | Acceptable scope | Typical failure |
|---|---|---|
| Remove an object | Fill the local gap using consistent adjacent geometry, perspective and light | Rebuilding furniture, limbs or the wider scene |
| Replace a background | Preserve subject silhouette, strands, fabric edges and plausible depth | Halo edges, reshaped face, copied background light |
| Restore damage | Address actual scratches, tears, dust or limited tonal decay | Invention of historically unknowable details |
| Improve readability | Conservative exposure, local contrast or bounded sharpening | Fake pores, haloed edges and global artificial crispness |
| Resize or reframe | Respect requested aspect ratio and protected anatomy | Stretching, crop-driven identity change or invented content |

### Capture fingerprint and materiality

Treat the original camera/scan as a coherent system: lens perspective, depth of field, sensor noise or film grain, image compression, exposure, color response and motion behavior belong together. Do not add a “photorealistic” finish that erases the actual source. Skin should retain subtle unevenness; hair should retain fine distinct strands; fabrics must not lose weave; foliage must not turn into repeated fragments. Repeated texture is a defect, not proof of detail.

**Soft-but-sharp artifact triage:** if edges seem superficially crisp but surfaces have waxy or flattened microtexture, distinguish optical softness, compression damage, intentional denoising, beauty filtering and generated reconstruction. The appearance itself does **not** establish an invisible watermark, provenance mechanism or model-specific cause.

### Two-pass workflow

**Pass 1: intervention.** Choose the smallest real edit operation supported by the authorized tool. For a masked edit, define a conservative mask and allow only the seam pixels needed to integrate shadows, reflection and color. Maintain an original image for readback.

**Pass 2: invariant comparison.** Compare original and edited image at the same crop and magnification. Inspect protected face and body features, object contours, surfaces, lighting direction, printed text, composition and local artifacts. A convincing new background does not count as success if the face has changed.

| Severity | Response |
|---|---|
| Minor edge seam or small texture anomaly | Correct that localized region; do not reprocess the whole image |
| Moderate waxiness, oversharpening or repeated surface detail | Return to original; reduce strength and isolate repair area |
| Severe identity drift or wholesale reconstruction | Reject result and start from the original with a narrower edit contract |
| No original to compare | Describe fidelity uncertainty; do not assert full preservation |

### Production prompt skeleton

> Edit the supplied image only in **{permitted_region}** to accomplish **{precise_change}**. Keep **{protected_people_and_objects}** unaltered, including facial anatomy, body proportions, natural pores, fine hair strands, fabric texture, existing lens characteristics and original framing. Match the source's light direction, perspective, grain, focus and color response. Avoid cosmetic retouch, invented accessories, universal sharpening and texture repetition. Inspect the modified boundary and unchanged regions against the supplied original.

**QA receipt:** requested change, preserved regions checked, source present/absent, actual editor used/none, visible defects, accepted/rejected decision and the smallest next action.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
