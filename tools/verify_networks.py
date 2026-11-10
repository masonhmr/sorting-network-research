"""Bounded regression checks for every archived network, not an exhaustive proof."""
from collections import Counter
import csv
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]

def validate_structure(net):
    n = net['n']
    if len(net['layers']) != net['depth']:
        raise ValueError(f"{net['id']}: depth mismatch")
    if sum(map(len, net['layers'])) != net['size']:
        raise ValueError(f"{net['id']}: size mismatch")
    for layer in net['layers']:
        wires = []
        for i, j in layer:
            if not 0 <= i < j < n:
                raise ValueError(f"{net['id']}: invalid comparator")
            wires.extend((i, j))
        if len(wires) != len(set(wires)):
            raise ValueError(f"{net['id']}: overlapping layer")

def check_case(net, values):
    expected = sorted(values)
    output = list(values)
    for layer in net['layers']:
        for i, j in layer:
            if output[i] > output[j]:
                output[i], output[j] = output[j], output[i]
    if net['category'] == 'median':
        n = net['n']
        positions = [n//2] if n % 2 else [n//2-1, n//2]
        # Even-N selectors may return the central pair in either order.
        valid = sorted(output[i] for i in positions) == [expected[i] for i in positions]
    else:
        valid = output == expected
    if not valid:
        raise RuntimeError(f"{net['id']}: counterexample {values}")

def cases(n):
    rng = random.Random(20261109 + n)
    yield list(range(n))
    yield list(range(n-1, -1, -1))
    # Every population count in three arrangements, including constant inputs.
    for ones in range(n+1):
        values = [0]*(n-ones) + [1]*ones
        yield values.copy()
        yield values[::-1]
        rng.shuffle(values)
        yield values.copy()
    for _ in range(1000):
        values = list(range(n))
        rng.shuffle(values)
        yield values
        yield [rng.randrange(3) for _ in range(n)]

def verifier_regressions():
    good = {'id':'test', 'n':3, 'size':3, 'depth':3, 'category':'average_swaps',
            'layers':[[[0,1]],[[1,2]],[[0,1]]]}
    check_case(good, [2,1,0])
    broken = dict(good, layers=[[[0,1]]])
    for checker in (validate_structure, lambda x: check_case(x, [2,1,0])):
        try:
            checker(broken)
        except (ValueError, RuntimeError):
            pass
        else:
            raise RuntimeError('Verifier failed to reject a damaged network')
    even = {'id':'even-test','n':4,'category':'median','layers':[]}
    check_case(even, [0,2,1,3])
    try:
        check_case(even, [1,0,2,3])
    except RuntimeError:
        pass
    else:
        raise RuntimeError('Verifier accepted incorrect central pair')

def main():
    verifier_regressions()
    data = json.loads((ROOT/'data/networks.json').read_text())
    if data['schema_version'] != 1:
        raise ValueError('Unsupported schema')
    nets = data['networks']
    counts = Counter(x['category'] for x in nets)
    if counts != {'median':57, 'average_swaps':26, 'worst_case_swaps':1}:
        raise ValueError(f'Unexpected inventory: {counts}')
    keys = [(x['category'], x['id']) for x in nets]
    targets = {(x['category'], x['n'], x['depth'] if x['category']=='median' else None) for x in nets}
    if len(keys) != len(set(keys)) or len(targets) != 70:
        raise ValueError('Duplicate entry or unexpected target count')
    with (ROOT/'data/average_swap_comparison.csv').open() as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 26 or len({int(r['inputs']) for r in rows}) != 26:
        raise ValueError('Unexpected average comparison inventory')
    for row in rows:
        match = [x for x in nets if x['category']=='average_swaps' and x['n']==int(row['inputs'])]
        if len(match)!=1 or (match[0]['size'],match[0]['depth']) != (int(row['new_size']),int(row['new_depth'])):
            raise ValueError('Average CSV dimensions disagree with network data')
    for index, net in enumerate(nets, 1):
        validate_structure(net)
        tested = 0
        for values in cases(net['n']):
            check_case(net, values)
            tested += 1
        print(f"PASS {index}/{len(nets)} {net['category']} {net['id']}: {tested} regression inputs", flush=True)
    print('PASS: all 84 networks passed bounded regression checks; NOT exhaustive correctness proofs or exact average verification')

if __name__ == '__main__':
    main()
