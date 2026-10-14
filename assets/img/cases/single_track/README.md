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

The benchmark card uses `single-track-results.png`, rendered from the complete supplied `single_track_results.pdf` without cropping or editing. Its original is stored at `assets/pdf/cases/single_track/single-track-results.pdf`. The card URL includes an image-hash version so updating the supplied figure also refreshes browser caches.

The Results section uses `results-cover.png`: final saved von Mises stress on the undeformed Y=0 section. The saved field is in MPa; coordinates are converted from meters to millimeters. No stress smoothing or deformation is applied. `results-cover.svg` and the PDF retain editable labels.

All 29,170 cell values are in `assets/data/cases/single_track/final-stress-cells.csv`. Time, source hash, section-selection rule, and color limits are in `final-stress-metadata.json`. Reproduce with `bin/render_single_track_stress.py`; automated glyph, collision, and single-panel alignment checks are recorded in `docs/benchmark-figure-qa/`. Manual visual review was unavailable in this session.
