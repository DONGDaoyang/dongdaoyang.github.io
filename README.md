# Residual Stress Hub

An independent research resource for residual stress computational cases, computational methods, and source materials. Built with Jekyll and [al-folio](https://github.com/alshedivat/al-folio); not an official institutional benchmark platform.

## Edit the website

| Content                             | File                                      |
| ----------------------------------- | ----------------------------------------- |
| Home                                | `_pages/about.md`                         |
| Welcome, gallery and resource links | `_data/residual_stress_hub.yml`           |
| Benchmarks list                     | `_pages/projects.md`                      |
| Single Track                        | `_projects/single_track.md`               |
| Thin-wall                           | `_projects/thin_wall.md`                  |
| Bridge                              | `_projects/bridge.md`                     |
| Cantilever                          | `_projects/cantilever.md`                 |
| Double-cantilever                   | `_projects/double_cantilever.md`          |
| New case template (unpublished)     | `_projects/case_template.md`              |
| Methods                             | `_pages/methods.md`                       |
| Resources                           | `_pages/resources.md`                     |
| Brand logo and favicon              | `assets/img/residual-stress-hub/logo.svg` |
| Orange/gray styling                 | `assets/css/residual-stress-hub.css`      |
| Site configuration                  | `_config.yml`                             |

The homepage shows a larger, centered, single-line title, an English welcome that invites discussion and introduces Python as the main programming language, then eight animation slots in a four-column desktop grid. Cantilever uses the supplied AVI converted into a looping animated WebP; seven slots are reserved for future animations. Edit `welcome` (Markdown) and `gallery` (titles, animation paths, poster images, and alt text) in `_data/residual_stress_hub.yml`. Smaller screens use two gallery columns. Methods introduces full thermo-mechanical analysis and inherent strain analysis.

On desktop, the shared page container occupies 70% of the viewport, capped at 2200px. Screens up to 1100px use 92% to retain room for mobile content.

The old `/projects/` URL still shows the benchmark list. Keep `_pages/projects_legacy.md` synchronized with `_pages/projects.md` when changing the list markup.

## Case images and videos

The benchmark order is **Single Track → Thin-wall → Bridge → Cantilever → Double-cantilever**. The corresponding image folders are:

- `assets/img/cases/single_track/`
- `assets/img/cases/thin-wall/`
- `assets/img/cases/bridge/`
- `assets/img/cases/cantilever/`
- `assets/img/cases/double_cantilever/`

Benchmark cards show only the image and case name. Thin-wall, Bridge, Cantilever, and Double-cantilever use the supplied results PDFs rendered as `results-cover.png`; their original PDFs are preserved in `assets/pdf/cases/<case>/results-cover.pdf`. Single Track uses the final saved von Mises stress on the native Y=0 section, with the full cell field available as CSV. Import records and hashes are in `docs/case-results-cover-assets.json`. Each image folder has a short README.

Other Cantilever assets:

- Cantilever figures: `assets/img/cases/cantilever/`
- Original figure PDFs: `assets/pdf/cases/cantilever/`
- Downloadable tables: `assets/data/cases/cantilever/`
- Videos: create `assets/video/cases/cantilever/` when needed.
- For later cases, use one named subdirectory per case.

To replace a card cover, place the image in its case folder and update `img` and the English `image_alt` in the case Markdown. Covers appear only when the configured file exists. Insert figures in the case body with ordinary Markdown; `img` does not automatically add a figure to the body.

Cantilever has three sections: **Overview / Problem set / Results**, with printing and simulation parameter tables inside Problem set and the original-article citation at the bottom. All case pages and the new-case template use that same three-section structure. Use `##` headings, Markdown tables, and `![Description](image-path)` figures. The expandable parameter block uses native `<details markdown="1">` with Markdown tables inside it. Copy `_projects/case_template.md` for a new case. The Cantilever dropdown includes all configured temperature nodes, boundary conditions, heat-source inputs, and material constants. Downloadable JSON and CSV files in `assets/data/cases/cantilever/` provide the same values with units and parameter-status notes.

**Cantilever** is an AM-Bench case, assembled from saved solver outputs. Current printing inputs, selected local calibration, and archived macro comparisons are distinguished where their parameter versions differ. The original AM-Bench article by Phan et al. (2019) is cited at the bottom of the case page. Asset provenance is recorded in `docs/cantilever-assets.json`; see the maintenance guide for the editing workflow.

Single Track, Thin-wall, Bridge, and Double-cantilever are visible case entries with Markdown detail pages. All five cases include supplied geometry images in Overview. Their process and simulation tables now come from the supplied solver configurations. Results include saved stress fields, local histories, calibration comparisons, strain profiles, and warpage where available. Full temperature tables expand below the summary tables, with YAML/JSON/CSV downloads. Bridge and Double-cantilever distinguish the latest identification from the archived figure vector; Single Track and Thin-wall use full thermal–mechanical analysis without invented inherent-strain values. Geometry previews use `geometry-overview.png`, and unmodified PDFs are downloadable from each case page. Asset records are in `docs/case-geometry-assets.json`.

For image/video embedding, new cases, deployment, and troubleshooting, see [the maintenance guide](docs/RESIDUAL_STRESS_HUB.md).

## Local preview and checks

### Live preview (recommended on this Mac)

Start Docker Desktop, then run from the website directory:

```bash
npm run dev
# Without npm: bash bin/preview
```

Open `http://localhost:4000/` alongside your editor. Save a `.md`, data file, image, or CSS file: Jekyll rebuilds the page and LiveReload refreshes the browser. Cantilever is at `http://localhost:4000/benchmarks/cantilever/`; the old `/benchmarks/example-1/` URL displays the same case directly. No GitHub commit or push is required to preview edits.

The first launch builds a Ruby environment and downloads gems; later launches reuse it. Keep the command running while editing. Stop with Ctrl+C, or run `npm run dev:stop` in another terminal. Restart after changing `_config.yml` or `_config.preview.yml`.

Preview uses `docker-compose.preview.yml` and `_config.preview.yml`: the source is mounted read-only, generated files stay inside the container, and uploaded images are shown without ImageMagick preprocessing. Production deployment still uses `_config.yml` and the existing GitHub Pages domain (`baseurl: ""`).

### Native Ruby alternative

With Ruby/Bundler versions compatible with `Gemfile.lock`:

```bash
bundle install
bundle exec jekyll serve --config _config.yml,_config.preview.yml --livereload
```

Use the browser preview for the real theme, navigation, Liquid-generated content, and styles; a generic Markdown editor preview does not reproduce the whole Jekyll website.

### Checks

```bash
npm run lint:prettier
npm run lint:style-contract
bundle exec jekyll build
npx playwright install chromium webkit
npm run test:visual
```

The browser checks target the Hub routes and case navigation, not the removed template blog/CV/publications pages. Plugin integration tests generate isolated temporary fixtures; those fixtures are never published.

## Archived source material

The earlier biography/publications page sources are preserved in `docs/archive/`, which is excluded from the generated website. The real research award announcement (`_news/announcement_3.md`) is retained for possible future use. News currently does not generate standalone pages.

Unrelated template pages, Einstein metadata and assets, demo media, and template-only automation have been removed. Math, charts, images, video markup, and the existing theme/plugin setup remain available for future scientific cases.

Case import and reproducibility instructions: [case data documentation](docs/RESIDUAL_STRESS_HUB.md#其他四个算例的数据与结果).
