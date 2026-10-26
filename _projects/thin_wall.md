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
img: /assets/img/cases/thin-wall/results-cover.png?v=bd0e5d284a4f
image_alt: "Four-layer thin-wall axial stress after anchor release, in MPa."
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

This is a four-layer S355 steel thin-wall model. The thermal–mechanical analysis follows successive line scans and cooling stages, then releases the specified anchors to calculate springback. The original thin-wall benchmark and experimental results are reported by Ding et al. <a href="#reference-1">[1]</a>

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

The S355 thermal and temperature-dependent mechanical parameters used in this simulation are adapted from Qi et al., supplementary Tables S2–S3 <a href="#reference-2">[2]</a>.

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

### Axial stress after release

<div class="rsh-case-figure-content" markdown="1">

![Four-layer thin-wall axial stress after anchor release, in MPa.](/assets/img/cases/thin-wall/results-cover.png?v=bd0e5d284a4f)

<p markdown="0"><em>Figure 2. Four-layer wall: axial stress $\sigma_{\mathrm{xx}}$ after anchor release (MPa).</em></p>

The contour is plotted on the undeformed half-width simulation domain. Positive values indicate tension and negative values indicate compression. The two outer anchors have been released, while the central anchor and the $y=0$ symmetry constraint remain.

[Download the figure PDF](/assets/pdf/cases/thin-wall/results-cover.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Temperature history at Point 1

<div class="rsh-case-figure-content" markdown="1">

![Nonempty temperature-time comparison at thin-wall measurement Point 1.](/assets/img/cases/thin-wall/temperature-point-1.png?v=20a5c3f2102f)

<p markdown="0"><em>Figure 3. Four-layer wall: temperature history at Point 1, in °C versus time in seconds.</em></p>

The solid DNS curve is compared with the dashed experimental reference. Repeated peaks reflect successive deposition and cooling cycles. Point labels follow the supplied records. Measurement coordinates were not supplied, so no new spatial location is assigned to this point.

[Download the figure PDF](/assets/pdf/cases/thin-wall/temperature-point-1.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Temperature history at Point 2

<div class="rsh-case-figure-content" markdown="1">

![Nonempty temperature-time comparison at thin-wall measurement Point 2.](/assets/img/cases/thin-wall/temperature-point-2.png?v=3427ba3f0774)

<p markdown="0"><em>Figure 4. Four-layer wall: temperature history at Point 2, in °C versus time in seconds.</em></p>

The solid DNS curve is compared with the dashed experimental reference. Repeated peaks reflect successive deposition and cooling cycles. Point labels follow the supplied records. Measurement coordinates were not supplied, so no new spatial location is assigned to this point.

[Download the figure PDF](/assets/pdf/cases/thin-wall/temperature-point-2.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Temperature history at Point 3

<div class="rsh-case-figure-content" markdown="1">

![Nonempty temperature-time comparison at thin-wall measurement Point 3.](/assets/img/cases/thin-wall/temperature-point-3.png?v=4efdc6968524)

<p markdown="0"><em>Figure 5. Four-layer wall: temperature history at Point 3, in °C versus time in seconds.</em></p>

The solid DNS curve is compared with the dashed experimental reference. Repeated peaks reflect successive deposition and cooling cycles. Point labels follow the supplied records. Measurement coordinates were not supplied, so no new spatial location is assigned to this point.

[Download the figure PDF](/assets/pdf/cases/thin-wall/temperature-point-3.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Vertical displacement after release

<div class="rsh-case-figure-content" markdown="1">

![Total released vertical displacement along the four-layer wall compared with supplied reference and experimental curves.](/assets/img/cases/thin-wall/thin_wall_displacement_comparison.png?v=f5012f7fa5e0)

<p markdown="0"><em>Figure 6. Four-layer wall: total released vertical displacement $u_z$ (mm).</em></p>

The profile follows $y=z=0$, with $x_{\mathrm{plot}}=x+250$ mm spanning 0–500 mm. This is the total displacement after release, whereas the springback increment below is the change caused by releasing the anchors. The supplied reference-simulation curve duplicates Experiment 1 and is not independent validation evidence.

[Download the figure PDF](/assets/pdf/cases/thin-wall/thin_wall_displacement_comparison.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Twenty-layer residual stress

<div class="rsh-case-figure-content" markdown="1">

![Longitudinal residual stress along the height of a separate twenty-layer wall compared with measurements.](/assets/img/cases/thin-wall/20-layer-stress-comparison.png?v=2fd858a17fa8)

<p markdown="0"><em>Figure 7. Twenty-layer wall: longitudinal residual stress $\sigma_{\mathrm{xx}}$ along the 40 mm deposited height (MPa).</em></p>

This is the separate twenty-layer configuration after unclamping, rather than the four-layer thermal-history case above. The simulation is compared with the neutron-diffraction measurements and reported error bars of Ding et al. (2011). It captures the tensile-to-compressive trend with height, while local stress magnitudes remain overpredicted.

[Download the figure PDF](/assets/pdf/cases/thin-wall/20-layer-stress-comparison.pdf)

</div>

</figure>

</div>

### Springback after release

The maximum release-induced displacement increment is **3.246338 mm**, with a vertical component of **3.242710 mm** at that node. It measures the change between the states before and after release, rather than the total released displacement shown in the profile.

[Download springback samples](/assets/data/cases/thin-wall/springback-summary.csv)

---

**Reference:**

<span id="reference-1"></span>

[1] Ding, J., Colegrove, P., Mehnen, J., Ganguly, S., Sequeira Almeida, P.M., Wang, F., Williams, S. (2011). Thermo-mechanical analysis of Wire and Arc Additive Layer Manufacturing process on large multi-layer parts. _Computational Materials Science_, **50**, 3315–3322. [https://doi.org/10.1016/j.commatsci.2011.06.023](https://doi.org/10.1016/j.commatsci.2011.06.023).

<span id="reference-2"></span>

[2] Qi, J., Liu, X., Dong, P., Li, Q., Yang, Y. (2025). An improved dynamic inherent strain method for efficient prediction of residual stresses and deformations in metal additive manufacturing. _Additive Manufacturing_, **114**, 105025. [https://doi.org/10.1016/j.addma.2025.105025](https://doi.org/10.1016/j.addma.2025.105025).
