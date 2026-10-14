---
layout: page
title: Thin-wall (WAAM)
card_title: "Thin-wall (WAAM · S355)"
description: This is a four-layer S355 steel thin-wall model. The thermal–mechanical analysis follows successive line scans and cooling stages, then
  releases the specified anchors to calculate springback. A separate 20-layer configuration is also available.
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

This is a four-layer S355 steel thin-wall model. The thermal–mechanical analysis follows successive line scans and cooling stages, then releases the specified anchors to calculate springback. A separate 20-layer configuration is also available.

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

| Parameter                           | Value                                | Unit / description                    |
| ----------------------------------- | ------------------------------------ | ------------------------------------- |
| Manufacturing process               | WAAM                                 | —                                     |
| Material                            | S355                                 | Deposit / substrate if different      |
| Heat-source power, P                | 2245                                 | W                                     |
| Scan speed, v                       | 8.33                                 | mm/s                                  |
| Physical deposition layer thickness | 2                                    | mm                                    |
| Hatch spacing                       | Not applicable — one track per layer | —                                     |
| Absorption efficiency               | 0.78                                 | Dimensionless                         |
| Heat-source model                   | Goldak double ellipsoid              | Volumetric heat source                |
| Heat-source radii                   | 2 / 6 / 2.5 / 3                      | mm; front / rear / transverse / depth |
| Cooling interval                    | 400                                  | s after each deposited layer          |

_Printing and heat-source values describe the supplied simulation configuration._

### Simulation parameters

| Parameter                            | Value / setting                                                                              | Unit / description                      |
| ------------------------------------ | -------------------------------------------------------------------------------------------- | --------------------------------------- |
| Initial / ambient temperature        | 25 / 25                                                                                      | °C                                      |
| High-temperature material model      | Complete temperature-dependent tables below; linear interpolation with endpoint holds        | —                                       |
| S355 properties evaluated at 20 °C   | E = 206 GPa; ν = 0.29; $\sigma_{\mathrm{y}}$ = 450 MPa; H = 7 GPa; $\sigma_{\max}$ = 520 MPa | From the same thermal–mechanical tables |
| Identified inherent strain           | Not used — this case uses full thermal–mechanical analysis                                   | —                                       |
| Thermal strain reference temperature | 20                                                                                           | °C                                      |
| Thermal strain cutoff                | No explicit cutoff configured                                                                | —                                       |

The material grade is S355. The supplied configuration identifies this material as `thin_wall_steel`.

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

Every configured temperature node is listed below, with exact conversion from K to °C. Each property is linearly interpolated within its own table and held at its nearest endpoint outside that range.

#### S355 — upper region and lower region

| Parameter            | Value   | Unit          |
| -------------------- | ------- | ------------- |
| Density              | 7860    | kg/m³         |
| Latent heat          | 0       | J/kg          |
| Solidus temperature  | 1273.15 | K             |
| Liquidus temperature | 1274.15 | K             |
| Maximum yield factor | 1       | Dimensionless |

##### Thermal conductivity

| Temperature (°C) | Temperature (K) | Thermal conductivity (W/(m·K)) |
| ---------------- | --------------- | ------------------------------ |
| 0                | 273.15          | 48.6                           |
| 700              | 973.15          | 48.6                           |

##### Specific heat capacity

| Temperature (°C) | Temperature (K) | Specific heat capacity (J/(kg·K)) |
| ---------------- | --------------- | --------------------------------- |
| 0                | 273.15          | 496                               |
| 700              | 973.15          | 496                               |

##### Young’s modulus

| Temperature (°C) | Temperature (K) | Young’s modulus (GPa) |
| ---------------- | --------------- | --------------------- |
| 20               | 293.15          | 206                   |
| 100              | 373.15          | 203                   |
| 200              | 473.15          | 201                   |
| 300              | 573.15          | 200                   |
| 400              | 673.15          | 165                   |
| 500              | 773.15          | 100                   |
| 600              | 873.15          | 60                    |
| 700              | 973.15          | 40                    |
| 800              | 1073.15         | 30                    |
| 900              | 1173.15         | 20                    |
| 1000             | 1273.15         | 10                    |

##### Thermal expansion coefficient

| Temperature (°C) | Temperature (K) | Thermal expansion coefficient (µm/(m·K)) |
| ---------------- | --------------- | ---------------------------------------- |
| 20               | 293.15          | 12                                       |
| 100              | 373.15          | 12                                       |
| 200              | 473.15          | 12                                       |
| 300              | 573.15          | 12                                       |
| 400              | 673.15          | 12                                       |
| 500              | 773.15          | 12                                       |
| 600              | 873.15          | 12                                       |
| 700              | 973.15          | 12                                       |
| 800              | 1073.15         | 12                                       |
| 900              | 1173.15         | 12                                       |
| 1000             | 1273.15         | 15                                       |

##### Poisson ratio

| Temperature (°C) | Temperature (K) | Poisson ratio (Dimensionless) |
| ---------------- | --------------- | ----------------------------- |
| 20               | 293.15          | 0.29                          |
| 100              | 373.15          | 0.29                          |
| 200              | 473.15          | 0.295                         |
| 300              | 573.15          | 0.295                         |
| 400              | 673.15          | 0.3                           |
| 500              | 773.15          | 0.3                           |
| 600              | 873.15          | 0.32                          |
| 700              | 973.15          | 0.32                          |
| 800              | 1073.15         | 0.35                          |
| 900              | 1173.15         | 0.35                          |
| 1000             | 1273.15         | 0.39                          |

##### Initial yield stress

| Temperature (°C) | Temperature (K) | Initial yield stress (MPa) |
| ---------------- | --------------- | -------------------------- |
| 20               | 293.15          | 450                        |
| 100              | 373.15          | 450                        |
| 200              | 473.15          | 420                        |
| 300              | 573.15          | 390                        |
| 400              | 673.15          | 320                        |
| 500              | 773.15          | 260                        |
| 600              | 873.15          | 170                        |
| 700              | 973.15          | 60                         |
| 800              | 1073.15         | 50                         |
| 900              | 1173.15         | 50                         |
| 1000             | 1273.15         | 50                         |

##### Hardening modulus

| Temperature (°C) | Temperature (K) | Hardening modulus (GPa) |
| ---------------- | --------------- | ----------------------- |
| 20               | 293.15          | 7                       |
| 100              | 373.15          | 7                       |
| 200              | 473.15          | 8                       |
| 300              | 573.15          | 6                       |
| 400              | 673.15          | 5                       |
| 500              | 773.15          | 4                       |
| 600              | 873.15          | 4.5                     |
| 700              | 973.15          | 4                       |
| 800              | 1073.15         | 3                       |
| 900              | 1173.15         | 0                       |
| 1000             | 1273.15         | 0                       |

##### Maximum yield stress

| Temperature (°C) | Temperature (K) | Maximum yield stress (MPa) |
| ---------------- | --------------- | -------------------------- |
| 20               | 293.15          | 520                        |
| 100              | 373.15          | 520                        |
| 200              | 473.15          | 500                        |
| 300              | 573.15          | 420                        |
| 400              | 673.15          | 370                        |
| 500              | 773.15          | 300                        |
| 600              | 873.15          | 215                        |
| 700              | 973.15          | 100                        |
| 800              | 1073.15         | 80                         |
| 900              | 1173.15         | 50                         |
| 1000             | 1273.15         | 50                         |

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

_Figure 4. X-direction strain histories._

[YY strain history](/assets/img/cases/thin-wall/strain-yy-history.png) · [ZZ strain history](/assets/img/cases/thin-wall/strain-zz-history.png) · [Download the history CSV](/assets/data/cases/thin-wall/thermal-mechanical-history.csv)

</div>

</figure>

</div>

### Springback after release

The saved maximum springback magnitude is **3.246338 mm**. At that node, the vertical component is **3.242710 mm**. This is a numerical springback result after releasing the configured anchors.

[Download springback samples](/assets/data/cases/thin-wall/springback-summary.csv)

---

**Data sources:** Supplied simulation inputs and saved solver outputs. Complete physical settings and temperature-dependent values are available in the YAML, JSON, and CSV downloads above.
