# Residual Stress Hub

## 定位与结构

继续使用当前域名。网站采用主题优先的研究资源定位，不以个人照片、履历或个人新闻作为首页内容。

- `/`：Hub 首页，介绍范围和栏目入口。
- `/benchmarks/`：Benchmarks 算例库，使用 `/benchmarks/`，不再作为个人 Project 展示；旧 `/projects/` 直接展示同一份算例列表，不经过跳转页。
- `/methods/`：完整热固耦合分析（Full thermal-mechanical analysis）和固有应变法分析（Inherent strain analysis）两个方法的简短介绍。
- `/resources/`：维护者的 GitHub 主页入口，可在确认后添加实际代码库或数据链接。
- 不设置独立 `/publications/` 页面；原入口源码只保留在不发布的归档目录。

原首页、个人简介及原论文列表入口备份在 `docs/archive/`。`docs/` 在站点配置中被排除，不会发布成网页。无关模板页面和模板项目已删除，不作为真实研究案例发布。

本站是独立维护的研究资源。Resources 当前仅链接到维护者的 GitHub 主页，不展示外部机构或参考网站的资源卡片。

## 统一导航与简洁页面

所有页面共享核心主题的一套顶部导航：**Home / Benchmarks / Methods / Resources**。不新增 Publications，也不为单个算例添加全站导航按钮。

站内链接直接指向 `/benchmarks/`。`_pages/projects_legacy.md` 仅兼容旧入口，正文与 `_pages/projects.md` 的列表保持一致；修改列表结构时需要同步这两个文件。它不显示过渡文案，也不设置 `redirect`。

Benchmarks 页面只显示一段简介、算例卡片或简短空状态；Methods 只介绍两种计算方法，不在 Benchmarks 底部再堆一组说明卡片。算例详情页保留返回 Benchmarks 的文字链接和正文，不添加第二排按钮、章节导航或侧栏目录。

`_config.yml` 对 `projects` 集合统一设置 `nav: false`、`toc: false`、`related_publications: false`，避免把算例加进顶部菜单、生成目录或调用个人 bibliography。新算例不要自行开启这些选项，原文链接直接写在正文最底部，不需要填写额外的 YAML 论文数据。

首页大标题居中、放大至桌面最高 4.2rem，并保持一行显示；栏目卡片和 Methods 面板不使用数字序号。各面板直接显示正文标题，不添加橙色小标题或分类标签。首页欢迎语位于大标题之后、动画之前，以加粗欢迎句开头，后续段落使用正文的灰色。

## 页面正文的 Markdown 写法

首页、Benchmarks、Methods 和 Resources 的正文使用 Markdown 标题、段落、列表和文字链接。首页欢迎语、图片画廊和 GitHub 资源数据在 `_data/residual_stress_hub.yml` 中维护。首页展示动画画廊，Benchmarks 算例列表由 Liquid 自动读取 `_projects/`。

页面中保留的 `<div>`、`<section>` 和 `<article>` 用于现有布局，`markdown="1"` 让 Jekyll 解析容器内的 Markdown。编辑文字时保留容器，块与块之间留一个空行。`{: .rsh-readable}` 等属性行用于文字样式，`{#define-title}` 等属性行用于标题锚点；修改文字时保留它们。首页图片画廊保留少量 HTML，以维持布局与无障碍属性。

```markdown
## Start with the quantity of interest.

{: #define-title}

- State the computational problem and the intended outputs.
- Specify geometry, material, and manufacturing process.

[Explore resources]({{ '/resources/' | relative_url }})
```

## Cantilever

`_projects/cantilever.md` 现在是 Cantilever 算例，正式地址为 `/benchmarks/cantilever/`。旧 `/benchmarks/example-1/` 通过 `_pages/example_1_legacy.md` 直接复用同一正文，不显示跳转页，也不需要再次点击。Benchmarks 卡片自动读取算例标题、封面和地址；首页图片由 `hub.gallery` 单独选择。

页面使用已有求解器输出，包含真实网格截面、局部热–力历史、局部固有应变标定比较、宏观弹性应变和释放变形；没有重新运行求解器或生成虚构结果。图和表的导出来源、哈希与转换步骤记录在 `docs/cantilever-assets.json`，不包含私人绝对路径。原图的曲线、图例和实验点保持不变。五个算例的 Overview 使用维护者后来提供的完整几何 PDF 页面预览，分别命名为 `geometry-overview.png`；原始 PDF 位于各自的 `assets/pdf/cases/<case>/geometry-overview.pdf`。导入记录与哈希保存在 `docs/case-geometry-assets.json`。原 Cantilever 网格截面仍保留在素材目录中；新几何图和现有宏观输出不是重新运行所得的同一套输入快照。 如需重新导入，使用 `bin/import_cantilever_assets.py --output-dir <求解器输出目录> --macro-mesh <宏观INP网格>`；该工具需要本地 Python 环境中的 numpy、matplotlib、meshio 和 pymupdf，只用于素材准备，不属于网站运行依赖。重新导入后仍须核对正文参数版本，工具不会自动将旧结果升级为新结果。

当前打印配置与存档热历史的配置哈希不匹配；所选局部优化的固有应变也不同于已有宏观配置。正文分别注明当前输入、所选标定和存档输出，不把它们当成同一套已验证计算。页脚已引用维护者提供的 Phan 等（2019）原始 AM-Bench 文章，DOI 和书目信息已通过 Crossref 核对；存档图中各条实验曲线与原文测量条件的对应关系仍未逐项核实。

Cantilever 正文采用 Overview、Problem set、Results 三段普通 Markdown；Problem set 分为打印参数和模拟参数两类；两张概要表下方提供可展开的材料常数和温度相关材料表。Overview 使用中子衍射法和轮廓法的简短实验介绍；模拟表列出温度相关材料参数、常温参数和已有固有应变识别值。新算例模板也采用普通 Markdown。只需编辑标题、段落、表格、图片路径和图注；完整参数使用 `<details markdown="1">` 原生展开控件，内部仍是 Markdown 表格。所有数据随页面静态输出，不需要点击后加载，折叠时也存在于 HTML 中。`assets/data/cases/cantilever/thermal-parameters.json` 包含完整配置、单位与参数状态；`temperature-dependent-properties.csv` 逐条列出 61 个原始温度节点值，方便程序和 AI 读取。更新参数时应同步正文、JSON 和 CSV。新算例草稿保持 `published: false`；当前五个算例均已发布。

## 算例顺序与图片目录

工艺标签写在算例 `title` 的括号中：Single track (DED)、Thin-wall (WAAM)、Bridge (LPBF)、Cantilever (LPBF)、Double-cantilever (LPBF)。Thin-wall 的原始 YAML 没有明确的工艺字段，WAAM 是暂定的网站分类，待维护者确认。标题标签与配置数值分别维护。概要表不展示 Elements / input mesh scale、Laser-on time stepping、Laser-off steps / mechanics interval、Geometry / saved mesh dimensions、Number of local deposited layers、Scan region / track length 或局部模型边界；完整配置下载保留这些设置。热源尺寸与层厚达到 200 µm 时用 mm，低于 200 µm 时用 µm；同一热源半径组使用一致单位。结果图注和解释须写明物理量、分量、单位、计算状态、取样位置及对比对象。Bridge 文件名中的 `3p75` 是局部横坐标，不能写成全局 `X = 3.75 mm`。坐标换算以论文和下文的用图清单为准。

Benchmarks 按 **Single track → Thin-wall → Bridge → Cantilever → Double-cantilever** 排序，通过五个 Markdown 文件的 `importance: 1–5` 控制，桌面每行使用三列卡片，手机保持单列。Bridge 页面新增在 `_projects/bridge.md`，地址为 `/benchmarks/bridge/`。

图片目录依次为 `assets/img/cases/single_track/`、`assets/img/cases/thin-wall/`、`assets/img/cases/bridge/`、`assets/img/cases/cantilever/`、`assets/img/cases/double_cantilever/`。列表卡片只显示图片和算例名称。五张列表封面已按维护者要求恢复为提交 `3c62167` 中的原始用图，独立保存为各目录下的 `card-cover.png`；来源路径和 SHA-256 见 `docs/benchmark-card-cover-assets.json`。详情页的论文结果图、温度曲线及图注修正继续保留。封面和详情图分别维护，`docs/benchmark-manuscript-figures.json` 的 `card_cover` 控制列表封面，离线导入器不会再用详情图覆盖它。所有图片完整显示，不裁剪。

Single track、Thin-wall、Bridge 和 Double-cantilever 的参数与结果已整理，来源和复现步骤见下方“其他四个算例的数据与结果”。五个算例均保留已提供的几何图。

## 发布真实算例

这里的 **Case 是算例，不是个人科研 Project**：一个算例描述一个明确的计算问题，组织几何、材料、边界条件、模型设置、结果与比较。可以来自维护者的工作、文献或其他合法公开来源；必须明确署名、来源和复现范围，不默认归属于维护者，也不默认是已验证 benchmark。

推荐结构：**Overview → Problem set（打印参数和模拟参数）→ Results → 原文引用（页面最底部）**。新算例模板使用同样的两类参数表。

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

对外网站统一使用英文，包括导航、标题、描述、正文、表格、图片替代文本和原文链接提示。维护文档可保留中文。正文围绕以下内容组织：

1. **Overview**：算例背景、目标、关注量和适用范围，可以放封面或示意图。
2. **Problem set**：打印参数、模拟参数两张概要表；完整温度相关材料表、热边界和数值控制放在可展开表格中，提供 YAML / JSON / CSV 下载。
3. **Results**：结果图、量化指标、比较条件和局限性。

正文之后仅附原文章引用和链接，不添加第五个论文区域、论文列表或独立 Publications 页面。原文章未确认时标为“Original article: not yet supplied.”，不创建虚假链接。

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

只上传真实且获准公开的图片。上面是路径示例，不是已经存在的案例或文件。卡片封面统一使用维护者提供的应力云图，建议 PNG / JPG / WebP；保留科学图中的色标、单位和坐标说明。现有封面的文件和来源见上方“算例顺序与图片目录”。

### 2. Benchmarks 列表的封面

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

`img` 会用于 Benchmarks 列表；`image_alt` 是图片的文字说明。卡片显示图片、名称和 GitHub 目录按钮，`description` 仍可用于页面元数据。详情页的二级、三级标题采用更大、更粗的深色字体；深色模式使用浅色字体。`permalink` 必须是唯一的案例地址，不要设成 `/` 或 `/benchmarks/`，否则会与首页或列表页冲突。

`hub_case: true` 才会进入 Hub 列表；`published: false` 是草稿，不会发布。原来的 `1_project.md`、`2_project.md` 占位项目已删除；新算例从 `case_template.md` 复制，不要把模板示例文字当成研究成果发布。

### 每个算例的 GitHub 目录按钮

在 `_data/benchmark_repositories.yml` 为对应算例填写完整的 GitHub 目录地址：

```yaml
single-track: ""
thin-wall: ""
bridge: "https://github.com/OWNER/REPOSITORY/tree/main/path/to/bridge"
cantilever: ""
double-cantilever: ""
```

上面的 Bridge 地址只是格式示例。五个实际字段目前均为空，按钮显示 “GitHub directory · Coming soon” 且禁用；填入地址后自动成为可点击的链接，在新标签页打开对应目录。键名与算例地址的最后一段一致，新算例也按此规则添加。不需要修改页面模板。`/benchmarks/` 和旧 `/projects/` 共用这份数据。

### 3. 详情页中的结果图和表格

`img` 只控制列表封面，详情页的每张图都在正文显式插入。本站的 `baseurl` 为空，普通 Markdown 可以直接使用站内绝对路径：

```markdown
## Results

<div class="rsh-case-figures" markdown="1">

<figure class="rsh-case-figure" markdown="1">

![Elastic strain XX along the cantilever.](/assets/img/cases/cantilever/x11.png)

_Figure 1. Pre-release elastic strain XX at height 11 mm. Strain is dimensionless._

</figure>

<figure class="rsh-case-figure" markdown="1">

![Elastic strain ZZ along the cantilever.](/assets/img/cases/cantilever/z11.png)

_Figure 2. Pre-release elastic strain ZZ at height 11 mm. Strain is dimensionless._

</figure>

</div>
```

每张图片及对应图注、下载链接放在一个 `figure` 中，多个 `figure` 放在同一个 `rsh-case-figures` 容器中；内部仍用 Markdown。桌面每行两图，767px 及以下自动单列，单张图也保持一列的宽度。段落与图注之间留空行；图注用 `_..._` 即可。页面样式自动控制图片宽度、图注和表格排版。文件名与大小写必须和素材一致，提交时同时提交 Markdown 与素材。

参数表直接使用 Markdown：

```markdown
_Table 1. Printing conditions._

| Parameter       | Value | Unit |
| --------------- | ----- | ---- |
| Laser power     | 195   | W    |
| Scan speed      | 0.80  | m/s  |
| Layer thickness | 20    | µm   |
```

页面保留四个 `##` 一级正文分节；分节内部可以用 `###` 加小节。样式通过 `_config.yml` 中的 `projects` 默认 `_styles` 加载，不需要每篇再写样式链接。

## 页面底部的原文链接

直接在四部分之后写普通 Markdown 链接；核对作者、题目、年份和 DOI 后再替换占位文字：

```markdown
---

Original article: [Authors, article title, journal, year.](https://doi.org/VERIFIED-DOI)
```

未确认时保留 “Original article: not yet supplied.”。不再使用 `source_article` YAML 或 `papers` 列表，也不维护全站 Publications。

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

每个算例的原文使用上面的 Markdown 写法，只在对应详情页底部显示一个链接。代码/数据条目使用 `title`、`description`、`url`。只加入真实且获准公开的材料。

样式在 `assets/css/residual-stress-hub.css`：通过核心主题现有的 `--global-*` CSS 变量统一导航、链接和页脚的配色，Hub 内容组件限定在 `.rsh` 下；论文式算例样式限定在含 Overview 标题的正文 article 下。没有新增本地布局、Sass 覆盖、插件或 CSS 构建流程。

品牌保留维护者批准的 v8 RS 轮廓，按要求将表面改为石墨灰和拉丝银。当前资源为 `rs-logo-metal.webp`，网页图标和 iOS 图标使用同版缩小 PNG。品牌字样浅色模式采用石墨灰 `#263746` 与钢灰 `#708698`，深色模式采用银白 `#E0E6EB` 与浅钢灰 `#A5B9C8`；导航、链接、面板及页脚使用同色系。正文图表的色标和数据保留原样。内置 imagegen 的编辑提示词见 `docs/metal-logo-prompt.txt`，来源和资源哈希见 `docs/metal-logo-assets.json`；旧 v8 文件保留为源素材。

保持现有 `url` / `baseurl`；列表的 Liquid 链接使用 `relative_url`，算例普通 Markdown 使用本站空 `baseurl` 对应的根路径。若以后部署到子目录，需同步调整 Markdown 路径。运行时归属仍遵循 [架构说明](ARCHITECTURE.md)。

## CI 与模板博客示例

本网站已移除模板的 `_posts` 博客目录。评论、Distill、RTL 和 Marimo 的集成测试不应再依赖公开网站中的示例文章。

`test/integration_fixture_helpers.sh` 在各测试的临时目录生成最小测试页面；评论、Distill 和新插件测试通过 `--source` 构建这些临时页面，仍使用真实站点的主题和插件配置。生产部署不调用这个辅助脚本，因此不会恢复博客或把测试页面发布到 Hub。

如果 Actions 报错 `site/blog/.../index.html: No such file or directory`，应检查对应的测试输入与生成路径，而不是把示例博客重新加入网站或关闭全部测试。时区弃用提示和 notebook 高亮提示与此缺页错误不同。

## 已完成的模板清理

保留的公开页面只有首页、Benchmarks、Methods、Resources、旧 `/projects/` 兼容入口和 404 页面。算例库依次包含 Single track、Thin-wall、Bridge、Cantilever 和 Double-cantilever，五个算例均包含配置参数和已有结果；保留未发布的新算例模板，旧 Example 1 地址仅作为兼容入口。

已删除模板博客入口、教学、书籍、个人 CV、人员列表、Repositories、插件展示、Publications 和占位项目；移除了爱因斯坦的头像、论文条目、引文统计、简历数据/PDF，以及模板图片、音频、视频、Notebook、Plotly 演示和 README 示例截图。外部示例博客导入与简历 JSON 导入已清空，社交/合作者/期刊数据为空映射，不包含虚假身份信息。`_bibliography/papers.bib` 保留空文件接口，未来可添加经过核实的真实文献，但不生成独立论文栏目。

真实获奖记录 `_news/announcement_3.md` 仍保留；当前 news 集合 `output: false`，不会发布独立新闻网页。原个人简介的精确副本在 `docs/archive/personal-bio.md`。

Cantilever 的图片在 `assets/img/cases/cantilever/`，PDF 在 `assets/pdf/cases/cantilever/`，可下载表格在 `assets/data/cases/cantilever/`。之前准备的 `case-1/` 图片和视频目录保留，避免影响已有素材；新增素材建议统一使用算例名称。

简历生成、示例引文更新、模板仓库 star 图、README 截图、模板发布和旧模板 Lighthouse 报告任务已移除，避免自动恢复无关内容。部署、格式检查、插件测试与升级工具仍保留。`test/visual/hub.spec.js` 改为检查实际 Hub 路由、统一导航、直达算例、Markdown 结构和图片加载，不再对比上游个人主页模板。浏览器检查默认跟随本站空 `baseurl`，不再强制 `/al-folio`。

保留主题与数学、图表、图片等插件的现有依赖，以便后续算例使用；不在此次内容清理中重构插件。上游架构和功能文档保留作技术参考，其中通用模板示例不代表本站已发布内容。

## 本地实时预览

启动 Docker Desktop，在网站目录运行：

```bash
npm run dev
```

浏览器打开 `http://localhost:4000/`，Cantilever 直接访问 `http://localhost:4000/benchmarks/cantilever/`。编辑器和浏览器并排放，保存 Markdown、数据、图片或 CSS 后，Jekyll 自动重建，浏览器自动刷新。无需提交 GitHub；通用 Markdown 预览不能完整呈现本网站的 Liquid、主题和导航。

首次启动需要构建 Ruby 环境并下载依赖，以后使用缓存。终端保持运行，Ctrl+C 停止；也可以在另一个终端执行 `npm run dev:stop`。不使用 npm 时执行 `bash bin/preview` / `bash bin/preview stop`。修改配置文件后要重启服务；未发布的算例仍不显示。

本地专用配置是 `_config.preview.yml`，启动文件是 `docker-compose.preview.yml` 和 `Dockerfile.preview`。不修改 Mac 系统 Ruby，源码只读挂载，生成网站留在容器内部。本地直接显示原始图片，不做 ImageMagick 转换；GitHub 部署仍使用原来的生产配置。

页面与文件对应表见 [README](../README.md#edit-the-website)。Cantilever 与新算例模板正文均为普通 Markdown，可直接修改论文式段落、表格和图片。实时预览呈现实际主题，但不是可视化所见即所得编辑器。

## 首页欢迎语与图片画廊

首页顺序是：居中的单行大标题、英文欢迎介绍、8 个动画位置、一次性的三个栏目入口。不再重复展示算例列表或多个指向 Benchmarks 的按钮。

`_data/residual_stress_hub.yml` 的 `welcome: |` 保存简短、平实的 Markdown 欢迎语，说明分享增材制造宏观模拟工作与数据、推动残余应力和变形计算方法发展的目标，并保留欢迎讨论和使用 Python 的说明。修改各段落时保持 YAML 缩进和段落间空行。

`gallery` 中保留 8 个条目。桌面第一行依次为点热源、Single track、Thin-wall、Scan，第二行为 Bridge、Cantilever、Double-cantilever 和一个预留位置，Bridge 位于第二行第一列。每个条目的 `title` 仅用于维护和无障碍标签，卡片不显示文字。目前已有七个动画，第八个位置留空。动画均来自维护者提供的 AVI，以原时长自动循环播放；原帧率不超过 20 fps 时保留全部帧，更高帧率按约 20 fps 采样。首页展示版用白色背景覆盖左下角坐标轴和右侧色标、图例，再按全部原始帧中构件的联合范围收紧取景，四周约留 7% 余量，以固定视窗避免主体跳动或被截断。输出画布仍为 1164 × 656，卡片布局和尺寸不变。原 AVI 保存在各自的 `assets/video/cases/` 目录，帧数、时长、遮挡区域、取景边界和来源哈希见 `docs/home-animation-assets.json`。导入脚本为 `bin/import_home_animations.py`；换用不同相机或几何范围的素材时需重新检查脚本中的取景边界。图片与首帧地址附带内容哈希版本号，替换素材后更新版本号以刷新浏览器缓存。算例页面的应力结果图和原始 AVI 保留原有色标与坐标。画面上没有名称、介绍句、占位文字或按钮。

桌面画廊使用 4 列、2 行；1100px 及以下使用 2 列、4 行。动画自动循环播放，无轮播、拖动或手动播放按钮。设置了系统“减少动态效果”的浏览器通过 `<picture>` 自动显示静态 `poster`，其他浏览器播放动画；页面不依赖 JavaScript 播放。首页选图与 Benchmarks 封面相互独立。

首页 Logo 位于标题文字前，与单行标题一起居中，由 `_data/residual_stress_hub.yml` 的 `logo` 指定，当前使用上文记录的金属版 RS。`hero_background` 为蜂窝背景。算例详情页复用品牌标识，Benchmarks、Methods 和 Resources 使用工艺横幅及各自栏目标题。

布局在 `_pages/about.md`，样式在 `assets/css/residual-stress-hub.css`。图标路径由 `_config.yml` 的 `icon` 和 `apple_touch_icon` 指定。品牌资源及来源统一见上文“数据与样式”，旧文件只作历史素材。

## 大屏页面宽度

`_config.yml` 的 `max_width: 2200px` 控制外层容器上限，站点 CSS 将桌面容器宽度设为窗口的 70%，1100px 及以下改为 92%，导航、正文与页脚保持对齐。首页动画画廊和 Benchmarks 三列卡片使用可用宽度；欢迎语在所有屏幕宽度下均使用单栏。算例正文取消额外的 52rem 上限，参数表随外层展开，算例的几何图和结果图采用两列网格，同一行共享小标题的高度，图片顶部对齐；普通说明段落保留 90ch 阅读宽度，桌面单图最高 24rem，完整保留图例和坐标。手机算例图片改为单列并取消高度上限。手机仍使用单列算例卡片和两列首页画廊。修改配置后需重启本地预览。

## 其他四个算例的数据与结果

Single track、Thin-wall、Bridge 和 Double-cantilever 采用与 Cantilever 一致的 **Overview → Problem set → Results**。Problem set 分为 Printing parameters 和 Simulation parameters；材料常数及全部温度相关材料节点在原生 details 中静态输出；工艺、环境温度、热源及数值控制不在展开表中重复列出，完整设置保留在配置下载中，AI 和程序无需展开即可读取 HTML。下载的 YAML 保留物理与数值设置，去除本地路径与运行输出位置。

- **Single track**：配置为 IN718 沉积层和 Ti-6Al-4V 基板，600 W、6 mm/s、单层 0.67 mm。几何图的基板宽度为 30 mm，而保存网格的 Y 跨度为 10 mm，正文明确区别。封面使用用户提供的 `single_track_results.pdf`；Results 保留最后保存的应力场，200 s 冷却后的物理时间约为 206.66667 s。云图是原生未变形 Y=0 截面，未平滑；CSV 包含所有 29,170 个单元，包括 active 标记。
- **Thin-wall**：主页面使用四层钢薄壁，2245 W、8.33 mm/s、层高 2 mm、层间冷却 400 s。使用 Y=0 半模型和指定锚点释放。另提供独立二十层 YAML；不将二十层设置冒充四层结果。保存的回弹模长为 3.246338 mm，对应竖向分量为 3.242710 mm。没有保存的固有应变识别结果，也未生成识别值。
- **Bridge**：使用 Ti-6Al-4V、100 W、600 mm/s、层高 30 µm、hatch 105 µm；宏观激活是 36 × 0.25 mm。保存识别的常温 H 与宏观配置的 H 分别为 1.828 和 1.8139 GPa，独立列出。局部热历史保留原曲线；当前展示的校准图和宏观剖面采用下文的论文用图清单。旧三页校准图仍保存在素材目录。
- **Double-cantilever**：使用 IN718 `dc`，285 W、960 mm/s、层高 40 µm、hatch 110 µm、逐层旋转 67°，宏观激活是 36 × 0.515 mm。未合并 Ti-6Al-4V `dc2`。最新固有应变为 εxx=εyy≈−4.339316‰、εzz≈19.647142‰；存档对比图使用 εxx=εyy≈−4.672144‰、εzz≈15.520310‰，正文分别标注。局部流动塑性历史保留；校准与释放翘曲采用下文的论文用图清单，不重新求解。旧三页校准图仍保存在素材目录。

温度表保留每个属性自身的原始节点，CSV 逐区域列出所有配置点；常温参数从同一套表插值或使用端点保持，宏观常数另行列出。相变值、零硬化等模型设置不冒称实验测量。原图中参考曲线保留原标签；其他算例的完整原始文章引用尚未提供，本次不补造书目。

导入工具需要本地 numpy、matplotlib、meshio、PyYAML、PyMuPDF；不增加网站运行依赖。先运行素材/页面导入，再运行 Single track 云图导出：

```bash
python bin/import_benchmark_assets.py --output-dir <opt_output> --solver-dir <opt_IS>
python bin/render_single_track_stress.py --source <opt_output>/am_solver/track1/vtk/step_00204.vtu --qa-dir /tmp/hub-case-figure-qa --skill-scripts <nature-figure>/scripts
```

导入记录、来源哈希和转换规则在 `docs/benchmark-case-assets.json`，Single track 场数据说明在对应 `final-stress-metadata.json`。云图自动 PDF 字体和碰撞审查通过；单面板对齐审查记录为不适用。300 dpi PNG 用于网页，SVG/PDF 保留文字。旧导入记录仅描述当时的检查，当前页面用图以以下论文清单为准。

Benchmarks 卡片的 `card_title` 显示名称、工艺与材料；详情页标题仍使用 `title`。Single track 同时标注 IN718 沉积层和 Ti-6Al-4V 基板。Thin-wall 的材料牌号由维护者确认为 S355，配置内标识仍为 `thin_wall_steel`。

品牌标题与 Logo 共用上文的石墨灰和银灰。蜂窝背景保留银灰金属反光、细密沉积层纹和轻微颗粒表现，首页三个入口卡片底色透明。

## Benchmarks 论文用图核对与更新

当前五个算例的 Results 由 `docs/benchmark-manuscript-figures.json` 维护。该清单将论文 `Optimization_base_Inherent_strain_method/main.tex` 中的图号与网站图片、标题、图注和解释逐一对应。`figures/main/` 和 `figures/appendices/` 是当前论文用图来源，不使用历史 Overleaf_upload 快照。

- Thin-wall 原来的温度和三个应变历史 PNG 是空坐标轴，页面已移除这些引用，改用附录 B 的三个测点温度对比。测点坐标未提供，不推断位置。四层墙的释放总位移、释放增量和二十层墙的应力图分别说明。
- Bridge 和 Double-cantilever 的云图使用轴向弹性应变及 µε 色标。局部标定比较采用论文的应变 parity 和空间图，避免把应变图标成应力图。
- Bridge 竖直取样线为全局 x = −6.75 mm、y = 0，局部高度为 z − 10 mm。Cantilever 的 11 mm 是零件底部以上的名义高度，对应全局 z = −1.5 mm。
- Bridge、Cantilever 和 Double-cantilever 的有效局部历史图保留，解释其单位与局部模型范围。Double-cantilever 的历史图只有应变，不以温度历史命名。

如需重新导入求解器参数，先运行旧的素材导入工具，再执行下列最终用图更新，以免旧脚本恢复空图或旧图注：

```bash
python bin/import_manuscript_case_figures.py --manuscript-dir <overleaf>/Optimization_base_Inherent_strain_method
npx prettier _projects/*.md docs/benchmark-manuscript-*.json --write
```

该离线工具只需要 PyMuPDF。它复制原始 PDF 并以 180 dpi 渲染完整页面，不裁剪图、不改变曲线、图例或数值。导入记录及源文件 SHA-256 在 `docs/benchmark-manuscript-assets.json`，它取代旧记录中同一路径的结果图来源。几何、求解器输入及数值下载维持各自的原始来源记录，旧结果与当前配置是否对应仍须分别核对。

## 首页欢迎语与栏目横幅

首页欢迎语位于 `_data/residual_stress_hub.yml` 的 `welcome`，以 “Howdy! Welcome to Residual Stress Hub.” 开场。正文明确覆盖多种金属增材制造及修复工艺的残余应力模拟，目前重点为基于可微分有限元的固有应变法。

Benchmarks（含旧 `/projects/`）、Methods 和 Resources 的页顶采用 `page_background` 指定的虚化金属激光沉积横幅，不再重复显示网站 Logo。页面原有的 Benchmarks / Methods / Resources 标题居中叠放在背景上，使用与 Residual Stress Hub 一致的字体、字重和石墨灰配色；深色模式使用浅蓝灰。标题只出现一次，简介在横幅下方显示。当前网页使用带真实 alpha 通道的 `assets/img/residual-stress-hub/additive-manufacturing-banner-transparent.webp`，源 PNG 为同名文件。工厂背景已移除，仅保留喷嘴、熔池和金属构件。`.rsh-process-banner` 容器无固定底色，图片通过四周透明遮罩和轻度模糊融入当前主题。旧的非透明生成图仅作素材存档。这是装饰图，不代表实验记录或模拟结果。

该图片使用内置 imagegen 工具生成并去背景，当前透明版提示词见 `docs/additive-banner-transparent-prompt.txt`，原始生成提示词保存在 `docs/additive-banner-prompt.txt`。WebP 以 `cwebp -q 88 -alpha_q 100` 压缩并保留 alpha，路径附加内容哈希以刷新缓存。

Methods 等 Hub 内容区的代码块采用 13 px 字号和 1.5 倍行高，内边距为 0.65 rem / 0.85 rem。行内代码为正文的 0.8 倍，最低 12 px；代码底色和文字使用低对比的同色系背景，减少对正文阅读的干扰。代码内容不变。

## Methods 的并列结构与弱形式

两种方法均按 **Model and weak forms → Element activation → Solution procedure → Cutting and stress release → Implementation and results** 组织。热力法给出热传导和力平衡的标准弱形式；固有应变法给出同一机械弱形式，再说明固有应变如何进入本构更新。正文不列强形式。两者分别解释新单元的加载、已激活材料的状态继承，以及切割后改变约束、保留应力和塑性历史并重新求平衡的过程。优化与运行细节放在原生 details 中。

弱形式不使用 aligned 或显式换行，`.rsh-equation` 在窄屏内横向滚动，保持一条公式一行且不撑宽整页。背景资料链接位于 Methods 页脚。
