---
layout: default
title: Home
permalink: /
nav: false # The core navbar adds the homepage automatically.
nav_order: 0
---

<!-- Edit the welcome and gallery in _data/residual_stress_hub.yml. -->

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">
{% assign hub = site.data.residual_stress_hub %}

<div class="rsh" id="hub-home" markdown="1">

<section class="rsh-hero{% if hub.hero_background != empty %} rsh-hero-with-background{% endif %}" aria-labelledby="hub-title" markdown="1">

{% if hub.hero_background != empty %}
<img class="rsh-hero-background" src="{{ hub.hero_background | relative_url }}" alt="" aria-hidden="true" fetchpriority="high">
{% endif %}

<div class="rsh-hero-brand" markdown="1">

<h1 id="hub-title"><img class="rsh-logo" src="{{ hub.logo | relative_url }}" alt="" aria-hidden="true" width="200" height="160"><span class="rsh-brand-name"><span class="rsh-stress-name">Residual Stress</span> <span class="rsh-hub-name">Hub</span></span></h1>

</div>

</section>

<section class="rsh-welcome rsh-section" aria-label="Welcome to Residual Stress Hub" markdown="1">

{{ hub.welcome }}

</section>

<section class="rsh-section" aria-label="Research animations">

<div class="rsh-gallery" role="region" aria-label="Research animation gallery">

<div class="rsh-gallery-grid">
{% for slide in hub.gallery %}
<figure class="rsh-gallery-item" aria-label="{{ slide.title | escape }}">
{% if slide.image %}
<picture>
{% if slide.poster %}<source srcset="{{ slide.poster | relative_url }}" media="(prefers-reduced-motion: reduce)">{% endif %}
<img src="{{ slide.image | relative_url }}" alt="{{ slide.alt | escape }}" width="{{ slide.width }}" height="{{ slide.height }}" decoding="async"{% if forloop.first %} fetchpriority="high"{% endif %}>
</picture>
{% else %}
<div class="rsh-animation-placeholder" role="img" aria-label="Animation pending"></div>
{% endif %}
</figure>
{% endfor %}
</div>

</div>

</section>

<section class="rsh-section" aria-labelledby="explore-title" markdown="1">

<div class="rsh-heading" markdown="1">

## Explore the Hub {#explore-title}

</div>

<div class="rsh-grid" markdown="1">

{% for item in hub.scope %}

<article class="rsh-card" markdown="1">

### {{ item.title }}

{{ item.description }}

[{{ item.action }} <span aria-hidden="true">→</span>]({{ item.url | relative_url }})
{: .rsh-text-link}

</article>

{% endfor %}

</div>

</section>

</div>
