---
layout: default
title: Home
permalink: /
nav: false # The core navbar adds the homepage automatically.
nav_order: 0
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">
{% assign hub = site.data.residual_stress_hub %}
{% assign cases = site.projects | where: "hub_case", true | where_exp: "case", "case.published != false" | sort: "importance" %}

<div class="rsh" id="hub-home">
  <section class="rsh-hero" aria-labelledby="hub-title">
    <div class="rsh-hero-copy">
      <p class="rsh-eyebrow">A FOCUSED RESEARCH RESOURCE</p>
      <h1 id="hub-title">Residual Stress <span>Hub.</span></h1>
      <p class="rsh-tagline">{{ hub.tagline }}</p>
      <p class="rsh-lead">{{ hub.intro }}</p>
      <div class="rsh-actions">
        <a class="rsh-button" href="{{ '/benchmarks/' | relative_url }}">Explore benchmarks <span aria-hidden="true">↗</span></a>
        <a class="rsh-secondary" href="{{ '/methods/' | relative_url }}">Start with the guide <span aria-hidden="true">→</span></a>
      </div>
      <p class="rsh-status"><span aria-hidden="true">●</span> {{ hub.status }}</p>
    </div>
    <figure class="rsh-visual">
      <div class="rsh-visual-label"><span>MATERIAL / INTERNAL VARIATION</span><span aria-hidden="true">01</span></div>
      <img src="{{ '/assets/img/residual-stress-hub/mesh.svg' | relative_url }}" alt="Conceptual illustration of a gray layered solid with orange internal accents, not a computed stress field." width="720" height="560" fetchpriority="high">
      <figcaption>Concept illustration — not measured or simulated stress data.</figcaption>
    </figure>
  </section>

  <section class="rsh-section" aria-labelledby="explore-title">
    <div class="rsh-heading"><p class="rsh-eyebrow">EXPLORE THE HUB</p><h2 id="explore-title">From a question to the evidence.</h2></div>
    <div class="rsh-grid">
      {% for item in hub.scope %}
      <article class="rsh-card">
        <span class="rsh-number" aria-hidden="true">{{ item.number }}</span>
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
        <a href="{{ item.url | relative_url }}">{{ item.action }} <span aria-hidden="true">→</span></a>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="rsh-section" aria-labelledby="cases-title">
    <div class="rsh-heading rsh-heading-row"><div><p class="rsh-eyebrow">BENCHMARK LIBRARY</p><h2 id="cases-title">From problem setup to results.</h2></div><a href="{{ '/benchmarks/' | relative_url }}">All benchmarks <span aria-hidden="true">→</span></a></div>
    {% if cases.size > 0 %}
    <div class="rsh-grid">
      {% for case in cases limit: 3 %}
      <article class="rsh-card">
        {% if case.img and case.img != empty %}<a class="rsh-case-cover" href="{{ case.url | relative_url }}"><img class="rsh-case-image" src="{{ case.img | relative_url }}" alt="{{ case.image_alt | default: case.title | escape }}" loading="lazy"></a>{% endif %}
        <p class="rsh-eyebrow">{{ case.case_type | default: "Computational case" }}</p>
        <h3><a href="{{ case.url | relative_url }}">{{ case.title | escape }}</a></h3>
        <p>{{ case.description }}</p>
      </article>
      {% endfor %}
    </div>
    {% else %}
    <div class="rsh-empty"><div><p class="rsh-eyebrow">CASE MATERIALS IN PREPARATION</p><h3>The library is being assembled.</h3><p>No case results have been published yet. Each case will include an overview, problem specification, parameter values, and results, with an original-article link at the bottom.</p></div><a href="{{ '/methods/' | relative_url }}">Case documentation guide <span aria-hidden="true">→</span></a></div>
    {% endif %}
  </section>

  <section class="rsh-section rsh-band" aria-labelledby="guide-title">
    <div><p class="rsh-eyebrow">METHODS & DOCUMENTATION</p><h2 id="guide-title">Make the comparison interpretable.</h2><p>A useful result needs more than a contour plot. Document what was modeled, what was compared, and which evidence supports the conclusion.</p></div>
    <a class="rsh-button" href="{{ '/methods/' | relative_url }}">Use the reporting guide <span aria-hidden="true">→</span></a>
  </section>

  <section class="rsh-section" aria-labelledby="scope-title">
    <div class="rsh-heading"><p class="rsh-eyebrow">ABOUT THIS HUB</p><h2 id="scope-title">A subject-first space for research.</h2></div>
    <p class="rsh-readable">This Hub organizes residual stress computational cases, not a personal project portfolio. Each case brings together its problem definition, model setup, results, and related literature. Its initial scope is metal additive manufacturing and numerical modeling. It is independently maintained; it is not an official university, laboratory, or standards-body platform.</p>
    <p class="rsh-note">External references are attributed to their original sources. A computational case is not described as a validated benchmark unless its specification and evidence support that claim.</p>
  </section>
</div>
