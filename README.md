# Mason Hemmer

### Algorithms research · Exact counting · AI-assisted engineering

**From a research objective to externally incorporated algorithmic improvements.**

Research contributions: **October 2026** · Portfolio verified: **November 6, 2026**

I established and directed a project to improve sorting and median-selection networks, organized the search and verification workflow, and coordinated submissions for external review. The public maintainer records credit the resulting networks and an idea behind exact average-swap counting.

**57 median-network contributions · 26 average-swap networks · 21 → 20 worst-case swaps for 10 inputs**

[Results matrix](docs/RESULTS.md) · [Methodology and derivation](docs/METHODOLOGY.md) · [Public evidence](docs/EVIDENCE.md) · [Run the checks](#reproduce-the-core-claims)

## Contribution timeline

Dates below are documented public incorporation dates, rather than inferred discovery dates. Each links to a permanent contribution record. Later improvements do not change this historical attribution.

| Public incorporation | Contribution | Permanent record |
| --- | --- | --- |
| **October 5, 2026** | First 19 median-selection networks | [Maintainer acknowledgment](https://github.com/bertdobbelaere/SorterHunter/commit/99eb2a5e7cfec223517a01bc7a80a51ca1b246de) |
| **October 10, 2026** | 10-input worst-case swaps: 21 → 20 | [Before/after diff](https://github.com/bertdobbelaere/SorterHunter/commit/9187435b0eb9ef6761a0a18c56331504d400a1bd) |
| **October 17, 2026** | 38 additional median-selection networks | [38 committed network files](https://github.com/bertdobbelaere/SorterHunter/commit/4f1b0c9351eb5aa5f2a4b6f582a4e7402cce0f57) |
| **October 18, 2026** | 26 average-swap networks and exact-counting idea credit | [Maintainer acknowledgment](https://github.com/bertdobbelaere/SorterHunter/commit/2d3c63b0ca965768243e0e3b1c33b4a030b08613) |

The second median batch is dated October 16 in the page history and October 17 in the Git commits. Both dates are retained in the [evidence ledger](docs/EVIDENCE.md).

## Selected before / after results

| Incorporated | Inputs | Objective | Old count | Contributed count | Reduction |
| --- | ---: | --- | ---: | ---: | ---: |
| 2026-10-10 | 10 | Worst-case swaps | 21 | **20** | **4.762%** |
| 2026-10-18 | 18 | Average swaps | 27.5617 ± 0.0013 | 27.53892317 | ≈ 0.083% |
| 2026-10-18 | 29 | Average swaps | 57.4128 ± 0.0019 | 57.30485000 | ≈ 0.188% |
| 2026-10-18 | 33 | Average swaps | 71.8951 ± 0.0022 | 71.38180359 | ≈ 0.714% |
| 2026-10-18 | 35 | Average swaps | 77.3440 ± 0.0021 | 76.99453654 | ≈ 0.452% |
| 2026-10-18 | 63 | Average swaps | 179.8926 ± 0.0045 | 178.91981218 | ≈ 0.541% |

The worst-case comparison is exact and retains 29 comparators and 8 layers. Average-swap percentages compare old sampled central values with the new exact-method values displayed in the public table; they are approximate, not certified exact gains. The 33-input published entry also changes depth from 16 to 15. See the [full 26-row matrix](docs/RESULTS.md) for dimensions, uncertainty, the 26-input tradeoff, and the unresolved sampled comparison at 31 inputs.

## Engineering approach

**Define a measurable objective.** Separate comparison count, parallel depth, average swaps, and worst-case swaps so that each search targets an explicit outcome.

**Build a verification path.** Use exact counting where feasible, cross-check with separately implemented code, and preserve sampled uncertainty where exact evaluation is unavailable.

**Close the loop with an external maintainer.** Package candidate networks and supporting evidence, coordinate review, and connect incorporated results to permanent public records.

The strongest evidence of this work is inspectable: upstream attribution, a pinned before/after matrix, the mathematical derivation, and executable reproduction checks.

## The counting idea

A comparison does not always cause a swap. To count average swaps exactly, mark one input rank, map smaller values to 0, the marked value to 1, and larger values to 2. Each resulting word represents a known number of distinct permutations. Count when the marked larger operand meets a smaller operand, and weight that event by the number of represented permutations.

This replaces direct enumeration of $n!$ permutations with $n\,2^{n-1}$ three-valued words. For comparator $k$, let $T_k$ be its weighted swap count:

$$A(N)=\frac{1}{n!}\sum_k T_k.$$

The maintainer credits an idea proposed by Mason Hemmer for this three-valued refinement. [Full derivation, assumptions, and prior-work attribution](docs/METHODOLOGY.md).

## Reproduce the core claims

Requires Python 3.10+ and a C++17 compiler. No external Python packages or network access are needed after cloning.

```bash
python3 tools/verify_counting.py
c++ -O3 -std=c++17 tools/verify_worst_case.cpp -o /tmp/verify_worst_case
/tmp/verify_worst_case
```

- The Python check compares exact per-comparator ternary totals against brute force for **24 deterministic test networks**, including non-sorting networks, across 2–7 inputs.
- The C++ check evaluates **all 3,628,800 permutations of each 10-input network**, checks sorted output, reports exact total swaps, and prints a worst-case witness. Expected maxima: **21 before, 20 after**.

These are new, readable reproduction tools for this portfolio. They are not the original search engine and do not reverify all 57 median or 26 average-swap contributions. [Recorded run output](docs/VALIDATION.txt).

## Project responsibilities

**Mason Hemmer:** project establishment, research direction, review of outputs, and submission coordination. **Claude agents:** historical search, implementation, and checking work. **ChatGPT / Codex:** AI-assisted review, additional checking, and implementation, as acknowledged in the upstream records. **Bert Dobbelaere / SorterHunter:** published starting networks, collection, and incorporation.

The underlying untangling construction is classical. Scope, prior work, and the distinction between incorporation and optimality are documented in [Methodology](docs/METHODOLOGY.md) and [Evidence](docs/EVIDENCE.md).

## Repository guide

| File | Purpose |
| --- | --- |
| [docs/RESULTS.md](docs/RESULTS.md) | Complete published before/after matrix and qualifications |
| [docs/METHODOLOGY.md](docs/METHODOLOGY.md) | Exact-counting derivation and transformation objective |
| [docs/EVIDENCE.md](docs/EVIDENCE.md) | Pinned third-party evidence and claim boundaries |
| [data/average_swap_comparison.csv](data/average_swap_comparison.csv) | Machine-readable 26-row comparison |
| [tools/verify_counting.py](tools/verify_counting.py) | Small-input exact-counting cross-check |
| [tools/verify_worst_case.cpp](tools/verify_worst_case.cpp) | Exhaustive 10-input before/after verification |

**Historical record policy:** Results are reported as incorporated in October 2026. They are not advertised as perpetually unbeaten records. Pinned source commits preserve the baseline and contributed values even if the live tables change.

Public records checked November 6, 2026. Upstream source notices are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
