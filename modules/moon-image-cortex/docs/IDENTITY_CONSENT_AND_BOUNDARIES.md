<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Identity, consent and boundaries

Human Canon Forge is a generic, optional method for keeping a person’s likeness coherent across user-authorized visual work. It is not a public identity database, face-recognition system, or inference engine.

## Consent and authority

- The subject has authority over their own appearance and the description used to represent them.
- For another person, establish their consent and the user’s right to use the image for this task. A request alone does not prove broad reuse rights.
- Consent to one edit or generation does not imply consent to retain a profile, train a model, publish an image, or use it in another context.
- Stop using supplied references when permission is withdrawn or becomes unclear.
- A profile is local to the user’s own context and should be shared only as necessary.

## Evidence lanes

Separate three kinds of information:

1. **Observed:** visible in a supplied image, with limits from crop, lighting, resolution, angle and image quality.
2. **Self-described:** supplied directly by the subject or authorized user.
3. **Unknown:** not reliably available. Leave it blank rather than completing a coherent-looking profile through guesswork.

Never convert an appearance observation into a sensitive identity claim. Do not infer race, ethnicity, health, disability, gender identity, sexuality, religion, personality, relationship, age beyond a necessary user-specified band, or other sensitive facts from an image.

## Generic profile shape

When explicitly requested and authorized, a user may keep a compact, editable record:

- profile owner and subject authority
- consent scope, date, allowed uses and expiry/revocation condition
- observed visual anchors with source and uncertainty
- subject-described attributes, in their own terms
- prohibited transformations and protected features
- allowed variation across setting, clothes, pose, lighting, crop and art medium
- reference files stored by the user outside the public module
- review date and deletion condition

Do not save biometric vectors, face embeddings, hidden identifiers, or unrelated personal records. A text profile is not a substitute for the reference image when exact visual continuity matters.

## Preservation and variation

For a conservative likeness task, define what should remain stable and what may vary. Preserve identity-relevant features and natural proportions unless the subject requests a change. Do not beautify, age, slim, enlarge, masculinize, feminize, or otherwise remodel the subject without explicit instruction from the subject.

If there is no reference image or sufficiently specific subject description, say that identity fidelity cannot be checked. Produce an original subject only if that is what the user wants; never promise likeness from absent evidence.

## Public-package boundary

No user’s face, body description, biometric information, photo, private visual canon, social-media image, or reference set is included in this module. Examples are synthetic and non-reconstructive. The public method is reusable; an individual’s profile remains user-controlled.


<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
