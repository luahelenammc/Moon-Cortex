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


<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
