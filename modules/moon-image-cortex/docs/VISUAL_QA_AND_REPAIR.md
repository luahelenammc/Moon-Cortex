<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Visual QA and repair

QA begins from the stated brief and actual available file. A checklist cannot prove a render that was never produced.

## Shared inspection order

1. **Artifact identity:** Is this the actual returned file, correct version, and intended crop/size?
2. **Brief fidelity:** Are subject, hierarchy, framing, meaning and protected details preserved?
3. **Technical quality:** Are there visible defects in edges, anatomy, lighting, texture, type, tiling or crop?
4. **Factual and rights review:** Are numbers, wording, source roles, consent and marks correct?
5. **Claim calibration:** Separate observed image properties from assumptions and renderer or model claims.

A repair states the defect, the smallest affected region or rule, and what remains unchecked.

## Photo and render symptoms

Watch for inconsistent reflections or shadows, impossible lens perspective, plastic or waxy texture, smudged micro-detail, over-sharpened halos, repeated forms, invented text, and detail that changes identity or scene facts. A soft-but-sharp look, flattened high-frequency texture, waxiness, or repeated tiles are symptoms, not proof of a cause.

The donor source hypothesized watermark-linked degradation but did not establish causality. Treat watermark causation as **unverified**. Do not infer provenance from texture, promise a watermark cure, or give watermark-removal/evasion instructions. If symptoms are present, reduce global micro-detail, simplify high-frequency textures, test a clean lower-detail render, or repair one local region. These are quality controls, not provenance tools.

## Tiling and mosaic QA

Use a repeated pattern only with a source whose rights and quality permit it. Before repeating, inspect source borders, resolution and tile-to-neighbor continuity. After assembly, inspect a contact sheet and seams at both native and enlarged scale. Check for repeated distinctive artifacts and crop drift. If a seam is structural, fix the source tile or mask; do not hide a poor tile under more texture.

## Text and typography QA

If wording matters, supply exact text separately and use deterministic typesetting when available. Check spelling, punctuation, line breaks, contrast, hierarchy, safe margins and legibility at intended display size. If the image model produces approximate lettering, report that the text is not verified and offer a deterministic correction route.

## Shared-axis weather/temperature fixture

This public example is a calculation fixture only; it is not a weather service or live forecast.

Use one Celsius axis from 0 °C to 40 °C for low, mean and high values. For a horizontal bar with width 400 px, marker position is:

position_px = ((value - minimum) / (maximum - minimum)) × width_px

Synthetic inputs: minimum 0 °C, maximum 40 °C, low 12 °C, mean 18 °C, high 23 °C, width 400 px.

- Low marker: (12 − 0) / (40 − 0) × 400 = 120 px, or 30%.
- Mean marker: (18 − 0) / (40 − 0) × 400 = 180 px, or 45%.
- High marker: (23 − 0) / (40 − 0) × 400 = 230 px, or 57.5%.

The range segment spans low to high. Place the mean marker by its value on the same ruler; do not center it decoratively and do not give low, mean and high unrelated scales. Check units, axis endpoints, numerical labels, rounding and placement after rendering. Calculations should be deterministic and independently verified before drawing.

## Anti-house-style check

If recent outputs are actually available, compare their palette, composition, motif, medium and focal treatment. Repeat a family only when the brief warrants it. Otherwise, do not invent a comparison. Choose alternatives because they fit the subject, not to satisfy random variety.

## Repair protocol

- Text error: correct the text in deterministic layout if possible.
- Global texture failure: simplify global detail or material count.
- One local defect: isolate the affected region and protect the rest.
- Wrong visual thesis: reconstruct and reroute; micro-edits cannot fix a bad brief.
- Rights or consent gap: stop use of that source; request authorized material or make an independent direction.
- No renderer or no actual artifact: return instructions only and label the render absent.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
