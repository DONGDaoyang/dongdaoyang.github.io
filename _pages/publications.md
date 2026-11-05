---
layout: page
title: Publications
description: Research carried out at HKUST from 2025 onward. My name is highlighted in the author lists.
permalink: /publications/
nav: true
nav_order: 1
---

<link rel="stylesheet" href="{{ '/assets/css/personal-home.css' | relative_url | bust_file_cache }}">

<div class="personal-publications">
{% assign groups = site.data.personal_publications | group_by: 'year' %}
{% for group in groups %}
<section class="personal-publication-year" aria-labelledby="year-{{ group.name }}">
<h2 id="year-{{ group.name }}">{{ group.name }}</h2>
<div>
{% for paper in group.items %}
<article class="personal-paper">
<h3><a href="{{ paper.url }}">{{ paper.title | escape }}</a></h3>
<p class="personal-authors">{% for author in paper.authors %}{% if author == 'Daoyang Dong' %}<strong>{{ author }}</strong>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}</p>
<p class="personal-venue"><em>{{ paper.journal }}</em>{% if paper.volume != empty and paper.volume %}, {{ paper.volume }}{% endif %}{% if paper.pages != empty and paper.pages %}, {{ paper.pages }}{% endif %} ({{ paper.year }}).{% if paper.kind == 'preprint' %} <span class="personal-tag">Preprint</span>{% endif %}</p>
<p class="personal-paper-links"><a href="{{ paper.url }}">{% if paper.kind == 'preprint' %}arXiv{% else %}DOI{% endif %} ↗</a>{% if paper.code %} · <a href="{{ paper.code }}">Code ↗</a>{% endif %}</p>
</article>
{% endfor %}
</div>
</section>
{% endfor %}
</div>
