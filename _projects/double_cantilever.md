---
layout: page
title: Double-cantilever (LPBF)
card_title: "Double-cantilever (LPBF · IN718)"
description: This is the IN718 double-cantilever model. A local thermal–mechanical simulation is used to identify inherent strain, and the macro
  model calculates residual stress and warpage after releasing the left and right interfaces.
permalink: /benchmarks/double-cantilever/
hub_case: true
published: true
importance: 5
case_type: Computational case
img: /assets/img/cases/double_cantilever/results-cover.png
image_alt: Double-cantilever saved simulation stress result.
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

This is the IN718 double-cantilever model. A local thermal–mechanical simulation is used to identify inherent strain, and the macro model calculates residual stress and warpage after releasing the left and right interfaces.

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Geometry and dimensions.](/assets/img/cases/double_cantilever/geometry-overview.png)

_Figure 1. Geometry and dimensions._

[Download the original geometry PDF](/assets/pdf/cases/double_cantilever/geometry-overview.pdf)

</div>

</figure>

</div>

## Problem set

### Printing parameters

| Parameter                           | Value                   | Unit / description                    |
| ----------------------------------- | ----------------------- | ------------------------------------- |
| Manufacturing process               | LPBF                    | —                                     |
| Material                            | IN718                   | Deposit / substrate if different      |
| Heat-source power, P                | 285                     | W                                     |
| Scan speed, v                       | 960                     | mm/s                                  |
| Physical deposition layer thickness | 40                      | µm                                    |
| Hatch spacing                       | 110                     | µm                                    |
| Absorption efficiency               | 0.4                     | Dimensionless                         |
| Heat-source model                   | Goldak double ellipsoid | Volumetric heat source                |
| Heat-source radii                   | 50 / 50 / 50 / 125      | µm; front / rear / transverse / depth |
| Cooling interval                    | 200                     | s after each deposited layer          |

_Printing and heat-source values describe the supplied simulation configuration._

### Simulation parameters

| Parameter                                            | Value / setting                                                                       | Unit / description  |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------- |
| Initial / ambient temperature                        | 25 / 25                                                                               | °C                  |
| High-temperature material model                      | Complete temperature-dependent tables below; linear interpolation with endpoint holds | —                   |
| Room-temperature macro material model                | E = 208 GPa; ν = 0.3; σᵧ = 1172 MPa; H = 0 GPa; σₘₐₓ = 1172 MPa                       | Constant properties |
| Latest identified inherent strain, ε*xx = ε*yy       | -4.3393159636                                                                         | ‰                   |
| Latest identified inherent strain, ε\*zz             | 19.6471416585                                                                         | ‰                   |
| Inherent strain in the displayed archived comparison | ε*xx = ε*yy = -4.67214412919; ε\*zz = 15.5203097174                                   | ‰                   |
| Macro layer activation                               | 36 × 0.515                                                                            | Layers × mm         |
| Macro constraints and release                        | macro fixed plane Z = 10 mm; release left and right interfaces at Z = 32.2 mm         | —                   |
| Thermal strain reference temperature                 | 25                                                                                    | °C                  |
| Thermal strain cutoff                                | solidus                                                                               | —                   |

This page uses the IN718 dc case. The separate Ti-6Al-4V dc2 case is not combined with this geometry. The physical print layer is 40 µm; macro activation uses a 515 µm pitch.

The latest saved identification and the displayed archived comparison are listed separately. The plotted curves and their reference frames are retained from the saved figures.

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

Every configured temperature node is listed below, with exact conversion from K to °C. Each property is linearly interpolated within its own table and held at its nearest endpoint outside that range.

#### IN718 — upper region and lower region

| Parameter            | Value  | Unit          |
| -------------------- | ------ | ------------- |
| Density              | 8146   | kg/m³         |
| Latent heat          | 286000 | J/kg          |
| Solidus temperature  | 1533   | K             |
| Liquidus temperature | 1609   | K             |
| Maximum yield factor | 1      | Dimensionless |

##### Thermal conductivity

| Temperature (°C) | Temperature (K) | Thermal conductivity (W/(m·K)) |
| ---------------- | --------------- | ------------------------------ |
| 20               | 293.15          | 11.4                           |
| 100              | 373.15          | 12.5                           |
| 300              | 573.15          | 14                             |
| 500              | 773.15          | 15.5                           |
| 700              | 973.15          | 21.5                           |
| 1350             | 1623.15         | 31.3                           |

##### Specific heat capacity

| Temperature (°C) | Temperature (K) | Specific heat capacity (J/(kg·K)) |
| ---------------- | --------------- | --------------------------------- |
| 20               | 293.15          | 427                               |
| 100              | 373.15          | 441                               |
| 300              | 573.15          | 481                               |
| 500              | 773.15          | 521                               |
| 700              | 973.15          | 601                               |
| 1350             | 1623.15         | 691                               |

##### Young’s modulus

| Temperature (°C) | Temperature (K) | Young’s modulus (GPa) |
| ---------------- | --------------- | --------------------- |
| 21               | 294.15          | 208                   |
| 93               | 366.15          | 205                   |
| 204              | 477.15          | 202                   |
| 316              | 589.15          | 194                   |
| 427              | 700.15          | 186                   |
| 538              | 811.15          | 179                   |
| 649              | 922.15          | 172                   |
| 760              | 1033.15         | 162                   |
| 871              | 1144.15         | 127                   |
| 954              | 1227.15         | 17.8                  |

##### Thermal expansion coefficient

| Temperature (°C) | Temperature (K) | Thermal expansion coefficient (µm/(m·K)) |
| ---------------- | --------------- | ---------------------------------------- |
| 21               | 294.15          | 12.8                                     |
| 93               | 366.15          | 12.8                                     |
| 204              | 477.15          | 13.5                                     |
| 316              | 589.15          | 13.9                                     |
| 427              | 700.15          | 14.2                                     |
| 538              | 811.15          | 14.4                                     |
| 649              | 922.15          | 15.1                                     |
| 760              | 1033.15         | 16.1                                     |
| 954              | 1227.15         | 16.2                                     |

##### Poisson ratio

| Temperature (°C) | Temperature (K) | Poisson ratio (Dimensionless) |
| ---------------- | --------------- | ----------------------------- |
| 21               | 294.15          | 0.3                           |
| 1350             | 1623.15         | 0.3                           |

##### Initial yield stress

| Temperature (°C) | Temperature (K) | Initial yield stress (MPa) |
| ---------------- | --------------- | -------------------------- |
| 21               | 294.15          | 1172                       |
| 93               | 366.15          | 1172                       |
| 427              | 700.15          | 1089                       |
| 538              | 811.15          | 1068                       |
| 649              | 922.15          | 1034                       |
| 760              | 1033.15         | 827                        |
| 871              | 1144.15         | 286                        |
| 954              | 1227.15         | 138                        |

##### Hardening modulus

| Temperature (°C) | Temperature (K) | Hardening modulus (GPa) |
| ---------------- | --------------- | ----------------------- |
| 21               | 294.15          | 0                       |
| 93               | 366.15          | 0                       |
| 427              | 700.15          | 0                       |
| 538              | 811.15          | 0                       |
| 649              | 922.15          | 0                       |
| 760              | 1033.15         | 0                       |
| 871              | 1144.15         | 0                       |
| 954              | 1227.15         | 0                       |

Maximum yield stress is 1 × the interpolated initial yield stress.

The local IN718 model uses zero hardening modulus and a maximum-yield factor of 1. The phase-change values are retained model inputs, separate from the temperature-dependent mechanical tables.

</details>

[Download full parameter JSON](/assets/data/cases/double_cantilever/thermal-parameters.json) · [Download temperature-dependent CSV](/assets/data/cases/double_cantilever/temperature-dependent-properties.csv) · [Download simulation YAML](/assets/data/cases/double_cantilever/simulation-parameters.yaml)

[Download macro configuration](/assets/data/cases/double_cantilever/macro-parameters.yaml) · [Download identification results](/assets/data/cases/double_cantilever/identification-results.json)

## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

### Residual stress field

<div class="rsh-case-figure-content" markdown="1">

![Residual stress field.](/assets/img/cases/double_cantilever/results-cover.png)

_Figure 2. Residual stress field._

[Download the stress-field figure](/assets/pdf/cases/double_cantilever/results-cover.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Temperature and strain histories

<div class="rsh-case-figure-content" markdown="1">

![X-, Y- and Z-direction strain histories.](/assets/img/cases/double_cantilever/thermal-history.png)

_Figure 3. X-, Y- and Z-direction strain histories._

[Download all local history pages](/assets/pdf/cases/double_cantilever/thermal-history.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Inherent-strain identification

<div class="rsh-case-figure-content" markdown="1">

![Stress and elastic strain comparison.](/assets/img/cases/double_cantilever/optimization-agreement.png)

_Figure 4. Stress and elastic strain comparison._

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Residual stress field comparison.](/assets/img/cases/double_cantilever/optimization-agreement-page-2.png)

_Figure 5. Residual stress field comparison._

[Download all comparison pages](/assets/pdf/cases/double_cantilever/optimization-agreement.pdf) · [Download the error metrics](/assets/data/cases/double_cantilever/optimization-metrics.csv)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Warpage after release

<div class="rsh-case-figure-content" markdown="1">

![Vertical displacement after release.](/assets/img/cases/double_cantilever/warpage.png)

_Figure 6. Vertical displacement after release._

[Download the warpage figure](/assets/pdf/cases/double_cantilever/warpage.pdf) · [Download displacement samples](/assets/data/cases/double_cantilever/warpage.csv)

</div>

</figure>

</div>

---

**Data sources:** Supplied simulation inputs and saved solver outputs. Complete physical settings and temperature-dependent values are available in the YAML, JSON, and CSV downloads above.
