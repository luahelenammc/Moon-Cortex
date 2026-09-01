from pathlib import Path
import zipfile

root = Path('.')
module = root / 'modules' / 'financial-living-system'
bootstrap = module / 'ADAPTIVE_FINANCE_BOOTSTRAP.md'


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8', newline='\n')


for path in module.rglob('*.md'):
    if path.name == 'CHANGELOG.md':
        continue
    write(path, read(path).replace('0.1.0-pre.3', '0.1.0-pre.4'))

for path in [root / 'README.md', root / 'ARCHITECTURE.md', root / 'LICENSING.md']:
    write(path, read(path).replace('0.1.0-pre.3', '0.1.0-pre.4'))

root_readme = read(root / 'README.md')
root_readme = root_readme.replace(
    '| Let an AI discover that financial field and instantiate the system adaptively | [Adaptive Finance Bootstrap](modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md) |',
    '| Use the Financial Living System with an AI | [Download the complete Financial Living System package (.zip)](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) and keep the full package together |'
)
root_readme = root_readme.replace(
    'The Financial Living System is not a budget template and does not require the user to know Moon Cortex vocabulary. Its canonical bootstrap is self-activating when supplied as operative context, unless the user explicitly asks only to read, review or analyze it.',
    'The Financial Living System is not a budget template and does not require the user to know Moon Cortex vocabulary. Its canonical transport unit is the complete module ZIP. The Adaptive Finance Bootstrap is the entrypoint inside that package, not a separate installable product.'
)
root_readme = root_readme.replace(
    '📘 [**Open the module README**](modules/financial-living-system/README.md) for the problem-first orientation, installation states, examples and module map.\n\n📦 [**Download the complete Financial Living System module (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip).',
    '📦 [**Download the complete Financial Living System module (.zip)**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) — this is the default transport and use surface.\n\n📘 [**Open the module README**](modules/financial-living-system/README.md) for package-first usage, installation states, examples and internal anatomy.'
)
write(root / 'README.md', root_readme)

module_readme = '''<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# 🌙 Moon Cortex · Financial Living System

**Adaptive personal-finance organization for AI: one integrated package that maps financial reality before choosing structure.**

A budget template starts with categories. A dashboard starts with widgets. A finance app starts with whatever its database already knows how to store. Real financial life often starts somewhere messier: several pay rhythms, money that belongs to another period, credit purchases that are not current cash outflows, protected reserves that look spendable, reimbursements that have not arrived, or a perfectly usable spreadsheet that should not be replaced.

The **Financial Living System** is the Moon Cortex finance module for turning that field into a living, user-owned financial system. It is not a menu of independent components. Its public files form one cooperating package: the **Adaptive Finance Bootstrap** is the entrypoint, while the capability map, invariants, installation bridge, privacy/claims contract, validation test and examples provide the surrounding system it relies on.

> 📦 **Start here: download the complete Financial Living System.**  
> 💸⬇️ [**Download `financial-living-system.zip`**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip) — the canonical transport and default use surface.

## One system, not a component shelf

Unlike Moon Source, whose public components can often be consulted independently by responsibility, the Financial Living System is distributed as an **integrated module**.

The files inside the package have different jobs, but they are not separate products, separate installation routes or interchangeable downloads. The normal contract is:

```text
download the complete Financial Living System package
        ↓
give the package to the AI as operative context
        ↓
Adaptive Finance Bootstrap starts the process
        ↓
companion contracts remain available to the bootstrap
        ↓
field discovery + capability compilation + validation
        ↓
user-local living financial system
```

**Package completeness does not mean loading every file into active context at once.** The full package should travel together so its contracts remain available; the executing AI should inspect and load the smallest relevant internal material as the setup requires.

That distinction is important:

> **The package is indivisible in distribution. Internal attention is still proportional.**

## Why the Financial Living System exists

Personal-finance systems commonly fail in two opposite ways: they are too thin to preserve real distinctions, or so elaborate that the user ends up maintaining the system instead of using it.

The Financial Living System takes a field-first route. It separates stable financial distinctions from conditional capabilities that should activate only when the user's actual situation earns them. The resulting local system can remain compact for a simple case and become richer only when credit, installments, irregular income, shared money, multiple currencies, protected reserves or other material complexity actually exists.

Its job is not to moralize spending or prescribe one ideal budget. Its job is to make financial state, obligations, timing and uncertainty **legible enough to reconcile and act on**.

## Use it in four steps

### 1. Download the complete package

Use the canonical ZIP:

📦 [**`financial-living-system.zip`**](https://github.com/luahelenammc/Moon-Cortex/raw/refs/heads/main/downloads/financial-living-system.zip)

Downloading or copying only one internal Markdown file is not the canonical setup path.

### 2. Give the package to the AI

Provide the complete ZIP, extracted directory or equivalent complete package surface as operative context. The user should not need to identify individual components or know Moon Cortex vocabulary.

### 3. Let the Adaptive Finance Bootstrap start automatically

Inside the package, [`ADAPTIVE_FINANCE_BOOTSTRAP.md`](ADAPTIVE_FINANCE_BOOTSTRAP.md) is the canonical entrypoint. No command phrase is required. The AI should begin adaptive setup automatically unless the user explicitly asks only to read, review or analyze the package without execution.

The bootstrap inspects supplied financial material first, discovers only material gaps, preserves sound existing systems, activates only earned capabilities and chooses a local form the host can actually maintain.

### 4. Keep the generated local system sovereign

The package governs setup and installation. After installation, ordinary finance work should run from the user's own local sources rather than requiring the Financial Living System ZIP or Moon Source on every interaction.

## The architecture in one minute

```text
financial-living-system.zip
        ↓ complete public module travels together
Adaptive Finance Bootstrap
        ↓ entrypoint + adaptive field discovery
Financial Field Model
        ↓
Capability Map + Financial Invariants
        ↓ only earned capabilities activate
local form + installation contract
        ↓
Financial Reality Test + readback
        ↓
user-local living financial system
```

The central law is:

> **Map the user's financial reality first, then generate the smallest local finance system that actually fits it.**

A few distinctions carry most of the financial model:

- credit purchase ≠ immediate cash outflow;
- statement payment = cash outflow + liability settlement;
- expected reimbursement ≠ current cash;
- internal transfer ≠ spending;
- protected reserve ≠ free cash;
- observed future pressure ≠ closed truth;
- available capability ≠ activated capability.

## What travels inside the package

These files cooperate as one public system:

| Internal part | Responsibility inside the package |
|---|---|
| [`ADAPTIVE_FINANCE_BOOTSTRAP.md`](ADAPTIVE_FINANCE_BOOTSTRAP.md) | Entry interface, field discovery, routing, compilation and installation orchestration |
| [`docs/UNIVERSAL_FINANCIAL_INVARIANTS.md`](docs/UNIVERSAL_FINANCIAL_INVARIANTS.md) | Financial distinctions that must survive local adaptation |
| [`docs/CAPABILITY_MAP.md`](docs/CAPABILITY_MAP.md) | Core and conditional capabilities plus activation/deactivation logic |
| [`docs/MOON_SOURCE_INSTALLATION_BRIDGE.md`](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md) | Optional Moon Source-aware installation governance |
| [`docs/PRIVACY_AND_CLAIMS.md`](docs/PRIVACY_AND_CLAIMS.md) | Safe-input, privacy, evidence and public-claim boundaries |
| [`docs/FINANCIAL_REALITY_TEST.md`](docs/FINANCIAL_REALITY_TEST.md) | Bounded validation and readback contract |
| [`examples/`](examples/) | Fictional scenarios showing how one package compiles differently across fields |
| [`CHANGELOG.md`](CHANGELOG.md) | Module chronology and public contract changes |

The table describes **internal anatomy**, not a choose-your-own-installation menu.

## What can be activated

The package carries a stable core plus conditional capabilities. Carrying a capability in the package does not mean activating it in the user's local system.

| Layer | Examples |
|---|---|
| Core | Current Financial State, Cycle Reconciliation, Temporal Ownership, Reserve Semantics, Double-Count Guards, Cycle Closing, Epistemic Typing |
| Conditional | Credit Card Intelligence, Installment Tail, Microfrequency, Next-Cycle Anticipation, Reimbursements, Shared Costs, Debt Schedule, Irregular Income, Multi-Currency, Tax Reserve, Subscriptions |

> **Access ≠ activation.**

A user without meaningful credit should not receive decorative card machinery. A user with an existing maintained spreadsheet should not receive a parallel five-file empire because folders happen to look serious.

## Installation states

The complete Financial Living System package can operate with or without the optional Moon Source bridge.

### Package setup

With the **complete Financial Living System package** available, an AI can discover the financial field, compile the Financial Field Model, map local terminology, select capabilities, choose an installation profile and produce an installation-ready plan.

This does **not** require Moon Source. It does require the Financial Living System package as the canonical transport unit.

### Moon Source-aware installation

When the current public [Moon Source](https://github.com/luahelenammc/Moon-Source) repository is deliberately available, the package can additionally use the [Moon Source Installation Bridge](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md). The Moon Source Kernel is read first, only the smallest relevant public methods are loaded, the local system is materialized and read back, and the Financial Reality Test is run proportionately.

### User-local runtime

After installation, ordinary finance work should operate from the user's own local sources. Moon Source remains a justified reconfiguration or repair dependency, not a permanent upstream API. The Financial Living System package remains the upstream public module, not the user's day-to-day ledger.

In shorthand:

```text
complete package in transport
Moon Source optional at installation
locally sovereign at runtime
```

## Examples

The package includes three fictional, didactic and non-evidentiary scenarios. They show how the **same integrated system** compiles differently when the field changes.

- [Simple Salaried User](examples/SIMPLE_SALARIED_USER.md) — a deliberately small local installation without credit machinery.
- [Credit and Non-Monthly Pay User](examples/CREDIT_AND_NONMONTHLY_PAY_USER.md) — biweekly income, credit tails, microfrequency and reimbursement.
- [Irregular Multi-Currency User](examples/IRREGULAR_MULTICURRENCY_USER.md) — uncertain income, multiple currencies, protected tax reserve and integration into an existing spreadsheet.

The examples are not separate presets to install and do not contain private Finanças Moon data.

## Evidence, boundary and reuse

The module is deliberately conservative about what its public artifacts prove.

- [Financial Reality Test](docs/FINANCIAL_REALITY_TEST.md) defines bounded synthetic validation.
- [Privacy, Claims and Attribution](docs/PRIVACY_AND_CLAIMS.md) defines safe-input rules and the public claim ceiling.
- [Universal Financial Invariants](docs/UNIVERSAL_FINANCIAL_INVARIANTS.md) defines the financial distinctions intended to survive across jurisdictions and payment systems.
- [Moon Source Installation Bridge](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md) defines the optional installation/context-governance relationship.
- [Moon Cortex Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) governs reuse under **CC BY 4.0** for the current public textual body.

The financial architecture was generalized from the private donor system **Finanças Moon**. Naming that lineage does not publish the donor corpus or turn private financial facts into evidence.

## Internal map for inspection

If you are auditing, adapting or studying the package, these are its canonical internal routes. Ordinary users should start from the complete ZIP above rather than collecting these files individually.

| Inspect | Internal route |
|---|---|
| Entry and orchestration contract | [ADAPTIVE_FINANCE_BOOTSTRAP.md](ADAPTIVE_FINANCE_BOOTSTRAP.md) |
| Capability activation rules | [docs/CAPABILITY_MAP.md](docs/CAPABILITY_MAP.md) |
| Cross-jurisdiction financial distinctions | [docs/UNIVERSAL_FINANCIAL_INVARIANTS.md](docs/UNIVERSAL_FINANCIAL_INVARIANTS.md) |
| Optional Moon Source installation bridge | [docs/MOON_SOURCE_INSTALLATION_BRIDGE.md](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md) |
| Validation contract | [docs/FINANCIAL_REALITY_TEST.md](docs/FINANCIAL_REALITY_TEST.md) |
| Privacy, claims and attribution | [docs/PRIVACY_AND_CLAIMS.md](docs/PRIVACY_AND_CLAIMS.md) |
| Fictional scenarios | [examples/](examples/) |
| Module chronology | [CHANGELOG.md](CHANGELOG.md) |

## Current baseline

**Version:** `0.1.0-pre.4`  
**Status:** public pre-release  
**Structural grammar:** MSL 4.3  
**Canonical module path:** `modules/financial-living-system/`  
**Canonical transport unit:** `downloads/financial-living-system.zip`  
**Canonical entrypoint inside the package:** `modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md`

The public package is English-first and model-agnostic. The executing AI should follow the user's language after activation. The current public module does not require a primary `SKILL.md`, bank connector, hosted UI or autonomous transaction layer.

Created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion**. Moon retains final authority.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex · Financial Living System** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · instantiated through **Adaptive Finance Bootstrap** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Cortex/archive/refs/heads/main.zip)
'''
write(module / 'README.md', module_readme)

bootstrap_text = read(bootstrap)
bootstrap_text = bootstrap_text.replace('**Standalone dependency:** none', '**Canonical transport requirement:** complete Financial Living System package (`financial-living-system.zip` or equivalent complete extracted directory)')
bootstrap_text = bootstrap_text.replace(
    'When this file is supplied to an AI as operative context, **begin the Adaptive Finance Bootstrap automatically**. No command phrase is required.\n\nDo not begin execution only when the user explicitly asks to read, review, explain or analyze the bootstrap without running it, or when a higher-priority instruction clearly makes execution inappropriate.\n\nUse this file as an adaptive interface. Do not summarize it back before doing the work unless the user explicitly asks for a summary.',
    'When the **complete Financial Living System package** is supplied to an AI as operative context, locate this file and **begin the Adaptive Finance Bootstrap automatically**. No command phrase is required.\n\nThis file is the entrypoint inside the package, not an independently supported distribution unit. If only this file is available, treat the Financial Living System transport as incomplete and resolve or request the complete package before claiming canonical setup or installation.\n\nDo not begin execution only when the user explicitly asks to read, review, explain or analyze the package without running it, or when a higher-priority instruction clearly makes execution inappropriate.\n\nUse this file as the package interface. Do not summarize it back before doing the work unless the user explicitly asks for a summary.'
)
old_section = '''## Standalone versus Moon Source-aware installation

### Standalone mode

With only this file available, the AI may:

- run discovery;
- build the Financial Field Model;
- generate a local lexicon;
- compile the needed capabilities;
- choose an installation profile;
- produce an installation-ready packet.

It must not claim to have read Moon Source or to have completed Moon Source-aware installation.

### Moon Source-aware installation mode

When the current public Moon Source repository is reachable, use the installation bridge in [`docs/MOON_SOURCE_INSTALLATION_BRIDGE.md`](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md). Read the Moon Source Kernel first, load only the smallest relevant public methods, materialize the local system, read it back and run the proportional Financial Reality Test.

After successful installation:

```text
self-contained in transport
Moon Source-aware at installation
locally sovereign at runtime
```

Moon Source should be consulted again only for a justified reconfiguration, migration, repair or explicit refresh.
'''
new_section = '''## Package-first versus Moon Source-aware installation

### Complete package mode

With the **complete Financial Living System package** available, the AI may:

- run discovery through this entrypoint;
- consult the package's companion contracts proportionately;
- build the Financial Field Model;
- generate a local lexicon;
- compile the needed capabilities;
- choose an installation profile;
- produce an installation-ready packet.

The package is the canonical transport unit. Its internal files are cooperating responsibilities, not alternative standalone install surfaces. Package completeness does not require loading every companion file into active context at once.

This mode does not require Moon Source and must not claim that Moon Source was read.

### Moon Source-aware installation mode

When the current public Moon Source repository is reachable, use the package's installation bridge in [`docs/MOON_SOURCE_INSTALLATION_BRIDGE.md`](docs/MOON_SOURCE_INSTALLATION_BRIDGE.md). Read the Moon Source Kernel first, load only the smallest relevant public methods, materialize the local system, read it back and run the proportional Financial Reality Test.

After successful installation:

```text
complete Financial Living System package in transport
Moon Source optional and deliberate at installation
locally sovereign at runtime
```

Moon Source should be consulted again only for a justified reconfiguration, migration, repair or explicit refresh.
'''
if old_section not in bootstrap_text:
    raise SystemExit('Expected bootstrap installation section not found')
bootstrap_text = bootstrap_text.replace(old_section, new_section)
write(bootstrap, bootstrap_text)

architecture = read(root / 'ARCHITECTURE.md')
architecture = architecture.replace(
    '- **Transport:** the canonical bootstrap artifact at `modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md` is self-contained and can begin setup without Moon Source.\n- **Installation:** a canonical Moon Source-aware installation consults the current public Moon Source repository, reads its Kernel first and uses only the methods needed for that installation.\n- **Runtime:** the generated user-local financial system operates from its own sources. Routine transactions do not require Moon Source retrieval.\n\nThe canonical public transport artifact is now named for its actual role: `modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md`. The pre-release namespace therefore distinguishes the **Financial Living System** module from the **Adaptive Finance Bootstrap** mechanism that instantiates it.\n\nIf the Moon Source bridge is unavailable, discovery and compilation may still finish. The result must say `ready_for_installation`, not pretend that Moon Source-aware installation happened.',
    '- **Transport:** the canonical transport unit is the complete `downloads/financial-living-system.zip` package (or an equivalent complete extracted directory). Its internal files travel as one module.\n- **Entrypoint:** `modules/financial-living-system/ADAPTIVE_FINANCE_BOOTSTRAP.md` starts and routes setup from inside that package; it is not the independently supported distribution unit.\n- **Installation:** a Moon Source-aware installation may additionally consult the current public Moon Source repository, read its Kernel first and use only the methods needed for that installation.\n- **Runtime:** the generated user-local financial system operates from its own sources. Routine transactions do not require the upstream package or Moon Source retrieval.\n\nThe package is indivisible in distribution but proportional in attention: all Financial Living System contracts remain available, while the executing AI loads only the internal material needed for the current field and step.\n\nIf the Moon Source bridge is unavailable, package-based discovery and compilation may still finish. The result must say `ready_for_installation`, not pretend that Moon Source-aware installation happened.'
)
write(root / 'ARCHITECTURE.md', architecture)

bridge = read(module / 'docs' / 'MOON_SOURCE_INSTALLATION_BRIDGE.md')
bridge = bridge.replace(
    'The canonical bootstrap artifact is independently readable and executable as a setup interface. It does not require the Moon Source repository to begin discovery or finish the Financial Field Model.',
    'The canonical transport unit is the complete Financial Living System package. `ADAPTIVE_FINANCE_BOOTSTRAP.md` is the entry interface inside that package, while the companion files remain available as cooperating contracts. The package does not require the Moon Source repository to begin discovery or finish the Financial Field Model. An isolated bootstrap file is not the canonical Financial Living System transport.'
)
write(module / 'docs' / 'MOON_SOURCE_INSTALLATION_BRIDGE.md', bridge)

root_changelog = read(root / 'CHANGELOG.md')
entry = '''## 0.1.0-pre.4 — 2026-09-01

Integrated-package contract clarification for the Financial Living System.

- made `downloads/financial-living-system.zip` the canonical transport and default use surface for the Financial Living System;
- clarified that the module's Markdown files are cooperating parts of one integrated system, not independent installable components;
- retained `ADAPTIVE_FINANCE_BOOTSTRAP.md` as the automatic entrypoint inside the complete package rather than a standalone distribution unit;
- preserved proportional internal loading: the package travels whole, while the executing AI consults only the internal material needed for the current field and step;
- replaced the old standalone-bootstrap setup contract with complete-package setup plus optional Moon Source-aware installation;
- preserved local runtime sovereignty after installation.

'''
root_changelog = root_changelog.replace('# Changelog\n\n', '# Changelog\n\n' + entry, 1)
write(root / 'CHANGELOG.md', root_changelog)

module_changelog = read(module / 'CHANGELOG.md')
module_entry = '''## 0.1.0-pre.4 — 2026-09-01

Package-integrity clarification.

- established the complete Financial Living System ZIP as the canonical transport and default use surface;
- clarified that internal Markdown files cooperate as one module and are not separate installation choices;
- retained the Adaptive Finance Bootstrap as the entrypoint inside the package;
- removed the prior standalone-bootstrap execution contract;
- preserved proportional internal loading, adaptive capability activation, optional Moon Source-aware installation and locally sovereign runtime.

'''
module_changelog = module_changelog.replace('# Financial Living System Changelog\n\n', '# Financial Living System Changelog\n\n' + module_entry, 1)
write(module / 'CHANGELOG.md', module_changelog)

zip_path = root / 'downloads' / 'financial-living-system.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(module.rglob('*')):
        if path.is_file():
            arcname = Path('financial-living-system') / path.relative_to(module)
            zf.write(path, arcname.as_posix())
