# Single Track images

Place this case's images in this directory.

- Card cover: use the filename configured in the case Markdown’s `img` field.
- Other result images can use descriptive names and be inserted in `_projects/single_track.md` with Markdown image syntax.
- To change the cover, update the page’s `img` field and provide a descriptive English `image_alt`.

Example:

```markdown
![Describe the stress component and units](/assets/img/cases/single_track/stress-contour.png)
```

The Overview uses `geometry-overview.png`, rendered from the supplied `single_track_geo.pdf`. The unmodified PDF is stored at `assets/pdf/cases/single_track/geometry-overview.pdf`.

The Results section uses `results-cover.png`, rendered from the canonical manuscript's `fig02_single_track_stress.pdf`. The complete page includes the von Mises stress color scale in MPa. The axial and through-thickness profiles come from `fig02_track1_stress_comparison.pdf` and retain the manuscript's sampling coordinates and original legend.

The reviewed figure-to-caption mapping is in `docs/benchmark-manuscript-figures.json`, and current source hashes are in `docs/benchmark-manuscript-assets.json`. Re-import with `bin/import_manuscript_case_figures.py` after any legacy solver import.

The older section rendering (`results-cover.svg`) and cell data remain archived separately. All 29,170 saved cell values are in `assets/data/cases/single_track/final-stress-cells.csv`. Their time, source hash, and section-selection rule remain in `final-stress-metadata.json`. The old `bin/render_single_track_stress.py` can reproduce that section, but the final manuscript import must run afterward to restore the displayed manuscript figure.

The benchmark list uses `card-cover.png`, restored byte-for-byte from the pre-revision cover in commit `3c62167`. The list cover is independent of the corrected detail-page figures. See `docs/benchmark-card-cover-assets.json` and the `card_cover` entry in `docs/benchmark-manuscript-figures.json`.
