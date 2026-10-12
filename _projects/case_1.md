---
layout: page
title: 算例1
description: "算例页面样本：展示问题、模型、图片和参考文献的组织方式；不包含真实计算或验证结果。"
permalink: /benchmarks/example-1/
hub_case: true
nav: false
toc: false
published: true # Explicitly labeled page sample, not a validated research benchmark.
importance: 1
case_type: Illustrative sample · Not validated
img: /assets/img/residual-stress-hub/mesh.svg
image_alt: "分层几何和计算网格的概念示意图，不是实际算例模型或应力结果。"
material:
process:
papers: [] # Each item: title, citation, optional role, note, and verified url.
---

<link rel="stylesheet" href="{{ '/assets/css/residual-stress-hub.css' | relative_url }}">

<div class="rsh">
  <p class="rsh-note">页面样本 / 未进行计算或验证。以下内容用于展示 Benchmarks 的组织方式，不作为科研成果或验证依据。</p>
  <div class="rsh-bottom-link"><a href="{{ '/benchmarks/' | relative_url }}">← All benchmarks</a></div>
  <p class="rsh-eyebrow">{{ page.case_type | escape }}</p>
  {% if page.material %}<p class="rsh-note">Material: {{ page.material | escape }}</p>{% endif %}
  {% if page.process %}<p class="rsh-note">Process: {{ page.process | escape }}</p>{% endif %}
  {% if page.img and page.img != empty %}
  <figure><img class="rsh-case-image" src="{{ page.img | relative_url }}" alt="{{ page.image_alt | default: page.title | escape }}"><figcaption class="rsh-note">概念示意图，仅用于展示图片位置，不是应力云图或实际模型。</figcaption></figure>
  {% endif %}

  <section class="rsh-guide-section" id="problem" aria-labelledby="problem-title">
    <p class="rsh-eyebrow">01 / PROBLEM SPECIFICATION</p><h2 id="problem-title">问题定义</h2>
    <p>这是「算例1」的页面样本，演示如何把一个计算问题组织成独立页面。真实算例在这里说明几何、材料、工况、边界条件、输出量和来源；当前样本没有指定物理问题或计算参数。</p>
  </section>

  <section class="rsh-guide-section" id="model" aria-labelledby="model-title">
    <p class="rsh-eyebrow">02 / MODEL & SETTINGS</p><h2 id="model-title">模型与计算设置</h2>
    <p>真实算例在这里记录模型方程、材料参数、网格、时间步长、求解器和软件版本。此样本尚未设置模型，也未运行求解器，不提供虚构的材料参数或计算精度。</p>
  </section>

  <section class="rsh-guide-section" id="results" aria-labelledby="results-title">
    <p class="rsh-eyebrow">03 / RESULTS & COMPARISON</p><h2 id="results-title">结果与对比</h2>
    <p>此样本目前没有应力云图、测量数据或对比曲线。上面的图片只是概念示意图；真实结果放在这一节，并标明应力分量、单位、坐标约定、工况和数据来源。</p>
  </section>

  <section class="rsh-guide-section" id="reproducibility" aria-labelledby="reproducibility-title">
    <p class="rsh-eyebrow">04 / FILES & SOURCES</p><h2 id="reproducibility-title">文件与复现</h2>
    <p>此样本没有计算输入文件、代码或数据下载。真实算例可以在这里链接模型文件、代码仓库和数据，记录版本、许可和访问限制。</p>
  </section>

  <section class="rsh-guide-section" id="related-papers" aria-labelledby="papers-title">
    <p class="rsh-eyebrow">RELATED LITERATURE</p><h2 id="papers-title">相关论文</h2>
    <p class="rsh-note">相关论文只放在算例页面底部，用于说明问题、方法或参考结果的来源，不另设 Publications 页面。</p>
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
    <p class="rsh-note">此页面样本尚未关联论文；补充真实算例时，在文件顶部的 papers 中添加核对过的论文信息。</p>
    {% endif %}
  </section>
</div>
