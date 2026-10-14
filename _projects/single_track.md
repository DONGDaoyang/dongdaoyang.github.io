---
layout: page
title: Single track (DED)
card_title: "Single track (DED · IN718 / Ti-6Al-4V)"
description: This is a single-track laser-deposition model with an IN718 track on a Ti-6Al-4V substrate. The thermal–mechanical analysis follows
  one 40 mm scan and the subsequent cooling stage to calculate residual stress.
permalink: /benchmarks/single-track/
hub_case: true
published: true
importance: 1
case_type: Computational case
img: /assets/img/cases/single_track/single-track-results.png?v=bc443dc64c1a
image_alt: Single track stress result from the supplied single_track_results figure.
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

This is a single-track laser-deposition model with an IN718 track on a Ti-6Al-4V substrate. The thermal–mechanical analysis follows one 40 mm scan and the subsequent cooling stage to calculate residual stress.

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

| Parameter                           | Value                                | Unit / description                    |
| ----------------------------------- | ------------------------------------ | ------------------------------------- |
| Manufacturing process               | DED                                  | —                                     |
| Material                            | IN718 / Ti-6Al-4V                    | Deposit / substrate if different      |
| Heat-source power, P                | 600                                  | W                                     |
| Scan speed, v                       | 6                                    | mm/s                                  |
| Physical deposition layer thickness | 0.67                                 | mm                                    |
| Hatch spacing                       | Not applicable — one track per layer | —                                     |
| Absorption efficiency               | 0.4                                  | Dimensionless                         |
| Heat-source model                   | Goldak double ellipsoid              | Volumetric heat source                |
| Heat-source radii                   | 0.8 / 0.8 / 0.8 / 0.8                | mm; front / rear / transverse / depth |
| Cooling interval                    | 200                                  | s after each deposited layer          |

_Printing and heat-source values describe the supplied simulation configuration._

### Simulation parameters

| Parameter                               | Value / setting                                                                                    | Unit / description                      |
| --------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Initial / ambient temperature           | 25 / 25                                                                                            | °C                                      |
| High-temperature material model         | Complete temperature-dependent tables below; linear interpolation with endpoint holds              | —                                       |
| IN718 properties evaluated at 20 °C     | E = 156.3 GPa; ν = 0.3; $\sigma_{\mathrm{y}}$ = 308.9 MPa; H = 1 GPa; $\sigma_{\max}$ = 370.68 MPa | From the same thermal–mechanical tables |
| Ti-6Al-4V properties evaluated at 20 °C | E = 125 GPa; ν = 0.34; $\sigma_{\mathrm{y}}$ = 955 MPa; H = 0 GPa; $\sigma_{\max}$ = 1146 MPa      | From the same thermal–mechanical tables |
| Identified inherent strain              | Not used — this case uses full thermal–mechanical analysis                                         | —                                       |
| Thermal strain reference temperature    | 20                                                                                                 | °C                                      |
| Thermal strain cutoff                   | No explicit cutoff configured                                                                      | —                                       |

The supplied drawing shows a 30 mm substrate width; the saved FE mesh spans 10 mm across Y. The result below uses the saved mesh.

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

Every configured temperature node is listed below, with exact conversion from K to °C. Each property is linearly interpolated within its own table and held at its nearest endpoint outside that range.

#### IN718 — upper region

| Parameter            | Value  | Unit          |
| -------------------- | ------ | ------------- |
| Density              | 8190   | kg/m³         |
| Latent heat          | 286000 | J/kg          |
| Solidus temperature  | 1533   | K             |
| Liquidus temperature | 1609   | K             |
| Maximum yield factor | 1.2    | Dimensionless |

##### Thermal conductivity

| Temperature (°C) | Temperature (K) | Thermal conductivity (W/(m·K)) |
| ---------------- | --------------- | ------------------------------ |
| 24.85            | 298             | 8.93                           |
| 99.85            | 373             | 10.8                           |
| 199.85           | 473             | 12.9                           |
| 299.85           | 573             | 15.2                           |
| 399.85           | 673             | 17.4                           |
| 499.85           | 773             | 18.7                           |
| 599.85           | 873             | 20.8                           |
| 699.85           | 973             | 21.9                           |
| 799.85           | 1073            | 26.9                           |
| 899.85           | 1173            | 25.8                           |
| 999.85           | 1273            | 26.7                           |
| 1099.85          | 1373            | 28.3                           |
| 1169.85          | 1443            | 29.3                           |
| 1335.85          | 1609            | 29.6                           |

##### Specific heat capacity

| Temperature (°C) | Temperature (K) | Specific heat capacity (J/(kg·K)) |
| ---------------- | --------------- | --------------------------------- |
| 24.85            | 298             | 435                               |
| 99.85            | 373             | 455                               |
| 199.85           | 473             | 479                               |
| 299.85           | 573             | 497                               |
| 399.85           | 673             | 515                               |
| 499.85           | 773             | 527                               |
| 599.85           | 873             | 558                               |
| 699.85           | 973             | 568                               |
| 799.85           | 1073            | 680                               |
| 899.85           | 1173            | 640                               |
| 999.85           | 1273            | 620                               |
| 1099.85          | 1373            | 640                               |
| 1169.85          | 1443            | 650                               |
| 1335.85          | 1609            | 720                               |

##### Young’s modulus

| Temperature (°C) | Temperature (K) | Young’s modulus (GPa) |
| ---------------- | --------------- | --------------------- |
| 26.85            | 300             | 156.3                 |
| 93.85            | 367             | 151.8                 |
| 204.85           | 478             | 144.9                 |
| 315.85           | 589             | 138                   |
| 426.85           | 700             | 131.4                 |
| 537.85           | 811             | 124.7                 |
| 649.85           | 923             | 124                   |
| 759.85           | 1033            | 123.4                 |
| 870.85           | 1144            | 107.7                 |
| 981.85           | 1255            | 92.05                 |
| 1093.85          | 1367            | 68.95                 |
| 1398.85          | 1672            | 23.79                 |

##### Thermal expansion coefficient

| Temperature (°C) | Temperature (K) | Thermal expansion coefficient (µm/(m·K)) |
| ---------------- | --------------- | ---------------------------------------- |
| 26.85            | 300             | 11.7                                     |
| 204.85           | 478             | 12.8                                     |
| 315.85           | 589             | 13.4                                     |
| 649.85           | 923             | 14.6                                     |
| 759.85           | 1033            | 15.1                                     |
| 870.85           | 1144            | 15.7                                     |
| 1093.85          | 1367            | 16.6                                     |
| 1398.85          | 1672            | 16.6                                     |

##### Poisson ratio

| Temperature (°C) | Temperature (K) | Poisson ratio (Dimensionless) |
| ---------------- | --------------- | ----------------------------- |
| 26.85            | 300             | 0.3                           |
| 93.85            | 367             | 0.3                           |
| 204.85           | 478             | 0.3                           |
| 315.85           | 589             | 0.3                           |
| 426.85           | 700             | 0.3                           |
| 537.85           | 811             | 0.3                           |
| 649.85           | 923             | 0.3                           |
| 759.85           | 1033            | 0.3                           |
| 870.85           | 1144            | 0.3                           |
| 981.85           | 1255            | 0.3                           |
| 1093.85          | 1367            | 0.3                           |
| 1398.85          | 1672            | 0.3                           |

##### Initial yield stress

| Temperature (°C) | Temperature (K) | Initial yield stress (MPa) |
| ---------------- | --------------- | -------------------------- |
| 26.85            | 300             | 308.9                      |
| 315.85           | 589             | 246.3                      |
| 537.85           | 811             | 226.1                      |
| 759.85           | 1033            | 207.7                      |
| 981.85           | 1255            | 114                        |

##### Hardening modulus

| Temperature (°C) | Temperature (K) | Hardening modulus (GPa) |
| ---------------- | --------------- | ----------------------- |
| 26.85            | 300             | 1                       |
| 315.85           | 589             | 1                       |
| 537.85           | 811             | 1                       |
| 759.85           | 1033            | 1                       |
| 981.85           | 1255            | 1                       |

Maximum yield stress is 1.2 × the interpolated initial yield stress.

#### Ti-6Al-4V — lower region

| Parameter            | Value  | Unit          |
| -------------------- | ------ | ------------- |
| Density              | 4400   | kg/m³         |
| Latent heat          | 270000 | J/kg          |
| Solidus temperature  | 1878   | K             |
| Liquidus temperature | 1928   | K             |
| Maximum yield factor | 1.2    | Dimensionless |

##### Thermal conductivity

| Temperature (°C) | Temperature (K) | Thermal conductivity (W/(m·K)) |
| ---------------- | --------------- | ------------------------------ |
| 24.85            | 298             | 7                              |
| 99.85            | 373             | 7.45                           |
| 199.85           | 473             | 8.75                           |
| 299.85           | 573             | 10.2                           |
| 399.85           | 673             | 11.4                           |
| 499.85           | 773             | 12.6                           |
| 599.85           | 873             | 14.2                           |
| 699.85           | 973             | 15.5                           |
| 799.85           | 1073            | 17.8                           |
| 899.85           | 1173            | 20.2                           |
| 999.85           | 1273            | 21                             |
| 1099.85          | 1373            | 21                             |
| 1199.85          | 1473            | 22.9                           |
| 1299.85          | 1573            | 23.7                           |
| 1399.85          | 1673            | 24.6                           |
| 1499.85          | 1773            | 25.8                           |
| 1599.85          | 1873            | 27                             |
| 1649.85          | 1923            | 30.9                           |
| 1699.85          | 1973            | 34.6                           |

##### Specific heat capacity

| Temperature (°C) | Temperature (K) | Specific heat capacity (J/(kg·K)) |
| ---------------- | --------------- | --------------------------------- |
| 24.85            | 298             | 546                               |
| 99.85            | 373             | 562                               |
| 199.85           | 473             | 584                               |
| 299.85           | 573             | 606                               |
| 399.85           | 673             | 629                               |
| 499.85           | 773             | 651                               |
| 599.85           | 873             | 673                               |
| 699.85           | 973             | 694                               |
| 799.85           | 1073            | 714                               |
| 899.85           | 1173            | 734                               |
| 999.85           | 1273            | 697                               |
| 1099.85          | 1373            | 660                               |
| 1199.85          | 1473            | 678                               |
| 1299.85          | 1573            | 696                               |
| 1399.85          | 1673            | 714                               |
| 1499.85          | 1773            | 732                               |
| 1599.85          | 1873            | 750                               |
| 1649.85          | 1923            | 795                               |
| 1699.85          | 1973            | 831                               |

##### Young’s modulus

| Temperature (°C) | Temperature (K) | Young’s modulus (GPa) |
| ---------------- | --------------- | --------------------- |
| 26.85            | 300             | 125                   |
| 259.85           | 533             | 110                   |
| 315.85           | 589             | 100                   |
| 426.85           | 700             | 93                    |
| 481.85           | 755             | 80                    |
| 537.85           | 811             | 74                    |
| 649.85           | 923             | 55                    |
| 799.85           | 1073            | 27                    |
| 824.85           | 1098            | 22                    |
| 849.85           | 1123            | 18                    |
| 1299.85          | 1573            | 12                    |
| 1599.85          | 1873            | 9                     |

##### Thermal expansion coefficient

| Temperature (°C) | Temperature (K) | Thermal expansion coefficient (µm/(m·K)) |
| ---------------- | --------------- | ---------------------------------------- |
| 26.85            | 300             | 8.78                                     |
| 259.85           | 533             | 9.83                                     |
| 315.85           | 589             | 10                                       |
| 426.85           | 700             | 10.7                                     |
| 481.85           | 755             | 11.1                                     |
| 537.85           | 811             | 11.2                                     |
| 649.85           | 923             | 11.7                                     |
| 799.85           | 1073            | 12.2                                     |
| 824.85           | 1098            | 12.3                                     |
| 849.85           | 1123            | 12.4                                     |
| 1299.85          | 1573            | 13                                       |
| 1599.85          | 1873            | 16.3                                     |

##### Poisson ratio

| Temperature (°C) | Temperature (K) | Poisson ratio (Dimensionless) |
| ---------------- | --------------- | ----------------------------- |
| 26.85            | 300             | 0.34                          |
| 259.85           | 533             | 0.34                          |
| 315.85           | 589             | 0.34                          |
| 426.85           | 700             | 0.34                          |
| 481.85           | 755             | 0.34                          |
| 537.85           | 811             | 0.34                          |
| 649.85           | 923             | 0.34                          |
| 799.85           | 1073            | 0.34                          |
| 824.85           | 1098            | 0.34                          |
| 849.85           | 1123            | 0.34                          |
| 1299.85          | 1573            | 0.34                          |
| 1599.85          | 1873            | 0.34                          |

##### Initial yield stress

| Temperature (°C) | Temperature (K) | Initial yield stress (MPa) |
| ---------------- | --------------- | -------------------------- |
| 26.85            | 300             | 955                        |
| 299.85           | 573             | 836                        |
| 499.85           | 773             | 732                        |
| 749.85           | 1023            | 581                        |
| 799.85           | 1073            | 547                        |
| 899.85           | 1173            | 480                        |
| 999.85           | 1273            | 405                        |
| 1099.85          | 1373            | 330                        |

##### Hardening modulus

| Temperature (°C) | Temperature (K) | Hardening modulus (GPa) |
| ---------------- | --------------- | ----------------------- |
| 26.85            | 300             | 0                       |
| 299.85           | 573             | 0                       |
| 499.85           | 773             | 0                       |
| 749.85           | 1023            | 0                       |
| 799.85           | 1073            | 0                       |
| 899.85           | 1173            | 0                       |
| 999.85           | 1273            | 0                       |
| 1099.85          | 1373            | 0                       |

Maximum yield stress is 1.2 × the interpolated initial yield stress.

</details>

[Download full parameter JSON](/assets/data/cases/single_track/thermal-parameters.json) · [Download temperature-dependent CSV](/assets/data/cases/single_track/temperature-dependent-properties.csv) · [Download simulation YAML](/assets/data/cases/single_track/simulation-parameters.yaml)

## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

### Residual stress field

<div class="rsh-case-figure-content" markdown="1">

![Von Mises stress at Y = 0 mm.](/assets/img/cases/single_track/results-cover.png)

_Figure 2. Von Mises stress at Y = 0 mm._

[Download the stress-field figure](/assets/pdf/cases/single_track/results-cover.pdf)

[Download all final cell stresses](/assets/data/cases/single_track/final-stress-cells.csv) · [Download stress-field metadata](/assets/data/cases/single_track/final-stress-metadata.json)

</div>

</figure>

</div>

---

**Original article:** Liao, S., Golgoon, A., Mozaffar, M., Cao, J. (2023). Efficient GPU-accelerated thermomechanical solver for residual stress prediction in additive manufacturing. _Computational Mechanics_, **71**, 879–893. [https://doi.org/10.1007/s00466-023-02273-3](https://doi.org/10.1007/s00466-023-02273-3).

**Data sources:** Supplied simulation inputs and saved solver outputs. Complete physical settings and temperature-dependent values are available in the YAML, JSON, and CSV downloads above.
