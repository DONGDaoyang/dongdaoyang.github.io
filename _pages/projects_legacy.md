---
layout: page
title: Benchmarks
description: "Reproducible thermal-mechanical and inherent-strain simulation workflows, with complete process and material data. Contributions and discussion are welcome."
permalink: /projects/
nav: false
toc: false
sitemap: false
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

<!-- Edit headings, paragraphs, and lists in Markdown. Containers retain the page layout. -->

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url | bust_file_cache }}">
{% assign cases = site.projects | where: "hub_case", true | where_exp: "case", "case.published != false" | sort: "importance" %}

<div class="rsh" markdown="1">

{% if cases.size > 0 %}

<div class="rsh-grid rsh-section" markdown="1">

{% for case in cases %}

<article class="rsh-card rsh-benchmark-card" markdown="1">

{% assign case_cover_path = case.img | split: "?" | first %}
{% assign case_cover = site.static_files | where: "path", case_cover_path | first %}
{% if case_cover %}

<a class="rsh-case-cover" href="{{ case.url | relative_url }}" aria-label="{{ case.card_title | default: case.title | escape }}"><img class="rsh-case-image" src="{{ case.img | relative_url }}" alt="{{ case.image_alt | default: case.title | escape }}" loading="lazy"></a>
{: .rsh-cover-wrap}

{% endif %}

## [{{ case.card_title | default: case.title | escape }}]({{ case.url | relative_url }})

</article>

{% endfor %}

</div>

{% else %}

<div class="rsh-empty rsh-section" markdown="1">

<div markdown="1">

## The library is being assembled.

Cases will appear here when their materials are ready.

</div>

</div>

{% endif %}

</div>
