"""Check the book manifest and local TeX inputs; not a mathematical review."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'course-study/chapters.json').read_text(encoding='utf-8'))
errors = []
seen = set()
def visit(p):
    if p in seen:
        return
    seen.add(p)
    if not p.is_file():
        errors.append(f'Missing input: {p.relative_to(root)}')
        return
    text = p.read_text(encoding='utf-8')
    if '\ufffd' in text:
        errors.append(f'Replacement character: {p.relative_to(root)}')
    text = re.sub(r'(?m)(?<!\\)%.*$', '', text)
    for name in re.findall(r'\\input\{([^}]+)\}', text):
        visit(root / (name if name.endswith('.tex') else name + '.tex'))
visit(root / 'main.tex')
for ch in manifest:
    p = root / 'course-study/chapters' / ch['id'] / 'chapter.tex'
    if p not in seen:
        errors.append(f'Chapter not included: {ch["id"]}')
    elif p.is_file():
        text = p.read_text(encoding='utf-8')
        for title in ch['sections']:
            if '\\section{' + title + '}' not in text:
                errors.append(f'Missing planned section: {ch["id"]}: {title}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(manifest)} chapters, {len(seen)} reachable TeX files; mathematical correctness not checked.')
