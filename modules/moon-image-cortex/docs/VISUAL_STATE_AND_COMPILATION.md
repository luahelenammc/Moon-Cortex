<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Visual state and compilation

The visual state is a temporary working model of this task, not a profile of the user. Keep it small enough to inspect and easy to revise.

## State record

| Field | Meaning |
|---|---|
| task_kind | new image, edit, aesthetic research, identity continuity, or QA |
| visual_brief | intended meaning, subject, audience, use, format, and success condition |
| source_roles | edit target, identity reference, composition reference, style reference, or factual source |
| observations | directly visible source properties; describe uncertainty and crop limits |
| user_description | what the user explicitly said about identity, taste, or intended meaning |
| geographic_context | optional scene place and historical period, selected or evidenced; **not** inferred from subject ethnicity/nationality |
| regional_adapter | optional explicitly chosen geography lens or custom context, with evidence and uncertainty |
| must_preserve | content, scene, proportions, identity, text, factual data, texture, or legal notices |
| allowed_change | exact transformation and areas in scope |
| avoid | excluded elements, motifs, moods, layouts, and unwanted effects |
| direction | chosen route, composition, palette, material, light, text, and rationale |
| provenance | user-supplied facts, observed details, external references, synthetic assumptions |
| permissions | image-edit permission, subject consent, brand use, publication status |
| unknowns | unresolved decisions, unavailable reference, ambiguous text, uncertain provenance |
| renderer_state | unavailable, prompt prepared, rendered, or inspected |
| qa_state | not checked, checked against direction, defects found, repaired, or unresolved |

Unknowns stay explicit. A guessed preference is not a stable personal fact; a visual impression is not a subject’s identity or protected attribute.

## Compilation steps

### 1. Recover intent

Ask for the desired communication and real viewing context. Convert adjectives into decisions: “quiet” may mean fewer focal points, lower contrast, negative space, softer light, or a different reading pace. Ask only the smallest question that would change the direction.

### 2. Reconstruct sources

For each input, state what is known, what is observed, and what may transfer. A reference image is not permission to reproduce. If a user asks to preserve a design, preserve only content they can authorize and the task requires.

### 3. Select a visual thesis

Write one sentence that joins subject, action and atmosphere. Use it to govern the frame. If two incompatible visual theses remain, show two directions instead of blending them by default.

### 4. Build the direction sheet

Describe, in order: dominant subject; frame and reading path; spatial relations; palette; material; light; focal detail; typography; required and excluded elements. Note which choices are fixed and which are exploratory.

### 5. Compile for the available medium

For image models, use concise positive instructions plus a short negative list. Put exact words, numerical data, UI, and repetitive geometry in a deterministic layout step when possible. For source-image edits, name protected areas and restrict the transformation.

### 6. Inspect and repair

Inspect the actual returned file at intended size. Compare it with the task’s highest-cost risks. Repair a local defect locally; if texture or tiling failure is global, simplify global detail. Do not rerender repeatedly without learning from the last result.

## Reference abstraction: Anti-Echo

Extract the minimum transferable properties for the requested role. From an aesthetic reference, this could be contrast, material, pacing, or spatial density. Do not carry over its subject, location, pose, exact crop, text, logo, character, or signature unless separately authorized and lawful.

For a corpus of references used for aesthetic extraction, move at least three of five axes away from the source when relevant: environment, composition, motif, scale, and light. This is a conservative originality heuristic, not a legal safe harbor. It is unnecessary when a user provides a target image specifically to edit.

## Change log for a single task

When a revision matters, record: version, change, reason, protected properties, and what remains unverified. Keep image content user-local unless the user explicitly asks to publish an authorized artifact.

## Visual-frame resolution across multiple specialists

The shared state is an **active frame**, not a giant prompt assembled from every engine. Reconstruct intent first, choose one primary route, then add supporting methods only for decisions they truly control.

### Priority resolution table

| When two modules disagree | Governing decision |
|---|---|
| Concept compiler suggests theatrical symbolism; task requests straightforward journalism | Required documentary credibility and user brief win |
| Style exploration proposes a strong period palette; supplied photograph has exact colors to preserve | Source preservation wins for the protected pixels |
| Photography route suggests lens grain; requested output is a clean deterministic UI mockup | Target medium and legibility win |
| Regional research lens suggests a local motif; no evidence links the scene to that place | Leave locale unspecified |
| Identity profiler gives uncertain visual observation; consenting subject corrects it | Subject's explicit correction wins |
| Specialized poster wants embedded text; exact factual copy is essential | External deterministic typesetting and factual QA win |

### Prompt compiler: meaningful sections

Use these fields only when needed:

1. **Task statement:** new image, bounded edit or review of an actual artifact.
2. **Visual proposition:** one sentence about subject, relationship and purpose.
3. **Scene/blocking:** frame ratio, viewpoint, foreground/background, action and negative space.
4. **Capture or illustration medium:** how perspective, line, paper, film, light and texture behave.
5. **Color and hierarchy:** restrained palette or specified color logic, readable anchors and focal rhythm.
6. **Sources and protected facts:** source roles, reference scope, permissions, identity rules and exact content.
7. **Optional specialist DNA:** only the distinctive instructions needed from selected route(s).
8. **Negative guidance:** concise, task-specific prohibitions rather than a universal anti-artifact wall.
9. **Acceptance conditions:** what the user must be able to see or preserve after any actual output.

### Variation mechanics

When a user requests diverse options, create **deep alternatives**. Two prompts that differ only in “ethereal” versus “cinematic” are still one design. Change medium, camera geometry, composition, environment or narrative scale, while keeping the semantic nucleus fixed. When one variant was sampled randomly, do not silently curate it into a preferred option.

### QA evidence states

`direction_prepared` means only text exists. `renderer_called` means a real external tool invocation occurred. `artifact_returned` means a file can be inspected. `inspected_against_source` means a comparison was actually performed. `accepted` requires the user's goal and relevant constraints to have been checked, not just plausible prose.

### Small executable handoff example

**Request:** A company wants a credible illustrated flyer for a community cycling workshop.  
**State:** `new_image`, public flyer, original graphics, no identity source, printed A4 output.  
**Primary route:** Omnialchemy for the visual thesis; add Vintage Editorial Rubber Hose Poster **only if** the client actually requests that style.  
**Direction:** Simple service scene with one strong action, limited palette and reserved space for exact event copy.  
**QA:** Text correctness, hierarchy at print size, unambiguous date/location, and no invented endorsement or trademark.  
**Renderer:** unavailable means direction plus typesetting instructions only, not a claimed finished flyer.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
