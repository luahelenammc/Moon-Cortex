<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Synthetic example: conservative photo edit

No image asset is included. The input below is a fictional instruction used to exercise the edit contract.

**User:** “Remove the empty takeaway cup from the table and keep everything else as close as possible.”

**Route:** Conservative photo-edit gate; renderer contract.

**Direction:** Use the supplied image only as the edit target. Remove the cup and reconstruct the tabletop surface and occluded texture. Protect people, faces, hands, food, labels, table edges, light, camera perspective, color and crop. Do not retouch skin or relight the scene.

**Edit instruction:** “Remove only the empty takeaway cup on the table near the lower right. Fill the occluded area using the immediately surrounding wood grain and lighting. Preserve every person, object, text, reflection, shadow, proportion and crop outside that small region. Do not add objects or beautify the photo.”

**QA:** Compare the target and result at native size. Check cup removal, grain continuity, table edge, shadows and all protected regions. If no renderer returned an image, report the instruction only and mark not rendered.


<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
