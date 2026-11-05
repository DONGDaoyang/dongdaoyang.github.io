---
layout: default
title: About
permalink: /
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/personal-home.css' | relative_url | bust_file_cache }}">

<div class="personal-home" markdown="1">

<section class="personal-hero" aria-labelledby="personal-name">
<div class="personal-intro" markdown="1">

<p class="personal-kicker">COMPUTATIONAL MECHANICS · HKUST</p>

# Daoyang Dong {#personal-name}

<p class="personal-role">PhD student · Hong Kong PhD Fellowship Scheme</p>

I am a PhD student in the [Department of Civil and Environmental Engineering](https://ce.hkust.edu.hk/) at the [Hong Kong University of Science and Technology](https://hkust.edu.hk/), working with [Prof. Tianju Xue](https://cetxue.people.ust.hk/) in the Computational Mechanics and Scientific Learning (CMSL) Lab.

My research focuses on **residual stress and distortion in metal additive manufacturing**, **differentiable finite element analysis**, and **optimization-based inherent strain methods**. I am interested in connecting physical models, numerical simulation, and gradient-based optimization.

I received my B.S. and M.S. degrees in Civil Engineering from [Southeast University](https://www.seu.edu.cn/english/) in 2021 and 2024, respectively, and joined the CMSL Lab in February 2025.

<nav class="personal-links" aria-label="Contact and research profiles">
<a href="mailto:ddongac@connect.ust.hk">Email</a>
<a href="https://github.com/DONGDaoyang">GitHub</a>
<a href="https://orcid.org/0009-0002-8854-9964">ORCID</a>
</nav>

</div>
<figure class="personal-portrait">
<img src="{{ '/assets/img/personal/daoyang-dong.jpg' | relative_url }}" alt="Daoyang Dong" width="360" height="270" fetchpriority="high">
<figcaption>Hong Kong University of<br>Science and Technology</figcaption>
</figure>
</section>

<section class="personal-section" aria-labelledby="research-interests" markdown="1">

## Research interests {#research-interests}

- **Metal additive manufacturing:** thermal-mechanical process simulation, residual stress, and distortion.
- **Differentiable simulation and optimization:** finite element analysis, parameter calibration, and inherent strain methods.
- **Efficient computational modeling:** computational acceleration for process simulation and manufacturing-related problems.

</section>

<section class="personal-section" aria-labelledby="selected-projects" markdown="1">

<div class="personal-section-heading">
<h2 id="selected-projects">Selected projects</h2>
<a href="{{ '/projects/' | relative_url }}">All projects →</a>
</div>

<article class="personal-project">
<a class="personal-project-preview" href="https://github.com/CMSL-HKUST/Opt-IS" aria-label="Opt-IS source code"><img src="{{ '/assets/img/personal/opt-is-simulation.png' | relative_url }}" alt="Temperature field in a single-track additive manufacturing simulation" width="1164" height="656" loading="lazy"></a>
<div markdown="1">

### [Opt-IS](https://github.com/CMSL-HKUST/Opt-IS)

A finite element workflow connecting local thermal-mechanical simulation, optimization of inherent strain, and macroscale residual stress and distortion prediction. Built on JAX-FEM and automatic differentiation.

<p class="personal-project-meta">Differentiable simulation · Additive manufacturing</p>

</div>
</article>

</section>

<section class="personal-section" aria-labelledby="selected-publications" markdown="1">

<div class="personal-section-heading">
<h2 id="selected-publications">Selected publications</h2>
<a href="{{ '/publications/' | relative_url }}">All publications →</a>
</div>

{% assign selected = site.data.personal_publications | where: 'kind', 'journal' | where: 'selected', true %}
{% for paper in selected %}

<article class="personal-paper">
<h3><a href="{{ paper.url }}">{{ paper.title | escape }}</a></h3>
<p class="personal-authors">{% for author in paper.authors %}{% if author == 'Daoyang Dong' %}<strong>{{ author }}</strong>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}</p>
<p class="personal-venue"><em>{{ paper.journal }}</em>, {{ paper.year }}.</p>
</article>
{% endfor %}

</section>

<section class="personal-section" aria-labelledby="education" markdown="1">

## Education {#education}

<div class="personal-education">
<div><span class="personal-date">2025–present</span><p><strong>Hong Kong University of Science and Technology</strong><br>PhD studies in Civil Engineering · Hong Kong PhD Fellowship Scheme</p></div>
<div><span class="personal-date">2021–2024</span><p><strong>Southeast University</strong><br>Master's degree in Civil Engineering</p></div>
<div><span class="personal-date">2017–2021</span><p><strong>Southeast University</strong><br>Bachelor's degree in Civil Engineering</p></div>
</div>

</section>

<section class="personal-section" aria-labelledby="recognition" markdown="1">

## Selected honors {#recognition}

<div class="personal-honor" markdown="1">

**AM-Bench 2025 Challenge** · With Shuheng Liao and Tianju Xue

- **1st place**, baseplate deflection prediction (CHAL-AMB2025-04-BD).
- **2nd place**, residual elastic strain prediction (CHAL-AMB2025-04-RS02).

[HKUST award record ↗](https://researchportal.hkust.edu.hk/en/prizes/am-bench-2025-challenge/)

</div>

</section>

</div>
