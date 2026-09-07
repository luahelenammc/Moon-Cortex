# Repository Naming and Versioning

Moon Cortex keeps human-facing identity separate from release state.

- **Title / name = identity.** A module title names the stable domain capability and should remain useful after an ordinary release advances.
- **Version = state.** A version records the current pre-release, compatibility or generation state in dedicated metadata and release history.

## Governed surfaces

For current public modules, keep the stable title in:

- module README headings;
- canonical entry headings;
- root navigation, cards and tables;
- public package labels and other human-facing distribution text.

Record release state separately in:

- `**Version:**` metadata;
- changelog and release records;
- technical filenames, paths and package names when those coordinates are useful;
- compatibility notes and historical prose.

The current active modules illustrate the contract:

```text
Title: Financial Living System
Version: 0.1.0-pre.4
Technical entry: modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md
Package: downloads/financial-living-system.zip

Title: Social Support Navigation System
Version: 0.1.0-pre.1
Technical entry: modules/social-support-navigation-system/SOCIAL_SUPPORT_NAVIGATOR.md
Package: downloads/social-support-navigation-system.zip
```

The title remains stable while the version changes. A technical path may retain a version marker when that is part of a compatibility or transport contract; that marker must not become the current human-facing title.

## Local sovereignty and inheritance

This rule governs the public repository body and module surfaces. It does not rename user-local systems, private donor sources or internal artifacts. Future Cortex modules should copy [the reusable template](../templates/REPOSITORY_NAMING_AND_VERSIONING.md), adapt the governed surfaces they expose, and install the automated guard before public promotion.

## Validation

Run:

```text
python scripts/check_title_version_separation.py
python scripts/test_title_version_separation.py
```

The guard checks active public module headings and their dedicated version metadata. It does not ban version-bearing changelog headings, historical references, technical coordinates or package filenames.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en)
