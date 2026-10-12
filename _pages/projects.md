---
layout: page
title: Benchmarks
description: "Residual stress cases: problem setup, parameter values, results, and original sources."
permalink: /benchmarks/
nav: true
nav_order: 1
toc: false
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">
{% assign cases = site.projects | where: "hub_case", true | where_exp: "case", "case.published != false" | sort: "importance" %}

<div class="rsh">
  <p class="rsh-eyebrow">RESIDUAL STRESS / BENCHMARK LIBRARY</p>
  <p class="rsh-readable">Select a case to explore its problem setup, parameter values, results, and original source. Illustrative page samples are clearly labeled and are not validated benchmarks.</p>
  {% if cases.size > 0 %}
  <div class="rsh-grid rsh-section">
    {% for case in cases %}
    <article class="rsh-card">
      {% if case.img and case.img != empty %}<a class="rsh-case-cover" href="{{ case.url | relative_url }}"><img class="rsh-case-image" src="{{ case.img | relative_url }}" alt="{{ case.image_alt | default: case.title | escape }}" loading="lazy"></a>{% endif %}
      <p class="rsh-eyebrow">{{ case.case_type | default: "Computational case" }}</p>
      <h2><a href="{{ case.url | relative_url }}">{{ case.title | escape }}</a></h2>
      <p>{{ case.description }}</p>
      <a href="{{ case.url | relative_url }}">View case <span aria-hidden="true">→</span></a>
    </article>
    {% endfor %}
  </div>
  {% else %}
  <div class="rsh-empty rsh-section"><div><p class="rsh-eyebrow">NOT YET PUBLISHED</p><h2>The library is being assembled.</h2><p>Cases will appear here when their materials are ready.</p></div></div>
  {% endif %}

</div>
