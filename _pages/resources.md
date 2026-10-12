---
layout: page
title: Resources
description: Original-source references and available research materials.
permalink: /resources/
nav: true
nav_order: 3
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">
{% assign hub = site.data.residual_stress_hub %}

<div class="rsh">
  <p class="rsh-eyebrow">RESOURCES / ORIGINAL SOURCES</p>
  <p class="rsh-readable">External resources remain owned and maintained by their original providers. Inclusion here does not imply affiliation, endorsement, or compatibility with every residual stress case.</p>
  <div class="rsh-resource-list rsh-section">
    {% for resource in hub.resources %}
    <article class="rsh-resource"><div><p class="rsh-eyebrow">{{ resource.type }}</p><h2><a href="{{ resource.url }}">{{ resource.title }} <span aria-hidden="true">↗</span></a></h2><p>{{ resource.description }}</p><p class="rsh-note">Source: {{ resource.source }}</p></div></article>
    {% endfor %}
  </div>

  <section class="rsh-section" aria-labelledby="materials-title"><div class="rsh-heading"><p class="rsh-eyebrow">CODE & DATA</p><h2 id="materials-title">Available research materials.</h2></div>
    {% if hub.research_resources.size > 0 %}
    <div class="rsh-resource-list">{% for resource in hub.research_resources %}<article class="rsh-resource"><h3><a href="{{ resource.url }}">{{ resource.title }}</a></h3><p>{{ resource.description }}</p></article>{% endfor %}</div>
    {% else %}<p class="rsh-note">No case-specific code or datasets are published by this Hub yet. Public benchmark information is available from the original sources above.</p>{% endif %}
  </section>
</div>
