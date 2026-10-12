#!/usr/bin/env bash
# Isolated source pages for plugin integration tests. Never restore the starter's
# demo blog into a customized site just to satisfy test assertions.

prepare_plugin_fixture() {
  local source_dir="$1"
  local suite="$2"
  mkdir -p "${source_dir}/_posts"

  # Merge after the real site config, retaining its theme and plugin wiring.
  # These unrelated inputs are not needed to test rendering/asset contracts.
  cat >"${source_dir}/_config.yml" <<'YAML'
external_sources: []
jekyll_get_json: []
imagemagick:
  enabled: false
related_blog_posts:
  enabled: false
YAML

  cat >"${source_dir}/index.md" <<'MARKDOWN'
---
layout: default
title: Integration test homepage
permalink: /
lang: en
---

An English page that does not opt in to post-specific features.
MARKDOWN

  case "${suite}" in
    comments)
      cat >"${source_dir}/_posts/2022-12-10-giscus-comments.md" <<'MARKDOWN'
---
layout: post
title: Giscus integration fixture
date: 2022-12-10
permalink: /blog/2022/giscus-comments/
giscus_comments: true
related_posts: false
---

Giscus rendering test.
MARKDOWN
      cat >"${source_dir}/_posts/2015-10-20-disqus-comments.md" <<'MARKDOWN'
---
layout: post
title: Disqus integration fixture
date: 2015-10-20
permalink: /blog/2015/disqus-comments/
disqus_comments: true
related_posts: false
---

Disqus rendering test.
MARKDOWN
      ;;
    distill)
      cat >"${source_dir}/_posts/2021-05-22-distill.md" <<'MARKDOWN'
---
layout: distill
title: Distill integration fixture
description: Cross-plugin rendering and asset contract test.
date: 2021-05-22
permalink: /blog/2021/distill/
giscus_comments: true
mermaid:
  enabled: true
tikzjax: true
authors: []
---

## Rendering fixture

This page exercises the Distill, chart, math, and comment integrations.
MARKDOWN
      ;;
    new-plugins)
      cat >"${source_dir}/_posts/2022-10-15-rtl.md" <<'MARKDOWN'
---
layout: post
title: RTL integration fixture
date: 2022-10-15
permalink: /blog/2022/rtl/
lang: fa
related_posts: false
---

RTL document attributes and asset test.
MARKDOWN
      cat >"${source_dir}/_posts/2025-04-28-marimo.md" <<'MARKDOWN'
---
layout: post
title: Marimo integration fixture
date: 2025-04-28
permalink: /blog/2025/marimo/
marimo: true
related_posts: false
---

<div class="al-marimo-inline" markdown="1">

```python
import marimo as mo
mo.md("Integration test")
```

</div>
MARKDOWN
      ;;
    *)
      echo "unknown plugin fixture suite: ${suite}" >&2
      return 1
      ;;
  esac
}
