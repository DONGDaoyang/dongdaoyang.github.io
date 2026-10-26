---
layout: page
title: "Cantilever (LPBF · IN625)"
card_title: "Cantilever (LPBF · IN625)"
description: "AM-Bench 2018-1 IN625 cantilever: residual stress measurements, inherent-strain identification, and release distortion."
permalink: /benchmarks/cantilever/
hub_case: true
published: true
importance: 4
case_type: Computational case · Solver-output study
img: /assets/img/cases/cantilever/card-cover.png?v=b6b1af42a36f
image_alt: "Cantilever benchmark model."
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

This is the AM-Bench 2018-1 IN625 cantilever model. After printing, residual stresses were measured using neutron diffraction and the contour method. Warpage displacement was measured after separating the cantilever from its supports. <a href="#reference-1">[1]</a>

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

| Parameter                                                         | Value             | Unit |
| ----------------------------------------------------------------- | ----------------- | ---- |
| Manufacturing process                                             | LPBF              | —    |
| Material                                                          | IN625             | —    |
| Laser power, $P$                                                  | 195               | W    |
| Scan speed, $V$                                                   | 800               | mm/s |
| Layer thickness                                                   | 20                | µm   |
| Hatch spacing                                                     | 100               | µm   |
| Absorption efficiency                                             | 0.37              | —    |
| Goldak heat-source dimensions (front / rear / transverse / depth) | 50 / 50 / 50 / 50 | µm   |
| Cooling interval (after each simulated layer)                     | 200               | s    |

### Simulation parameters

| Parameter                                                                                         | Value / setting                                                                  | Unit              |
| ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------- |
| Ambient temperature                                                                               | 25                                                                               | °C                |
| High-temperature material model                                                                   | See tables below                                                                 | —                 |
| Elastic parameters (20 °C, constant)                                                              | $E$ = 208<br>$\nu$ = 0.277                                                       | GPa<br>—          |
| Plastic parameters (20 °C, constant)                                                              | $\sigma_{\mathrm{y}}$ = 725<br>$H$ = 0.75714<br>$\sigma_{\mathrm{max}}$ = 990    | MPa<br>GPa<br>MPa |
| Elastic parameters (saved local identification)                                                   | $E$ = 156.3<br>$\nu$ = 0.300                                                     | GPa<br>—          |
| Plastic parameters (saved local identification)                                                   | $\sigma_{\mathrm{y}}$ = 308.9<br>$H$ = 1.000<br>$\sigma_{\mathrm{max}}$ = 370.68 | MPa<br>GPa<br>MPa |
| Identified inherent strain, $\varepsilon_{\mathrm{xx}}^{\ast} = \varepsilon_{\mathrm{yy}}^{\ast}$ | −3.655                                                                           | ‰                 |
| Identified inherent strain, $\varepsilon_{\mathrm{zz}}^{\ast}$                                    | +9.504                                                                           | ‰                 |
| Layer activation                                                                                  | 25 × 0.5; an additional 50-layer run is shown for warpage                        | Layers × mm       |
| Constraints and release                                                                           | Fixed substrate bottom; release the interface over $X$ = 0–55 mm                 | —                 |

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

The temperature-dependent conductivity, elastic, thermal-expansion and plastic parameters used in the local scan model for inherent-strain identification are taken from Table S6 of Qi et al. <a href="#reference-2">[2]</a>.

#### Material constants

| Parameter                                       | Value / setting                               | Unit     |
| ----------------------------------------------- | --------------------------------------------- | -------- |
| Material regions                                | Build and substrate use the same IN625 tables | —        |
| Density, $\rho$                                 | 8190                                          | kg/m³    |
| Latent heat, $L$                                | 286000                                        | J/kg     |
| Solidus temperature, $T_{\mathrm{s}}$           | 1533                                          | K        |
| Liquidus temperature, $T_{\mathrm{l}}$          | 1609                                          | K        |
| Volumetric heat capacity, $\rho C_{\mathrm{p}}$ | $\rho C_{\mathrm{p}}(T)$                      | J/(m³·K) |

_Density, latent heat, solidus/liquidus temperatures, and specific heat are retained configuration inputs whose material-source validation is still pending._

#### Conductivity, elasticity, and thermal expansion

| $T$ (°C) | Thermal conductivity, $k$ (W/(m·K)) | Young’s modulus, $E$ (GPa) | Poisson ratio, $\nu$ | Thermal expansion coefficient, $\alpha$ (10⁻⁶ K⁻¹) |
| -------- | ----------------------------------- | -------------------------- | -------------------- | -------------------------------------------------- |
| 20       | 9.8                                 | 208                        | 0.277                | —                                                  |
| 100      | 10.7                                | 204                        | 0.28                 | 5.56                                               |
| 200      | 12.5                                | 198                        | 0.286                | 6.28                                               |
| 300      | 14.1                                | 192                        | 0.29                 | 6.61                                               |
| 400      | 15.6                                | 186                        | 0.295                | 7.38                                               |
| 550      | 17.4                                | 179                        | 0.305                | 7.93                                               |
| 650      | 18.9                                | 170                        | 0.321                | 9.47                                               |
| 750      | 20.1                                | 161                        | 0.34                 | 10.5                                               |
| 870      | 22.7                                | 148                        | 0.336                | 11.6                                               |

_The dash means no value is tabulated at that temperature. For $\alpha$ below 100 °C, the solver holds the first value, 5.56 × 10⁻⁶ K⁻¹._

#### Specific heat, $C_{\mathrm{p}}$

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

#### Temperature-dependent plasticity

| $T$ (°C) | Initial yield stress, $\sigma_{\mathrm{y}}$ (MPa) | Hardening modulus, $H$ (GPa) | Maximum yield stress, $\sigma_{\mathrm{max}}$ (MPa) |
| -------- | ------------------------------------------------- | ---------------------------- | --------------------------------------------------- |
| 20       | 725                                               | 0.7571428571428572           | 990                                                 |
| 300      | 610                                               | 0.14285714285714285          | 660                                                 |
| 600      | 515                                               | 0.1285714285714286           | 560                                                 |
| 800      | 100                                               | 0.05714285714285715          | 120                                                 |

Between tabulated temperatures, properties are linearly interpolated. Outside each property's own temperature range, the nearest endpoint is held constant. Maximum yield stress corresponds to the configured cap at equivalent plastic strain 0.35. These settings do not establish a validated melting-temperature material model.

</details>

[Download the full parameter JSON](/assets/data/cases/cantilever/thermal-parameters.json) · [Download all temperature-dependent values as CSV](/assets/data/cases/cantilever/temperature-dependent-properties.csv)

## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

### Axial stress after cutting

<div class="rsh-case-figure-content" markdown="1">

![Cantilever post-cut axial stress on undeformed geometry, in MPa.](/assets/img/cases/cantilever/results-cover.png?v=447bfee4b3b8)

<p markdown="0"><em>Figure 2. Cantilever post-cut axial stress $\sigma_{\mathrm{xx}}$ in the 50-group calculation (MPa).</em></p>

The color scale shows axial stress on the undeformed geometry. The 50 mechanical activation groups represent a numerical deposition grouping and are distinct from the physical print layers.

[Download the figure PDF](/assets/pdf/cases/cantilever/results-cover.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Local thermal and strain histories

<div class="rsh-case-figure-content" markdown="1">

![Cantilever local temperature and axial plastic and elastic strain during scanning and cooling.](/assets/img/cases/cantilever/thermal-history.png)

<p markdown="0"><em>Figure 3. Saved Cantilever local history: temperature (°C) and axial strain (dimensionless).</em></p>

The upper panel shows temperature and the lower panel separates the saved plastic and elastic $xx$ strains at local cell 389, centered at $(-0.0125,0.0125,0.0100)$ mm. These are archived local scanning and cooling histories, not the full cantilever build or a new calculation.

[Download local history PDF](/assets/pdf/cases/cantilever/thermal-history.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Local elastic-strain agreement

<div class="rsh-case-figure-content" markdown="1">

![Cantilever Opt-IS versus DNS elastic-strain parity plots for the xx, yy and zz components.](/assets/img/cases/cantilever/strain-parity.png?v=e712cd19ecee)

<p markdown="0"><em>Figure 4. Cantilever local calibration: $xx$, $yy$ and $zz$ elastic-strain parity (µε).</em></p>

The three panels compare Opt-IS with DNS on 800 paired active native cells. The dashed diagonal denotes exact agreement. The plot assesses local elastic-strain agreement, separate from the experimental part-scale comparisons below.

[Download the figure PDF](/assets/pdf/cases/cantilever/strain-parity.pdf) · [Download archived error metrics](/assets/data/cases/cantilever/optimization-metrics.csv)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Local elastic-strain maps

<div class="rsh-case-figure-content" markdown="1">

![Cantilever local axial elastic-strain maps from DNS and Opt-IS with their signed difference.](/assets/img/cases/cantilever/strain-maps.png?v=2767b68420dc)

<p markdown="0"><em>Figure 5. Cantilever local top-layer $\varepsilon^{\mathrm{e}}_{\mathrm{xx}}$ maps (µε).</em></p>

The panels show DNS, Opt-IS, and Opt-IS minus DNS at $z=0.030$ mm. The signed difference identifies where the local reduced model departs from DNS. These are calibration-model coordinates, not the nominal heights of the full cantilever.

[Download the figure PDF](/assets/pdf/cases/cantilever/strain-maps.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Pre-cut xx elastic strain

<div class="rsh-case-figure-content" markdown="1">

![Cantilever xx elastic strain at nominal height 11 mm before cutting.](/assets/img/cases/cantilever/x11.png?v=ba4c380f9e0c)

<p markdown="0"><em>Figure 6. Cantilever $\varepsilon^{\mathrm{e}}_{\mathrm{xx}}$ at nominal height 11.0 mm before cutting (µε).</em></p>

The 25-group model is sampled along the central plane $y=0$ at global $z=-1.5$ mm. Opt-IS, MIS, and DIS are compared with experimental profiles retaining their original nearby height labels. Nominal height is measured from the part base and is not the global $z$ coordinate.

[Download the figure PDF](/assets/pdf/cases/cantilever/x11.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Pre-cut zz elastic strain

<div class="rsh-case-figure-content" markdown="1">

![Cantilever zz elastic strain at nominal height 11 mm before cutting.](/assets/img/cases/cantilever/z11.png?v=d86a149287b9)

<p markdown="0"><em>Figure 7. Cantilever $\varepsilon^{\mathrm{e}}_{\mathrm{zz}}$ at nominal height 11.0 mm before cutting (µε).</em></p>

The 25-group model is sampled along the central plane $y=0$ at global $z=-1.5$ mm. Opt-IS, MIS, and DIS are compared with experimental profiles retaining their original nearby height labels. Nominal height is measured from the part base and is not the global $z$ coordinate.

[Download the figure PDF](/assets/pdf/cases/cantilever/z11.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Stress along a supporting leg

<div class="rsh-case-figure-content" markdown="1">

![Cantilever axial stress from the bottom to the top of one supporting leg.](/assets/img/cases/cantilever/leg-stress-comparison.png?v=40df9dd9e397)

<p markdown="0"><em>Figure 8. Cantilever axial stress $\sigma_{\mathrm{xx}}$ along one leg (MPa).</em></p>

Opt-IS is compared with two experimental profiles from the bottom to the top of the leg. The prediction captures the transition from compression to tension, but this transition occurs at a lower height than in the experimental profiles.

[Download the figure PDF](/assets/pdf/cases/cantilever/leg-stress-comparison.pdf)

</div>

</figure>

<figure class="rsh-case-figure" markdown="1">

### Vertical displacement after cutting

<div class="rsh-case-figure-content" markdown="1">

![Cantilever vertical displacement after cutting compared across Opt-IS, MIS, DIS and experiment.](/assets/img/cases/cantilever/warpage.png?v=040f4f18afa6)

<p markdown="0"><em>Figure 9. Cantilever post-cut vertical displacement $u_z$ (mm).</em></p>

The Opt-IS calculations with 25 and 50 activation groups are compared with MIS, DIS, and the experimental profile. Each Opt-IS curve contains 11 displayed calculation points. The curves show uplift at the left end and small displacement near the opposite end.

[Download the figure PDF](/assets/pdf/cases/cantilever/warpage.pdf) · [Download 25-group displacement samples](/assets/data/cases/cantilever/warpage-25-layer.csv) · [Download 50-group displacement samples](/assets/data/cases/cantilever/warpage-50-layer.csv)

</div>

</figure>

</div>

---

**Reference:**

<span id="reference-1"></span>

[1] Phan, T.Q., Strantza, M., Hill, M.R., Gnaupel-Herold, T.H., Heigel, J., D’Elia, C.R., DeWald, A.T., Clausen, B., Pagan, D.C., Peter Ko, J.Y., Brown, D.W., Levine, L.E. (2019). Elastic Residual Strain and Stress Measurements and Corresponding Part Deflections of 3D Additive Manufacturing Builds of IN625 AM-Bench Artifacts Using Neutron Diffraction, Synchrotron X-Ray Diffraction, and Contour Method. _Integrating Materials and Manufacturing Innovation_, **8**, 318–334. [https://doi.org/10.1007/s40192-019-00149-0](https://doi.org/10.1007/s40192-019-00149-0).

<span id="reference-2"></span>

[2] Qi, J., Liu, X., Dong, P., Li, Q., Yang, Y. (2025). An improved dynamic inherent strain method for efficient prediction of residual stresses and deformations in metal additive manufacturing. _Additive Manufacturing_, **114**, 105025. [https://doi.org/10.1016/j.addma.2025.105025](https://doi.org/10.1016/j.addma.2025.105025).
