# Residual Stress Hub

## 定位与结构

继续使用当前域名。网站采用主题优先的研究资源定位，不以个人照片、履历或个人新闻作为首页内容。

- `/`：Hub 首页，介绍范围和栏目入口。
- `/benchmarks/`：Benchmarks 算例库，使用 `/benchmarks/`，不再作为个人 Project 展示；旧 `/projects/` 直接展示同一份算例列表，不经过跳转页。
- `/methods/`：编辑性的案例报告指南，不宣称是官方标准。
- `/resources/`：有来源归属的外部参考资源、代码和数据，不再设置全站论文栏目。
- 原 `/publications/` 页面设为 `published: false`，保留源码但不发布，也不放进导航。

原首页及原论文列表入口备份在 `docs/archive/`。`docs/` 在站点配置中被排除，不会发布成网页。旧模板项目设为 `published: false`，保留源码，不作为真实研究案例发布。

参考 PFHub 的案例规范、方法和资源组织方式，不复制其文本、标识、赞助商信息或官方身份。本站是独立维护的研究资源，不宣称获得学校、实验室、NIST 或其他机构背书。

## 统一导航与简洁页面

所有页面共享核心主题的一套顶部导航：**Home / Benchmarks / Methods / Resources**。不新增 Publications，也不为单个算例添加全站导航按钮。

站内链接直接指向 `/benchmarks/`。`_pages/projects_legacy.md` 仅兼容旧入口，正文与 `_pages/projects.md` 的列表保持一致；修改列表结构时需要同步这两个文件。它不显示过渡文案，也不设置 `redirect`。

Benchmarks 页面只显示一段简介、算例卡片或简短空状态；报告指南集中放在 Methods，不在 Benchmarks 底部再堆一组说明卡片。算例详情页保留返回 Benchmarks 的文字链接和正文，不添加第二排按钮、章节导航或侧栏目录。

`_config.yml` 对 `projects` 集合统一设置 `nav: false`、`toc: false`、`related_publications: false`，避免把算例加进顶部菜单、生成目录或调用个人 bibliography。新算例不要自行开启这些选项，论文区域使用模板自己的 `papers` 数据。

## 已发布的页面样本：算例1

`_projects/case_1.md` 发布在 `/benchmarks/example-1/`，标题为「算例1」。它只示范页面结构，使用本站原创概念示意图，不包含真实计算结果、验证数据或关联论文。首页和 Benchmarks 都显示它的可点击卡片，并明确标注 `Illustrative sample`。

替换成真实算例时，修改该文件的题目、简介、封面、模型设置和结果，并补充 `papers`。只有有充分验证证据时才去掉样本标记或宣称已验证 benchmark。未完成的其他算例保持 `published: false`。

## 发布真实算例

这里的 **Case 是算例，不是个人科研 Project**：一个算例描述一个明确的计算问题，组织几何、材料、边界条件、模型设置、结果与比较。可以来自维护者的工作、文献或其他合法公开来源；必须明确署名、来源和复现范围，不默认归属于维护者，也不默认是已验证 benchmark。

推荐结构：**算例封面/摘要 → 问题定义 → 模型设置 → 结果与比较 → 文件与复现 → 相关论文（页面最底部）**。

复制 `_projects/case_template.md` 为新的算例文件，修改标题和唯一的 `permalink`，填写正文和图片。该模板默认 `published: false`，不发布占位内容。`_projects` 只是沿用 Jekyll 集合名，不代表页面内容是个人项目。

将案例 Markdown 放在 `_projects/` 中，只有 `hub_case: true` 的案例进入列表。删去旧模板的占位内容，不要仅修改标题后就发布。

```yaml
---
layout: page
title: "填写真实案例标题"
description: "填写研究问题和有证据支持的贡献。"
permalink: /benchmarks/your-case/
hub_case: true
published: false # 材料确认后才改为 true
importance: 1
case_type: Computational case
img: assets/img/research/your-figure.png
image_alt: "描述真实图中的比较对象。"
---
```

正文按以下结构组织：

1. **Problem specification**：研究问题、几何、材料、工况、输出量和适用范围。
2. **Model & assumptions**：模型、输入数据、边界条件、求解器和数值设置。
3. **Results & comparison**：真实结果图、量化指标、对比基准和局限性。
4. **Reproducibility & sources**：版本、可用文件、许可及访问限制。
5. **Related papers**：在该算例页面底部列出相关论文，说明其与问题定义、方法或参考结果的关系。

材料未确认时保持草稿状态。应力图要有分量、单位、色标和坐标约定；没有实证支撑时，不把普通案例称为经过验证的 benchmark。

## 给每个案例添加图片

### 1. 图片文件放哪里

建议每个案例单独建一个目录，文件名用英文小写和短横线，避免空格；例如：

```text
assets/img/cases/your-case/
  cover.png
  stress-map.png
  comparison.png
_projects/your-case.md
```

只上传真实且获准公开的图片。上面是路径示例，不是已经存在的案例或文件。建议封面用 PNG / JPG / WebP，优先选能概括研究问题的几何图、应力图或对比图；保留科学图中的色标、单位和坐标说明。

### 2. 首页和 Benchmarks 列表的封面

在 `_projects/your-case.md` 最顶部的 YAML 区域设置：

```yaml
---
layout: page
title: "填写真实案例标题"
description: "填写案例说明"
permalink: /benchmarks/your-case/
hub_case: true
published: true # 仅在图片和正文确认可以公开后开启
importance: 1
case_type: Computational case
img: /assets/img/cases/your-case/cover.png
image_alt: "描述封面图展示的对象和结果。"
---
```

`img` 会用于首页案例卡片和 Benchmarks 列表；`image_alt` 是图片的文字说明。`permalink` 必须是唯一的案例地址，不要设成 `/` 或 `/benchmarks/`，否则会与首页或列表页冲突。

`hub_case: true` 才会进入 Hub 列表；`published: false` 是草稿，不会发布。原来的 `1_project.md`、`2_project.md` 仍是隐藏的模板，不要把里面的示例文字当成研究成果发布。

### 3. 详情页中的结果图

`img` 不会自动出现在详情页正文中，需要另外插入。普通 Markdown 图片写法：

```markdown
![描述应力分量、单位和比较对象。]({{ '/assets/img/cases/your-case/stress-map.png' | relative_url }})

图 1：填写真实图注，说明工况、应力分量、单位和数据来源。
```

需要控制宽度并绑定图注时，可以使用：

```html
<figure>
  <img
    src="{{ '/assets/img/cases/your-case/comparison.png' | relative_url }}"
    alt="描述比较对象和坐标轴。"
    style="display: block; width: 100%; height: auto;"
    loading="lazy"
  />
  <figcaption>图 2：填写真实对比条件、单位和图源。</figcaption>
</figure>
```

文件名和大小写必须与实际图片一致。上传时同时提交案例 Markdown 和图片文件，不要只提交 `img` 路径。

## 把论文放在算例详情页底部

模板已在正文最后提供 `Related papers` 区域，读取该算例顶部 YAML 中的 `papers`。只填写经过核对的真实论文；示例写法如下，不要原样发布：

```yaml
papers:
  - title: "真实论文标题"
    citation: "真实作者、年份、期刊及卷页信息"
    role: "Problem source" # 或 Method / Reference results 等，按实际关系填写
    note: "说明论文提供了哪些工况、模型或比较数据；区分原文结果和你的复现结果。"
    url: "填写核对过的 DOI 或出版社完整链接"
```

`title` / `citation` 用于标题和署名，`role` / `note` 解释关联，`url` 可省略（没有核实的链接时不创建假链接）。暂时没有相关论文就保留 `papers: []`。不再维护全站 Publications 列表，论文直接写进所属算例的 `papers`。

一篇论文可以关联多个算例；一个算例也可以关联多篇论文。新增算例时保留模板底部的 Liquid 循环，添加 `papers` 即可显示，不需要修改主题或 Gemfile。

## 导航和旧页面排查

Benchmarks 使用 `/benchmarks/` 地址，详情页应是 `/benchmarks/your-case/`；旧 `/projects/` 直接显示相同列表，不需要等待跳转或再次点击。当前个人域名仍作为 Hub 的域名使用，地址中出现 GitHub 用户名不代表页面跳回个人介绍。

全站品牌由 `_config.yml` 的 `title` 控制；核心主题还会使用 `first_name` / `last_name` 生成页脚及作者元数据，因此这些字段也使用 Hub 名称。研究成果中的真实作者署名不受影响。

若首页已更新但 Benchmarks 仍显示旧版：

1. 记录点击后地址栏中的完整地址，确认访问的是当前部署而不是旧书签或另一台本地服务。
2. 查看最新 `Deploy site` 是否成功完成；格式检查通过不代表部署也已完成。
3. 在无痕窗口访问当前站点，排除浏览器缓存。未确认前不要把缓存当成唯一原因。
4. 若使用本地 Jekyll 服务，修改 `_config.yml` 后需要停止并重新启动服务。
5. 若仍有问题，提供点击入口、最终 URL 和截图；避免在未复现前盲目改域名或链接。

## 数据与样式

共享内容位于 `_data/residual_stress_hub.yml`。`research_resources` 目前为空，避免把空仓库或不存在的数据作为成果；已移除全站 `publications` 数据项。

算例专属论文使用上面的 `papers`，只在对应详情页底部显示。代码/数据条目使用 `title`、`description`、`url`。只加入真实且获准公开的材料。

内容样式在 `assets/css/residual-stress-hub.css`，限定在 `.rsh` 下；没有增加本地主题覆盖、插件或 CSS 构建流程。首页概念图不是应力计算或测量结果。

保持现有 `url` / `baseurl`，内部链接使用 `relative_url`。运行时归属仍遵循 [架构说明](ARCHITECTURE.md)。
