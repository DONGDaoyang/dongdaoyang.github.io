---
layout: page
title: "Thin-wall (WAAM · S355)"
card_title: "Thin-wall (WAAM · S355)"
description: This is a four-layer S355 steel thin-wall model. The thermal–mechanical analysis follows successive line scans and cooling stages, then
  releases the specified anchors to calculate springback.
permalink: /benchmarks/thin-wall/
hub_case: true
published: true
importance: 2
case_type: Computational case
img: /assets/img/cases/thin-wall/results-cover.png
image_alt: Thin-wall saved simulation stress result.
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

This is a four-layer S355 steel thin-wall model. The thermal–mechanical analysis follows successive line scans and cooling stages, then releases the specified anchors to calculate springback.

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Geometry and dimensions.](/assets/img/cases/thin-wall/geometry-overview.png)

_Figure 1. Geometry and dimensions._

[Download the original geometry PDF](/assets/pdf/cases/thin-wall/geometry-overview.pdf)

</div>

</figure>

</div>

## Problem set

### Printing parameters

| Parameter                                                         | Value           | Unit |
| ----------------------------------------------------------------- | --------------- | ---- |
| Manufacturing process                                             | WAAM            | —    |
| Material                                                          | S355            | —    |
| Heat-source power, $P$                                            | 2245            | W    |
| Scan speed, $V$                                                   | 8.33            | mm/s |
| Physical deposition layer thickness                               | 2               | mm   |
| Hatch spacing                                                     | N/A             | —    |
| Absorption efficiency                                             | 0.78            | —    |
| Goldak heat-source dimensions (front / rear / transverse / depth) | 2 / 6 / 2.5 / 3 | mm   |
| Cooling interval (after each deposited layer)                     | 400             | s    |

### Simulation parameters

| Parameter                            | Value / setting                                                         | Unit              |
| ------------------------------------ | ----------------------------------------------------------------------- | ----------------- |
| Ambient temperature                  | 25                                                                      | °C                |
| High-temperature material model      | See tables below                                                        | —                 |
| S355 elastic parameters (20 °C)      | $E$ = 206<br>$\nu$ = 0.29                                               | GPa<br>—          |
| S355 plastic parameters (20 °C)      | $\sigma_{\mathrm{y}}$ = 450<br>$H$ = 7<br>$\sigma_{\mathrm{max}}$ = 520 | MPa<br>GPa<br>MPa |
| Identified inherent strain           | Not used — this case uses full thermal–mechanical analysis              | —                 |
| Thermal strain reference temperature | 20                                                                      | °C                |
| Thermal strain cutoff                | No explicit cutoff configured                                           | —                 |

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

The S355 thermal and temperature-dependent mechanical parameters used in this simulation are adapted from Qi et al., supplementary Tables S2–S3 <a href="#reference-1">[1]</a>.

#### S355 — upper region and lower region

| Parameter                              | Value   | Unit  |
| -------------------------------------- | ------- | ----- |
| Density, $\rho$                        | 7860    | kg/m³ |
| Latent heat, $L$                       | 0       | J/kg  |
| Solidus temperature, $T_{\mathrm{s}}$  | 1273.15 | K     |
| Liquidus temperature, $T_{\mathrm{l}}$ | 1274.15 | K     |
| Maximum yield factor                   | 1       | —     |

##### Thermal conductivity, $k$

| $T$ (°C) | Thermal conductivity, $k$ (W/(m·K)) |
| -------- | ----------------------------------- |
| 0        | 48.6                                |
| 700      | 48.6                                |

##### Specific heat capacity, $C_{\mathrm{p}}$

| $T$ (°C) | Specific heat capacity, $C_{\mathrm{p}}$ (J/(kg·K)) |
| -------- | --------------------------------------------------- |
| 0        | 496                                                 |
| 700      | 496                                                 |

##### Young’s modulus, $E$

| $T$ (°C) | Young’s modulus, $E$ (GPa) |
| -------- | -------------------------- |
| 20       | 206                        |
| 100      | 203                        |
| 200      | 201                        |
| 300      | 200                        |
| 400      | 165                        |
| 500      | 100                        |
| 600      | 60                         |
| 700      | 40                         |
| 800      | 30                         |
| 900      | 20                         |
| 1000     | 10                         |

##### Thermal expansion coefficient, $\alpha$

| $T$ (°C) | Thermal expansion coefficient, $\alpha$ (µm/(m·K)) |
| -------- | -------------------------------------------------- |
| 20       | 12                                                 |
| 100      | 12                                                 |
| 200      | 12                                                 |
| 300      | 12                                                 |
| 400      | 12                                                 |
| 500      | 12                                                 |
| 600      | 12                                                 |
| 700      | 12                                                 |
| 800      | 12                                                 |
| 900      | 12                                                 |
| 1000     | 15                                                 |

##### Poisson ratio, $\nu$

| $T$ (°C) | Poisson ratio, $\nu$ (—) |
| -------- | ------------------------ |
| 20       | 0.29                     |
| 100      | 0.29                     |
| 200      | 0.295                    |
| 300      | 0.295                    |
| 400      | 0.3                      |
| 500      | 0.3                      |
| 600      | 0.32                     |
| 700      | 0.32                     |
| 800      | 0.35                     |
| 900      | 0.35                     |
| 1000     | 0.39                     |

##### Initial yield stress, $\sigma_{\mathrm{y}}$

| $T$ (°C) | Initial yield stress, $\sigma_{\mathrm{y}}$ (MPa) |
| -------- | ------------------------------------------------- |
| 20       | 450                                               |
| 100      | 450                                               |
| 200      | 420                                               |
| 300      | 390                                               |
| 400      | 320                                               |
| 500      | 260                                               |
| 600      | 170                                               |
| 700      | 60                                                |
| 800      | 50                                                |
| 900      | 50                                                |
| 1000     | 50                                                |

##### Hardening modulus, $H$

| $T$ (°C) | Hardening modulus, $H$ (GPa) |
| -------- | ---------------------------- |
| 20       | 7                            |
| 100      | 7                            |
| 200      | 8                            |
| 300      | 6                            |
| 400      | 5                            |
| 500      | 4                            |
| 600      | 4.5                          |
| 700      | 4                            |
| 800      | 3                            |
| 900      | 0                            |
| 1000     | 0                            |

##### Maximum yield stress, $\sigma_{\mathrm{max}}$

| $T$ (°C) | Maximum yield stress, $\sigma_{\mathrm{max}}$ (MPa) |
| -------- | --------------------------------------------------- |
| 20       | 520                                                 |
| 100      | 520                                                 |
| 200      | 500                                                 |
| 300      | 420                                                 |
| 400      | 370                                                 |
| 500      | 300                                                 |
| 600      | 215                                                 |
| 700      | 100                                                 |
| 800      | 80                                                  |
| 900      | 50                                                  |
| 1000     | 50                                                  |

The phase-change settings are numerical model inputs: latent heat is zero and the configured solidus / liquidus are 1273.15 / 1274.15 K. They are not claimed as measured steel melting temperatures.

</details>

[Download full parameter JSON](/assets/data/cases/thin-wall/thermal-parameters.json) · [Download temperature-dependent CSV](/assets/data/cases/thin-wall/temperature-dependent-properties.csv) · [Download simulation YAML](/assets/data/cases/thin-wall/simulation-parameters.yaml)

[Download the separate 20-layer YAML](/assets/data/cases/thin-wall/simulation-20-layer.yaml)

## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

### Residual stress field

<div class="rsh-case-figure-content" markdown="1">

![Residual stress field.](/assets/img/cases/thin-wall/results-cover.png)

_Figure 2. Residual stress field._

[Download the stress-field figure](/assets/pdf/cases/thin-wall/results-cover.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Temperature and strain histories

<div class="rsh-case-figure-content" markdown="1">

![Temperature history.](/assets/img/cases/thin-wall/temperature-history.png)

_Figure 3. Temperature history._

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![X-direction strain histories.](/assets/img/cases/thin-wall/strain-xx-history.png)

_Figure 4. $X$-direction strain histories._

[$Y$-direction strain history](/assets/img/cases/thin-wall/strain-yy-history.png) · [$Z$-direction strain history](/assets/img/cases/thin-wall/strain-zz-history.png) · [Download the history CSV](/assets/data/cases/thin-wall/thermal-mechanical-history.csv)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Vertical displacement after release

<div class="rsh-case-figure-content" markdown="1">

![Vertical displacement after release.](/assets/img/cases/thin-wall/thin_wall_displacement_comparison.png?v=71ab55f09e5e)

_Figure 5. Vertical displacement after release._

[Download the figure PDF](/assets/pdf/cases/thin-wall/thin_wall_displacement_comparison.pdf)

</div>

</figure>

</div>

### Springback after release

The maximum springback magnitude is **3.246338 mm**, with a vertical component of **3.242710 mm** at that node.

[Download springback samples](/assets/data/cases/thin-wall/springback-summary.csv)

---

**Reference:**

<span id="reference-1"></span>

[1] Qi, J., Liu, X., Dong, P., Li, Q., Yang, Y. (2025). An improved dynamic inherent strain method for efficient prediction of residual stresses and deformations in metal additive manufacturing. _Additive Manufacturing_, **114**, 105025. [https://doi.org/10.1016/j.addma.2025.105025](https://doi.org/10.1016/j.addma.2025.105025).
