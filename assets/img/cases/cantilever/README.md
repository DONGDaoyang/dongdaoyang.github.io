# Cantilever images

Place this case's images in this directory.

- Card cover: use the filename configured in the case Markdown’s `img` field.
- Other result images can use descriptive names and be inserted in `_projects/cantilever.md` with Markdown image syntax.
- To change the cover, update the page’s `img` field and provide a descriptive English `image_alt`.

Example:

```markdown
![Describe the stress component and units](/assets/img/cases/cantilever/stress-contour.png)
```

The Overview uses `geometry-overview.png`, rendered from the supplied `cantilever.pdf`. The unmodified PDF is stored at `assets/pdf/cases/cantilever/geometry-overview.pdf`.

The displayed detail-page result figures use the canonical manuscript PDFs. See `docs/benchmark-manuscript-figures.json` for the figure-to-caption mapping and `docs/benchmark-manuscript-assets.json` for current source hashes. Earlier import records describe historical assets.

The homepage uses `cantilever-animation.webp` (all 50 frames of the supplied `cantilever.avi`, looping at 10 fps). `cantilever-animation-poster.png` is its static first frame for reduced-motion preferences. The original AVI is preserved under `assets/video/cases/cantilever/`; provenance is in `docs/home-animation-assets.json`.

The benchmark list uses `card-cover.png`, restored byte-for-byte from the pre-revision cover in commit `3c62167`. The list cover is independent of the corrected detail-page figures. See `docs/benchmark-card-cover-assets.json` and the `card_cover` entry in `docs/benchmark-manuscript-figures.json`.
