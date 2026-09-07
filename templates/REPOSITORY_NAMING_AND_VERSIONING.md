# Repository Naming and Versioning Template

Use this template for a Moon Cortex module or related public repository.

## Title–version separation

**Title / name = identity.** Keep the human-facing capability or module title stable across ordinary releases.

**Version = state.** Record the current release state separately in metadata, changelogs, registries and release records.

## Governed surfaces

Use the stable title in:

- README and canonical entry headings;
- root navigation, cards and tables;
- public package labels.

Keep version markers in dedicated metadata and technical/history coordinates:

- `**Version:**` fields;
- changelogs and release notes;
- technical filenames, paths, package names and compatibility identifiers;
- explicitly historical prose.

```text
Stable title: [human-facing identity]
Current version: [release state]
Canonical entry: [technical path]
Package: [technical package path]
Validation command: python scripts/check_title_version_separation.py
```

Add an automated guard and a regression test before public promotion. A technical version marker must not become the current human-facing title.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en)
