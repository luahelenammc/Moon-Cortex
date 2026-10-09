<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Tool and renderer contract

Moon Image Cortex is an instruction and QA system. A renderer is an optional external capability and is never implied by possession of this package.

## Execution states

| State | Meaning | Permitted claim |
|---|---|---|
| Direction prepared | A visual brief and design choices are written | “Direction prepared” |
| Prompt prepared | Prompt or edit instruction exists | “Prompt prepared; not rendered” |
| Rendered | A named available tool returned an image in this task | “Rendered with [tool]” |
| Inspected | The actual returned image was opened and checked | Report observed properties and defects |
| Repaired | A new render or deterministic edit was performed and checked | Report which issue was addressed and remaining uncertainty |

Do not skip a state in language. A prompt is not a render, an API call is not visual QA, and a visual QA instruction is not proof of fidelity.

## Renderer handoff

Before invoking a renderer, confirm that the tool is available in this session and that the task’s image and permissions allow its use. Pass only necessary task material. Return the prompt or instruction separately from the final image so the user can inspect or reuse it.

For exact lettering, charts, repeated tile geometry, and critical layout, prefer deterministic typesetting or drawing when available. Use generative rendering for visual material where it is appropriate. Always inspect a returned image before saying it satisfies the brief.

## No renderer available

Give the user a complete direction sheet, a prompt they can take elsewhere, and a compact QA checklist. Mark generated_image as absent and say “not rendered.” Do not pretend that a downloaded placeholder or prompt is an image result.

## Identity and image sources

A user-provided photo may be used only within the task’s authorized edit or reference role. A profile never substitutes for current consent. Never fetch or store a person’s image from a social profile to fill an identity gap. See [Identity, consent and boundaries](IDENTITY_CONSENT_AND_BOUNDARIES.md).

## External services

No API keys, renderer credentials, vendor setup, analytics, data feeds, or model weights are bundled. A user may bring an authorized tool. Tool availability, current model capabilities, and licensing terms must be checked at the time of use.


<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
