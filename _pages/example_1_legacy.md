---
layout: page
title: Cantilever (LPBF)
description: "A printed cantilever: local thermal–mechanical response, inherent-strain calibration, residual elastic strain, and distortion after release."
permalink: /benchmarks/example-1/
nav: false
toc: false
related_publications: false
_styles: |
  @import url("/assets/css/residual-stress-hub.css");
---

{% assign cantilever = site.projects | where: "permalink", "/benchmarks/cantilever/" | first %}
{{ cantilever.content }}
