---
layout: page
title: Resources
description: My GitHub profile and available project repositories.
permalink: /resources/
nav: true
nav_order: 3
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

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">
{% assign hub = site.data.residual_stress_hub %}

<div class="rsh" markdown="1">

Visit my GitHub profile to explore my public repositories and follow project updates.
{: .rsh-readable}

<div class="rsh-resource-list rsh-section" markdown="1">

{% for resource in hub.resources %}

<article class="rsh-resource" markdown="1">

<div markdown="1">

## [{{ resource.title }} <span aria-hidden="true">↗</span>]({{ resource.url }})

{{ resource.description }}

{{ resource.source }}
{: .rsh-note}

</div>

</article>

{% endfor %}

</div>

{% if hub.research_resources.size > 0 %}

<section class="rsh-section" aria-labelledby="materials-title" markdown="1">

<div class="rsh-heading" markdown="1">

## Available research materials. {#materials-title}

</div>

<div class="rsh-resource-list" markdown="1">

{% for resource in hub.research_resources %}

<article class="rsh-resource" markdown="1">

### [{{ resource.title }}]({{ resource.url }})

{{ resource.description }}

</article>

{% endfor %}

</div>

</section>

{% endif %}

</div>
