# Daoyang Dong — personal homepage

Academic homepage at **https://dongdaoyang.github.io/**, built with Jekyll and al-folio.

## Edit the site

| Content                                              | File                               |
| ---------------------------------------------------- | ---------------------------------- |
| Biography, research interests, education, and honors | `_pages/about.md`                  |
| Publications                                         | `_data/personal_publications.json` |
| Publications page                                    | `_pages/publications.md`           |
| Research projects                                    | `_pages/projects.md`               |
| Portrait and project previews                        | `assets/img/personal/`             |
| Page styling                                         | `assets/css/personal-home.css`     |
| Site settings                                        | `_config.yml`                      |

See [content sources and maintenance notes](docs/PERSONAL-SITE.md).

## Local preview

Run `npm run dev` with Docker Desktop running, then open **http://localhost:4002/**. The personal site and Residual Stress Hub have separate source directories and Git remotes.

## Checks and publishing

Run `npm run lint:prettier`, `npm run lint:style-contract`, and `bundle exec jekyll build` from the repository root. As this is a user site at the root of `dongdaoyang.github.io`, its `baseurl` remains empty. Pushing `main` runs the deployment workflow, which builds the site and publishes the generated `gh-pages` branch.

## Residual Stress Hub

The independent research resource now lives at **https://rshub-am.github.io/**, with source in [rshub-am/rshub-am.github.io](https://github.com/rshub-am/rshub-am.github.io). Its local directory is `rshub-am.github.io`.

Compatibility redirects for the previous `/benchmarks/`, `/methods/`, and `/resources/` URLs are kept in `_pages/hub-redirects/`. Existing legacy assets are retained so direct links to previously published figures and data remain valid. Maintain new research-resource content in the separate Hub repository.
