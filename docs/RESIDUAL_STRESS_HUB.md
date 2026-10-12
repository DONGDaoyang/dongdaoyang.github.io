# Residual Stress Hub

## 定位与结构

继续使用当前域名。网站采用主题优先的研究资源定位，不以个人照片、履历或个人新闻作为首页内容。

- `/`：Hub 首页，介绍范围和栏目入口。
- `/projects/`：Cases，保留原 URL，以免破坏原项目入口。
- `/methods/`：编辑性的案例报告指南，不宣称是官方标准。
- `/resources/`：有来源归属的外部参考资源，以及之后加入的真实论文、代码和数据。
- `/publications/`：保留旧地址，指向 Resources 中的研究输出。

原首页及原论文列表入口备份在 `docs/archive/`。`docs/` 在站点配置中被排除，不会发布成网页。旧模板项目设为 `published: false`，保留源码，不作为真实研究案例发布。

参考 PFHub 的案例规范、方法和资源组织方式，不复制其文本、标识、赞助商信息或官方身份。本站是独立维护的研究资源，不宣称获得学校、实验室、NIST 或其他机构背书。

## 发布真实案例

将案例 Markdown 放在 `_projects/` 中，只有 `hub_case: true` 的案例进入列表。删去旧模板的占位内容，不要仅修改标题后就发布。

```yaml
---
layout: page
title: "填写真实案例标题"
description: "填写研究问题和有证据支持的贡献。"
permalink: /projects/your-case/
hub_case: true
published: false # 材料确认后才改为 true
importance: 1
case_type: Research case
img: assets/img/research/your-figure.png
image_alt: "描述真实图中的比较对象。"
---
```

正文按以下结构组织：

1. **Problem specification**：研究问题、几何、材料、工况、输出量和适用范围。
2. **Model & assumptions**：模型、输入数据、边界条件、求解器和数值设置。
3. **Results & comparison**：真实结果图、量化指标、对比基准和局限性。
4. **Reproducibility & sources**：论文、版本、可用文件、许可及访问限制。

材料未确认时保持草稿状态。应力图要有分量、单位、色标和坐标约定；没有实证支撑时，不把普通案例称为经过验证的 benchmark。

## 数据与样式

共享内容位于 `_data/residual_stress_hub.yml`。`publications` 和 `research_resources` 目前为空，避免把示例文献、空仓库或不存在的数据作为成果。

论文条目使用 `title`、`citation`、`url`；代码/数据条目使用 `title`、`description`、`url`。只加入真实且获准公开的材料。

内容样式在 `assets/css/residual-stress-hub.css`，限定在 `.rsh` 下；没有增加本地主题覆盖、插件或 CSS 构建流程。首页概念图不是应力计算或测量结果。

保持现有 `url` / `baseurl`，内部链接使用 `relative_url`。运行时归属仍遵循 [架构说明](ARCHITECTURE.md)。
