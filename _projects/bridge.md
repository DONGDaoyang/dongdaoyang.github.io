---
layout: page
title: "Bridge (LPBF · Ti-6Al-4V)"
card_title: "Bridge (LPBF · Ti-6Al-4V)"
description: This is a Ti-6Al-4V bridge model. A local thermal–mechanical simulation is used to identify inherent strain, which is then applied
  to the full bridge model to calculate residual elastic strain.
permalink: /benchmarks/bridge/
hub_case: true
published: true
importance: 3
case_type: Computational case
img: /assets/img/cases/bridge/results-cover.png
image_alt: Bridge saved simulation stress result.
---

{% assign hub = site.data.residual_stress_hub %}

<div class="rsh rsh-page-brand">
<section class="rsh-hero rsh-hero-with-background" aria-label="Residual Stress Hub">
<img class="rsh-hero-background" src="{{ hub.hero_background | relative_url }}" alt="" aria-hidden="true">
<a class="rsh-hero-brand rsh-site-title" href="{{ '/' | relative_url }}" aria-label="Residual Stress Hub home">
<img class="rsh-logo" src="{{ hub.logo | relative_url }}" alt="" aria-hidden="true" width="200" height="160">
<span class="rsh-brand-name"><span class="rsh-stress-name">Residual Stress</span> <span class="rsh-hub-name">Hub</span></span>
</a>
</section>
</div>

[← All benchmarks](/benchmarks/)

## Overview

This is a Ti-6Al-4V bridge model. A local thermal–mechanical simulation is used to identify inherent strain, which is then applied to the full bridge model to calculate residual elastic strain. <a href="#reference-1">[1]</a>

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Geometry and dimensions.](/assets/img/cases/bridge/geometry-overview.png)

_Figure 1. Geometry and dimensions._

[Download the original geometry PDF](/assets/pdf/cases/bridge/geometry-overview.pdf)

</div>

</figure>

</div>

## Problem set

### Printing parameters

| Parameter                                                         | Value             | Unit |
| ----------------------------------------------------------------- | ----------------- | ---- |
| Manufacturing process                                             | LPBF              | —    |
| Material                                                          | Ti-6Al-4V         | —    |
| Heat-source power, $P$                                            | 100               | W    |
| Scan speed, $V$                                                   | 600               | mm/s |
| Physical deposition layer thickness                               | 30                | µm   |
| Hatch spacing                                                     | 105               | µm   |
| Absorption efficiency                                             | 0.3               | —    |
| Goldak heat-source dimensions (front / rear / transverse / depth) | 54 / 54 / 54 / 30 | µm   |
| Cooling interval (after each deposited layer)                     | 200               | s    |

### Simulation parameters

| Parameter                                                                                         | Value / setting                                                                | Unit              |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------- |
| Ambient temperature                                                                               | 25                                                                             | °C                |
| High-temperature material model                                                                   | See tables below                                                               | —                 |
| Elastic parameters (room temperature, constant)                                                   | $E$ = 114.58<br>$\nu$ = 0.3                                                    | GPa<br>—          |
| Plastic parameters (room temperature, constant)                                                   | $\sigma_{\mathrm{y}}$ = 1151<br>$H$ = 1.8139<br>$\sigma_{\mathrm{max}}$ = 1310 | MPa<br>GPa<br>MPa |
| Identified inherent strain, $\varepsilon_{\mathrm{xx}}^{\ast} = \varepsilon_{\mathrm{yy}}^{\ast}$ | -2.820                                                                         | ‰                 |
| Identified inherent strain, $\varepsilon_{\mathrm{zz}}^{\ast}$                                    | 2.879                                                                          | ‰                 |
| Layer activation                                                                                  | 36 × 0.25                                                                      | Layers × mm       |
| Constraints and release                                                                           | fixed plane $Z$ = 0 mm; no release                                             | —                 |
| Thermal strain reference temperature                                                              | 25                                                                             | °C                |
| Thermal strain cutoff                                                                             | solidus                                                                        | —                 |

The physical print layer is 30 µm. The 250 µm layer pitch used in the model is a separate coarse activation setting.

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

The temperature-dependent thermal and mechanical parameters used in the local scan model for inherent-strain identification are adapted from Ganeriwala et al. (Tables 1 and 2). <a href="#reference-1">[1]</a>

#### Ti-6Al-4V — upper region and lower region

| Parameter                              | Value  | Unit  |
| -------------------------------------- | ------ | ----- |
| Density, $\rho$                        | 4417.8 | kg/m³ |
| Latent heat, $L$                       | 270000 | J/kg  |
| Solidus temperature, $T_{\mathrm{s}}$  | 1878   | K     |
| Liquidus temperature, $T_{\mathrm{l}}$ | 1928   | K     |
| Maximum yield factor                   | 1.2    | —     |

##### Thermal conductivity, $k$

| $T$ (K) | $T$ (°C) | Thermal conductivity, $k$ (W/(m·K)) |
| ------- | -------- | ----------------------------------- |
| 273     | -0.15    | 6.18                                |
| 1254    | 980.85   | 19                                  |
| 1264    | 990.85   | 19.2                                |
| 1913    | 1639.85  | 27.7                                |
| 1923    | 1649.85  | 33.4                                |
| 3550    | 3276.85  | 36.8                                |

##### Specific heat capacity, $C_{\mathrm{p}}$

| $T$ (K) | $T$ (°C) | Specific heat capacity, $C_{\mathrm{p}}$ (J/(kg·K)) |
| ------- | -------- | --------------------------------------------------- |
| 273     | -0.15    | 517                                                 |
| 1254    | 980.85   | 881                                                 |
| 1264    | 990.85   | 707                                                 |
| 1913    | 1639.85  | 756                                                 |
| 1923    | 1649.85  | 829                                                 |
| 3550    | 3276.85  | 829                                                 |

##### Young’s modulus, $E$

| $T$ (K) | $T$ (°C) | Young’s modulus, $E$ (GPa) |
| ------- | -------- | -------------------------- |
| 293     | 19.85    | 115                        |
| 961     | 687.85   | 60.7                       |
| 973     | 699.85   | 59.8                       |
| 1173    | 899.85   | 24                         |
| 1264    | 990.85   | 16.7                       |
| 1538    | 1264.85  | 11                         |

##### Thermal expansion coefficient, $\alpha$

| $T$ (K) | $T$ (°C) | Thermal expansion coefficient, $\alpha$ (µm/(m·K)) |
| ------- | -------- | -------------------------------------------------- |
| 273     | -0.15    | 8.85                                               |
| 1254    | 980.85   | 10.72                                              |
| 1264    | 990.85   | 10.74                                              |
| 1913    | 1639.85  | 11.97                                              |
| 1923    | 1649.85  | 20.17                                              |
| 3550    | 3276.85  | 0                                                  |

##### Poisson ratio, $\nu$

| $T$ (K) | $T$ (°C) | Poisson ratio, $\nu$ (—) |
| ------- | -------- | ------------------------ |
| 293     | 19.85    | 0.3                      |
| 961     | 687.85   | 0.3                      |
| 973     | 699.85   | 0.3                      |
| 1173    | 899.85   | 0.3                      |
| 1264    | 990.85   | 0.3                      |
| 1538    | 1264.85  | 0.3                      |

##### Initial yield stress, $\sigma_{\mathrm{y}}$

| $T$ (K) | $T$ (°C) | Initial yield stress, $\sigma_{\mathrm{y}}$ (MPa) |
| ------- | -------- | ------------------------------------------------- |
| 293     | 19.85    | 1151                                              |
| 961     | 687.85   | 365.8                                             |
| 973     | 699.85   | 257.6                                             |
| 1173    | 899.85   | 69                                                |
| 1264    | 990.85   | 69                                                |
| 1538    | 1264.85  | 69                                                |

##### Hardening modulus, $H$

| $T$ (K) | $T$ (°C) | Hardening modulus, $H$ (GPa) |
| ------- | -------- | ---------------------------- |
| 293     | 19.85    | 1.828                        |
| 961     | 687.85   | 1                            |
| 973     | 699.85   | 1                            |
| 1173    | 899.85   | 1                            |
| 1264    | 990.85   | 1                            |
| 1538    | 1264.85  | 1                            |

Maximum yield stress, $\sigma_{\mathrm{max}}$, is $1.2\,\sigma_{\mathrm{y}}$ at each interpolated temperature.

</details>

[Download full parameter JSON](/assets/data/cases/bridge/thermal-parameters.json) · [Download temperature-dependent CSV](/assets/data/cases/bridge/temperature-dependent-properties.csv) · [Download simulation YAML](/assets/data/cases/bridge/simulation-parameters.yaml)

[Download simulation configuration](/assets/data/cases/bridge/macro-parameters.yaml) · [Download identification results](/assets/data/cases/bridge/identification-results.json)

## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

### Residual stress field

<div class="rsh-case-figure-content" markdown="1">

![Residual stress field.](/assets/img/cases/bridge/results-cover.png)

_Figure 2. Residual stress field._

[Download the stress-field figure](/assets/pdf/cases/bridge/results-cover.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Temperature and strain histories

<div class="rsh-case-figure-content" markdown="1">

![Temperature and X-direction strain histories.](/assets/img/cases/bridge/thermal-history.png)

_Figure 3. Temperature and $X$-direction strain histories._

[Download the history CSV](/assets/data/cases/bridge/thermal-mechanical-history.csv)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Inherent-strain identification

<div class="rsh-case-figure-content" markdown="1">

![Stress and elastic strain comparison.](/assets/img/cases/bridge/optimization-agreement.png)

_Figure 4. Stress and elastic strain comparison._

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Residual stress field comparison.](/assets/img/cases/bridge/optimization-agreement-page-2.png)

_Figure 5. Residual stress field comparison._

[Download all comparison pages](/assets/pdf/cases/bridge/optimization-agreement.pdf) · [Download the error metrics](/assets/data/cases/bridge/optimization-metrics.csv)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Residual elastic strain

<div class="rsh-case-figure-content" markdown="1">

![X-direction elastic strain at X = 3.75 mm.](/assets/img/cases/bridge/x3p75.png)

_Figure 6. $X$-direction elastic strain at $X$ = 3.75 mm._

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Z-direction elastic strain at X = 3.75 mm.](/assets/img/cases/bridge/z3p75.png)

_Figure 7. $Z$-direction elastic strain at $X$ = 3.75 mm._

Additional profiles: [3.75 mm, $Y$-direction](/assets/img/cases/bridge/y3p75.png) · [7.75 mm, $X$-direction](/assets/img/cases/bridge/x7p75.png) · [7.75 mm, $Y$-direction](/assets/img/cases/bridge/y7p75.png) · [7.75 mm, $Z$-direction](/assets/img/cases/bridge/z7p75.png).

</div>

</figure>

</div>

---

**Reference:**

<span id="reference-1"></span>

[1] Ganeriwala, R.K., Strantza, M., King, W.E., Clausen, B., Phan, T.Q., Levine, L.E., Brown, D.W., Hodge, N.E. (2019). Evaluation of a thermomechanical model for prediction of residual stress during laser powder bed fusion of Ti-6Al-4V. _Additive Manufacturing_, **27**, 489–502. [https://doi.org/10.1016/j.addma.2019.03.034](https://doi.org/10.1016/j.addma.2019.03.034).
