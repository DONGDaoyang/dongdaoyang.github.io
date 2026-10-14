#!/usr/bin/env python3
"""Render saved Single Track stress on the undeformed native FE section."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.colors import Normalize
import meshio
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=Path, required=True)
parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
parser.add_argument('--qa-dir', type=Path, required=True)
parser.add_argument('--skill-scripts', type=Path, required=True)
args = parser.parse_args()
sys.path.insert(0, str(args.skill_scripts))
from audit_panel_alignment import require_matplotlib_panel_alignment

# Contract: show the saved final von Mises stress, without claiming validation.
# One native Y=0 section, no smoothing, deformation, or resampling. Every active
# cell on the section is retained; the entire cell field is exported as CSV.
mesh = meshio.read(args.source)
assert len(mesh.cells) == 1 and mesh.cells[0].type == 'hexahedron'
points = mesh.points * 1000.0  # Source coordinates are meters.
cells = mesh.cells[0].data
stress = mesh.cell_data['stress_mises'][0].ravel()  # Saved solver field is MPa.
active = mesh.cell_data['active'][0].ravel().astype(bool)
time = mesh.cell_data['time'][0].ravel()
assert np.isfinite(stress).all() and np.all(stress >= 0)
assert np.allclose(time, time[0])
faces = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
                  [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7]])
section = {}
for face in faces:
    ids = cells[:, face]
    on_plane = np.all(np.isclose(points[ids, 1], 0, atol=1e-6), axis=1) & active
    for cell_id in np.flatnonzero(on_plane):
        # The plane is shared by two symmetric cells; retain the positive-Y
        # face once. Do not average the two sides or change stored stresses.
        center_y = points[cells[cell_id], 1].mean()
        if center_y >= 0:
            section[tuple(sorted(ids[cell_id]))] = cell_id
assert section
polygons, values = [], []
for face_ids, cell_id in section.items():
    xy = points[list(face_ids)][:, [0, 2]]
    centered = xy - xy.mean(0)
    order = np.argsort(np.arctan2(centered[:, 1], centered[:, 0]))
    polygons.append(xy[order])
    values.append(stress[cell_id])
values = np.asarray(values)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'], 'font.size': 10,
                     'svg.fonttype': 'none', 'pdf.fonttype': 42})
fig, ax = plt.subplots(figsize=(7.2, 3.2), layout='constrained')
collection = PolyCollection(polygons, array=values, cmap='viridis',
                            norm=Normalize(vmin=0, vmax=float(values.max())),
                            edgecolors='none', rasterized=True)
ax.add_collection(collection)
ax.set(xlim=(-26, 26), ylim=(-11.6, 1.5), xlabel='X (mm)', ylabel='Z (mm)')
ax.set_aspect('equal')
ax.spines[['top', 'right']].set_visible(False)
colorbar = fig.colorbar(collection, ax=ax, shrink=0.8, pad=0.025)
colorbar.set_label('Von Mises stress (MPa)')
fig.canvas.draw()
args.qa_dir.mkdir(parents=True, exist_ok=True)
require_matplotlib_panel_alignment(fig, json_out=str(args.qa_dir / 'single-track-stress.alignment.json'),
                                  tolerance_pt=1.5, gutter_tolerance_pt=1.5, strict=True)
image_dir = args.repo / 'assets/img/cases/single_track'
pdf_dir = args.repo / 'assets/pdf/cases/single_track'
data_dir = args.repo / 'assets/data/cases/single_track'
for d in [image_dir, pdf_dir, data_dir]:
    d.mkdir(parents=True, exist_ok=True)
fig.savefig(image_dir / 'results-cover.png', dpi=300, facecolor='white')
fig.savefig(image_dir / 'results-cover.svg', facecolor='white')
fig.savefig(pdf_dir / 'results-cover.pdf', facecolor='white')
plt.close(fig)
centers = points[cells].mean(1)
with (data_dir / 'final-stress-cells.csv').open('w', newline='') as handle:
    writer = csv.writer(handle)
    writer.writerow(['cell_id', 'x_mm', 'y_mm', 'z_mm', 'active', 'time_s', 'stress_xx_mpa', 'stress_yy_mpa', 'stress_zz_mpa', 'von_mises_mpa'])
    for i, xyz in enumerate(centers):
        writer.writerow([i, *xyz, int(active[i]), float(time[i]),
                         *[float(mesh.cell_data[k][0][i]) for k in ['stress_xx', 'stress_yy', 'stress_zz']], float(stress[i])])
metadata = {'source_filename': args.source.name,
            'source_sha256': hashlib.sha256(args.source.read_bytes()).hexdigest(),
            'time_s': float(time[0]), 'total_cells': len(cells), 'active_cells': int(active.sum()),
            'section_cells': len(section), 'section': 'Y=0; positive-Y adjacent active cells; undeformed native geometry',
            'field': 'stress_mises', 'unit': 'MPa', 'coordinate_conversion': 'meters to millimeters',
            'color_limits_mpa': [0, float(values.max())], 'colormap': 'viridis',
            'smoothing': False, 'deformation': False,
            'section_selection_reason': 'A longitudinal section through the track and substrate shows the internal stress field.',
            'full_field_export': 'All cells retained in final-stress-cells.csv, including inactive cells with an active flag.',
            'figure_contract': 'Saved final stress distribution; one FE realization; no experimental validation or statistical uncertainty claimed.'}
(data_dir / 'final-stress-metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
print(json.dumps({k:metadata[k] for k in ['time_s', 'total_cells', 'section_cells', 'color_limits_mpa']}))
