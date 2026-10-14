# Bridge images

Place this case's images in this directory.

- Card cover: use the filename configured in the case Markdown’s `img` field.
- Other result images can use descriptive names and be inserted in `_projects/bridge.md` with Markdown image syntax.
- To change the cover, update the page’s `img` field and provide a descriptive English `image_alt`.

Example:

```markdown
![Describe the stress component and units](/assets/img/cases/bridge/stress-contour.png)
```

The Overview uses `geometry-overview.png`, rendered from the supplied `bridge_geo.pdf`. The unmodified PDF is stored at `assets/pdf/cases/bridge/geometry-overview.pdf`.

The benchmark card currently uses `results-cover.png`, rendered from `bridge_results.pdf`. Its original PDF is stored at `assets/pdf/cases/bridge/results-cover.pdf`. Change `img` in the case Markdown to use a different cover.

Saved local histories, three-page calibration comparison, and six residual elastic-strain profiles are imported. The latest identification and the archived figure vector are distinguished in the page and JSON.

Figure/data provenance is recorded in `docs/benchmark-case-assets.json`. Complete inputs are downloadable in `assets/data/cases/` under this case’s directory.
