# Verification scope

Run `python tools/verify_all.py` from the repository root (Python 3.12 and C++17). No Python packages or network access are required. GitHub Actions runs this command on every push and pull request; failures return a nonzero exit status.

| Check | Coverage | What it establishes |
| --- | --- | --- |
| Inventory | 57 median + 26 average + 1 worst-case versions; 70 distinct targets | Counts, unique entries, CSV dimensions |
| Structure | Every archived network | Comparator bounds, exact size, stated layer count, disjoint wires per layer |
| Regression inputs | Every archived network, over 2,000 deterministic inputs each | No counterexample among the tested inputs; **not exhaustive correctness** |
| Counting identity | 24 deterministic networks, 2–7 inputs | Exact per-comparator agreement between weighted ternary enumeration and all permutations |
| Worst-case reproduction | Both 10-input networks, all 10! permutations each | Sorting correctness, exact total/average swaps and exact maximum, with witnesses |
| Optional upstream check | Every contributed sequence plus the baseline | Exact transcription and attribution match against pinned source pages |

The regression corpus includes sorted/reversed distinct inputs, binary inputs at every population count in three arrangements, 1,000 seeded random permutations, and 1,000 seeded random ternary inputs. Median tests compare the center value for odd sizes and the unordered pair of central values for even sizes. Small damaged-network tests exercise rejection of invalid dimensions, incorrect sorting, and an incorrect central pair.

For the exhaustive result, the C++ checker reads the actual archived JSON sequences via a temporary text file prepared by the runner. It does not verify a separate hard-coded copy. The runner checks both networks' structures before execution. Exact averages are computed from integer swap totals over 3,628,800 permutations.

## Optional online provenance check

```bash
python tools/verify_upstream.py
```

This fetches only commit-pinned public SorterHunter HTML snapshots, requires the named attribution on each contributed row, and compares every comparator and layer. It is kept out of offline CI so upstream availability cannot make a correct local test fail. It is an attribution/transcription check, not an independent mathematical proof.

## Limits

The suite does not exhaustively verify all 57 median networks or 26 large sorting networks, recompute their swap averages, certify their search optimality, or reproduce the original research campaign. Symbolic proof attempts during this portfolio update encountered resource limits; no inconclusive result is labeled as a pass. The published large-input exact-method averages retain their upstream attribution and rounding. The 52-input average is sampled.

The recorded local output is in [VALIDATION.txt](VALIDATION.txt). Historical incorporation dates are separate from validation dates. The GitHub Actions run attached to a commit is the authoritative status for that commit.
