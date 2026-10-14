# Double-cantilever images

Place this case's images in this directory.

- Card cover: use the filename configured in the case Markdown’s `img` field.
- Other result images can use descriptive names and be inserted in `_projects/double_cantilever.md` with Markdown image syntax.
- To change the cover, update the page’s `img` field and provide a descriptive English `image_alt`.

Example:

```markdown
![Describe the stress component and units](/assets/img/cases/double_cantilever/stress-contour.png)
```

The Overview uses `geometry-overview.png`, rendered from the supplied `double_cantilever.pdf`. The unmodified PDF is stored at `assets/pdf/cases/double_cantilever/geometry-overview.pdf`.

The benchmark card currently uses `results-cover.png`, rendered from `dc_results.pdf`. Its original PDF is stored at `assets/pdf/cases/double_cantilever/results-cover.pdf`. Change `img` in the case Markdown to use a different cover.

This page uses the IN718 `dc` case. Saved local histories, three-page calibration comparison, and released-warpage figure are imported. The latest identification and archived figure vector remain separate; the Ti-6Al-4V `dc2` case is not merged into this page.

Figure/data provenance is recorded in `docs/benchmark-case-assets.json`. Complete inputs are downloadable in `assets/data/cases/` under this case’s directory.
