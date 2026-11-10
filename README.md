# Median-selection and swap-count optimization

**Mason Hemmer · AI-assisted research · October 2026**

My project contributed a 10-input sorting network that reduces worst-case swaps from **21 to 20**, using the same **29 comparators and 8 layers**. Bert Dobbelaere incorporated it into SorterHunter on October 10, 2026. The included C++ checker evaluates all **3,628,800 input permutations** for both networks.

[Verify the result](#run-the-checks) · [Network data](data/networks.json) · [Results](docs/RESULTS.md) · [Upstream evidence](docs/EVIDENCE.md) · [Methodology](docs/METHODOLOGY.md)

## What this project contributed

These contributions concern **median selection, average swaps, and worst-case swaps**. This portfolio makes no claim to a new general sorting-network size or depth record in the main sorting tables, and no claim of global optimality or measured runtime speedup.

| Objective | Accepted network versions | Distinct targets | Evidence in this repository |
| --- | ---: | ---: | --- |
| Median selection | 57 | 43 | All sequences and layer schedules; bounded correctness checks |
| Average swaps | 26 | 26 | All sequences; bounded sorting checks; published comparison values |
| Worst-case swaps | 1 | 1 | Sequence; exhaustive before/after swap counts |
| **Total** | **84** | **70** | **14 median versions revisit an earlier target** |

A median target is an input-count/depth pair; an average-swap target is an input count; the worst-case objective is counted separately. These are contribution counts, not 70 independently proven records. In particular, the old sampled 31-input average does not establish a positive gain. The November 7 audit found 68 contributed entries still listed; that is a dated observation, not a live guarantee.

## Lead result: one fewer worst-case swap

| Metric | Previous network | Contributed network |
| --- | ---: | ---: |
| Inputs | 10 | 10 |
| Comparators | 29 | 29 |
| Layers | 8 | 8 |
| Maximum swaps | 21 | **20** |
| Average swaps | 10.77619048 | 11.49365079 |

The maximum falls by **4.7619%**. The average increases: this network targets the worst case. Both counts are reproduced locally, with an input witnessing each maximum. [Maintainer's before/after commit](https://github.com/bertdobbelaere/SorterHunter/commit/9187435b0eb9ef6761a0a18c56331504d400a1bd).

## Average-swap results in context

| Inputs | Old published average | Contributed average | Approximate reduction | Size/depth |
| ---: | ---: | ---: | ---: | --- |
| 26 | 49.3629 ± 0.0018 | 48.39758018 | 1.956% | 139/14 → 138/15 |
| 33 | 71.8951 ± 0.0022 | 71.38180359 | 0.714% | 199/16 → 199/15 |
| 63 | 179.8926 ± 0.0045 | 178.91981218 | 0.541% | 515/21 → 515/21 |

The old values are sampled estimates. New values above are **reported by the upstream exact method**, rounded for display; this repository does not recompute those large-input averages. The 26-input result trades an extra layer for fewer comparators. All other positive displayed reductions in the [26-row matrix](docs/RESULTS.md) are below 1%; the 31-input gain is unresolved against its sampled baseline. None of these percentages is a measured execution-time improvement.

## Run the checks

Use Linux, Python 3.12, and a C++17 compiler. The suite uses only the Python standard library and a C++17 compiler; no package installation or network access is needed:

```bash
python3 -m venv .venv
source .venv/bin/activate
python tools/verify_all.py
```

The same command runs on every push and pull request in [GitHub Actions](.github/workflows/verify.yml).

The suite checks the inventory and layer schedules, tests every bundled network on more than 2,000 deterministic inputs, cross-checks the counting identity on 24 small networks, and exhaustively verifies both 10-input swap counts. The large-network regression tests are not exhaustive proofs. The suite **does not** establish large-input swap averages or optimality. [Verification scope and recorded output](docs/VERIFICATION.md).

## The exact-counting idea—and its limit

The upstream maintainer credits an idea I proposed: distinguish one input rank and map other ranks to smaller/equal/larger values. Weighted counts of these three-valued inputs give exact swap probabilities. The simple reference algorithm visits `n × 2^(n−1)` words.

At 63 inputs that is **290,536,219,160,925,437,952 words**. This reference implementation cannot practically reproduce the published 63-input average. The large-input computation's implementation, resource usage, and exact integer certificate are not included here; bit slicing alone does not resolve that gap. The value is retained as upstream-reported, not presented as a locally reproduced result. [Derivation and scope](docs/METHODOLOGY.md).

## My role and AI assistance

I established and directed the project and was responsible for submission. The [maintainer's acknowledgment](https://github.com/bertdobbelaere/SorterHunter/commit/99eb2a5e7cfec223517a01bc7a80a51ca1b246de) documents those responsibilities. Claude agents ran the historical searches and wrote checkers; ChatGPT reviewed the submission, wrote additional checking code, hardened inputs, and reran checks. The current portfolio tools and documentation were also developed with AI assistance.

This repository does not claim that I personally wrote every implementation. It provides the accepted outputs, the public attribution, and checks a reviewer can run. The original search engine and a complete decision-by-decision project log are not included. Starting networks and the collection are credited to Bert Dobbelaere; the untangling construction is classical.

## Public incorporation dates

| Date | Contribution | Permanent evidence |
| --- | --- | --- |
| October 5, 2026 | 19 median versions | [Acknowledgment](https://github.com/bertdobbelaere/SorterHunter/commit/99eb2a5e7cfec223517a01bc7a80a51ca1b246de) |
| October 10, 2026 | 21 → 20 worst-case swaps | [Before/after](https://github.com/bertdobbelaere/SorterHunter/commit/9187435b0eb9ef6761a0a18c56331504d400a1bd) |
| October 17, 2026 | 38 median versions | [Network additions](https://github.com/bertdobbelaere/SorterHunter/commit/4f1b0c9351eb5aa5f2a4b6f582a4e7402cce0f57) |
| October 18, 2026 | 26 average-swap versions and counting-idea credit | [Acknowledgment](https://github.com/bertdobbelaere/SorterHunter/commit/2d3c63b0ca965768243e0e3b1c33b4a030b08613) |

These are incorporation dates, not inferred discovery dates. The second median batch's page history says October 16; its commits are October 17. Historical versions remain in the dataset even when a later network improves them.

MIT licensed; upstream attribution and license are preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). See [application wording](docs/APPLICATION.md) for a short factual project description.
