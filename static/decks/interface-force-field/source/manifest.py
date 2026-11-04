#!/usr/bin/env python3
"""Record final artifact hashes after exports and the title image are ready."""
import hashlib
import json
from pathlib import Path

bundle = Path(__file__).resolve().parent.parent
destination = bundle/'artifact-manifest.json'
hero = bundle.parents[1]/'images/writings/interface-force-field-title.png'
files = [path for path in sorted(bundle.rglob('*')) if path.is_file()
         and path != destination and '__pycache__' not in path.parts and path.suffix != '.pyc']
manifest = {'schema':'iff-presentation.artifacts/v2',
            'files':{str(path.relative_to(bundle)):{'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                      'bytes':path.stat().st_size} for path in files},
            'title_image':{'url':'/images/writings/interface-force-field-title.png',
                           'sha256':hashlib.sha256(hero.read_bytes()).hexdigest(),
                           'bytes':hero.stat().st_size}}
destination.write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Recorded {len(files)} bundle files and the actual title image; manifest excludes itself.')
