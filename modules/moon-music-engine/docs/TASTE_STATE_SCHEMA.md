<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Taste State · Portable Contract

A **user-owned, editable, optional** Markdown/JSON state for the Taste Cartographer. A schema declaration is not a database, account integration, automated profiler or guarantee of long-term memory.

## Fields and meaning

| Field | Purpose |
|---|---|
| `schema`, `revision`, `updated_at` | local compatibility and traceable updates |
| `evidence` | limited source snippets with item/version, user reaction, context, provenance and confidence |
| `constellations` | names, **combined** musical features, conditions/counterconditions and evidence IDs |
| `deep_core`, `current_orbit`, `dormant_loves` | references to constellation IDs; none is mandatory |
| `saturation` | temporarily overplayed material, distinct from aversion |
| `anti_taste` | context-bound dislikes/counterexamples |
| `bridges`, `hypotheses` | tentative connections or experiments, not observed truths |
| `contexts`, `discovery_radius` | user-defined uses and Orbit/Adjacent/Bridge/Edge/Rift |
| `feedback`, `revisions` | user reactions and smallest defensible changes |
| `sharing` | opt-in for profile-informed creation; external transfer defaults off |

`confidence`: `low`, `medium`, `high`, never a fake percentage. `label`: `love`, `like`, `interesting`, `not now`, `indifferent`, `dislike`, `hate`, `overplayed`. `provenance`: `user-stated`, `user-curated`, `source-supported`, `observed-audio`, `inferred`, `proposed`. Do not label an assumed musical trait as "observed".

## Minimal JSON starter · entirely fictional

```json
{
  "schema": "moon-music-engine/taste-state/0.1",
  "revision": 1,
  "updated_at": null,
  "evidence": [
    {
      "id": "e1",
      "provenance": "user-stated",
      "item": "Fictional track: Paper Lanterns",
      "label": "love",
      "liked_features": ["soft hand percussion", "patient melodic build"],
      "disliked_features": [],
      "context": "evening",
      "confidence": "high"
    }
  ],
  "constellations": [
    {
      "id": "c1",
      "name": "Soft rhythmic propulsion and a patient arc",
      "features": ["restrained percussion", "gradually emerging melody"],
      "conditions": ["relaxed listening"],
      "counterconditions": ["persistent harsh high frequencies"],
      "evidence_ids": ["e1"],
      "confidence": "low"
    }
  ],
  "deep_core": [],
  "current_orbit": ["c1"],
  "dormant_loves": [],
  "saturation": [],
  "anti_taste": [],
  "bridges": [],
  "contexts": ["evening"],
  "discovery_radius": "Adjacent",
  "hypotheses": [],
  "feedback": [],
  "sharing": {
    "use_for_creation": false,
    "share_full_profile_with_external_generator": false
  },
  "revisions": [
    {"revision": 1, "change": "Provisional map from one user statement"}
  ]
}
```

This **illustrative template** is not a verified real profile. A single track does not establish a Deep Core. Blank arrays indicate **no recorded evidence**, not "the person never likes this."

## Delta rules

- **New evidence:** attach a provenance ID and confidence; don't silently strengthen unrelated constellations.
- **Contextual correction:** "like the sax only when soft" becomes a *condition*, not "loves sax".
- **Temporary fatigue:** add saturation without deleting enduring affection.
- **Version-specific liking:** record the preferred version/arrangement, not a blanket artist judgment.
- **Contradiction:** keep distinct constellations or revise the rule; do not average contradictory choices.
- **Rejection of a recommendation:** update the tested feature hypothesis, not the entire musical identity.
- **Deletion/disable:** stop downstream use immediately; change stored data only in authorized, accessible user-controlled locations. No claim of deleting platform-held histories.

The listener decides where this state lives and whether it may be reused. A chat output is not persistent merely because this schema exists. Never publish a filled private state to the public repository.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
