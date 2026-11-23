<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Moon Cortex Ecosystem Governance

## Purpose and authority

The atlas is a **discovery and interoperability surface**. It may describe public relationships, canonical entry points, route contracts and validation state. It does not become the source of truth for any listed project's domain, factual claims, releases, runtime, local records, decisions or permissions.

The human or governing project retains final authority. Each indexed public project owns its own semantic body and release process. A catalog relationship does not install a dependency or give one project control over another.

The atlas uses two distinct contracts:

- [Moon Source · Source Operations](https://github.com/luahelenammc/Moon-Source/blob/main/docs/SOURCE_OPERATIONS.md) remains authoritative for source succession, lifecycle and the smallest sovereign destination.
- [Moon Cortex · Cross-repository Compatibility](CROSS_REPOSITORY_COMPATIBILITY.md) owns only the operational inventory and checking of public links between opted-in repositories.

## What may enter the registry

An entry may be added when its public source and responsibility are identified, its canonical entry is verified, its relationship to the atlas is useful, and its privacy boundary can be stated without exposing private context.

The public registry excludes private projects, user records, clinical or personal cases, identity corpora, credentials and unpublished manuscripts. An uncreated or unverified project may be noted as pending **only with null canonical URL fields**; do not guess a URL from a proposed name. Projects do not need an atlas entry to remain valid or usable.

For each public project, keep these fields current:

| Field | Meaning |
|---|---|
| `id` | Stable registry identifier, independent of repository display name. |
| `class` | The project's function, not a claim of rank or ownership. |
| `canonical_repo`, `canonical_entry` | Verified public URLs where an authorized reader can begin. Pending projects use `null`. |
| `summary`, `owned_function` | A concise statement of purpose and jurisdiction. |
| `status_verified_at` | Date the state was read back from its live source. |
| `head_at_status_check` | Informational commit observed on that date; it is not a runtime pin or a claim that the source will remain unchanged. |
| `distribution` | Existing, verified public transports only. |
| `imports`, `references`, `exports` | Functional dependencies, nonbinding discovery references and capabilities. Do not place optional references in `imports`. |
| `privacy_boundary` | Public/private limits relevant to discovery and reuse. |
| `legacy_routes` | Exact legacy URLs of routes in the compatibility registry owned by this project; the URL is the stable route ID. |
| `validation_ref` | Local checker or policy that validates this entry. |

`registry/ecosystem.json` is an index, not a mirror of the indexed sources. The public source remains canonical even when the atlas links to it.

## Change and removal procedure

For a material public update, use the following order:

1. **Discover** the affected URL, file, package or anchor and its known uses.
2. **Classify** the surface as a Markdown page, raw file, ZIP, website, release, asset or other route.
3. **Preserve** the old route when it has been used or is promised by a local contract.
4. **Select** a canonical target owned by the destination project.
5. **Implement** a readable pointer, exact-byte mirror, functional package copy, archive state or real site redirect only where the host supports it.
6. **Test** file paths, fragments, ZIP integrity and live HTTP status when reachable. A failed or blocked check remains unverified.
7. **Read back** the committed target and its branch or release state.
8. **Register** only the route actually observed and implemented.
9. **Monitor** the changed scope in CI and record recovery references.

A public entry may be revised or retired through a normal reviewed change. Keep provenance and a successor pointer when a public path has an established role. Do not remove history or replace a project's meaning with an atlas description.

## Versioning and review

A discovery, translation or link repair does not by itself change a project's semantic version. A change to operational behavior follows the versioning rule of the source that owns that behavior. Atlas metadata is dated by `status_verified_at`; it does not refresh itself in the background.

Before publishing a change, run the offline checker and synthetic regression suite. Run the online check where network conditions permit; report host errors as `external_unverified`. Review the visible page in both languages and ensure the five existing applied systems retain their current paths and downloads.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](../LICENSING.md) · [Federation Atlas](../ECOSYSTEM.md)
