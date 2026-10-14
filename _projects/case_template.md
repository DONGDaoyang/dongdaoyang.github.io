---
layout: page
title: Your case title (PROCESS)
description: "Describe the computational problem and quantities of interest."
permalink: /benchmarks/your-case/
hub_case: true
published: false
importance: 2
case_type: Computational case
img: # Optional list cover: /assets/img/cases/your-case/geometry.png
image_alt: # Describe the cover in English.
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

Introduce the research question, motivation, quantities of interest, and scope. Identify whether this is an original computational problem or a reproduction of a published problem.

<!-- Add figures with ordinary Markdown, for example:
<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Geometry and boundary conditions.](/assets/img/cases/your-case/geometry.png)

_Figure 1. Geometry and dimensions._

</div>

</figure>

</div>
-->

## Problem set

Append the manufacturing process in parentheses to the case title, such as `Cantilever (LPBF)`. Use mm for heat-source dimensions and layer thicknesses of 200 µm or more; keep smaller dimensions in µm.

Describe the geometry, material, printing or loading conditions, initial state, and boundary conditions. Explain layer activation and release if applicable. Distinguish physical process conditions from numerical assumptions and make the evaluation locations explicit.

Keep the last column for units (use — for dimensionless values). Put qualifiers such as cooling timing and heat-source dimension order in the parameter label. Name Goldak dimensions directly without a separate heat-source-model row. Group room-temperature elastic and plastic parameters into separate rows; put one property and its matching unit on each line using `<br>`.

### Printing parameters

| Parameter                                             | Value          | Unit        |
| ----------------------------------------------------- | -------------- | ----------- |
| Process and material                                  | To be supplied | —           |
| Power, $P$; scan speed, $V$; physical layer thickness | To be supplied | W, mm/s, µm |
| Hatch spacing and Goldak heat-source dimensions       | To be supplied | µm          |

### Simulation parameters

| Parameter                                                                                                                              | Value / setting                                                                                            | Unit              |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------- |
| High-temperature material model (temperature-dependent tables)                                                                         | To be supplied                                                                                             | —                 |
| Room-temperature elastic parameters                                                                                                    | $E$ = To be supplied<br>$\nu$ = To be supplied                                                             | GPa<br>—          |
| Room-temperature plastic parameters                                                                                                    | $\sigma_{\mathrm{y}}$ = To be supplied<br>$H$ = To be supplied<br>$\sigma_{\mathrm{max}}$ = To be supplied | MPa<br>GPa<br>MPa |
| Identified inherent strain, $\varepsilon_{\mathrm{xx}}^{\ast}$, $\varepsilon_{\mathrm{yy}}^{\ast}$, $\varepsilon_{\mathrm{zz}}^{\ast}$ | To be supplied                                                                                             | ‰                 |
| Macro layer activation, if used                                                                                                        | To be supplied                                                                                             | Layers × mm       |

<details class="rsh-parameter-details" markdown="1">
<summary>Temperature-dependent material parameters</summary>

List only material constants and complete temperature-dependent material tables here. Keep process settings, ambient temperature, thermal boundaries, heat-source inputs and numerical controls in the printing/simulation summary tables and full configuration downloads. Preserve every temperature node and provide matching YAML, JSON and CSV downloads. Label material properties with $C_{\mathrm{p}}$, $k$, $\alpha$, $E$, $\nu$, $\sigma_{\mathrm{y}}$, $H$, and $\sigma_{\mathrm{max}}$. Use mathematical notation for variables wherever they occur, with upright subscripts. Display inherent strains with superscript stars and three decimal places; preserve full precision in the downloadable data.

</details>

## Results

Keep figure captions short: name the result, direction and location, for example “$X$-direction stress at $X$ = 7.5 mm.” State calibration/validation scope and parameter versions in the surrounding text or downloadable metadata.

<!-- Example result image:
<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

<div class="rsh-case-figure-content" markdown="1">

![Describe the stress component, units, and comparison.](/assets/img/cases/your-case/stress.png)

_Figure 2. $X$-direction stress at $X$ = 7.5 mm._

</div>

</figure>

</div>
-->

---

_Original article: not yet supplied._

<!-- Replace the line above with a normal Markdown citation link:
Original article: [Authors, article title, journal, year.](https://doi.org/VERIFIED-DOI)
-->
