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

The displayed detail-page result figures use the canonical manuscript PDFs. See `docs/benchmark-manuscript-figures.json` for the figure-to-caption mapping and `docs/benchmark-manuscript-assets.json` for current source hashes. Earlier import records describe historical assets.

This page uses the IN718 `dc` case. Saved local histories, three-page calibration comparison, and released-warpage figure are imported. The latest identification and archived figure vector remain separate; the Ti-6Al-4V `dc2` case is not merged into this page.

Figure/data provenance is recorded in `docs/benchmark-case-assets.json`. Complete inputs are downloadable in `assets/data/cases/` under this case’s directory.

The benchmark list uses `card-cover.png`, restored byte-for-byte from the pre-revision cover in commit `3c62167`. The list cover is independent of the corrected detail-page figures. See `docs/benchmark-card-cover-assets.json` and the `card_cover` entry in `docs/benchmark-manuscript-figures.json`.
