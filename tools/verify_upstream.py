"""Optional online check: compare every archived sequence with pinned upstream HTML.

This verifies transcription and attribution, not the correctness of the source.
Run separately from offline CI: python tools/verify_upstream.py
"""
import json
from pathlib import Path
import re
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]

def parse_rows(page):
    result = {}
    for name, body in re.findall(r'<tr id="(N\d+L\d+D\d+[^\"]*)">(.*?)</tr>', page, re.S):
        mono = re.search(r'<p class="mono">(.*?)</p>', body, re.S)
        if mono is None:
            continue
        layers = []
        for line in re.split(r'<br\s*/?>', mono.group(1)):
            pairs = [[int(i),int(j)] for i,j in re.findall(r'\((\d+),(\d+)\)', line)]
            if pairs:
                layers.append(pairs)
        result[name] = (layers, 'Mason Hemmer' in body)
    return result

def main():
    nets = json.loads((ROOT/'data/networks.json').read_text())['networks']
    nets.append(json.loads((ROOT/'data/worst_case_baseline.json').read_text()))
    cache = {}
    for net in nets:
        page, anchor = net['source'].split('#')
        prefix = 'https://github.com/bertdobbelaere/SorterHunter/blob/'
        if not page.startswith(prefix):
            raise ValueError('Unexpected upstream source')
        suffix = page[len(prefix):]
        if not re.fullmatch(r'[0-9a-f]{40}/[a-z_]+\.html', suffix):
            raise ValueError('Source must be a pinned HTML snapshot')
        if page not in cache:
            url = 'https://raw.githubusercontent.com/bertdobbelaere/SorterHunter/' + suffix
            with urlopen(url, timeout=60) as response:
                cache[page] = parse_rows(response.read().decode())
        layers, credited = cache[page][anchor]
        if layers != net['layers'] or (net['category'] != 'baseline' and not credited):
            raise ValueError(f"{net['id']}: upstream sequence/attribution mismatch")
    print('PASS: 84 contributed sequences and 1 baseline match pinned upstream sources')

if __name__ == '__main__':
    main()
