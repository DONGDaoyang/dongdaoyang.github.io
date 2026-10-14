---
layout: page
title: Cantilever (LPBF)
card_title: "Cantilever (LPBF · IN625)"
description: "AM-Bench 2018-1 IN625 cantilever: residual stress measurements, inherent-strain identification, and release distortion."
permalink: /benchmarks/cantilever/
hub_case: true
published: true
importance: 4
case_type: Computational case · Solver-output study
img: /assets/img/cases/cantilever/results-cover.png
image_alt: "Supplied Cantilever simulation result used as the benchmark card cover."
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

This is the AM-Bench 2018-1 IN625 cantilever model. After printing, residual stresses were measured using neutron diffraction and the contour method. Warpage displacement was measured after separating the cantilever from its supports.

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Geometry and dimensions.](/assets/img/cases/cantilever/geometry-overview.png)

_Figure 1. Geometry and dimensions._

[Download the original geometry PDF](/assets/pdf/cases/cantilever/geometry-overview.pdf)

</div>

</figure>

</div>

## Problem set

### Printing parameters

| Parameter             | Value                   | Unit / description                    |
| --------------------- | ----------------------- | ------------------------------------- |
| Manufacturing process | LPBF                    | —                                     |
| Material              | IN625                   | Nickel-based alloy                    |
| Laser power, P        | 195                     | W                                     |
| Scan speed, v         | 800                     | mm/s                                  |
| Layer thickness       | 20                      | µm                                    |
| Hatch spacing         | 100                     | µm                                    |
| Absorption efficiency | 0.37                    | Dimensionless                         |
| Heat-source model     | Goldak double ellipsoid | Volumetric heat source                |
| Heat-source radii     | 50 / 50 / 50 / 50       | µm; front / rear / transverse / depth |
| Cooling interval      | 200                     | s after each simulated layer          |

_Printing and heat-source values describe the current simulation configuration._

### Simulation parameters

| Parameter                                                                       | Value / setting                                                                                                                   | Unit        |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Initial / ambient temperature                                                   | 25 / 25                                                                                                                           | °C          |
| High-temperature material model                                                 | Full temperature-dependent tables below; linear interpolation with endpoint holds                                                 | —           |
| Room-temperature material model                                                 | Constant properties at 20 °C: E = 208 GPa, ν = 0.277, $\sigma_{\mathrm{y}}$ = 725 MPa, H = 0.75714 GPa, $\sigma_{\max}$ = 990 MPa | —           |
| Material settings for the saved local identification                            | E = 156.3 GPa, ν = 0.300, $\sigma_{\mathrm{y}}$ = 308.9 MPa, H = 1.000 GPa, $\sigma_{\max}$ = 370.68 MPa                          | —           |
| Identified inherent strain, $\varepsilon_{xx}^{\ast} = \varepsilon_{yy}^{\ast}$ | −3.655369                                                                                                                         | ‰           |
| Identified inherent strain, $\varepsilon_{zz}$                                  | +9.504349                                                                                                                         | ‰           |
| Inherent strain in the archived macro configuration                             | $\varepsilon_{xx}^{\ast} = \varepsilon_{yy}^{\ast} = −2.867190\,;\quad \varepsilon_{zz} = +17.244139$                             | ‰           |
| Macro layer activation                                                          | 25 × 0.5; an additional 50-layer run is shown for warpage                                                                         | Layers × mm |
| Macro constraints and release                                                   | Fixed substrate bottom; release the interface over X = 0–55 mm                                                                    | —           |

_The selected identification and archived macro figures use different parameter versions; the existing figures are retained from the saved outputs._

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

These tables list every configured temperature point. Temperatures are shown in both °C and K; all material tables apply to both the build and the substrate.

#### Material constants

| Parameter                | Value / setting                               | Unit     |
| ------------------------ | --------------------------------------------- | -------- |
| Material regions         | Build and substrate use the same IN625 tables | —        |
| Density, ρ               | 8190                                          | kg/m³    |
| Latent heat, L           | 286000                                        | J/kg     |
| Solidus temperature      | 1533 K / 1259.85 °C                           | —        |
| Liquidus temperature     | 1609 K / 1335.85 °C                           | —        |
| Volumetric heat capacity | ρ × cₚ(T)                                     | J/(m³·K) |

_Density, latent heat, solidus/liquidus temperatures, and specific heat are retained configuration inputs whose material-source validation is still pending._

#### Conductivity, elasticity, and thermal expansion

| Temperature (°C) | Temperature (K) | k (W/(m·K)) | E (GPa) | ν     | α (10⁻⁶ K⁻¹) |
| ---------------- | --------------- | ----------- | ------- | ----- | ------------ |
| 20               | 293.15          | 9.8         | 208     | 0.277 | —            |
| 100              | 373.15          | 10.7        | 204     | 0.28  | 5.56         |
| 200              | 473.15          | 12.5        | 198     | 0.286 | 6.28         |
| 300              | 573.15          | 14.1        | 192     | 0.29  | 6.61         |
| 400              | 673.15          | 15.6        | 186     | 0.295 | 7.38         |
| 550              | 823.15          | 17.4        | 179     | 0.305 | 7.93         |
| 650              | 923.15          | 18.9        | 170     | 0.321 | 9.47         |
| 750              | 1023.15         | 20.1        | 161     | 0.34  | 10.5         |
| 870              | 1143.15         | 22.7        | 148     | 0.336 | 11.6         |

_The dash means no value is tabulated at that temperature. For α below 100 °C, the solver holds the first value, 5.56 × 10⁻⁶ K⁻¹._

#### Specific heat

| Temperature (°C) | Temperature (K) | cₚ (J/(kg·K)) |
| ---------------- | --------------- | ------------- |
| 24.85            | 298             | 435           |
| 99.85            | 373             | 455           |
| 199.85           | 473             | 479           |
| 299.85           | 573             | 497           |
| 399.85           | 673             | 515           |
| 499.85           | 773             | 527           |
| 599.85           | 873             | 558           |
| 699.85           | 973             | 568           |
| 799.85           | 1073            | 680           |
| 899.85           | 1173            | 640           |
| 999.85           | 1273            | 620           |
| 1099.85          | 1373            | 640           |
| 1169.85          | 1443            | 650           |
| 1335.85          | 1609            | 720           |

_These are the complete configured specific-heat values. Their temperatures are converted from the original Kelvin nodes without rounding to nominal 25 °C or 100 °C intervals._

#### Temperature-dependent plasticity

| Temperature (°C) | Temperature (K) | Initial yield stress (MPa) | Hardening modulus (GPa) | Maximum yield stress (MPa) |
| ---------------- | --------------- | -------------------------- | ----------------------- | -------------------------- |
| 20               | 293.15          | 725                        | 0.7571428571428572      | 990                        |
| 300              | 573.15          | 610                        | 0.14285714285714285     | 660                        |
| 600              | 873.15          | 515                        | 0.1285714285714286      | 560                        |
| 800              | 1073.15         | 100                        | 0.05714285714285715     | 120                        |

Between tabulated temperatures, properties are linearly interpolated. Outside each property's own temperature range, the nearest endpoint is held constant. Maximum yield stress corresponds to the configured cap at equivalent plastic strain 0.35. These settings do not establish a validated melting-temperature material model.

</details>

[Download the full parameter JSON](/assets/data/cases/cantilever/thermal-parameters.json) · [Download all temperature-dependent values as CSV](/assets/data/cases/cantilever/temperature-dependent-properties.csv)

## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

### Temperature and strain histories

<div class="rsh-case-figure-content" markdown="1">

![Temperature and X-direction strain histories.](/assets/img/cases/cantilever/thermal-history.png)

_Figure 2. Temperature and X-direction strain histories._

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Inherent-strain identification

<div class="rsh-case-figure-content" markdown="1">

![Stress and elastic strain comparison.](/assets/img/cases/cantilever/optimization-agreement.png)

_Figure 3. Stress and elastic strain comparison._

[Download the complete calibration figure](/assets/pdf/cases/cantilever/optimization-agreement.pdf) · [Download the error metrics](/assets/data/cases/cantilever/optimization-metrics.csv)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Residual elastic strain

<div class="rsh-case-figure-content" markdown="1">

![X-direction elastic strain at Z ≈ 11 mm.](/assets/img/cases/cantilever/x11.png)

_Figure 4. X-direction elastic strain at Z ≈ 11 mm._

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Z-direction elastic strain at Z ≈ 11 mm.](/assets/img/cases/cantilever/z11.png)

_Figure 5. Z-direction elastic strain at Z ≈ 11 mm._

Additional profiles: [2.2 mm, XX](/assets/img/cases/cantilever/x2p2.png) · [2.2 mm, ZZ](/assets/img/cases/cantilever/z2p2.png) · [9.5 mm, XX](/assets/img/cases/cantilever/x9p5.png) · [9.5 mm, ZZ](/assets/img/cases/cantilever/z9p5.png).

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Vertical displacement after release.](/assets/img/cases/cantilever/warpage.png)

_Figure 6. Vertical displacement after release._

[Download the 25-layer displacement samples](/assets/data/cases/cantilever/warpage-25-layer.csv) · [Download the 50-layer displacement samples](/assets/data/cases/cantilever/warpage-50-layer.csv)

</div>

</figure>

</div>

---

**Original article:** Phan, T.Q., Strantza, M., Hill, M.R., Gnaupel-Herold, T.H., Heigel, J., D’Elia, C.R., DeWald, A.T., Clausen, B., Pagan, D.C., Peter Ko, J.Y., Brown, D.W., Levine, L.E. (2019). Elastic Residual Strain and Stress Measurements and Corresponding Part Deflections of 3D Additive Manufacturing Builds of IN625 AM-Bench Artifacts Using Neutron Diffraction, Synchrotron X-Ray Diffraction, and Contour Method. _Integrating Materials and Manufacturing Innovation_, **8**, 318–334. [https://doi.org/10.1007/s40192-019-00149-0](https://doi.org/10.1007/s40192-019-00149-0).
