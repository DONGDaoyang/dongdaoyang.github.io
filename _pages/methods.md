---
layout: page
title: Methods
description: Full thermal-mechanical analysis and inherent strain analysis for residual stress and deformation.
permalink: /methods/
nav: true
nav_order: 2
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

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">

<div class="rsh" markdown="1">

We study residual stress and deformation using two computational approaches.
{: .rsh-readable}

<section class="rsh-guide-section" id="thermo-mechanical" aria-labelledby="thermo-mechanical-title" markdown="1">

## Full thermal-mechanical analysis {#thermo-mechanical-title}

This approach follows the thermal and mechanical response throughout the manufacturing process. The temperature history, thermal expansion, and temperature-dependent material behaviour are used to resolve how residual stress and deformation develop during heating and cooling.

The model describes the heat source, material properties, process sequence, and mechanical constraints explicitly. It provides a detailed view of the process history, including the response after support removal.

</section>

<section class="rsh-guide-section" id="inherent-strain" aria-labelledby="inherent-strain-title" markdown="1">

## Inherent strain analysis {#inherent-strain-title}

This approach represents the accumulated irreversible deformation through an inherent strain field. The identified strain values are applied to a structural model to calculate residual stress and deformation without resolving every thermal cycle at the part scale.

Inherent strain values can be identified from local thermal-mechanical simulations or experimental measurements. Their calibration conditions and applicability are central to interpreting predictions for a complete part and its deformation after release.

</section>

</div>
