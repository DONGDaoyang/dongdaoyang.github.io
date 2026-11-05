---
layout: page
title: Projects
description: Research software and open computational resources.
permalink: /projects/
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/personal-home.css' | relative_url | bust_file_cache }}">

<div class="personal-projects" markdown="1">

<article class="personal-project personal-project-expanded">
<a class="personal-project-preview" href="https://github.com/CMSL-HKUST/Opt-IS" aria-label="Opt-IS source code"><img src="{{ '/assets/img/personal/opt-is-simulation.png' | relative_url }}" alt="Temperature evolution during a single-track additive manufacturing simulation" width="1164" height="656" loading="lazy"></a>
<div markdown="1">

## Opt-IS

**Optimization-based inherent strain modeling for additive manufacturing.**

Opt-IS connects local thermal-mechanical process simulation, gradient-based calibration of inherent strain, and macroscale residual stress and distortion prediction. The workflow builds on JAX-FEM and JAX automatic differentiation, with case configurations and input meshes for reproducible simulations.

[Source code ↗](https://github.com/CMSL-HKUST/Opt-IS)
{: .personal-project-links}

</div>
</article>

<article class="personal-project personal-project-expanded">
<a class="personal-project-preview" href="https://rshub-am.github.io/" aria-label="Visit Residual Stress Hub"><img src="{{ '/assets/img/personal/residual-stress-hub.png' | relative_url }}" alt="Elastic strain distribution in an additively manufactured cantilever" width="1164" height="656" loading="lazy"></a>
<div markdown="1">

## Residual Stress Hub

**Computational cases, methods, and related research resources.**

Residual Stress Hub collects residual stress simulation cases across metal additive manufacturing and repair processes. It connects problem specifications, model setups, and results to their original sources, with a current emphasis on inherent strain methods based on differentiable finite element analysis.

[Website ↗](https://rshub-am.github.io/) · [Source code ↗](https://github.com/rshub-am/rshub-am.github.io)
{: .personal-project-links}

</div>
</article>

<article class="personal-text-project" markdown="1">

## Physics-guided diffusion for inverse design

Collaborative research on using differentiable physical solvers to guide diffusion models for the inverse design of disordered metamaterials. The associated preprint studies effective thermal conductivity, load-displacement response, and energy absorption involving fractures.

[Preprint ↗](https://arxiv.org/abs/2603.16209) · [Code ↗](https://github.com/CMSL-HKUST/physics-guidance)
{: .personal-project-links}

</article>

</div>
