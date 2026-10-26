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

The benchmark card and displayed result figures now use the canonical manuscript PDFs. See `docs/benchmark-manuscript-figures.json` for the figure-to-caption mapping and `docs/benchmark-manuscript-assets.json` for current source hashes. Earlier import records describe historical assets.

Saved local histories are retained with units and model scope. Displayed calibration plots and part-scale results now use the manuscript figures. Older comparison PDFs and additional profiles remain archived separately. The latest identification and archived figure vectors remain distinct.

Figure/data provenance is recorded in `docs/benchmark-case-assets.json`. Complete inputs are downloadable in `assets/data/cases/` under this case’s directory.
