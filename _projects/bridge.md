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
img: /assets/img/cases/bridge/card-cover.png?v=21931f5eab15
image_alt: "Bridge benchmark model."
---

{% assign hub = site.data.residual_stress_hub %}

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url | bust_file_cache }}">

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

### Axial elastic-strain field

<div class="rsh-case-figure-content" markdown="1">

![Bridge axial elastic-strain field with a color scale in microstrain.](/assets/img/cases/bridge/results-cover.png?v=3810220e4237)

<p markdown="0"><em>Figure 2. Bridge axial elastic strain $\varepsilon^{\mathrm{e}}_{\mathrm{xx}}$ (µε).</em></p>

The color scale measures elastic strain. Positive values show axial extension and negative values show axial contraction. This part-scale result is distinct from the local DNS calibration model shown below.

[Download the figure PDF](/assets/pdf/cases/bridge/results-cover.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Local thermal and strain histories

<div class="rsh-case-figure-content" markdown="1">

![Bridge local temperature and axial plastic and elastic strain during scanning and cooling.](/assets/img/cases/bridge/thermal-history.png)

<p markdown="0"><em>Figure 3. Saved Bridge local history: temperature (°C) and axial strain (dimensionless).</em></p>

The upper panel tracks temperature and the lower panel separates the saved plastic and elastic $xx$ strains at local cell 451, centered at $(0,0,0.0150)$ mm. The time axis covers the local scanning and cooling calculation. It is not the complete bridge build history or a new solver run.

[Download local history CSV](/assets/data/cases/bridge/thermal-mechanical-history.csv) · [Download local history PDF](/assets/pdf/cases/bridge/thermal-history.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Local elastic-strain agreement

<div class="rsh-case-figure-content" markdown="1">

![Bridge Opt-IS versus DNS elastic-strain parity plots for the xx, yy and zz components.](/assets/img/cases/bridge/strain-parity.png?v=718cb6e725e8)

<p markdown="0"><em>Figure 4. Bridge local calibration: $xx$, $yy$ and $zz$ elastic-strain parity (µε).</em></p>

The three panels compare Opt-IS with DNS on 882 paired active native cells. The dashed diagonal represents exact agreement. Scatter away from that line shows the remaining component-specific mismatch.

[Download the figure PDF](/assets/pdf/cases/bridge/strain-parity.pdf) · [Download archived error metrics](/assets/data/cases/bridge/optimization-metrics.csv)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Local elastic-strain maps

<div class="rsh-case-figure-content" markdown="1">

![Bridge local axial elastic-strain maps.](/assets/img/cases/bridge/strain-spatial-page-1.png?v=9cc2e642e679)

<p markdown="0"><em>Figure 5. Bridge local model: $\varepsilon^{\mathrm{e}}_{\mathrm{xx}}$ maps (µε).</em></p>

From left to right: DNS, Opt-IS, and the signed difference Opt-IS minus DNS on the top layer. The difference map locates the spatial calibration mismatch.

[Download the figure PDF](/assets/pdf/cases/bridge/strain-spatial.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Local elastic-strain profiles

<div class="rsh-case-figure-content" markdown="1">

![Bridge local top-plane elastic-strain profiles.](/assets/img/cases/bridge/strain-spatial-page-2.png?v=92ca4ccfb80a)

<p markdown="0"><em>Figure 6. Bridge local model: $xx$, $yy$ and $zz$ top-plane elastic-strain profiles (µε).</em></p>

The three panels compare the normal elastic-strain components along the same native top-plane sampling row. These local profiles are distinct from the full bridge measurement lines below.

[Download the figure PDF](/assets/pdf/cases/bridge/strain-spatial.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Part-scale axial elastic strain

<div class="rsh-case-figure-content" markdown="1">

![Bridge axial elastic strain across the span compared with experimental measurements.](/assets/img/cases/bridge/axial-strain-profile.png?v=660c7a8bb22d)

<p markdown="0"><em>Figure 7. Bridge $\varepsilon^{\mathrm{e}}_{\mathrm{xx}}$ across the span (µε).</em></p>

The profile follows $y=0$ and $z=17.75$ mm over $x\in[-10.5,10.5]$ mm. Experimental points and their reported error bars follow Ganeriwala et al. (2019). Opt-IS captures the broad tensile region but not the higher measured strain near the right end. The confidence level of the reported error bars is unspecified.

[Download the figure PDF](/assets/pdf/cases/bridge/axial-strain-profile.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Vertical-line xx elastic strain

<div class="rsh-case-figure-content" markdown="1">

![Bridge xx elastic strain along the vertical sampling line.](/assets/img/cases/bridge/x3p75.png?v=ff23235c7de8)

<p markdown="0"><em>Figure 8. Bridge $\varepsilon^{\mathrm{e}}_{\mathrm{xx}}$ along the vertical line (µε).</em></p>

The line is at global $x=-6.75$ mm and $y=0$, over $z=10$–19 mm. The plotted height is $z_{\mathrm{local}}=z-10$ mm. The filename label “3.75” refers to the local horizontal position $x+10.5$, rather than a global $x=3.75$ mm plane. The curves compare Opt-IS, MIS, DIS, the supplied reference simulation, and experimental data.

[Download the figure PDF](/assets/pdf/cases/bridge/x3p75.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Vertical-line zz elastic strain

<div class="rsh-case-figure-content" markdown="1">

![Bridge zz elastic strain along the vertical sampling line.](/assets/img/cases/bridge/z3p75.png?v=9c781ac171a9)

<p markdown="0"><em>Figure 9. Bridge $\varepsilon^{\mathrm{e}}_{\mathrm{zz}}$ along the vertical line (µε).</em></p>

The line is at global $x=-6.75$ mm and $y=0$, over $z=10$–19 mm. The plotted height is $z_{\mathrm{local}}=z-10$ mm. The filename label “3.75” refers to the local horizontal position $x+10.5$, rather than a global $x=3.75$ mm plane. The curves compare Opt-IS, MIS, DIS, the supplied reference simulation, and experimental data.

[Download the figure PDF](/assets/pdf/cases/bridge/z3p75.pdf)

</div>

</figure>

</div>

---

**Reference:**

<span id="reference-1"></span>

[1] Ganeriwala, R.K., Strantza, M., King, W.E., Clausen, B., Phan, T.Q., Levine, L.E., Brown, D.W., Hodge, N.E. (2019). Evaluation of a thermomechanical model for prediction of residual stress during laser powder bed fusion of Ti-6Al-4V. _Additive Manufacturing_, **27**, 489–502. [https://doi.org/10.1016/j.addma.2019.03.034](https://doi.org/10.1016/j.addma.2019.03.034).
