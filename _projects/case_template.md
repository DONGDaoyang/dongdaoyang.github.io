---
layout: page
title: "Replace with the case title"
description: "Describe the computational problem, quantities of interest, and scope in English."
permalink: /benchmarks/replace-with-case-slug/
hub_case: true
nav: false
toc: false
published: false # Publish only after adding real case materials.
importance: 1
case_type: Computational case
img: # Add a real cover path, e.g. /assets/img/cases/your-case/cover.png.
image_alt: "Describe the cover image in English."
source_article:
  title: # Add the original article title.
  url: # Add a verified DOI or publisher URL; leave blank until confirmed.
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">

<div class="rsh">
  <div class="rsh-bottom-link"><a href="{{ '/benchmarks/' | relative_url }}">← All benchmarks</a></div>
  <p class="rsh-eyebrow">{{ page.case_type | escape }}</p>

  <section class="rsh-guide-section" id="overview" aria-labelledby="overview-title">
    <h2 id="overview-title">Overview</h2>
    <p>Introduce the background, computational objectives, quantities of interest, and scope in English. State whether the problem is original or taken from the literature.</p>
    {% if page.img and page.img != empty %}
    <figure><img class="rsh-case-image" src="{{ page.img | relative_url }}" alt="{{ page.image_alt | default: page.title | escape }}"></figure>
    {% endif %}
  </section>

  <section class="rsh-guide-section" id="problem-set" aria-labelledby="problem-set-title">
    <h2 id="problem-set-title">Problem set</h2>
    <p>Describe the geometry, materials, loading, boundary and initial conditions, and model assumptions. Add geometry or boundary-condition diagrams where helpful.</p>
  </section>

  <section class="rsh-guide-section" id="parameter-values" aria-labelledby="parameter-values-title">
    <h2 id="parameter-values-title">Parameter values</h2>
    <p>Provide real parameter values and their sources. Include units and applicable conditions for each entry; do not use placeholders as actual simulation inputs.</p>
    <div class="rsh-parameter-table">
      <table>
        <caption>Parameter values (not yet specified)</caption>
        <thead><tr><th scope="col">Parameter</th><th scope="col">Value</th><th scope="col">Unit</th><th scope="col">Notes / source</th></tr></thead>
        <tbody>
          <tr><th scope="row">Material properties</th><td>Not specified</td><td>Not specified</td><td>Material model, temperature dependence, and source</td></tr>
          <tr><th scope="row">Loading / process inputs</th><td>Not specified</td><td>Not specified</td><td>Loading conditions or process inputs and source</td></tr>
          <tr><th scope="row">Mesh size</th><td>Not specified</td><td>Not specified</td><td>Discretization and mesh settings</td></tr>
          <tr><th scope="row">Time increment</th><td>Not specified</td><td>Not specified</td><td>Time discretization and solver settings</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="rsh-guide-section" id="results" aria-labelledby="results-title">
    <h2 id="results-title">Results</h2>
    <p>Present actual result figures and comparison curves. Identify stress components, units, coordinate conventions, conditions, data sources, and limitations. Distinguish original-article results from reproduced results.</p>
  </section>

  <div class="rsh-source-link">
    {% if page.source_article.url and page.source_article.url != empty %}
    <p>Original article: <a href="{{ page.source_article.url | escape }}">{{ page.source_article.title | default: "Read the original article" | escape }}</a></p>
    {% else %}
    <p class="rsh-note">Original article: not yet supplied.</p>
    {% endif %}
  </div>
</div>
