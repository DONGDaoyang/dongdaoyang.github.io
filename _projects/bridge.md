---
layout: page
title: Bridge (LPBF)
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

This is a Ti-6Al-4V bridge model. A local thermal–mechanical simulation is used to identify inherent strain, which is then applied to the full bridge model to calculate residual elastic strain.

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

| Parameter                           | Value                   | Unit / description                    |
| ----------------------------------- | ----------------------- | ------------------------------------- |
| Manufacturing process               | LPBF                    | —                                     |
| Material                            | Ti-6Al-4V               | Deposit / substrate if different      |
| Heat-source power, $P$              | 100                     | W                                     |
| Scan speed, $V$                     | 600                     | mm/s                                  |
| Physical deposition layer thickness | 30                      | µm                                    |
| Hatch spacing                       | 105                     | µm                                    |
| Absorption efficiency               | 0.3                     | Dimensionless                         |
| Heat-source model                   | Goldak double ellipsoid | Volumetric heat source                |
| Heat-source radii                   | 54 / 54 / 54 / 30       | µm; front / rear / transverse / depth |
| Cooling interval                    | 200                     | s after each deposited layer          |

_Printing and heat-source values describe the supplied simulation configuration._

### Simulation parameters

| Parameter                                                                                                | Value / setting                                                                                                                 | Unit / description  |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Initial / ambient temperature                                                                            | 25 / 25                                                                                                                         | °C                  |
| High-temperature material model                                                                          | Complete temperature-dependent tables below; linear interpolation with endpoint holds                                           | —                   |
| Room-temperature macro material model                                                                    | $E$ = 114.58 GPa; $\nu$ = 0.3; $\sigma_{\mathrm{y}}$ = 1151 MPa; $H$ = 1.8139 GPa; $\sigma_{\mathrm{max}}$ = 1310 MPa           | Constant properties |
| Latest identified inherent strain, $\varepsilon_{\mathrm{xx}}^{\ast} = \varepsilon_{\mathrm{yy}}^{\ast}$ | -2.820                                                                                                                          | ‰                   |
| Latest identified inherent strain, $\varepsilon_{\mathrm{zz}}^{\ast}$                                    | 2.879                                                                                                                           | ‰                   |
| Inherent strain in the displayed archived comparison                                                     | $\varepsilon_{\mathrm{xx}}^{\ast} = \varepsilon_{\mathrm{yy}}^{\ast} = -2.820\,;\quad \varepsilon_{\mathrm{zz}}^{\ast} = 2.879$ | ‰                   |
| Macro layer activation                                                                                   | 36 × 0.25                                                                                                                       | Layers × mm         |
| Macro constraints and release                                                                            | macro fixed plane $Z$ = 0 mm; no macro release                                                                                  | —                   |
| Thermal strain reference temperature                                                                     | 25                                                                                                                              | °C                  |
| Thermal strain cutoff                                                                                    | solidus                                                                                                                         | —                   |

The physical print layer is 30 µm. The 250 µm layer pitch used in the macro model is a separate coarse activation setting.

The latest saved identification and the displayed archived comparison are listed separately. The plotted curves and their reference frames are retained from the saved figures.

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

Every configured temperature node is listed below, with exact conversion from K to °C. Each property is linearly interpolated within its own table and held at its nearest endpoint outside that range.

#### Ti-6Al-4V — upper region and lower region

| Parameter                              | Value  | Unit          |
| -------------------------------------- | ------ | ------------- |
| Density, $\rho$                        | 4417.8 | kg/m³         |
| Latent heat, $L$                       | 270000 | J/kg          |
| Solidus temperature, $T_{\mathrm{s}}$  | 1878   | K             |
| Liquidus temperature, $T_{\mathrm{l}}$ | 1928   | K             |
| Maximum yield factor                   | 1.2    | Dimensionless |

##### Thermal conductivity, $k$

| Temperature, $T$ (°C) | Temperature, $T$ (K) | Thermal conductivity, $k$ (W/(m·K)) |
| --------------------- | -------------------- | ----------------------------------- |
| -0.15                 | 273                  | 6.18                                |
| 980.85                | 1254                 | 19                                  |
| 990.85                | 1264                 | 19.2                                |
| 1639.85               | 1913                 | 27.7                                |
| 1649.85               | 1923                 | 33.4                                |
| 3276.85               | 3550                 | 36.8                                |

##### Specific heat capacity, $C_{\mathrm{p}}$

| Temperature, $T$ (°C) | Temperature, $T$ (K) | Specific heat capacity, $C_{\mathrm{p}}$ (J/(kg·K)) |
| --------------------- | -------------------- | --------------------------------------------------- |
| -0.15                 | 273                  | 517                                                 |
| 980.85                | 1254                 | 881                                                 |
| 990.85                | 1264                 | 707                                                 |
| 1639.85               | 1913                 | 756                                                 |
| 1649.85               | 1923                 | 829                                                 |
| 3276.85               | 3550                 | 829                                                 |

##### Young’s modulus, $E$

| Temperature, $T$ (°C) | Temperature, $T$ (K) | Young’s modulus, $E$ (GPa) |
| --------------------- | -------------------- | -------------------------- |
| 19.85                 | 293                  | 115                        |
| 687.85                | 961                  | 60.7                       |
| 699.85                | 973                  | 59.8                       |
| 899.85                | 1173                 | 24                         |
| 990.85                | 1264                 | 16.7                       |
| 1264.85               | 1538                 | 11                         |

##### Thermal expansion coefficient, $\alpha$

| Temperature, $T$ (°C) | Temperature, $T$ (K) | Thermal expansion coefficient, $\alpha$ (µm/(m·K)) |
| --------------------- | -------------------- | -------------------------------------------------- |
| -0.15                 | 273                  | 8.85                                               |
| 980.85                | 1254                 | 10.72                                              |
| 990.85                | 1264                 | 10.74                                              |
| 1639.85               | 1913                 | 11.97                                              |
| 1649.85               | 1923                 | 20.17                                              |
| 3276.85               | 3550                 | 0                                                  |

##### Poisson ratio, $\nu$

| Temperature, $T$ (°C) | Temperature, $T$ (K) | Poisson ratio, $\nu$ (Dimensionless) |
| --------------------- | -------------------- | ------------------------------------ |
| 19.85                 | 293                  | 0.3                                  |
| 687.85                | 961                  | 0.3                                  |
| 699.85                | 973                  | 0.3                                  |
| 899.85                | 1173                 | 0.3                                  |
| 990.85                | 1264                 | 0.3                                  |
| 1264.85               | 1538                 | 0.3                                  |

##### Initial yield stress, $\sigma_{\mathrm{y}}$

| Temperature, $T$ (°C) | Temperature, $T$ (K) | Initial yield stress, $\sigma_{\mathrm{y}}$ (MPa) |
| --------------------- | -------------------- | ------------------------------------------------- |
| 19.85                 | 293                  | 1151                                              |
| 687.85                | 961                  | 365.8                                             |
| 699.85                | 973                  | 257.6                                             |
| 899.85                | 1173                 | 69                                                |
| 990.85                | 1264                 | 69                                                |
| 1264.85               | 1538                 | 69                                                |

##### Hardening modulus, $H$

| Temperature, $T$ (°C) | Temperature, $T$ (K) | Hardening modulus, $H$ (GPa) |
| --------------------- | -------------------- | ---------------------------- |
| 19.85                 | 293                  | 1.828                        |
| 687.85                | 961                  | 1                            |
| 699.85                | 973                  | 1                            |
| 899.85                | 1173                 | 1                            |
| 990.85                | 1264                 | 1                            |
| 1264.85               | 1538                 | 1                            |

Maximum yield stress, $\sigma_{\mathrm{max}}$, is $1.2\,\sigma_{\mathrm{y}}$ at each interpolated temperature.

</details>

[Download full parameter JSON](/assets/data/cases/bridge/thermal-parameters.json) · [Download temperature-dependent CSV](/assets/data/cases/bridge/temperature-dependent-properties.csv) · [Download simulation YAML](/assets/data/cases/bridge/simulation-parameters.yaml)

[Download macro configuration](/assets/data/cases/bridge/macro-parameters.yaml) · [Download identification results](/assets/data/cases/bridge/identification-results.json)

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

**Original article:** Ganeriwala, R.K., Strantza, M., King, W.E., Clausen, B., Phan, T.Q., Levine, L.E., Brown, D.W., Hodge, N.E. (2019). Evaluation of a thermomechanical model for prediction of residual stress during laser powder bed fusion of Ti-6Al-4V. _Additive Manufacturing_, **27**, 489–502. [https://doi.org/10.1016/j.addma.2019.03.034](https://doi.org/10.1016/j.addma.2019.03.034).

**Data sources:** Supplied simulation inputs and saved solver outputs. Complete physical settings and temperature-dependent values are available in the YAML, JSON, and CSV downloads above.
