---
layout: page
title: "Single track (DED · IN718 / Ti-6Al-4V)"
card_title: "Single track (DED · IN718 / Ti-6Al-4V)"
description: This is a single-track laser-deposition model with an IN718 track on a Ti-6Al-4V substrate. The thermal–mechanical analysis follows
  one 40 mm scan and the subsequent cooling stage to calculate residual stress.
permalink: /benchmarks/single-track/
hub_case: true
published: true
importance: 1
case_type: Computational case
img: /assets/img/cases/single_track/single-track-results.png?v=bc443dc64c1a
image_alt: Single track residual stress.
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

This is a single-track laser-deposition model with an IN718 track on a Ti-6Al-4V substrate. The thermal–mechanical analysis follows one 40 mm scan and the subsequent cooling stage to calculate residual stress. <a href="#reference-1">[1]</a>

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Geometry and dimensions.](/assets/img/cases/single_track/geometry-overview.png)

_Figure 1. Geometry and dimensions._

[Download the original geometry PDF](/assets/pdf/cases/single_track/geometry-overview.pdf)

</div>

</figure>

</div>

## Problem set

### Printing parameters

| Parameter                                                         | Value                 | Unit |
| ----------------------------------------------------------------- | --------------------- | ---- |
| Manufacturing process                                             | DED                   | —    |
| Material (deposit / substrate)                                    | IN718 / Ti-6Al-4V     | —    |
| Heat-source power, $P$                                            | 600                   | W    |
| Scan speed, $V$                                                   | 6                     | mm/s |
| Physical deposition layer thickness                               | 0.67                  | mm   |
| Hatch spacing                                                     | N/A                   | —    |
| Absorption efficiency                                             | 0.4                   | —    |
| Goldak heat-source dimensions (front / rear / transverse / depth) | 0.8 / 0.8 / 0.8 / 0.8 | mm   |
| Cooling interval (after each deposited layer)                     | 200                   | s    |

### Simulation parameters

| Parameter                            | Value / setting                                                              | Unit              |
| ------------------------------------ | ---------------------------------------------------------------------------- | ----------------- |
| Ambient temperature                  | 25                                                                           | °C                |
| High-temperature material model      | See tables below                                                             | —                 |
| IN718 elastic parameters (20 °C)     | $E$ = 156.3<br>$\nu$ = 0.3                                                   | GPa<br>—          |
| IN718 plastic parameters (20 °C)     | $\sigma_{\mathrm{y}}$ = 308.9<br>$H$ = 1<br>$\sigma_{\mathrm{max}}$ = 370.68 | MPa<br>GPa<br>MPa |
| Ti-6Al-4V elastic parameters (20 °C) | $E$ = 125<br>$\nu$ = 0.34                                                    | GPa<br>—          |
| Ti-6Al-4V plastic parameters (20 °C) | $\sigma_{\mathrm{y}}$ = 955<br>$H$ = 0<br>$\sigma_{\mathrm{max}}$ = 1146     | MPa<br>GPa<br>MPa |
| Identified inherent strain           | Not used — this case uses full thermal–mechanical analysis                   | —                 |
| Thermal strain reference temperature | 20                                                                           | °C                |
| Thermal strain cutoff                | No explicit cutoff configured                                                | —                 |

The supplied drawing shows a 30 mm substrate width; the saved FE mesh spans 10 mm across $Y$. The result below uses the saved mesh.

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

The temperature-dependent material parameters used in this thermal–mechanical simulation are taken from Liao et al., Tables 2–3 <a href="#reference-1">[1]</a>.

#### IN718 — upper region

| Parameter                              | Value  | Unit  |
| -------------------------------------- | ------ | ----- |
| Density, $\rho$                        | 8190   | kg/m³ |
| Latent heat, $L$                       | 286000 | J/kg  |
| Solidus temperature, $T_{\mathrm{s}}$  | 1533   | K     |
| Liquidus temperature, $T_{\mathrm{l}}$ | 1609   | K     |
| Maximum yield factor                   | 1.2    | —     |

##### Thermal conductivity, $k$

| $T$ (K) | $T$ (°C) | Thermal conductivity, $k$ (W/(m·K)) |
| ------- | -------- | ----------------------------------- |
| 298     | 24.85    | 8.93                                |
| 373     | 99.85    | 10.8                                |
| 473     | 199.85   | 12.9                                |
| 573     | 299.85   | 15.2                                |
| 673     | 399.85   | 17.4                                |
| 773     | 499.85   | 18.7                                |
| 873     | 599.85   | 20.8                                |
| 973     | 699.85   | 21.9                                |
| 1073    | 799.85   | 26.9                                |
| 1173    | 899.85   | 25.8                                |
| 1273    | 999.85   | 26.7                                |
| 1373    | 1099.85  | 28.3                                |
| 1443    | 1169.85  | 29.3                                |
| 1609    | 1335.85  | 29.6                                |

##### Specific heat capacity, $C_{\mathrm{p}}$

| $T$ (K) | $T$ (°C) | Specific heat capacity, $C_{\mathrm{p}}$ (J/(kg·K)) |
| ------- | -------- | --------------------------------------------------- |
| 298     | 24.85    | 435                                                 |
| 373     | 99.85    | 455                                                 |
| 473     | 199.85   | 479                                                 |
| 573     | 299.85   | 497                                                 |
| 673     | 399.85   | 515                                                 |
| 773     | 499.85   | 527                                                 |
| 873     | 599.85   | 558                                                 |
| 973     | 699.85   | 568                                                 |
| 1073    | 799.85   | 680                                                 |
| 1173    | 899.85   | 640                                                 |
| 1273    | 999.85   | 620                                                 |
| 1373    | 1099.85  | 640                                                 |
| 1443    | 1169.85  | 650                                                 |
| 1609    | 1335.85  | 720                                                 |

##### Young’s modulus, $E$

| $T$ (K) | $T$ (°C) | Young’s modulus, $E$ (GPa) |
| ------- | -------- | -------------------------- |
| 300     | 26.85    | 156.3                      |
| 367     | 93.85    | 151.8                      |
| 478     | 204.85   | 144.9                      |
| 589     | 315.85   | 138                        |
| 700     | 426.85   | 131.4                      |
| 811     | 537.85   | 124.7                      |
| 923     | 649.85   | 124                        |
| 1033    | 759.85   | 123.4                      |
| 1144    | 870.85   | 107.7                      |
| 1255    | 981.85   | 92.05                      |
| 1367    | 1093.85  | 68.95                      |
| 1672    | 1398.85  | 23.79                      |

##### Thermal expansion coefficient, $\alpha$

| $T$ (K) | $T$ (°C) | Thermal expansion coefficient, $\alpha$ (µm/(m·K)) |
| ------- | -------- | -------------------------------------------------- |
| 300     | 26.85    | 11.7                                               |
| 478     | 204.85   | 12.8                                               |
| 589     | 315.85   | 13.4                                               |
| 923     | 649.85   | 14.6                                               |
| 1033    | 759.85   | 15.1                                               |
| 1144    | 870.85   | 15.7                                               |
| 1367    | 1093.85  | 16.6                                               |
| 1672    | 1398.85  | 16.6                                               |

##### Poisson ratio, $\nu$

| $T$ (K) | $T$ (°C) | Poisson ratio, $\nu$ (—) |
| ------- | -------- | ------------------------ |
| 300     | 26.85    | 0.3                      |
| 367     | 93.85    | 0.3                      |
| 478     | 204.85   | 0.3                      |
| 589     | 315.85   | 0.3                      |
| 700     | 426.85   | 0.3                      |
| 811     | 537.85   | 0.3                      |
| 923     | 649.85   | 0.3                      |
| 1033    | 759.85   | 0.3                      |
| 1144    | 870.85   | 0.3                      |
| 1255    | 981.85   | 0.3                      |
| 1367    | 1093.85  | 0.3                      |
| 1672    | 1398.85  | 0.3                      |

##### Initial yield stress, $\sigma_{\mathrm{y}}$

| $T$ (K) | $T$ (°C) | Initial yield stress, $\sigma_{\mathrm{y}}$ (MPa) |
| ------- | -------- | ------------------------------------------------- |
| 300     | 26.85    | 308.9                                             |
| 589     | 315.85   | 246.3                                             |
| 811     | 537.85   | 226.1                                             |
| 1033    | 759.85   | 207.7                                             |
| 1255    | 981.85   | 114                                               |

##### Hardening modulus, $H$

| $T$ (K) | $T$ (°C) | Hardening modulus, $H$ (GPa) |
| ------- | -------- | ---------------------------- |
| 300     | 26.85    | 1                            |
| 589     | 315.85   | 1                            |
| 811     | 537.85   | 1                            |
| 1033    | 759.85   | 1                            |
| 1255    | 981.85   | 1                            |

Maximum yield stress, $\sigma_{\mathrm{max}}$, is $1.2\,\sigma_{\mathrm{y}}$ at each interpolated temperature.

#### Ti-6Al-4V — lower region

| Parameter                              | Value  | Unit  |
| -------------------------------------- | ------ | ----- |
| Density, $\rho$                        | 4400   | kg/m³ |
| Latent heat, $L$                       | 270000 | J/kg  |
| Solidus temperature, $T_{\mathrm{s}}$  | 1878   | K     |
| Liquidus temperature, $T_{\mathrm{l}}$ | 1928   | K     |
| Maximum yield factor                   | 1.2    | —     |

##### Thermal conductivity, $k$

| $T$ (K) | $T$ (°C) | Thermal conductivity, $k$ (W/(m·K)) |
| ------- | -------- | ----------------------------------- |
| 298     | 24.85    | 7                                   |
| 373     | 99.85    | 7.45                                |
| 473     | 199.85   | 8.75                                |
| 573     | 299.85   | 10.2                                |
| 673     | 399.85   | 11.4                                |
| 773     | 499.85   | 12.6                                |
| 873     | 599.85   | 14.2                                |
| 973     | 699.85   | 15.5                                |
| 1073    | 799.85   | 17.8                                |
| 1173    | 899.85   | 20.2                                |
| 1273    | 999.85   | 21                                  |
| 1373    | 1099.85  | 21                                  |
| 1473    | 1199.85  | 22.9                                |
| 1573    | 1299.85  | 23.7                                |
| 1673    | 1399.85  | 24.6                                |
| 1773    | 1499.85  | 25.8                                |
| 1873    | 1599.85  | 27                                  |
| 1923    | 1649.85  | 30.9                                |
| 1973    | 1699.85  | 34.6                                |

##### Specific heat capacity, $C_{\mathrm{p}}$

| $T$ (K) | $T$ (°C) | Specific heat capacity, $C_{\mathrm{p}}$ (J/(kg·K)) |
| ------- | -------- | --------------------------------------------------- |
| 298     | 24.85    | 546                                                 |
| 373     | 99.85    | 562                                                 |
| 473     | 199.85   | 584                                                 |
| 573     | 299.85   | 606                                                 |
| 673     | 399.85   | 629                                                 |
| 773     | 499.85   | 651                                                 |
| 873     | 599.85   | 673                                                 |
| 973     | 699.85   | 694                                                 |
| 1073    | 799.85   | 714                                                 |
| 1173    | 899.85   | 734                                                 |
| 1273    | 999.85   | 697                                                 |
| 1373    | 1099.85  | 660                                                 |
| 1473    | 1199.85  | 678                                                 |
| 1573    | 1299.85  | 696                                                 |
| 1673    | 1399.85  | 714                                                 |
| 1773    | 1499.85  | 732                                                 |
| 1873    | 1599.85  | 750                                                 |
| 1923    | 1649.85  | 795                                                 |
| 1973    | 1699.85  | 831                                                 |

##### Young’s modulus, $E$

| $T$ (K) | $T$ (°C) | Young’s modulus, $E$ (GPa) |
| ------- | -------- | -------------------------- |
| 300     | 26.85    | 125                        |
| 533     | 259.85   | 110                        |
| 589     | 315.85   | 100                        |
| 700     | 426.85   | 93                         |
| 755     | 481.85   | 80                         |
| 811     | 537.85   | 74                         |
| 923     | 649.85   | 55                         |
| 1073    | 799.85   | 27                         |
| 1098    | 824.85   | 22                         |
| 1123    | 849.85   | 18                         |
| 1573    | 1299.85  | 12                         |
| 1873    | 1599.85  | 9                          |

##### Thermal expansion coefficient, $\alpha$

| $T$ (K) | $T$ (°C) | Thermal expansion coefficient, $\alpha$ (µm/(m·K)) |
| ------- | -------- | -------------------------------------------------- |
| 300     | 26.85    | 8.78                                               |
| 533     | 259.85   | 9.83                                               |
| 589     | 315.85   | 10                                                 |
| 700     | 426.85   | 10.7                                               |
| 755     | 481.85   | 11.1                                               |
| 811     | 537.85   | 11.2                                               |
| 923     | 649.85   | 11.7                                               |
| 1073    | 799.85   | 12.2                                               |
| 1098    | 824.85   | 12.3                                               |
| 1123    | 849.85   | 12.4                                               |
| 1573    | 1299.85  | 13                                                 |
| 1873    | 1599.85  | 16.3                                               |

##### Poisson ratio, $\nu$

| $T$ (K) | $T$ (°C) | Poisson ratio, $\nu$ (—) |
| ------- | -------- | ------------------------ |
| 300     | 26.85    | 0.34                     |
| 533     | 259.85   | 0.34                     |
| 589     | 315.85   | 0.34                     |
| 700     | 426.85   | 0.34                     |
| 755     | 481.85   | 0.34                     |
| 811     | 537.85   | 0.34                     |
| 923     | 649.85   | 0.34                     |
| 1073    | 799.85   | 0.34                     |
| 1098    | 824.85   | 0.34                     |
| 1123    | 849.85   | 0.34                     |
| 1573    | 1299.85  | 0.34                     |
| 1873    | 1599.85  | 0.34                     |

##### Initial yield stress, $\sigma_{\mathrm{y}}$

| $T$ (K) | $T$ (°C) | Initial yield stress, $\sigma_{\mathrm{y}}$ (MPa) |
| ------- | -------- | ------------------------------------------------- |
| 300     | 26.85    | 955                                               |
| 573     | 299.85   | 836                                               |
| 773     | 499.85   | 732                                               |
| 1023    | 749.85   | 581                                               |
| 1073    | 799.85   | 547                                               |
| 1173    | 899.85   | 480                                               |
| 1273    | 999.85   | 405                                               |
| 1373    | 1099.85  | 330                                               |

##### Hardening modulus, $H$

| $T$ (K) | $T$ (°C) | Hardening modulus, $H$ (GPa) |
| ------- | -------- | ---------------------------- |
| 300     | 26.85    | 0                            |
| 573     | 299.85   | 0                            |
| 773     | 499.85   | 0                            |
| 1023    | 749.85   | 0                            |
| 1073    | 799.85   | 0                            |
| 1173    | 899.85   | 0                            |
| 1273    | 999.85   | 0                            |
| 1373    | 1099.85  | 0                            |

Maximum yield stress, $\sigma_{\mathrm{max}}$, is $1.2\,\sigma_{\mathrm{y}}$ at each interpolated temperature.

</details>

[Download full parameter JSON](/assets/data/cases/single_track/thermal-parameters.json) · [Download temperature-dependent CSV](/assets/data/cases/single_track/temperature-dependent-properties.csv) · [Download simulation YAML](/assets/data/cases/single_track/simulation-parameters.yaml)

## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

### Residual stress field

<div class="rsh-case-figure-content" markdown="1">

![Von Mises stress at Y = 0 mm.](/assets/img/cases/single_track/results-cover.png)

_Figure 2. Von Mises stress at $Y$ = 0 mm._

[Download the stress-field figure](/assets/pdf/cases/single_track/results-cover.pdf)

[Download all final cell stresses](/assets/data/cases/single_track/final-stress-cells.csv) · [Download stress-field metadata](/assets/data/cases/single_track/final-stress-metadata.json)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### X-direction stress comparison

<div class="rsh-case-figure-content" markdown="1">

![X-direction stress comparison.](/assets/img/cases/single_track/single_track_stress_xx_comparison.png?v=20df8276736a)

_Figure 3. $X$-direction stress comparison._

[Download the figure PDF](/assets/pdf/cases/single_track/single_track_stress_xx_comparison.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Z-direction stress comparison

<div class="rsh-case-figure-content" markdown="1">

![Z-direction stress comparison.](/assets/img/cases/single_track/single_track_stress_zz_comparison.png?v=c5212cb76553)

_Figure 4. $Z$-direction stress comparison._

[Download the figure PDF](/assets/pdf/cases/single_track/single_track_stress_zz_comparison.pdf)

</div>

</figure>

</div>

---

**Reference:**

<span id="reference-1"></span>

[1] Liao, S., Golgoon, A., Mozaffar, M., Cao, J. (2023). Efficient GPU-accelerated thermomechanical solver for residual stress prediction in additive manufacturing. _Computational Mechanics_, **71**, 879–893. [https://doi.org/10.1007/s00466-023-02273-3](https://doi.org/10.1007/s00466-023-02273-3).
