#!/usr/bin/env python3
"""One-time asset preparation, not a Jekyll plugin or website runtime.

Existing PDFs and CSVs are copied unchanged; PNGs show complete PDF pages.
The original geometry figure depicts the native mesh, not residual stress.
Re-import only after confirming the page describes the supplied run versions.
Requires numpy, matplotlib, meshio, and pymupdf in the chosen local environment.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib, json, shutil
import pymupdf
import meshio
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection, LineCollection

parser = argparse.ArgumentParser(description="Import saved Cantilever figures and tables without editing their numerical content.")
parser.add_argument("--output-dir", type=Path, required=True, help="Solver output root")
parser.add_argument("--macro-mesh", type=Path, required=True, help="Primary macro INP mesh, in millimeters")
args = parser.parse_args()
repo = Path(__file__).resolve().parents[1]
source = args.output_dir.resolve()
image_dir = repo / 'assets/img/cases/cantilever'
data_dir = repo / 'assets/data/cases/cantilever'
pdf_dir = repo / 'assets/pdf/cases/cantilever'
for directory in [image_dir, data_dir, pdf_dir]:
    directory.mkdir(parents=True, exist_ok=True)
records = []

def record(label, src, target, operation):
    records.append({'label': label, 'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
                    'website_file': str(target.relative_to(repo)), 'operation': operation,
                    'website_sha256': hashlib.sha256(target.read_bytes()).hexdigest()})

def pdf_preview(label, relative, name, page=0, dpi=180):
    src = source / relative
    doc = pymupdf.open(src)
    out = image_dir / f'{name}.png'
    doc[page].get_pixmap(dpi=dpi, alpha=False).save(out)
    record(label, src, out, f'Full PDF page {page + 1} rasterized at {dpi} dpi; no cropping or curve editing')
    dst = pdf_dir / f'{name}.pdf'
    shutil.copyfile(src, dst)
    record(label, src, dst, 'Unmodified PDF copy')

pdf_preview('Saved local thermal/mechanical history',
            'plot/plot_figures/am_history/cantilever/cantilever_am_bottom_centre_history.pdf', 'thermal-history')
pdf_preview('Selected optimization: paired stress and elastic strain',
            'plot/plot_figures/postprocessed/optimization_dns/cantilever_optimization_vs_dns.pdf', 'optimization-agreement', dpi=160)
for key in ['x2p2', 'z2p2', 'x9p5', 'z9p5', 'x11', 'z11', 'warpage']:
    pdf_preview('Archived macro comparison: ' + key,
                f'plot/plot_figures/postprocessed/cantilever/{key}.pdf', key)
for src_name, dest_name in [
    ('data/optimization_dns/cantilever_metrics.csv', 'optimization-metrics.csv'),
    ('data/cantilever/output_cantilever_current_cut_warpage.csv', 'warpage-25-layer.csv'),
    ('data/cantilever/output_cantilever_compare_cut_warpage.csv', 'warpage-50-layer.csv'),
]:
    src = source / src_name
    dst = data_dir / dest_name
    shutil.copyfile(src, dst)
    record('Saved numeric output', src, dst, 'Unmodified numeric CSV copy')

# Geometry comes from the macro FE input, not a deformed result or stress field.
mesh_path = args.macro_mesh.resolve()
mesh = meshio.read(mesh_path)
points = mesh.points
hexes = np.concatenate([block.data for block in mesh.cells if block.type == 'hexahedron'])
faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7]]
face_ids = set()
for face in faces:
    ids = hexes[:, face]
    central = np.all(np.isclose(points[ids, 1], 0.0, atol=1e-7), axis=1)
    face_ids.update(tuple(sorted(row)) for row in ids[central])
assert face_ids, 'The mesh must contain faces on Y=0.'
polygons = [[], []]
boundaries = [Counter(), Counter()]
for ids in face_ids:
    coords = points[list(ids)][:, [0, 2]]
    center = coords.mean(axis=0)
    order = np.argsort(np.arctan2(coords[:, 1] - center[1], coords[:, 0] - center[0]))
    coords = coords[order]
    group = int(center[1] >= -12.5 - 1e-7)
    polygons[group].append(coords)
    vertices = [tuple(np.round(x, 6)) for x in coords]
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        boundaries[group][tuple(sorted([a, b]))] += 1
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'svg.fonttype': 'none', 'pdf.fonttype': 42})
fig, ax = plt.subplots(figsize=(10.2, 4.3), layout='constrained')
for group, color in [(0, '#dadcde'), (1, '#f7c197')]:
    ax.add_collection(PolyCollection(polygons[group], facecolors=color, edgecolors='none', rasterized=True))
    ax.add_collection(LineCollection([list(edge) for edge, count in boundaries[group].items() if count == 1],
                                    colors='#62676b', linewidths=0.6))
ax.plot([0, 55], [-12.5, -12.5], '--', color='#a84309', lw=1.9, label='Released interface after cutting')
ax.scatter(np.arange(-9, 90, 4), np.full(25, -25.2), marker='^', s=25, color='#62676b', label='Fixed substrate bottom')
ax.annotate('Build direction', xy=(100, -0.5), xytext=(100, -18), rotation=90,
            ha='center', va='center', arrowprops={'arrowstyle': '->', 'color': '#a84309'}, color='#a84309')
ax.set(xlim=(-14, 105), ylim=(-30, 4), xlabel='X (mm)', ylabel='Z (mm)')
ax.set_aspect('equal', adjustable='box')
ax.spines[['top', 'right']].set_visible(False)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.22), ncol=2, frameon=False, fontsize=9)
fig.canvas.draw()
for extension in ['svg', 'pdf']:
    dst = (image_dir if extension == 'svg' else pdf_dir) / f'geometry.{extension}'
    fig.savefig(dst, facecolor='white', bbox_inches='tight')
    record('Undeformed macro mesh cross-section', mesh_path, dst,
           'Y=0 native HEX8 faces; mm input coordinates; uniform geometry colors, not stress values')
plt.close(fig)
meta = json.loads((source / 'data/cantilever/am_history/cantilever_am_bottom_centre_history.json').read_text())
am = source / 'cantilever/generated_configs/am.yaml'
notes = {
    'case': 'Cantilever', 'assets': records,
    'original_article': {'doi': '10.1007/s40192-019-00149-0', 'citation': 'Phan et al. (2019), Integrating Materials and Manufacturing Innovation 8, 318–334.', 'source': 'User-supplied reference; bibliographic metadata checked against Crossref.', 'scope': 'Original AM-Bench experimental article; archived curve-by-curve attribution has not been independently verified.'},
    'figure_policy': 'Existing numerical figures are reused without altering data, curves, labels or legends. New geometry is an undeformed mesh cross-section.',
    'local_history_config_hash_matches_current': hashlib.sha256(am.read_bytes()).hexdigest() == meta['configuration_sha256'],
    'limitations': [
        'The currently available AM configuration differs from the history provenance hash; printing settings are current configured inputs, not a verified immutable snapshot of the archived run.',
        'Selected optimization and archived macro comparisons use different inherent-strain vectors; neither is relabeled as the other.',
        'Paired DNS fields are optimization/calibration data, not held-out experimental validation.',
        'The archived macro figure labels and experimental point sets are retained. No fabrication, smoothing or digitization.',
        'The original AM-Bench experimental article is cited; curve-by-curve attribution and matched measurement conditions for the archived comparisons have not been independently verified.',
        'Manual visual QA was unavailable to the agent. Browser image loading and rendered structure are tested separately.'
    ],
    'geometry': {'input_units': 'mm', 'plane_y_mm': 0, 'points': len(points), 'hexahedra': len(hexes),
                 'bounds_mm': [points.min(0).tolist(), points.max(0).tolist()],
                 'cross_section_faces': len(face_ids), 'alignment': 'Not applicable: one axes panel'},
}
(repo / 'docs/cantilever-assets.json').write_text(json.dumps(notes, indent=2) + '\n')
print('Imported', len(records), 'assets. Geometry section faces:', len(face_ids))
