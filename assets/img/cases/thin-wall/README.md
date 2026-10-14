# Thin-wall images

Place this case's images in this directory.

- Card cover: use the filename configured in the case Markdown’s `img` field.
- Other result images can use descriptive names and be inserted in `_projects/thin_wall.md` with Markdown image syntax.
- To change the cover, update the page’s `img` field and provide a descriptive English `image_alt`.

Example:

```markdown
![Describe the stress component and units](/assets/img/cases/thin-wall/stress-contour.png)
```

The Overview uses `geometry-overview.png`, rendered from the supplied `thin-wall_geo.pdf`. The unmodified PDF is stored at `assets/pdf/cases/thin-wall/geometry-overview.pdf`.

The benchmark card currently uses `results-cover.png`, rendered from `thin_wall_results.pdf`. Its original PDF is stored at `assets/pdf/cases/thin-wall/results-cover.pdf`. Change `img` in the case Markdown to use a different cover.

Saved temperature and XX/YY/ZZ strain histories are also imported. The page reports the numerical springback summary and links the complete history CSV. The four-layer and twenty-layer configurations remain separate.

Figure/data provenance is recorded in `docs/benchmark-case-assets.json`. Complete inputs are downloadable in `assets/data/cases/` under this case’s directory.
