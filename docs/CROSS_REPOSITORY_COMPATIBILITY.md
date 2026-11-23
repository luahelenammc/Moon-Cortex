<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Cross-repository Compatibility and Link Continuity

## Scope

This contract governs **public route inventory and link checks** for repositories that choose to register a relationship in the [Moon Cortex ecosystem registry](../registry/ecosystem.json). It does not govern the meaning, ownership, privacy policy, release or runtime of any participating project.

The underlying principle of source succession remains with [Moon Source · Source Operations](https://github.com/luahelenammc/Moon-Source/blob/main/docs/SOURCE_OPERATIONS.md) and its [Archive and Legacy contract](https://github.com/luahelenammc/Moon-Source/tree/main/archive). The [AOP migration record](https://github.com/luahelenammc/Adaptive-Orchestration-Protocol/blob/main/docs/MIGRATION_AND_COMPATIBILITY.md) is a concrete operational precedent for readable pointers and functional ZIP mirrors. Moon Cortex adds no second theory of source succession; it checks whether a registered route preserves access to its actual successor.

## Route record

`registry/legacy-routes.json` records only a route that was actually discovered and is owned by a participating public source. It does not serve as a wishlist or contain guessed future URLs.

Each route requires:

| Field | Requirement |
|---|---|
| `legacy_url`, `legacy_repo`, `legacy_path` | Exact public source URL, repository and old path observed. |
| `target_project_id`, `target_canonical_url` | Registered public project and a URL inside that project's canonical repository. |
| `route_class` | Human-readable class such as `markdown`, `raw`, `binary`, `site`, `release`, `asset` or `archive`. |
| `compatibility_behavior` | One of the behaviors below, matching what the host actually supports. |
| `owner_repo` | Repository responsible for preserving the old route. |
| `first_known_use`, `old_status`, `test_method` | Evidence about the old route and how it is checked. |
| `last_checked`, `result` | Actual check date and result; never report an unrun check as passing. |
| `recovery_ref`, `policy_source` | Recovery reference and governing policy URL(s). |

Allowed `compatibility_behavior` values are `human_readable_pointer`, `functional_binary_mirror`, `exact_byte_web_mirror`, `static_site_301_or_308_if_supported`, `frozen_archive`, `git_history_only` and `not_changed`.

An empty `routes` list means this change introduced no verified legacy-route migration. It is preferable to an invented row.

## Behaviors by surface

| Surface | Valid continuity behavior |
|---|---|
| GitHub `blob/.../file.md` | Preserve the file at the old path and make it a readable pointer to the current canonical file when succession occurred. GitHub does not provide an arbitrary 301 for that Markdown file. |
| GitHub `raw/...` | Preserve either readable pointer bytes or the exact canonical bytes when the source contract requires that. A raw URL has no rendered navigation. |
| ZIP download | Keep a real, integrity-checked payload or a real archive; compare member list and SHA-256. A ZIP is not a redirect. |
| Static website | Use HTTP 301/308 only if its configured hosting layer supports and verifies it. Otherwise retain a page with a successor link. |
| GitHub release, tag, commit or issue | Keep its address and history. Add a supersession note when the surface supports one. |
| External link or QR code | Record the original URI and the limits of control; test only what can be reached. |

## Check semantics

The checker validates the registry shape, uniqueness and cycles; confirms local canonical paths and Markdown fragments; and compares the tracked download manifest against real ZIP bytes. Its default mode is offline and deterministic. `--online` makes bounded requests to active public canonical repositories and entries.

Results have three meanings:

- **PASS:** a local path/hash check or a live HTTP response was actually observed and met the contract.
- **FAIL:** an observed missing path, bad fragment, wrong target, invalid ZIP, SHA mismatch, cycle or HTTP 404/410 violates the contract.
- **UNVERIFIED:** the network, host, rate limit, authentication boundary or external service prevented a conclusive check.

`UNVERIFIED` is not a success. The live check is intentionally optional in CI so a GitHub outage does not block unrelated documentation work. An operator may use `--strict-online` when release acceptance requires all live URLs to resolve.

## Opt-in binding and maintenance

A participating repository needs only a small local binding: identify its governing source, the public paths it owns, the permitted compatibility behaviors and its recovery reference. It does not need to copy this policy or another repository's content. For each change, the responsible owner updates the route record only after preservation, test and readback.

When a registered route fails, restore the old pointer or package first, then repair the canonical target. Prefer a reviewed revert or corrective commit over rewriting history. If a project is private or cannot be read, mark it blocked; do not publish its path or infer a public route.

## Current state

No path was renamed or moved for this atlas change. `registry/legacy-routes.json` therefore starts with zero routes. The existing five Moon-Cortex module paths and ten ZIP packages remain at their baseline locations and are checked by the repository's package validators plus `registry/distribution-manifest.json`.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](../LICENSING.md) · [Federation Atlas](../ECOSYSTEM.md)
