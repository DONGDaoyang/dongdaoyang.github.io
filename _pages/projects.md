---
layout: page
title: Cases
description: Problem specifications, research results, and their supporting evidence.
permalink: /projects/
nav: true
nav_order: 1
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">
{% assign hub = site.data.residual_stress_hub %}
{% assign cases = site.projects | where: "hub_case", true | where_exp: "case", "case.published != false" | sort: "importance" %}

<div class="rsh">
  <p class="rsh-eyebrow">RESIDUAL STRESS / CASE LIBRARY</p>
  <p class="rsh-readable">Each case connects a defined research question to a documented method and its evidence. Only supplied, reviewed research materials will appear in this library.</p>
  {% if cases.size > 0 %}
  <div class="rsh-grid rsh-section">
    {% for case in cases %}
    <article class="rsh-card">
      {% if case.img %}<img class="rsh-case-image" src="{{ case.img | relative_url }}" alt="{{ case.image_alt | default: case.title | escape }}" loading="lazy">{% endif %}
      <p class="rsh-eyebrow">{{ case.case_type | default: "RESEARCH CASE" }}</p>
      <h2><a href="{{ case.url | relative_url }}">{{ case.title }}</a></h2>
      <p>{{ case.description }}</p>
      <a href="{{ case.url | relative_url }}">Read the case <span aria-hidden="true">→</span></a>
    </article>
    {% endfor %}
  </div>
  {% else %}
  <div class="rsh-empty rsh-section"><div><p class="rsh-eyebrow">NOT YET PUBLISHED</p><h2>Case materials are being prepared.</h2><p>No simulation figures, measured data, or quantitative research claims have been published here yet. The former template projects are not research cases.</p></div></div>
  {% endif %}

  <section class="rsh-section" id="case-specification" aria-labelledby="specification-title">
    <div class="rsh-heading"><p class="rsh-eyebrow">CASE SPECIFICATION</p><h2 id="specification-title">A consistent format. Traceable evidence.</h2><p>Each future entry will use the following four-part structure.</p></div>
    <div class="rsh-grid rsh-grid-two">
      {% for field in hub.case_fields %}
      <article class="rsh-card"><span class="rsh-number" aria-hidden="true">0{{ forloop.index }}</span><h3>{{ field.title }}</h3><p>{{ field.detail }}</p></article>
      {% endfor %}
    </div>
  </section>
  <div class="rsh-bottom-link"><a href="{{ '/methods/' | relative_url }}">Continue to the reporting guide <span aria-hidden="true">→</span></a></div>
</div>
