"""Create clean, looping homepage animations from the supplied AVI exports."""

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps
import hashlib
import io
import json
import shutil
import struct

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description='Import homepage AVI animations and hide display overlays.')
parser.add_argument('--source-root', type=Path, default=Path.home() / 'Desktop/opt_output')
source_root = parser.parse_args().source_root
manifest_path = root / 'docs/home-animation-assets.json'
manifest = json.loads(manifest_path.read_text())
records = manifest.get('animations', [manifest])

def chunks(data, start, end):
    while start + 8 <= end:
        tag = data[start:start+4]
        size = struct.unpack_from('<I', data, start+4)[0]
        body = start + 8
        if body + size > end:
            raise ValueError('Truncated AVI chunk')
        if tag in (b'RIFF', b'LIST'):
            yield from chunks(data, body+4, body+size)
        else:
            yield tag, body, size
        start = body + size + (size % 2)

cases = [
    ('point', 'point.avi'),
    ('single_track', 'single_track.avi'),
    ('thin_wall', 'thin-wall.avi'),
    ('scan', 'scan-2.avi'),
    ('bridge', 'bridge.avi'),
    ('cantilever', 'cantilever.avi'),
    ('double_cantilever', 'double_cantilever.avi'),
]

# Viewports measured over every frame of the current source exports.
# Review these bounds when replacing a source with a different camera or geometry.
framing = {'point': {'model_bounds': [572, 104, 1660, 1112],
           'crop': [88, 28, 2144, 1188],
           'source_frame_count': 16},
 'single_track': {'model_bounds': [412, 308, 1800, 1132],
                  'crop': [264, 245, 1948, 1195],
                  'source_frame_count': 205},
 'thin_wall': {'model_bounds': [372, 336, 1956, 976],
               'crop': [256, 144, 2072, 1168],
               'source_frame_count': 2200},
 'scan': {'model_bounds': [640, 256, 1740, 1172],
          'crop': [255, 187, 2125, 1241],
          'source_frame_count': 364},
 'cantilever': {'model_bounds': [316, 252, 1896, 1180],
                'crop': [159, 182, 2053, 1250],
                'source_frame_count': 50},
 'bridge': {'model_bounds': [556, 344, 1772, 1128],
            'crop': [362, 284, 1966, 1188],
            'source_frame_count': 36},
 'double_cantilever': {'model_bounds': [448, 400, 1824, 1024],
                       'crop': [347, 267, 1925, 1157],
                       'source_frame_count': 18}}

for case, filename in cases:
    data = (source_root / filename).read_bytes()
    entries = list(chunks(data, 0, len(data)))
    header = next((offset for tag, offset, size in entries if tag == b'avih'))
    frame_us, _, _, _, source_count, _, _, _, width, height, *_ = struct.unpack_from('<14I', data, header)
    assert (width, height) == (2328, 1312), 'Review overlay rectangles before importing a different export size'
    overlay_masks = {'coordinate_axes': [0, 1000, 270, 1312], 'color_legend': [1980, 0, 2328, 1312]}
    frame_entries = [(offset, size) for tag, offset, size in entries if tag == b'00dc']
    assert len(frame_entries) == source_count == framing[case]['source_frame_count']
    display_crop = framing[case]['crop']
    stride = max(1, round(50000 / frame_us))
    image_dir = root / 'assets/img/cases' / case
    video_dir = root / 'assets/video/cases' / case
    image_dir.mkdir(parents=True, exist_ok=True)
    video_dir.mkdir(parents=True, exist_ok=True)
    animation = image_dir / f'{case.replace("_", "-")}-animation.webp'
    poster = image_dir / f'{case.replace("_", "-")}-animation-poster.png'
    original = video_dir / filename
    frames, durations = [], []
    for index in range(0, source_count, stride):
        offset, size = frame_entries[index]
        with Image.open(io.BytesIO(data[offset:offset+size])) as image:
            assert image.size == (width, height)
            clean = image.convert('RGB')
            draw = ImageDraw.Draw(clean)
            for x0, y0, x1, y1 in overlay_masks.values():
                draw.rectangle((x0, y0, x1-1, y1-1), fill='white')
            viewport = clean.crop(display_crop)
            frames.append(ImageOps.pad(viewport, (width//2, height//2), method=Image.Resampling.LANCZOS, color='white'))
            viewport.close()
            clean.close()
        durations.append(min(stride, source_count-index) * frame_us // 1000)
    poster_tmp = poster.with_name(poster.stem + '.tmp.png')
    animation_tmp = animation.with_name(animation.stem + '.tmp.webp')
    frames[0].save(poster_tmp)
    poster_tmp.replace(poster)
    frames[0].save(animation_tmp, save_all=True, append_images=frames[1:], duration=durations,
                   loop=0, quality=85, method=4, allow_mixed=True)
    animation_tmp.replace(animation)
    shutil.copyfile(source_root / filename, original)
    with Image.open(animation) as encoded:
        assert encoded.is_animated and encoded.size == (width//2, height//2)
        total_ms = 0
        for index in range(encoded.n_frames):
            encoded.seek(index)
            encoded.load()
            total_ms += encoded.info['duration']
        assert total_ms == sum(durations)
        output_count = encoded.n_frames
    record = {
        'source_filename': filename,
        'source_sha256': hashlib.sha256(data).hexdigest(),
        'original': str(original.relative_to(root)),
        'animation': str(animation.relative_to(root)),
        'animation_sha256': hashlib.sha256(animation.read_bytes()).hexdigest(),
        'poster': str(poster.relative_to(root)),
        'source_frame_count': source_count,
        'source_frame_rate': 1000000 / frame_us,
        'sampled_frame_count': len(frames),
        'frame_count': output_count,
        'frame_duration_ms': stride * frame_us // 1000,
        'duration_ms': total_ms,
        'dimensions': [width//2, height//2],
        'loop': 'infinite',
        'hidden_overlays': overlay_masks,
        'overlay_background': '#ffffff',
        'display_crop': display_crop,
        'model_bounds_all_frames': framing[case]['model_bounds'],
        'conversion': f'Motion JPEG AVI sampled every {stride} frame(s), resized proportionally to half the original dimensions, and encoded as animated WebP. Coordinate axes and the color legend covered with the white export background for homepage display. Empty margins trimmed to a fixed viewport enclosing the model throughout all source frames, with approximately 7% margin per side, then fitted to the existing card dimensions. Original duration preserved; no added motion. Original AVI retained unchanged. Identical consecutive frames may be merged by the encoder.'
    }
    records = [r for r in records if r['source_filename'] != filename] + [record]
    manifest_path.write_text(json.dumps({'animations': records}, indent=2) + '\n')
    print(filename, output_count, 'frames,', total_ms, 'ms,', animation.stat().st_size, 'bytes', flush=True)
    for frame in frames:
        frame.close()

by_case = {Path(record['animation']).parent.name: record for record in records}
manifest_path.write_text(json.dumps({'animations': [by_case[case] for case, _ in cases]}, indent=2) + '\n')
