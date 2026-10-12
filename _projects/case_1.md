---
layout: page
title: Example 1
description: "An illustrative case-page sample showing problem setup, parameter values, and results. No computation or validation has been performed."
permalink: /benchmarks/example-1/
hub_case: true
nav: false
toc: false
published: true # Public page sample, not a validated benchmark.
importance: 1
case_type: Illustrative sample · Not validated
img: /assets/img/residual-stress-hub/mesh.svg
image_alt: "Conceptual layered solid and mesh with orange internal accents; not an actual case model or stress result."
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
    <p>Example 1 demonstrates the structure of a benchmark page. No computation or validation has been performed; this sample is not a research result or validation evidence.</p>
    {% if page.img and page.img != empty %}
    <figure><img class="rsh-case-image" src="{{ page.img | relative_url }}" alt="{{ page.image_alt | default: page.title | escape }}"><figcaption class="rsh-note">Concept illustration only — not an actual model or computed result.</figcaption></figure>
    {% endif %}
  </section>

  <section class="rsh-guide-section" id="problem-set" aria-labelledby="problem-set-title">
    <h2 id="problem-set-title">Problem set</h2>
    <p>A real case specifies its geometry, materials, loading, boundary and initial conditions, and model assumptions here. This sample does not yet define a physical problem or a solver model.</p>
  </section>

  <section class="rsh-guide-section" id="parameter-values" aria-labelledby="parameter-values-title">
    <h2 id="parameter-values-title">Parameter values</h2>
    <p>No computational parameters have been specified. The table below illustrates the reporting format; its empty values are placeholders, not actual simulation inputs.</p>
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
    <p>No stress contours, measurements, or comparison curves are available for this sample. A completed case presents its results here, identifying stress components, units, coordinate conventions, conditions, comparison sources, and limitations.</p>
  </section>

  <div class="rsh-source-link">
    {% if page.source_article.url and page.source_article.url != empty %}
    <p>Original article: <a href="{{ page.source_article.url | escape }}">{{ page.source_article.title | default: "Read the original article" | escape }}</a></p>
    {% else %}
    <p class="rsh-note">Original article: not yet supplied.</p>
    {% endif %}
  </div>
</div>
