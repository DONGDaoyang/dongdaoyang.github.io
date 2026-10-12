---
layout: page
title: Methods
description: A reporting guide for clear, reproducible residual stress computational cases.
permalink: /methods/
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">

<div class="rsh">
  <p class="rsh-eyebrow">METHODS / REPORTING GUIDE</p>
  <p class="rsh-readable">Use this checklist to document a computational case before sharing its results. This is the Hub's editorial guide, not an official standard or a claim that any particular model has been validated.</p>

  <section class="rsh-guide-section" id="define" aria-labelledby="define-title"><p class="rsh-eyebrow">01 / DEFINE THE PROBLEM</p><h2 id="define-title">Start with the quantity of interest.</h2><ul><li>State the computational problem and the intended outputs.</li><li>Specify geometry, material, manufacturing process, and the state at which results are evaluated.</li><li>For each stress output, identify the component, coordinate system, sign convention, location, and unit.</li><li>Describe the scope of the case and the conditions to which its conclusions apply.</li></ul></section>

  <section class="rsh-guide-section" id="document" aria-labelledby="document-title"><p class="rsh-eyebrow">02 / DOCUMENT THE MODEL</p><h2 id="document-title">Make assumptions visible.</h2><ul><li>Record the model formulation, constitutive assumptions, and material-property sources.</li><li>Describe loading, constraints, initial conditions, process inputs, and relevant coupling choices.</li><li>Report mesh or discretization, time increments, solver settings, software, and version.</li><li>Explain simplifications and document available convergence or numerical sensitivity checks.</li></ul></section>

  <section class="rsh-guide-section" id="compare" aria-labelledby="compare-title"><p class="rsh-eyebrow">03 / PRESENT THE COMPARISON</p><h2 id="compare-title">Keep the evidence next to the claim.</h2><ul><li>Label axes, color scales, units, and the state represented by every figure.</li><li>Identify the source and conditions of measurements or reference simulations.</li><li>Explain how comparison locations, quantities, and conditions are matched; note differences.</li><li>Define error or performance metrics and identify the baseline before quoting an improvement.</li><li>For timing comparisons, report hardware, problem size, solver settings, and which stages are timed.</li><li>Include uncertainty where available and state limitations where it is not.</li></ul></section>

  <section class="rsh-guide-section" id="share" aria-labelledby="share-title"><p class="rsh-eyebrow">04 / SHARE RESPONSIBLY</p><h2 id="share-title">Give readers a route to the source.</h2><ul><li>List related papers at the bottom of the case page. Explain whether each supplies the problem, method, or reference results, and credit its original authors.</li><li>Link available code, input files, and datasets; record their versions and licenses.</li><li>Describe files needed to reproduce the case and what cannot currently be shared.</li><li>Confirm permission to reuse figures and to publish collaborator or unpublished materials.</li></ul></section>

  <div class="rsh-bottom-link"><a href="{{ '/resources/' | relative_url }}">Explore original-source resources <span aria-hidden="true">→</span></a></div>
</div>
