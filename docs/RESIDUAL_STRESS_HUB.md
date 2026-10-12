# Residual Stress Hub

## 定位与结构

继续使用当前域名。网站采用主题优先的研究资源定位，不以个人照片、履历或个人新闻作为首页内容。

- `/`：Hub 首页，介绍范围和栏目入口。
- `/benchmarks/`：Benchmarks 算例库，使用 `/benchmarks/`，不再作为个人 Project 展示；旧 `/projects/` 直接展示同一份算例列表，不经过跳转页。
- `/methods/`：编辑性的案例报告指南，不宣称是官方标准。
- `/resources/`：有来源归属的外部参考资源、代码和数据，不再设置全站论文栏目。
- 不设置独立 `/publications/` 页面；原入口源码只保留在不发布的归档目录。

原首页、个人简介及原论文列表入口备份在 `docs/archive/`。`docs/` 在站点配置中被排除，不会发布成网页。无关模板页面和模板项目已删除，不作为真实研究案例发布。

参考 PFHub 的案例规范、方法和资源组织方式，不复制其文本、标识、赞助商信息或官方身份。本站是独立维护的研究资源，不宣称获得学校、实验室、NIST 或其他机构背书。

## 统一导航与简洁页面

所有页面共享核心主题的一套顶部导航：**Home / Benchmarks / Methods / Resources**。不新增 Publications，也不为单个算例添加全站导航按钮。

站内链接直接指向 `/benchmarks/`。`_pages/projects_legacy.md` 仅兼容旧入口，正文与 `_pages/projects.md` 的列表保持一致；修改列表结构时需要同步这两个文件。它不显示过渡文案，也不设置 `redirect`。

Benchmarks 页面只显示一段简介、算例卡片或简短空状态；报告指南集中放在 Methods，不在 Benchmarks 底部再堆一组说明卡片。算例详情页保留返回 Benchmarks 的文字链接和正文，不添加第二排按钮、章节导航或侧栏目录。

`_config.yml` 对 `projects` 集合统一设置 `nav: false`、`toc: false`、`related_publications: false`，避免把算例加进顶部菜单、生成目录或调用个人 bibliography。新算例不要自行开启这些选项，原文链接使用模板自己的 `source_article` 数据。

## 已发布的页面样本：Example 1

`_projects/case_1.md` 发布在 `/benchmarks/example-1/`，英文标题为「Example 1」。它只示范页面结构，使用本站原创概念示意图，不包含真实计算结果、验证数据或关联论文。首页和 Benchmarks 都显示它的可点击卡片，并明确标注 `Illustrative sample`。

替换成真实算例时，修改该文件的题目、简介、封面、模型设置和结果，并补充 `source_article`。只有有充分验证证据时才去掉样本标记或宣称已验证 benchmark。未完成的其他算例保持 `published: false`。

## 发布真实算例

这里的 **Case 是算例，不是个人科研 Project**：一个算例描述一个明确的计算问题，组织几何、材料、边界条件、模型设置、结果与比较。可以来自维护者的工作、文献或其他合法公开来源；必须明确署名、来源和复现范围，不默认归属于维护者，也不默认是已验证 benchmark。

推荐结构：**Overview → Problem set → Parameter values → Results → 原文链接（页面最底部）**。

复制 `_projects/case_template.md` 为新的算例文件，修改标题和唯一的 `permalink`，填写正文和图片。该模板默认 `published: false`，不发布占位内容。`_projects` 只是沿用 Jekyll 集合名，不代表页面内容是个人项目。

将案例 Markdown 放在 `_projects/` 中，只有 `hub_case: true` 的案例进入列表。删去旧模板的占位内容，不要仅修改标题后就发布。

```yaml
---
layout: page
title: "Replace with the real case title"
description: "Describe the computational problem, quantities of interest, and scope in English."
permalink: /benchmarks/your-case/
hub_case: true
published: false # 材料确认后才改为 true
importance: 1
case_type: Computational case
img: /assets/img/cases/your-case/cover.png
image_alt: "Describe the objects and comparison shown in the real figure."
---
```

对外网站统一使用英文，包括导航、标题、描述、正文、表格、图片替代文本和原文链接提示。维护文档可保留中文。正文仅分为四部分：

1. **Overview**：算例背景、目标、关注量和适用范围，可以放封面或示意图。
2. **Problem set**：几何、材料、载荷、边界条件、初始条件和模型假设。
3. **Parameter values**：参数名称、取值、单位和来源，以及网格、时间步长等计算设置。
4. **Results**：结果图、量化指标、比较条件和局限性。

四部分之后仅附一个原文章链接，不添加第五个论文区域、论文列表或独立 Publications 页面。原文章未确认时标为“Original article: not yet supplied.”，不创建虚假链接。

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
title: "Replace with the real case title"
description: "Describe the case in English."
permalink: /benchmarks/your-case/
hub_case: true
published: true # 仅在图片和正文确认可以公开后开启
importance: 1
case_type: Computational case
img: /assets/img/cases/your-case/cover.png
image_alt: "Describe the objects and results in the cover image."
---
```

`img` 会用于首页案例卡片和 Benchmarks 列表；`image_alt` 是图片的文字说明。`permalink` 必须是唯一的案例地址，不要设成 `/` 或 `/benchmarks/`，否则会与首页或列表页冲突。

`hub_case: true` 才会进入 Hub 列表；`published: false` 是草稿，不会发布。原来的 `1_project.md`、`2_project.md` 仍是隐藏的模板，不要把里面的示例文字当成研究成果发布。

### 3. 详情页中的结果图

`img` 不会自动出现在详情页正文中，需要另外插入。普通 Markdown 图片写法：

```markdown
![Describe the stress component, units, and comparison.]({{ '/assets/img/cases/your-case/stress-map.png' | relative_url }})

Figure 1. Describe the actual conditions, stress component, units, and data source.
```

需要控制宽度并绑定图注时，可以使用：

```html
<figure>
  <img
    src="{{ '/assets/img/cases/your-case/comparison.png' | relative_url }}"
    alt="Describe the comparison and axes."
    style="display: block; width: 100%; height: auto;"
    loading="lazy"
  />
  <figcaption>Figure 2. Describe the actual comparison conditions, units, and source.</figcaption>
</figure>
```

文件名和大小写必须与实际图片一致。上传时同时提交案例 Markdown 和图片文件，不要只提交 `img` 路径。

## 页面底部的原文链接

在算例文件顶部 YAML 中填写 `source_article`，模板会在 Results 后显示一个原文链接：

```yaml
source_article:
  title: "Original article title"
  url: # 填写核对过的 DOI 或出版社完整链接。
```

`title` 作为链接文字，`url` 是原文地址。未确认时把 `url` 留空，页面显示“Original article: not yet supplied.”。不再使用 `papers` 列表，也不维护全站 Publications。样本中没有虚构论文；拿到实际原文章后再补充。

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

每个算例的原文使用上面的 `source_article`，只在对应详情页底部显示一个链接。代码/数据条目使用 `title`、`description`、`url`。只加入真实且获准公开的材料。

样式在 `assets/css/residual-stress-hub.css`：通过核心主题现有的 `--global-*` CSS 变量统一导航、链接和页脚的配色，内容组件仍限定在 `.rsh` 下。没有新增本地布局、Sass 覆盖、插件或 CSS 构建流程。

配色采用橙色与中性灰色：灰色作为材料、结构和网格的视觉底色，橙色作为内部变化与重点信息的视觉强调。浅色模式使用深橙色文字以保持可读性，深色模式使用浅橙色强调。概念图的橙色带只是视觉隐喻，不表示已计算的应力分量、数值或拉压符号；实际结果图应另外提供真实色标、单位和坐标约定。首页和样本页保留非真实结果说明。

保持现有 `url` / `baseurl`，内部链接使用 `relative_url`。运行时归属仍遵循 [架构说明](ARCHITECTURE.md)。

## CI 与模板博客示例

本网站已移除模板的 `_posts` 博客目录。评论、Distill、RTL 和 Marimo 的集成测试不应再依赖公开网站中的示例文章。

`test/integration_fixture_helpers.sh` 在各测试的临时目录生成最小测试页面；评论、Distill 和新插件测试通过 `--source` 构建这些临时页面，仍使用真实站点的主题和插件配置。生产部署不调用这个辅助脚本，因此不会恢复博客或把测试页面发布到 Hub。

如果 Actions 报错 `site/blog/.../index.html: No such file or directory`，应检查对应的测试输入与生成路径，而不是把示例博客重新加入网站或关闭全部测试。时区弃用提示和 notebook 高亮提示与此缺页错误不同。

## 已完成的模板清理

保留的公开页面只有首页、Benchmarks、Methods、Resources、旧 `/projects/` 兼容入口和 404 页面。保留 Example 1 与未发布的新算例模板。

已删除模板博客入口、教学、书籍、个人 CV、人员列表、Repositories、插件展示、Publications 和占位项目；移除了爱因斯坦的头像、论文条目、引文统计、简历数据/PDF，以及模板图片、音频、视频、Notebook、Plotly 演示和 README 示例截图。外部示例博客导入与简历 JSON 导入已清空，社交/合作者/期刊数据为空映射，不包含虚假身份信息。`_bibliography/papers.bib` 保留空文件接口，未来可添加经过核实的真实文献，但不生成独立论文栏目。

你的照片 `assets/img/ddy.jpg`、`assets/img/ddy22.jpg` 和真实获奖记录 `_news/announcement_3.md` 没有删除；当前 news 集合 `output: false`，不会发布独立新闻网页。原个人简介的精确副本在 `docs/archive/personal-bio.md`。

Example 1 的图片与视频目录已准备好：`assets/img/cases/case-1/`、`assets/video/cases/case-1/`。其中 README 只说明用法，不是假素材，且被排除在部署之外。添加其他算例时按同样方式建立新目录。

简历生成、示例引文更新、模板仓库 star 图、README 截图、模板发布和旧模板 Lighthouse 报告任务已移除，避免自动恢复无关内容。部署、格式检查、插件测试与升级工具仍保留。`test/visual/hub.spec.js` 改为检查实际 Hub 路由、统一导航、直达算例、四段结构和图片加载，不再对比上游个人主页模板。浏览器检查默认跟随本站空 `baseurl`，不再强制 `/al-folio`。

保留主题与数学、图表、图片等插件的现有依赖，以便后续算例使用；不在此次内容清理中重构插件。上游架构和功能文档保留作技术参考，其中通用模板示例不代表本站已发布内容。
