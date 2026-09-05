#!/usr/bin/env python3
"""Check GitBook math delimiters and independently recompute the published allocation.

This is a source consistency check, not verification of the population dataset
or of unimplemented on-chain policy. Use only Python's standard library.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []
blocks = []
for page in sorted(ROOT.rglob('*.md')):
    if '.git' in page.parts:
        continue
    fence = None
    math = None
    for number, line in enumerate(page.read_text().splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith(('```', '~~~')):
            marker = stripped[:3]
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence:
            continue
        text = re.sub(r'`+[^`]*`+', '', line)
        if stripped == '$$':
            if math is None:
                math = []
            else:
                formula = '\n'.join(math)
                blocks.append((page, formula))
                if not formula or formula.count('{') != formula.count('}') or r'\_' in formula:
                    errors.append(f'{page.relative_to(ROOT)}:{number}: malformed math block')
                math = None
            continue
        if math is not None:
            math.append(line)
        elif re.search(r'(?<!\\)\$|\\(?:frac|sum|sqrt|displaystyle|operatorname)\b|\\_', text):
            errors.append(f'{page.relative_to(ROOT)}:{number}: math outside display delimiters')
    if math is not None:
        errors.append(f'{page.relative_to(ROOT)}: unclosed math block')

page = ROOT / 'governance/sovereign-participation-reference.md'
source = page.read_text()
expected = r'\operatorname{Allocation}_i = 386{,}000{,}000 \left( \frac{0.75}{193} + 0.25 \frac{\sqrt{\operatorname{Population}_i}}{\sum_{j=1}^{193}\sqrt{\operatorname{Population}_j}} \right)'
formulas = [formula for path, formula in blocks if path == page]
if len(formulas) != 3 or formulas[0] != expected:
    errors.append('sovereign formula structure or count changed; requires policy review')

rows = []
for line in source.splitlines():
    cells = [cell.strip() for cell in line.split('|')]
    if len(cells) != 9 or not re.fullmatch('[A-Z]{3}', cells[3]) or not cells[4][:1].isdigit():
        continue
    def integer(cell):
        return int(re.sub(r'[\s,*]', '', cell))
    rows.append((cells[3], *(integer(cell) for cell in cells[4:8])))
if len(rows) != 193 or len({row[0] for row in rows}) != 193:
    errors.append('allocation table must contain 193 unique ISO3 rows')
else:
    with localcontext() as ctx:
        ctx.prec = 80
        roots = {iso: Decimal(pop).sqrt() for iso, pop, *_ in rows}
        denominator = sum(roots.values())
        exact = {iso: Decimal(386000000) * (Decimal('0.75') / 193 + Decimal('0.25') * root / denominator)
                 for iso, root in roots.items()}
        floors = {iso: int(value.to_integral_value(rounding=ROUND_FLOOR)) for iso, value in exact.items()}
        remainder = 386000000 - sum(floors.values())
        ranked = sorted(exact, key=lambda iso: (-(exact[iso] - floors[iso]), iso))
        rounded = {iso: value + (iso in ranked[:remainder]) for iso, value in floors.items()}
        for iso, pop, base, variable, total in rows:
            if pop <= 0 or base != 1500000 or base + variable != total or total != rounded[iso]:
                errors.append(f'{iso}: allocation does not match formula and largest-remainder rounding')
        if sum(floors.values()) != 385999899 or remainder != 101 or sum(r[-1] for r in rows) != 386000000:
            errors.append('allocation conservation or published rounding explanation differs')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'math_blocks={len(blocks)}; allocation_rows={len(rows)}; allocation_total=386000000; rounding_remainder=101; OK')
