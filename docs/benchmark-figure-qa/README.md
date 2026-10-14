# Benchmark figure checks

The Single Track cover is rendered from the final saved solver field by `bin/render_single_track_stress.py`. The field values are preserved without smoothing, and the selection rule and source hash are provided in `assets/data/cases/single_track/final-stress-metadata.json`.

- Source audit: no failures. The two warnings concern the lack of TIFF output and the 300 dpi raster export being below a 600 dpi publication default. The website uses PNG at 300 dpi; editable vector SVG and PDF are also available.
- PDF glyph audit: minimum text size 10 pt; no text below the 5 pt floor.
- Rendered collision audit: passed, with no failures or warnings.
- Panel alignment audit: not applicable to this single-panel figure.
- Manual visual inspection was unavailable in this session. Browser tests check image loading, expandable tables, and horizontal overflow.

All other imported results use the original complete PDF pages or supplied PNG files, retaining their curves, labels, and scales. These audit records apply to the newly rendered Single Track figure only. Imported-asset provenance is recorded in `docs/benchmark-case-assets.json`.
