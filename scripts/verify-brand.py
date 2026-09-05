#!/usr/bin/env python3
"""Verify local Guide links and unchanged canonical artwork embedded in previews."""
from pathlib import Path
import base64
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
errors = []
links = 0
for page in ROOT.rglob('*.md'):
    if '.git' in page.parts:
        continue
    text = page.read_text()
    targets = re.findall(r'\]\(([^)]+)\)', text) + re.findall(r'(?:href|src)="([^"]+)"', text)
    for target in targets:
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        path = (page.parent / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT) or not path.exists():
            errors.append(f'{page.relative_to(ROOT)}: missing local link: {target}')
        links += 1
folder = ROOT / '.gitbook/assets/brand'
manifest = json.loads((folder/'provenance.json').read_text())
hashes = {source['sha256'] for source in manifest['sources']}
# Full hashes identify approved original bytes, not newly painted artwork.
assert hashes == {
    '0ce7d305e03a254c750b804c2326f3da9d58c9be06b22f239831a9bbfef5a3c6',
    '7aa3def5ce460dfd73491e717378439a43220d942a00a6af8b7cc527b6fb7479',
}
images = 0
for path in folder.glob('*.svg'):
    tree = ET.parse(path)
    for element in tree.iter():
        if element.tag.rsplit('}',1)[-1] not in {'svg','rect','image'}:
            errors.append(f'{path.name}: unsupported preview element')
        if element.tag.endswith('}image'):
            uri = element.attrib['href']
            if not uri.startswith(('data:image/png;base64,','data:image/jpeg;base64,')):
                errors.append(f'{path.name}: preview image must contain original bytes')
                continue
            digest = hashlib.sha256(base64.b64decode(uri.split(',',1)[1], validate=True)).hexdigest()
            if digest not in hashes:
                errors.append(f'{path.name}: changed canonical artwork')
            images += 1
if images != 3:
    errors.append('expected three original-artwork previews')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'local_link_paths={links}; canonical_artwork_previews={images}; OK')
