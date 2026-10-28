---
layout: page
title: Benchmarks
description: "Reproducible thermal-mechanical and inherent-strain simulation workflows, with complete process and material data. Contributions and discussion are welcome."
permalink: /benchmarks/
nav: true
nav_order: 1
toc: false
---

{% assign hub = site.data.residual_stress_hub %}

<div class="rsh rsh-page-brand rsh-process-banner" aria-hidden="true">
<img src="{{ hub.page_background | relative_url }}" alt="" aria-hidden="true" width="2172" height="724" fetchpriority="high">
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

{% assign case_slug = case.url | split: '/' | last %}
{% assign repository_url = site.data.benchmark_repositories[case_slug] | default: '' | strip %}

<div class="rsh-case-repository">
{% if repository_url != '' %}
<a class="rsh-repository-button" href="{{ repository_url | escape }}" target="_blank" rel="noopener noreferrer" aria-label="{{ case.title | escape }}: GitHub directory (opens in a new tab)">GitHub directory <span aria-hidden="true">↗</span></a>
{% else %}
<button class="rsh-repository-button" type="button" disabled aria-label="{{ case.title | escape }}: GitHub directory coming soon">GitHub directory <span class="rsh-repository-status">Coming soon</span></button>
{% endif %}
</div>

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
