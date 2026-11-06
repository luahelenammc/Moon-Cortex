<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Taste Privacy, Source Rights and Platforms

Taste Cartographer is a **documentation-based, opt-in method**. It has no bundled data collector, Spotify importer, access token, user database or hidden background observer.

## Public/private boundary

Public: reusable method, schema, synthetic examples, evidence weighting, conditional preference logic, discovery routes, user-consent gates and minimal creation bridge.

Private: real user's track favorites, library, listening history, timestamps, playlists, personal music associations, profile corrections and local Taste State. **Never copy these into the GitHub repo or the public Agent Skill.**

Use the smallest input necessary, keep user control over local state, distinguish observations from hypotheses, allow correction and retracement, and avoid collecting private metadata such as IP, device identifiers and granular timestamps. No inference of health, sexuality, gender, religion, political stance, ethnicity or other sensitive traits from music.

## Spotify policy gate

The [Spotify Developer Policy](https://developer.spotify.com/policy) (effective May 15, 2025; reviewed November 6, 2026) restricts analysis of Spotify Content/Service for user profiles and using Spotify Platform or Content to train **or otherwise ingest** into an AI or machine-learning model. [Developer Terms](https://developer.spotify.com/terms) also apply.

**Do not implement Spotify API-derived taste profiling, automated playlist scraping, ingestion of Spotify Content or upload of raw Spotify datasets to an AI for profile construction.** An available API key or a user's Spotify login is not a substitute for permission under the service terms. A user may be able to download their account data, but the export itself **does not automatically license AI model ingestion or derivative profiling**. Before considering any external dataset, verify current platform rules and permitted purpose; when unclear or prohibited, do not ingest.

Safe standard intake: **the person's own words** about what they like/dislike, voluntarily named reference tracks and self-written notes about musical characteristics. External music-catalog research can support permitted verification of public track identity, but it must not become hidden personal tracking.

Other providers may have different terms. Check the relevant terms at the time of use. Don't imply native integrations or rights that have not been verified.

## Privacy and writes

Separate four acts: (1) temporary conversation, (2) creating a proposed Taste State, (3) saving or updating it in an authorized user-controlled location, (4) passing a minimal sonic payload to an external generator. **No step authorizes the next by default.**

A user can ask to correct, stop using, export or delete a local state. Write or delete only where tools and permissions actually exist. Do not promise removal from other providers, connected apps or hidden assistant memory. Don't store raw event logs when a smaller set of user-confirmed features is sufficient.

Music rights are independent: preference for an artist does not authorize copying lyrics, melodies, samples or distinctive arrangement. See [Reference-to-Feature Translator](../modes/REFERENCE_TO_FEATURE_TRANSLATOR.md).

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
