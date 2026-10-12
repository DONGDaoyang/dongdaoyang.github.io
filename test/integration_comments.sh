#!/usr/bin/env bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
tmp_override="${tmp_dir}/comments-test-override.yml"
tmp_site="${tmp_dir}/site"

cleanup() {
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

# Use temporary test pages, not removable demo content from the public site.
source "$(dirname "${BASH_SOURCE[0]}")/integration_fixture_helpers.sh"
tmp_source="${tmp_dir}/source"
prepare_plugin_fixture "${tmp_source}" "comments"
fixture_config="${tmp_source}/_config.yml"

cat >"${tmp_override}" <<'YAML'
giscus:
  repo: alshedivat/al-folio
  repo_id: R_kgDOExample
  category: Comments
  category_id: DIC_kwDOExample
disqus_shortname: integration-test
YAML

bundle exec jekyll build --source "${tmp_source}" \
  --config "_config.yml,${fixture_config},${tmp_override}" -d "${tmp_site}" >/dev/null

giscus_page="${tmp_site}/blog/2022/giscus-comments/index.html"
disqus_page="${tmp_site}/blog/2015/disqus-comments/index.html"

for page in "${giscus_page}" "${disqus_page}"; do
  if [ ! -f "${page}" ]; then
    echo "comments test fixture was not generated at ${page}" >&2
    exit 1
  fi
done

grep -q 'https://giscus.app/client.js' "${giscus_page}"
if grep -q 'giscus comments misconfigured' "${giscus_page}"; then
  echo "unexpected giscus misconfiguration warning in ${giscus_page}" >&2
  exit 1
fi

grep -q 'id="disqus_thread"' "${disqus_page}"
grep -q '.disqus.com/embed.js' "${disqus_page}"

echo "comments integration checks passed"
