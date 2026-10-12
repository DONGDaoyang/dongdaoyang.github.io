---
layout: page
title: "Replace with the computational case title"
description: "Describe the computational problem and quantities of interest, not a personal achievement."
permalink: /benchmarks/replace-with-case-slug/
hub_case: true
nav: false
toc: false
published: false # Copy this template; publish only after replacing all instructions with real case materials.
importance: 1
case_type: Computational case
img: # Add the path to the real case cover, e.g. /assets/img/cases/your-case/cover.png.
image_alt: # Describe what the cover actually shows.
material:
process:
papers: [] # Each item: title, citation, optional role, note, and verified url.
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">

<div class="rsh">
  <div class="rsh-bottom-link"><a href="{{ '/benchmarks/' | relative_url }}">← All benchmarks</a></div>
  <p class="rsh-eyebrow">{{ page.case_type | escape }}</p>
  {% if page.material %}<p class="rsh-note">Material: {{ page.material | escape }}</p>{% endif %}
  {% if page.process %}<p class="rsh-note">Process: {{ page.process | escape }}</p>{% endif %}
  {% if page.img and page.img != empty %}
  <figure><img class="rsh-case-image" src="{{ page.img | relative_url }}" alt="{{ page.image_alt | default: page.title | escape }}"></figure>
  {% endif %}

  <section class="rsh-guide-section" id="problem" aria-labelledby="problem-title">
    <p class="rsh-eyebrow">01 / PROBLEM SPECIFICATION</p><h2 id="problem-title">The computational problem.</h2>
    <p>Replace with the real geometry, material, process, boundary conditions, quantities of interest, and source of the case. State whether this is an original problem, a literature-based case, or a reproduction.</p>
  </section>

  <section class="rsh-guide-section" id="model" aria-labelledby="model-title">
    <p class="rsh-eyebrow">02 / MODEL & SETTINGS</p><h2 id="model-title">How the case is computed.</h2>
    <p>Replace with the model formulation, assumptions, inputs, mesh, time steps, solver settings, and software version. Attribute methods and inputs to their actual sources.</p>
  </section>

  <section class="rsh-guide-section" id="results" aria-labelledby="results-title">
    <p class="rsh-eyebrow">03 / RESULTS & COMPARISON</p><h2 id="results-title">What the calculation shows.</h2>
    <p>Insert real figures and captions here. Identify stress components, units, coordinates, comparison conditions, and limitations. Distinguish results reproduced here from figures or data taken from a paper.</p>
  </section>

  <section class="rsh-guide-section" id="reproducibility" aria-labelledby="reproducibility-title">
    <p class="rsh-eyebrow">04 / FILES & SOURCES</p><h2 id="reproducibility-title">Inputs and reproducibility.</h2>
    <p>Link the actual input files, code, or datasets available for this case, with versions and licenses. State access restrictions and permission to reuse any source figures. If files are not available, say so.</p>
  </section>

  <section class="rsh-guide-section" id="related-papers" aria-labelledby="papers-title">
    <p class="rsh-eyebrow">RELATED LITERATURE</p><h2 id="papers-title">Related papers.</h2>
    <p class="rsh-note">Original sources for this case’s problem, methods, or reference results.</p>
    {% if page.papers.size > 0 %}
    <ol class="rsh-references">
      {% for paper in page.papers %}
      <li>
        <h3>{% if paper.url and paper.url != empty %}<a href="{{ paper.url | escape }}">{{ paper.title | escape }}</a>{% else %}{{ paper.title | escape }}{% endif %}</h3>
        <p>{{ paper.citation | escape }}</p>
        {% if paper.role %}<p class="rsh-eyebrow">{{ paper.role | escape }}</p>{% endif %}
        {% if paper.note %}<p>{{ paper.note | escape }}</p>{% endif %}
      </li>
      {% endfor %}
    </ol>
    {% else %}
    <p class="rsh-note">No related papers have been added for this case yet.</p>
    {% endif %}
  </section>
</div>
