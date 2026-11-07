"""Readable exact counter demo, not the original bit-sliced research implementation.

Cross-check every comparator's weighted ternary count against brute-force
permutation counts for deterministic sorting and arbitrary comparator networks.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial
import random

def permutation_totals(n, network):
    counts = [0] * len(network)
    for perm in permutations(range(n)):
        x = list(perm)
        for k, (i, j) in enumerate(network):
            if x[i] > x[j]:
                counts[k] += 1
                x[i], x[j] = x[j], x[i]
    return counts

def ternary_totals(n, network):
    counts = [0] * len(network)
    for marked in range(n):
        other = [i for i in range(n) if i != marked]
        for mask in range(1 << (n - 1)):
            x = [2] * n
            x[marked] = 1
            a = mask.bit_count()
            weight = factorial(a) * factorial(n - 1 - a)
            for bit, wire in enumerate(other):
                if mask & (1 << bit):
                    x[wire] = 0
            for k, (i, j) in enumerate(network):
                if x[i] == 1 and x[j] == 0:
                    counts[k] += weight
                if x[i] > x[j]:
                    x[i], x[j] = x[j], x[i]
    return counts

def main():
    rng = random.Random(20261106)
    cases = 0
    for n in range(2, 8):
        insertion = [(j - 1, j) for i in range(1, n) for j in range(i, 0, -1)]
        networks = [insertion]
        networks += [[tuple(sorted(rng.sample(range(n), 2))) for _ in range(n * 3)] for _ in range(3)]
        for net in networks:
            expected = permutation_totals(n, net)
            actual = ternary_totals(n, net)
            if expected != actual:
                raise RuntimeError(f'Per-comparator mismatch for n={n}: {expected} != {actual}')
            cases += 1
        print(f'n={n}: 4 networks passed; insertion-network average={Fraction(sum(ternary_totals(n, insertion)), factorial(n))}')
    print(f'PASS: {cases} networks, exact per-comparator agreement')

if __name__ == '__main__':
    main()
