#!/usr/bin/env python3
"""Refresh benchmark results from the reviewed manuscript figure manifest.

Offline content preparation only. Copy original PDFs and render complete pages
without changing curves, legends, labels, or numerical results.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

import pymupdf

from case_figure_layout import figure_grid, align_case_figure_headers


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manuscript-dir', type=Path, required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    manifest = json.loads((repo / 'docs/benchmark-manuscript-figures.json').read_text())
    source_root = args.manuscript_dir.resolve()
    records = []

    # Validate all inputs before replacing any website content.
    for case in manifest['cases']:
        for figure in case['figures']:
            if 'source' in figure:
                source = source_root / figure['source']
                with pymupdf.open(source) as document:
                    assert 1 <= figure.get('page', 1) <= len(document), source
            else:
                assert (repo / figure['image'].lstrip('/')).is_file(), figure['image']

    for case in manifest['cases']:
        cards = []
        for number, figure in enumerate(case['figures'], start=2):
            links = list(figure.get('links', []))
            if 'source' in figure:
                source = source_root / figure['source']
                image = Path('assets/img/cases') / case['folder'] / (figure['name'] + '.png')
                pdf = Path('assets/pdf/cases') / case['folder'] / (figure.get('pdf_name', figure['name']) + '.pdf')
                shutil.copyfile(source, repo / pdf)
                with pymupdf.open(source) as document:
                    document[figure.get('page', 1) - 1].get_pixmap(dpi=180, alpha=False).save(repo / image)
                for target, operation in [(pdf, 'Unmodified PDF copy'), (image, f'Complete PDF page {figure.get("page", 1)} rendered at 180 dpi')]:
                    records.append({'source': figure['source'], 'source_sha256': sha256(source),
                                    'website_file': str(target), 'website_sha256': sha256(repo / target), 'operation': operation})
                image_url = '/' + str(image) + '?v=' + sha256(repo / image)[:12]
                links.insert(0, ['Download the figure PDF', '/' + str(pdf)])
            else:
                image_url = figure['image']
            figure['_image_url'] = image_url
            card = f'### {figure["heading"]}\n\n![{figure["alt"]}]({image_url})\n\n'
            # Keep Markdown emphasis from consuming underscores in math subscripts.
            card += f'<p markdown="0"><em>Figure {number}. {figure["caption"]}</em></p>\n\n{figure["explanation"]}\n\n'
            if links:
                card += ' · '.join(f'[{label}]({url})' for label, url in links) + '\n\n'
            cards.append(card)

        page = repo / '_projects' / (case['key'] + '.md')
        content = page.read_text()
        before, separator, old_results = content.partition('## Results\n')
        assert separator, page
        _, footer_separator, footer = old_results.partition('\n---\n')
        assert footer_separator, page
        cover = next(f for f in case['figures'] if f.get('cover'))
        before = re.sub(r'^img:.*$', 'img: ' + cover['_image_url'], before, count=1, flags=re.MULTILINE)
        before = re.sub(r'^image_alt:.*$', 'image_alt: ' + json.dumps(cover['alt']), before, count=1, flags=re.MULTILINE)
        results = '\n' + figure_grid(cards) + case.get('after', '')
        page.write_text(before + separator + align_case_figure_headers(results) + footer_separator + footer)

    (repo / 'docs/benchmark-manuscript-assets.json').write_text(json.dumps({
        'manuscript': 'Optimization_base_Inherent_strain_method/main.tex',
        'manuscript_sha256': sha256(source_root / 'main.tex'),
        'policy': 'Canonical manuscript PDFs copied unchanged. Complete pages rendered without cropping or curve edits. Supersedes older result-figure import records for the listed website files.',
        'assets': records,
    }, indent=2) + '\n')
    print(f'Refreshed {len(manifest["cases"])} benchmark pages and {len(records)} figure assets.')


if __name__ == '__main__':
    main()
