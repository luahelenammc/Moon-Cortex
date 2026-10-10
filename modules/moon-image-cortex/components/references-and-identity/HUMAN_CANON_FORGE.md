<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Human Canon Forge

**System:** Moon Image Cortex · **Type:** conditional cross-cutting component
**Parent authority:** [Visual Director](../../VISUAL_DIRECTOR.md#first-use) · [Component index](../../docs/COMPONENT_INDEX.md)

This file is a subordinate component, **not** another general entry, personal memory, or renderer. Use it only when the task earns it. Public documentation does not install tools or persist identity data.

## Trigger and first use

Use **only** for a consenting person's user-authorized likeness across portraits, editing or fictionalized scenes. This is a generic method, never an embedded personal identity pack. Review [identity and consent rules](../../docs/IDENTITY_CONSENT_AND_BOUNDARIES.md) first.

## Consent and evidence

Explicitly separate image observations (subject to light/crop uncertainty), the person's own description/corrections, and unknown features. An uploaded image or one-off edit instruction is **not** permanent consent for retention, training, redistribution or future use. A subject's corrections override guessed traits. Do not infer gender, sexuality, race, health, class, psychology, trauma, morality or identity from facial features.

## Public local profile schema

- `profile_owner`, `scope`, `consent_status`, `retention_choice`, `reference_roles`.
- `confirmed_features` and `visual_constraints`, with uncertainty and source identified.
- `protected_identity_features` and `allowed_variations` by task (pose, apparel, scene and light).
- `do_not_change`, including no unrequested beautification, body reshaping or feature replacement.
- `revision_log`, `withdrawal_rule` and `private_storage_owner` when the user chooses retention.

The profile is assembled **in the user's authorized local context**, not stored in this module or uploaded to a public repository.

## Procedure and outputs

Establish permission → classify references → document only relevant stable features → ask subject for corrections where practical → produce a minimal identity-preserving render/edit instruction → inspect only an actual returned image for drift → revise the private profile if authorized. Output a user-owned `identity_profile`, a protected-features checklist, optional reference-sheet direction and honest fidelity uncertainty.

## Synthetic activation

A consenting fictional subject asks to change the background of their existing portrait. Protect their face and body proportions, change the background only, and do not invent a face description from an absent photo.

## Consent-based likeness workflow

The purpose is **specific-person continuity**, not generating a generic attractive person. A human subject has authority over their own presentation: photographic observations are provisional, corrections from the person outrank model guesses, and the profile is only a task-scoped aid to an explicitly authorized visual goal.

### Operating modes

| Mode | What may be prepared | Boundary |
|---|---|---|
| Self-profile | User-controlled description of stable visual features for future authorized portraits | The person may revise or withdraw it; no retention is assumed |
| Consenting third-party portrait | Likeness constraints for a defined portrait or project | Establish subject permission and scope; avoid reuse beyond consent |
| Reference-sheet direction | Instructions for front, three-quarter and profile views where source evidence permits | Do not invent hidden features, tattoos or body details |
| Identity-preserving edit | Protected features and smallest acceptable visual delta | Use Conservative Photo Edit; original image remains the comparison source |
| Stylized avatar | Stable identity cues with bounded stylization level | Disclose stylization and protect explicitly identified features |

### Reference intake

Prefer a small *authorized* set of clearly distinct roles: front view, three-quarter view, side view, full-body clothed reference where truly necessary, customary hair, relevant visible marks or accessories, and the subject's own description. Do not request intimate or excessive source imagery simply to improve rendering. A single photograph cannot establish every feature.

Classify each detail as **confirmed by subject**, **visually observed with uncertainty**, **task variation** or **unknown**. Light, makeup, hair styling, expression, pose, clothing and camera distortion can change apparent features. Nothing in an image authorizes guesses about psychology, morality, race, health, sexuality, gender identity or social class.

### A minimal user-controlled visual profile

`subject_permission` · `task_and_retention_scope` · `reference_roles` · `confirmed_visual_cues` · `observations_and_uncertainties` · `must_preserve` · `allowed_transformations` · `never_infer` · `idealization_level` · `revision_and_withdrawal`.

Separate **stable continuity** (facial proportions, distinctive visible marks as confirmed, hairstyle when the subject wants it protected) from **authorized variants** (wardrobe, scene, lighting, age-specific period portrayal, editorial makeup, artistic medium). A change in style is not permission to change someone's body.

### Twelve-step procedure

1. Define person, purpose, consent and permissible output.
2. Classify each photo's viewpoint, conditions and role.
3. Read stable visible features, marking uncertainty.
4. Record subject-described corrections and priorities.
5. Separate stable characteristics from scene/wardrobe variants.
6. Define `must_preserve` and `must_not_infer`.
7. Select stylization: none, light, strong or symbolic, only as requested.
8. Draft a compact profile and obtain correction where appropriate.
9. Build a reference-sheet or image-generation instruction with protected cues.
10. Inspect an actual returned image for identity drift; do not claim fidelity from text alone.
11. Generate a *bounded* correction prompt for the drifted traits.
12. Offer the subject the ability to revise, export or discard local state.

### Fidelity audit

Inspect facial geometry, eyes, brows, hairline/hair behavior, neck/shoulder proportions when relevant, skin microtexture, age depiction where authorized and any protected clothing/marks. Distinguish model-created idealization from the person's actual desired self-image. When fidelity cannot be checked because originals or tool outputs are unavailable, say so clearly.

**Handoff example:** “For this consenting subject, retain the specific facial proportions and confirmed hairstyle from the supplied references; change only background and jacket. Do not replace with a generic fashion face or reshape body proportions. Verify against original at matching scale.”

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
