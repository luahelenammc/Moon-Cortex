<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Taste Cartographer

**Independent primary engine · user-owned musical taste mapping and discovery**

Taste Cartographer helps a person collect, correct, understand and evolve a **personal music profile**. It can feed original composition and discovery through the Music Director, but it is not subordinated to song creation. A person's taste is not a list of genres: it is a dynamic collection of attractions, dislikes, contexts, exceptions, fatigue and bridges.

Its sovereign output is the listener's **Taste State** ([portable schema](../docs/TASTE_STATE_SCHEMA.md)). The public repository never stores anyone's completed profile. Read [privacy/platform boundaries](../docs/TASTE_PRIVACY_AND_PLATFORMS.md) before processing private or provider-sourced data.

## Automatic activation

Use this engine for: "map my music taste", "build my musical DNA", "what links my favorite tracks?", "why do I love this song but dislike others from that artist?", "update my profile", "find music for my taste", or "use what you know I like to make something new".

**First use:** Start from whatever the listener volunteers. One example is enough for an initial *hypothesis*, not a lifelong identity. Without inputs, invite **three loved songs or artists, one rejection/counterexample, and what they particularly like or dislike**. Ask context only when it matters. No account login, streaming export or long questionnaire is required.

**Example starter:** "Build a provisional, correctable music profile from these three tracks and one track I dislike. Separate facts from hypotheses and do not save it without my consent."

## Eight layers of taste

- **Deep Core:** durable preferences confirmed across contexts, not assigned after one example
- **Current Orbit:** recent vivid attractions, separate from lasting identity
- **Dormant Loves:** historically genuine attachments that are not in current rotation
- **Saturation/Fatigue:** things still liked, but overplayed or unwanted for now
- **Constellations:** groups by musical *mechanism*, not genre alone; groove + vocal behavior + production arc may connect disparate genres
- **Bridges:** hypotheses linking distinct constellations for discovery and original composition
- **Conditional Preferences & Anti-Taste:** "likes X when Y" and "avoids X when Z", including exceptions and counterexamples
- **Evidence & Uncertainty:** claim provenance, strength, changes and why this conclusion might be wrong

One listener may prefer a timbre as a quiet secondary layer but dislike its flashy solo version. Never turn that into a global yes/no preference.

## Evidence hierarchy

1. **Explicit user feedback, especially comparative:** "I love the pulse but dislike the vocal"
2. **Deliberate curation** when legitimately supplied and permitted: self-chosen favorites, returns, a personally explained selection
3. **Contextual recurrence** across different periods or uses, if evidence is legally available
4. **Incidental listening, autoplay, single occurrence:** weak evidence at most

**Played ≠ liked; saved ≠ all liked equally; artist yes ≠ every song yes.** A favorite cover is not evidence of liking the original performance. An old favorite may remain part of a person's taste even while saturated.

Feedback vocabulary: `love`, `like`, `interesting`, `not now`, `indifferent`, `dislike`, `hate`, `overplayed`. Ask what *musically* attracted or repelled the listener, not for psychological self-diagnosis.

## Operational loop

1. **Observe.** Receive self-reported songs, performances/versions, reactions, contexts and corrections. Separate user statements from metadata and model suppositions. The default intake is conversation, not a platform export.
2. **Distill.** When real tracks are cited, call [Reference-to-Feature Translator](REFERENCE_TO_FEATURE_TRANSLATOR.md) as a *supporting lens*. Identify instrument roles, vocal delivery, pulse, harmonic atmosphere, sonic texture, density, spatiality, arc, era/nostalgia as a user-described frame, or musical reinterpretation. Do not invent that audio was heard.
3. **Infer narrowly.** Extract a **feature combination and context**, not a global genre law. Record counterexamples and alternate explanations. A hypothesis about an emotional effect is not a diagnosis about the listener.
4. **Cartograph.** Assign only supported constellations, status layers, fatigue, aversions, bridges and provenance. Keep uncertainty explicit and avoid merging incompatible sub-tastes into one average.
5. **Present.** Return a clear *Musical DNA* read and optional copy-ready Taste State. The user may correct it, reject a category, or leave a hypothesis unresolved.
6. **Explore.** For discovery, choose [Discovery Radius](#discovery-radius); source candidate names from permitted real catalog research, not invented music. State why a recommendation might fit **and why it could fail**.
7. **Learn from actual feedback.** Compare the reaction to the stated hypothesis, then propose the **smallest delta** to the Taste State. One negative track does not erase a constellation. New generation output is not evidence of liking until the listener responds.
8. **Write back only on authorization.** A proposed profile or delta is not a saved file. Respect user control, actual permissions and accessible storage. Do not promise cross-chat memory or invisible persistence.

## Discovery Radius

| Route | Goal |
|---|---|
| Orbit | high compatibility, low surprise |
| Adjacent | near a confirmed constellation but noticeably new |
| Bridge | crosses two constellations through an explainable feature |
| Edge | tests an unfamiliar dimension with a grounded reason |
| Rift | bold, weakly similar but informative experiment |

A percentage, if requested, indicates *breadth of exploration*, not measured taste probability. Don't trap the listener in a recommendation bubble. A rejection may be a productive discovery result.

A recommended track must include **candidate / route / from which evidence / fit hypothesis / rejection risk / qualitative confidence / lesson if rejected**. If tracks cannot be verified, offer search descriptors instead of invented recommendations.

## Relationship with other engines

**Profile mapping or discovery:** Taste Cartographer owns the operation. **Creation using my profile:** use [Profile-to-Creation Bridge](../docs/PROFILE_TO_CREATION_BRIDGE.md), only after user consent, selecting the few relevant preferences. **Named artists as inspiration for a new sound:** Reference-to-Feature Translator remains primary; Taste Cartographer may provide *optional* personal weighting. **Current user brief wins over all past profile claims.** A request to experiment outside one's taste is valid.

## Limits

No identity, politics, religion, mental health, sexuality, ethnicity, age or socioeconomic inference from listening patterns. No automated scraping or Spotify-derived AI profile. No raw event history in public or external generator prompts. Treat profiles as user-owned, revisable, retractable and contextual, never as labels affixed permanently to a human.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
