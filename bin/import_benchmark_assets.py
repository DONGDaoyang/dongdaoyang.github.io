#!/usr/bin/env python3
"""Prepare four case pages from supplied solver inputs and saved figures.

This is an offline content importer, not website runtime. Physics tables are
copied exactly; path/runtime settings are omitted from public configurations.
Saved figures are copied or rendered as complete PDF pages without curve edits.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import shutil

import numpy as np
import pymupdf
import yaml

from case_figure_layout import format_case_figures

parser = argparse.ArgumentParser()
parser.add_argument('--output-dir', type=Path, required=True)
parser.add_argument('--solver-dir', type=Path, required=True)
args = parser.parse_args()
repo = Path(__file__).resolve().parents[1]
output, solver = args.output_dir, args.solver_dir
records = []
properties = {
    'conductivity': ('Thermal conductivity', 'values', 'W/(m·K)'),
    'heat_capacity': ('Specific heat capacity', 'values', 'J/(kg·K)'),
    'elastic_modulus': ("Young’s modulus", 'values_gpa', 'GPa'),
    'thermal_expansion': ('Thermal expansion coefficient', 'values_micro_per_k', 'µm/(m·K)'),
    'poisson_ratio': ('Poisson ratio', 'values', 'Dimensionless'),
    'yield_stress': ('Initial yield stress', 'values_mpa', 'MPa'),
    'hardening_modulus': ('Hardening modulus', 'values_gpa', 'GPa'),
    'maximum_yield_stress': ('Maximum yield stress', 'values_mpa', 'MPa'),
}
cases = {
    'single_track': {'title': 'Single Track', 'slug': 'single-track', 'folder': 'single_track', 'importance': 1, 'cover': 'single-track-results.png', 'cover_alt': 'Single Track residual stress.',
                     'config': solver / 'am_solver/cases/track1/track1.yaml', 'config_origin': 'opt_IS/am_solver/cases/track1/track1.yaml',
                     'overview': 'This is a single-track laser-deposition model with an IN718 track on a Ti-6Al-4V substrate. The thermal–mechanical analysis follows one 40 mm scan and the subsequent cooling stage to calculate residual stress.',
                     'dimensions': 'Track: 40 × 1.6 × 0.67 mm; saved substrate mesh: 50 × 10 × 11 mm',
                     'process': 'DED',
                     'note': 'The supplied drawing shows a 30 mm substrate width; the saved FE mesh spans 10 mm across Y. The result below uses the saved mesh.'},
    'thin_wall': {'title': 'Thin-wall', 'slug': 'thin-wall', 'folder': 'thin-wall', 'importance': 2,
                  'config': solver / 'am_solver/cases/thin_wall/thin_wall.yaml', 'config_origin': 'opt_IS/am_solver/cases/thin_wall/thin_wall.yaml',
                  'overview': 'This is a four-layer steel thin-wall model. The thermal–mechanical analysis follows successive line scans and cooling stages, then releases the specified anchors to calculate springback. A separate 20-layer configuration is also available.',
                  'dimensions': 'Saved half-domain mesh: 500 × 30 × 20 mm; deposited height: 8 mm',
                  'process': 'WAAM',  # Provisional site classification; the source YAML does not name the process.
                  'note': 'The steel grade is not specified in the configuration.'},
    'bridge': {'title': 'Bridge', 'slug': 'bridge', 'folder': 'bridge', 'importance': 3, 'solver_case': 'bridge',
               'config': output / 'bridge/generated_configs/am.yaml', 'config_origin': 'opt_output/bridge/generated_configs/am.yaml',
               'overview': 'This is a Ti-6Al-4V bridge model. A local thermal–mechanical simulation is used to identify inherent strain, which is then applied to the full bridge model to calculate residual elastic strain.',
               'dimensions': 'Bridge: 21 × 5 × 9 mm; substrate: 41 × 25 × 10 mm', 'process': 'LPBF',
               'note': 'The physical print layer is 30 µm. The 250 µm layer pitch used in the macro model is a separate coarse activation setting.'},
    'double_cantilever': {'title': 'Double-cantilever', 'slug': 'double-cantilever', 'folder': 'double_cantilever', 'importance': 5, 'solver_case': 'dc',
                          'config': output / 'dc/generated_configs/am.yaml', 'config_origin': 'opt_output/dc/generated_configs/am.yaml',
                          'overview': 'This is the IN718 double-cantilever model. A local thermal–mechanical simulation is used to identify inherent strain, and the macro model calculates residual stress and warpage after releasing the left and right interfaces.',
                          'dimensions': 'Double-cantilever span / height: 127 / 18.5 mm; substrate: 190.8 × 30 × 10 mm', 'process': 'LPBF',
                          'note': 'This page uses the IN718 dc case. The separate Ti-6Al-4V dc2 case is not combined with this geometry. The physical print layer is 40 µm; macro activation uses a 515 µm pitch.'},
}


def f(value):
    if isinstance(value, bool):
        return 'Enabled' if value else 'Disabled'
    if isinstance(value, (float, int)):
        if not math.isfinite(value):
            return 'No finite cap' if value > 0 else str(value)
        return f'{value:.12g}'
    if isinstance(value, list):
        return ' / '.join(f(v) for v in value)
    return str(value)


def dimension(values_m, suffix=''):
    """Use mm from 200 µm; keep smaller dimensions in µm."""
    values = values_m if isinstance(values_m, list) else [values_m]
    if min(values) >= 200e-6:
        scale, unit = 1000, 'mm'
    else:
        scale, unit = 1e6, 'µm'
    return ' / '.join(f(value * scale) for value in values), unit + suffix


def table(headers, rows):
    lines = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join('---' for _ in headers) + ' |']
    lines += ['| ' + ' | '.join(f(v).replace('|', '\\|') for v in row) + ' |' for row in rows]
    return '\n'.join(lines) + '\n'


def safe_public(value):
    if isinstance(value, dict):
        return {k: safe_public(v) for k, v in value.items() if k not in ['paths', 'runtime', 'output']}
    if isinstance(value, list):
        return [safe_public(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        return 'unbounded' if value > 0 else str(value)
    if isinstance(value, str):
        for root, label in [(str(output), 'opt_output'), (str(solver), 'opt_IS'), (str(solver).replace('opt_IS', 'Opt_IS'), 'opt_IS')]:
            value = value.replace(root, label)
    return value


def provenance(src):
    for root, label in [(output, 'opt_output'), (solver, 'opt_IS')]:
        if src.is_relative_to(root):
            return f'{label}/{src.relative_to(root)}'
    return src.name


def record(src, dst, operation):
    records.append({'source': provenance(src), 'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
                    'website_file': str(dst.relative_to(repo)), 'website_sha256': hashlib.sha256(dst.read_bytes()).hexdigest(), 'operation': operation})


def copy_asset(src, dst):
    assert src.is_file(), src
    if src.suffix == '.csv':
        original = src.read_text()
        public = safe_public(original)
        dst.write_text(public)
        operation = ('CSV values retained; source paths made relative'
                     if public != original else 'Unmodified CSV values')
    else:
        shutil.copyfile(src, dst)
        operation = 'Unmodified copy'
    record(src, dst, operation)


def import_pdf(case, relative, name, pages=(0,)):
    src = output / relative
    pdf_dir = repo / f'assets/pdf/cases/{case["folder"]}'
    image_dir = repo / f'assets/img/cases/{case["folder"]}'
    copy_asset(src, pdf_dir / f'{name}.pdf')
    doc = pymupdf.open(src)
    for page in pages:
        dst = image_dir / (f'{name}.png' if page == 0 else f'{name}-page-{page + 1}.png')
        temporary = dst.with_suffix('.tmp.png')
        doc[page].get_pixmap(dpi=180, alpha=False).save(temporary)
        temporary.replace(dst)
        record(src, dst, f'Full PDF page {page + 1} rendered at 180 dpi; no cropping or curve edits')


def room_values(mat):
    result = {}
    for key, (_, value_key, _) in properties.items():
        if key in mat:
            prop = mat[key]
            assert len(prop['temperature_k']) == len(prop[value_key])
            assert np.all(np.diff(prop['temperature_k']) > 0)
            result[key] = float(np.interp(293.15, prop['temperature_k'], prop[value_key]))
    if 'maximum_yield_stress' not in result:
        result['maximum_yield_stress'] = result['yield_stress'] * mat.get('maximum_yield_factor', 1)
    return result


def material_setting(mat):
    return f'E = {f(float(mat["elastic_modulus_pa"]) / 1e9)} GPa; ν = {f(mat["poisson_ratio"])}; σᵧ = {f(float(mat["initial_yield_stress_pa"]) / 1e6)} MPa; H = {f(float(mat["hardening_modulus_pa"]) / 1e9)} GPa; σₘₐₓ = {f(float(mat["maximum_yield_stress_pa"]) / 1e6)} MPa'


manifest = json.loads((output / 'data/optimization_dns/optimization_dns_manifest.json').read_text())
reports = {d['case']: d for d in manifest['reports']}
for key, case in cases.items():
    folder = case['folder']
    dirs = {kind: repo / f'assets/{kind}/cases/{folder}' for kind in ['data', 'img', 'pdf']}
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)
    cfg = yaml.safe_load(case['config'].read_text())
    payload = {'case': case['title'], 'source': case['config_origin'], 'source_sha256': hashlib.sha256(case['config'].read_bytes()).hexdigest(),
               **safe_public(cfg), 'room_temperature_evaluation': {'temperature_c': 20, 'method': 'Linear interpolation; endpoint hold outside each property table',
                                                                'regions': {r: room_values(m) for r, m in cfg['materials'].items()}}}
    if key == 'thin_wall':
        variant = solver / 'am_solver/cases/thin_wall/thin_wall20.yaml'
        payload['variants'] = {'20_layer': safe_public(yaml.safe_load(variant.read_text()))}
        (dirs['data'] / 'simulation-20-layer.yaml').write_text('# Portable physics configuration; local paths and runtime outputs omitted.\n' + yaml.safe_dump(payload['variants']['20_layer'], sort_keys=False, allow_unicode=True))
    solver_case = case.get('solver_case')
    latest = None
    if solver_case:
        current_am = solver / f'opt_solver/cases/{solver_case}/am.yaml'
        forward_src = solver / f'opt_solver/cases/{solver_case}/forward.yaml'
        forward = yaml.safe_load(forward_src.read_text())
        optimization = yaml.safe_load((output / f'{solver_case}/generated_configs/optimization.yaml').read_text())
        latest_src = output / f'{solver_case}/optimization/epsilon_result.json'
        latest = json.loads(latest_src.read_text())
        report = reports[solver_case]
        payload['current_am_configuration'] = safe_public(yaml.safe_load(current_am.read_text()))
        payload['macro_configuration'] = safe_public(forward)
        payload['local_identification_material'] = safe_public(optimization['material'])
        payload['latest_identification'] = safe_public(latest)
        payload['displayed_comparison_inherent_strain'] = report['inherent_strain']
        payload['displayed_comparison_reference'] = report['dns_source']
        payload['comparison_note'] = 'Displayed figures use their archived manifest vector and reference. The latest identification is reported separately.'
        (dirs['data'] / 'macro-parameters.yaml').write_text('# Portable macro configuration; the default inherent strain is a seed, not the identified result.\n' + yaml.safe_dump(safe_public(forward), sort_keys=False, allow_unicode=True))
        copy_asset(output / f'data/optimization_dns/{solver_case}_metrics.csv', dirs['data'] / 'optimization-metrics.csv')
        (dirs['data'] / 'identification-results.json').write_text(json.dumps({'latest': safe_public(latest), 'displayed_comparison': {'inherent_strain': report['inherent_strain'], 'reference': report['dns_source']}}, indent=2, allow_nan=False) + '\n')
    (dirs['data'] / 'thermal-parameters.json').write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
    (dirs['data'] / 'simulation-parameters.yaml').write_text('# Portable saved physics configuration; local paths and runtime outputs omitted.\n' + yaml.safe_dump(safe_public(cfg), sort_keys=False, allow_unicode=True))
    csv_rows = []
    material_sections = []
    unique = []
    for region, mat in cfg['materials'].items():
        existing = next((item for item in unique if item[1] == mat), None)
        if existing:
            continue
        same_regions = [r for r, v in cfg['materials'].items() if v == mat]
        unique.append((region, mat))
        scalars = [(name, mat[field], unit) for field, name, unit in [
            ('density_kg_m3', 'Density', 'kg/m³'), ('latent_heat_j_kg', 'Latent heat', 'J/kg'),
            ('solidus_temperature_k', 'Solidus temperature', 'K'), ('liquidus_temperature_k', 'Liquidus temperature', 'K'),
            ('maximum_yield_factor', 'Maximum yield factor', 'Dimensionless')] if field in mat]
        block = f'#### {mat["name"]} — {" and ".join(r.replace("_", " ") for r in same_regions)}\n\n'
        block += table(['Parameter', 'Value', 'Unit'], scalars) + '\n'
        for prop, (label, value_key, unit) in properties.items():
            if prop not in mat:
                continue
            temperatures, values = mat[prop]['temperature_k'], mat[prop][value_key]
            assert len(temperatures) == len(values) and np.all(np.diff(temperatures) > 0)
            block += f'##### {label}\n\n' + table(['Temperature (°C)', 'Temperature (K)', f'{label} ({unit})'], [(round(t - 273.15, 8), t, v) for t, v in zip(temperatures, values)]) + '\n'
            for r in same_regions:
                csv_rows.extend((r, mat['name'], prop, t, round(t - 273.15, 8), v, unit, 'configured') for t, v in zip(temperatures, values))
        if 'maximum_yield_stress' not in mat:
            factor = mat.get('maximum_yield_factor', 1)
            block += f'Maximum yield stress is {f(factor)} × the interpolated initial yield stress.\n\n'
        material_sections.append(block)
    with (dirs['data'] / 'temperature-dependent-properties.csv').open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['region', 'material', 'property', 'temperature_k', 'temperature_c', 'value', 'unit', 'status'])
        writer.writerows(csv_rows)
    heat, path = cfg['heat_source'], cfg['toolpath']
    scan = path['scan']
    printing = [('Manufacturing process', case['process'], '—'),
                ('Material', ' / '.join(m['name'] for _, m in unique), 'Deposit / substrate if different'),
                ('Heat-source power, P', heat['power_w'], 'W'), ('Scan speed, v', scan['velocity_m_s'] * 1000, 'mm/s'),
                ('Physical deposition layer thickness', *dimension(path['layer_height_m'])),
                ('Hatch spacing', *(dimension(scan['hatch_spacing_m']) if 'hatch_spacing_m' in scan else ('Not applicable — one track per layer', '—'))),
                ('Absorption efficiency', heat['efficiency'], 'Dimensionless'), ('Heat-source model', 'Goldak double ellipsoid', 'Volumetric heat source'),
                ('Heat-source radii', *dimension([heat[p] for p in ['front_radius_x_m', 'rear_radius_x_m', 'radius_y_m', 'radius_z_m']], '; front / rear / transverse / depth')),
                ('Cooling interval', path['cooling_time_s'], 's after each deposited layer')]
    simulation = [('Initial / ambient temperature', f'{f(cfg["thermal"]["initial_temperature_c"])} / {f(cfg["thermal"]["convection"]["ambient_temperature_c"])}', '°C'),
                  ('High-temperature material model', 'Complete temperature-dependent tables below; linear interpolation with endpoint holds', '—')]
    if solver_case:
        simulation += [('Room-temperature macro material model', material_setting(forward['material']), 'Constant properties'),
                       ('Material model for the saved local identification', material_setting(optimization['material']), 'Constant properties'),
                       ('Latest identified inherent strain, ε*xx = ε*yy', latest['inherent_strain']['xx'] * 1000, '‰'),
                       ('Latest identified inherent strain, ε*zz', latest['inherent_strain']['zz'] * 1000, '‰'),
                       ('Inherent strain in the displayed archived comparison', f'ε*xx = ε*yy = {f(report["inherent_strain"]["xx"] * 1000)}; ε*zz = {f(report["inherent_strain"]["zz"] * 1000)}', '‰'),
                       ('Macro layer activation', f'{forward["toolpath"]["number_of_layers"]} × {f(forward["toolpath"]["layer_height_m"] * 1000)}', 'Layers × mm')]
    else:
        for region, mat in unique:
            r = room_values(mat)
            simulation.append((f'{mat["name"]} properties evaluated at 20 °C', f'E = {f(r["elastic_modulus"])} GPa; ν = {f(r["poisson_ratio"])}; σᵧ = {f(r["yield_stress"])} MPa; H = {f(r["hardening_modulus"])} GPa; σₘₐₓ = {f(r["maximum_yield_stress"])} MPa', 'From the same thermal–mechanical tables'))
        simulation.append(('Identified inherent strain', 'Not used — this case uses full thermal–mechanical analysis', '—'))
    simulation += [('Thermal strain reference temperature', cfg['mechanics']['thermal_strain_reference_temperature_c'], '°C'),
                   ('Thermal strain cutoff', cfg['mechanics'].get('thermal_strain_cutoff', 'No explicit cutoff configured'), '—')]
    macro_constraints = {'bridge': 'Fixed plane Z = 0 mm; no release',
                         'double_cantilever': 'Fixed plane Z = 10 mm; release left and right interfaces at Z = 32.2 mm'}
    if key in macro_constraints:
        simulation.append(('Macro constraints and release', macro_constraints[key], '—'))
    frontmatter = {'layout': 'page', 'title': f'{case["title"]} ({case["process"]})', 'description': case['overview'], 'permalink': f'/benchmarks/{case["slug"]}/', 'hub_case': True, 'published': True, 'importance': case['importance'], 'case_type': 'Computational case', 'img': f'/assets/img/cases/{folder}/{case.get("cover", "results-cover.png")}', 'image_alt': case.get('cover_alt', f'{case["title"]} residual stress.')}
    if 'cover' in case:
        cover = dirs['img'] / case['cover']
        if cover.is_file():
            frontmatter['img'] += '?v=' + hashlib.sha256(cover.read_bytes()).hexdigest()[:12]
    text = '---\n' + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=140) + '---\n\n[← All benchmarks](/benchmarks/)\n\n## Overview\n\n' + case['overview'] + '\n\n'
    text += f'![Geometry and dimensions.](/assets/img/cases/{folder}/geometry-overview.png)\n\n_Figure 1. Geometry and dimensions._\n\n[Download the original geometry PDF](/assets/pdf/cases/{folder}/geometry-overview.pdf)\n\n'
    text += '## Problem set\n\n### Printing parameters\n\n' + table(['Parameter', 'Value', 'Unit / description'], printing) + '\n_Printing and heat-source values describe the supplied simulation configuration._\n\n### Simulation parameters\n\n' + table(['Parameter', 'Value / setting', 'Unit / description'], simulation) + '\n' + case['note'] + '\n\n'
    if solver_case:
        text += 'The latest saved identification and the displayed archived comparison are listed separately. The plotted curves and their reference frames are retained from the saved figures.\n\n'
    text += '<details class="rsh-parameter-details" markdown="1">\n<summary>Temperature-dependent material parameters</summary>\n\n'
    text += 'Every configured temperature node is listed below, with exact conversion from K to °C. Each property is linearly interpolated within its own table and held at its nearest endpoint outside that range.\n\n'
    text += '\n'.join(material_sections)
    if key == 'thin_wall':
        text += 'The phase-change settings are numerical model inputs: latent heat is zero and the configured solidus / liquidus are 1273.15 / 1274.15 K. They are not claimed as measured steel melting temperatures.\n\n'
    if key == 'double_cantilever':
        text += 'The local IN718 model uses zero hardening modulus and a maximum-yield factor of 1. The phase-change values are retained model inputs, separate from the temperature-dependent mechanical tables.\n\n'
    text += '</details>\n\n'
    text += f'[Download full parameter JSON](/assets/data/cases/{folder}/thermal-parameters.json) · [Download temperature-dependent CSV](/assets/data/cases/{folder}/temperature-dependent-properties.csv) · [Download simulation YAML](/assets/data/cases/{folder}/simulation-parameters.yaml)\n\n'
    if key == 'thin_wall':
        text += f'[Download the separate 20-layer YAML](/assets/data/cases/{folder}/simulation-20-layer.yaml)\n\n'
    if solver_case:
        text += f'[Download macro configuration](/assets/data/cases/{folder}/macro-parameters.yaml) · [Download identification results](/assets/data/cases/{folder}/identification-results.json)\n\n'
    text += '## Results\n\n### Residual stress field\n\n'
    captions = {'single_track': 'Von Mises stress at Y = 0 mm.',
                'thin_wall': 'Residual stress field.',
                'bridge': 'Residual stress field.',
                'double_cantilever': 'Residual stress field.'}
    text += f'![{captions[key]}](/assets/img/cases/{folder}/results-cover.png)\n\n_Figure 2. {captions[key]}_\n\n[Download the stress-field figure](/assets/pdf/cases/{folder}/results-cover.pdf)\n\n'
    if key == 'single_track':
        text += '[Download all final cell stresses](/assets/data/cases/single_track/final-stress-cells.csv) · [Download stress-field metadata](/assets/data/cases/single_track/final-stress-metadata.json)\n\n'
    elif key == 'thin_wall':
        for name in ['temperature_history', 'strain_xx_history', 'strain_yy_history', 'strain_zz_history']:
            copy_asset(output / f'plot/plot_figures/solver_diagnostics/am_solver/thin_wall/postprocess/{name}.png', dirs['img'] / f'{name.replace("_", "-")}.png')
        copy_asset(output / 'am_solver/thin_wall/postprocess/history.csv', dirs['data'] / 'thermal-mechanical-history.csv')
        copy_asset(output / 'am_solver/thin_wall/springback_summary.csv', dirs['data'] / 'springback-summary.csv')
        with (dirs['data'] / 'springback-summary.csv').open() as handle:
            springback = next(csv.DictReader(handle))
        text += '### Temperature and strain histories\n\n![Temperature history.](/assets/img/cases/thin-wall/temperature-history.png)\n\n_Figure 3. Temperature history._\n\n![X-direction strain histories.](/assets/img/cases/thin-wall/strain-xx-history.png)\n\n_Figure 4. X-direction strain histories._\n\n'
        text += '[YY strain history](/assets/img/cases/thin-wall/strain-yy-history.png) · [ZZ strain history](/assets/img/cases/thin-wall/strain-zz-history.png) · [Download the history CSV](/assets/data/cases/thin-wall/thermal-mechanical-history.csv)\n\n### Springback after release\n\n'
        text += f'The saved maximum springback magnitude is **{float(springback["maximum_springback_mm"]):.6f} mm**. At that node, the vertical component is **{float(springback["uz_at_max_mm"]):.6f} mm**. This is a numerical springback result after releasing the configured anchors.\n\n[Download springback samples](/assets/data/cases/thin-wall/springback-summary.csv)\n\n'
    elif solver_case:
        if key == 'bridge':
            import_pdf(case, 'plot/plot_figures/am_history/bridge/bridge_am_bottom_centre_history.pdf', 'thermal-history')
            copy_asset(output / 'data/bridge/am_history/bridge_am_bottom_centre_history.csv', dirs['data'] / 'thermal-mechanical-history.csv')
            text += f'### Temperature and strain histories\n\n![Temperature and X-direction strain histories.](/assets/img/cases/{folder}/thermal-history.png)\n\n_Figure 3. Temperature and X-direction strain histories._\n\n[Download the history CSV](/assets/data/cases/{folder}/thermal-mechanical-history.csv)\n\n'
        else:
            import_pdf(case, 'plot/plot_figures/am_history/dc/flow_plastic/am_strain_history.pdf', 'thermal-history')
            text += f'### Temperature and strain histories\n\n![X-, Y- and Z-direction strain histories.](/assets/img/cases/{folder}/thermal-history.png)\n\n_Figure 3. X-, Y- and Z-direction strain histories._\n\n[Download all local history pages](/assets/pdf/cases/{folder}/thermal-history.pdf)\n\n'
        import_pdf(case, f'plot/plot_figures/postprocessed/optimization_dns/{solver_case}_optimization_vs_dns.pdf', 'optimization-agreement', pages=(0, 1))
        text += f'### Inherent-strain identification\n\n![Stress and elastic strain comparison.](/assets/img/cases/{folder}/optimization-agreement.png)\n\n_Figure 4. Stress and elastic strain comparison._\n\n'
        text += f'![Residual stress field comparison.](/assets/img/cases/{folder}/optimization-agreement-page-2.png)\n\n_Figure 5. Residual stress field comparison._\n\n[Download all comparison pages](/assets/pdf/cases/{folder}/optimization-agreement.pdf) · [Download the error metrics](/assets/data/cases/{folder}/optimization-metrics.csv)\n\n'
        if key == 'bridge':
            for name in ['x3p75', 'y3p75', 'z3p75', 'x7p75', 'y7p75', 'z7p75']:
                import_pdf(case, f'plot/plot_figures/postprocessed/bridge/{name}.pdf', name)
            text += '### Residual elastic strain\n\n![X-direction elastic strain at X = 3.75 mm.](/assets/img/cases/bridge/x3p75.png)\n\n_Figure 6. X-direction elastic strain at X = 3.75 mm._\n\n![Z-direction elastic strain at X = 3.75 mm.](/assets/img/cases/bridge/z3p75.png)\n\n_Figure 7. Z-direction elastic strain at X = 3.75 mm._\n\n'
            text += 'Additional profiles: [3.75 mm, YY](/assets/img/cases/bridge/y3p75.png) · [7.75 mm, XX](/assets/img/cases/bridge/x7p75.png) · [7.75 mm, YY](/assets/img/cases/bridge/y7p75.png) · [7.75 mm, ZZ](/assets/img/cases/bridge/z7p75.png).\n\n'
        else:
            import_pdf(case, 'plot/plot_figures/postprocessed/dc/warpage_disp2.pdf', 'warpage')
            copy_asset(output / 'data/dc/output_dc_plot_disp2.csv', dirs['data'] / 'warpage.csv')
            text += '### Warpage after release\n\n![Vertical displacement after release.](/assets/img/cases/double_cantilever/warpage.png)\n\n_Figure 6. Vertical displacement after release._\n\n[Download the warpage figure](/assets/pdf/cases/double_cantilever/warpage.pdf) · [Download displacement samples](/assets/data/cases/double_cantilever/warpage.csv)\n\n'
    text += '---\n\n**Data sources:** Supplied simulation inputs and saved solver outputs. Complete physical settings and temperature-dependent values are available in the YAML, JSON, and CSV downloads above.\n'
    (repo / f'_projects/{key}.md').write_text(format_case_figures(text))
    records.append({'case': case['title'], 'configuration_source': case['config_origin'], 'configuration_sha256': payload['source_sha256'], 'temperature_table_records': len(csv_rows), 'data_policy': 'All configured temperature nodes preserved; no invented measurements or inherent strain.'})
(repo / 'docs/benchmark-case-assets.json').write_text(json.dumps({'assets': records, 'notes': ['Current identification results and archived figure vectors are distinguished.', 'Single Track final stresses are rendered separately from native VTK.', 'Public parameter snapshots omit machine-local paths and runtime outputs.']}, indent=2, ensure_ascii=False) + '\n')
print('Prepared case pages:', ', '.join(cases))
print('Imported figure/data files:', sum('website_file' in r for r in records))
