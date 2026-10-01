<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Scientific References

**MSL profile:** 5.1-compatible method reference; sources support statistical concepts, not the validity of this module or any forecast produced with it.

## Forecast verification and scoring

- Brier, G. W. (1950). [Verification of forecasts expressed in terms of probability](https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2). *Monthly Weather Review*, 78(1), 1–3.
- Murphy, A. H. (1973). [A new vector partition of the probability score](https://doi.org/10.1175/1520-0450(1973)012%3C0595:ANVPOT%3E2.0.CO;2). *Journal of Applied Meteorology*, 12(4), 595–600.
- Gneiting, T., Balabdaoui, F., & Raftery, A. E. (2007). [Probabilistic forecasts, calibration and sharpness](https://doi.org/10.1111/j.1467-9868.2007.00587.x). *Journal of the Royal Statistical Society: Series B*, 69(2), 243–268.
- Gneiting, T., & Raftery, A. E. (2007). [Strictly proper scoring rules, prediction, and estimation](https://doi.org/10.1198/016214506000001437). *Journal of the American Statistical Association*, 102(477), 359–378.

## Bayesian and reference-class methods

- Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). [Bayesian Data Analysis, Third Edition](https://www.routledge.com/Bayesian-Data-Analysis-Third-Edition/Gelman-Carlin-Stern-Dunson-Vehtari-Rubin/p/book/9781439840955). CRC Press. A general reference for Bayesian modeling; it does not select a prior for this module.
- Flyvbjerg, B. (2008). [Curbing optimism bias and strategic misrepresentation in planning: Reference class forecasting in practice](https://doi.org/10.1080/09654310701747936). *European Planning Studies*, 16(1), 3–21. Its application is project planning; transfer to another domain requires a separately defensible class.

## Expert elicitation

- Hemming, V., Burgman, M. A., Hanea, A. M., McBride, M. F., & Wintle, B. C. (2018). [A practical guide to structured expert elicitation using the IDEA protocol](https://doi.org/10.1111/2041-210X.12857). *Methods in Ecology and Evolution*, 9, 169–180.
- University of Sheffield. [Sheffield Elicitation Framework (SHELF)](https://shelf.sites.sheffield.ac.uk/). Official framework resources for eliciting probability distributions from groups of experts.

## Uncertainty propagation and recalibration

- Joint Committee for Guides in Metrology. (2008). [JCGM 101: Evaluation of measurement data — Supplement 1: Propagation of distributions using a Monte Carlo method](https://doi.org/10.59161/JCGM101-2008). BIPM. This standard concerns measurement uncertainty; its computational principle does not validate arbitrary forecast inputs.
- Kull, M., Silva Filho, T. M., & Flach, P. (2017). [Beta calibration: A well-founded and easily implemented improvement on logistic calibration for binary classifiers](https://proceedings.mlr.press/v54/kull17a.html). *Proceedings of AISTATS*, PMLR 54, 623–631. Beta calibration is cited as a published alternative; it is not implemented in this reference code.

## Calibrated language

- IPCC. (2021). [AR6 WGI Chapter 1: Framing, context and methods](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-1/). The IPCC defines calibrated likelihood terms for its assessment context. Do not claim equivalent semantics in unrelated fields.

These sources ground selected methods and concepts. They do not establish universal validity, domain suitability, or measured performance for Probability Calibration System.

<!-- MOON-CORTEX-PUBLIC-STAMP -->

---

> 🌙 **Moon Cortex** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Cortex/blob/main/LICENSING.md) · [Moon Source bridge](https://github.com/luahelenammc/Moon-Source) · [Professional context](https://www.luahelena.com.br/ia/?lang=en) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
