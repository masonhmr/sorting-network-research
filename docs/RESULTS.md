# Published results matrix

**Contribution period: October 2026.** All numbers describe the pinned incorporation snapshots, not a claim of current best performance. Exact discovery and original submission dates are not inferred from commit timestamps.

## Average swaps: all 26 credited entries

**Public incorporation: October 18, 2026.**

Baseline: [page immediately before incorporation](https://github.com/bertdobbelaere/SorterHunter/blob/cbc16ccc17bd24b2f4265aa3a4139e02d23ea61b/sorting_networks_avgswaps.html). Contribution: [October 18, 2026 snapshot](https://github.com/bertdobbelaere/SorterHunter/blob/2d3c63b0ca965768243e0e3b1c33b4a030b08613/sorting_networks_avgswaps.html). These pinned snapshots prevent later table changes from silently altering the comparison.

All old averages in this table are sampled estimates. The new values use the maintainer's exact method except the 52-input estimate. Percentages below compare displayed central values; they are approximate descriptive differences, not exact certified gains or runtime speedups. The source's ± terms are reproduced without assuming a confidence level.

| Incorporated | Inputs | Old published average | Contributed average | Displayed-mean reduction | Size / depth (old → new) |
| --- | ---: | ---: | ---: | ---: | --- |
| 2026-10-18 | 18 | 27.5617 ± 0.0013 | 27.53892317 | ≈ 0.083% | 77/12 → 77/12 |
| 2026-10-18 | 19 | 30.3220 ± 0.0013 | 30.31516042 | ≈ 0.023% | 85/12 → 85/12 |
| 2026-10-18 | 24 | 43.0628 ± 0.0016 | 43.05845856 | ≈ 0.010% | 120/13 → 120/13 |
| 2026-10-18 | 26 | 49.3629 ± 0.0018 | 48.39758018 | ≈ 1.956% | 139/14 → 138/15 |
| 2026-10-18 | 29 | 57.4128 ± 0.0019 | 57.30485000 | ≈ 0.188% | 164/15 → 164/15 |
| 2026-10-18 | 31 | 63.7472 ± 0.0022 | 63.74755294 | Unresolved¹ | 180/14 → 180/14 |
| 2026-10-18 | 33 | 71.8951 ± 0.0022 | 71.38180359 | ≈ 0.714% | 199/16 → 199/15 |
| 2026-10-18 | 35 | 77.3440 ± 0.0021 | 76.99453654 | ≈ 0.452% | 220/17 → 220/17 |
| 2026-10-18 | 37 | 82.4906 ± 0.0024 | 82.13723147 | ≈ 0.428% | 240/17 → 240/17 |
| 2026-10-18 | 41 | 96.3299 ± 0.0027 | 95.88952840 | ≈ 0.457% | 282/19 → 282/19 |
| 2026-10-18 | 43 | 99.9393 ± 0.0027 | 99.58105941 | ≈ 0.358% | 303/19 → 303/19 |
| 2026-10-18 | 45 | 108.7602 ± 0.0028 | 108.25524114 | ≈ 0.464% | 324/19 → 324/19 |
| 2026-10-18 | 47 | 114.4640 ± 0.0030 | 114.28902412 | ≈ 0.153% | 340/19 → 340/19 |
| 2026-10-18 | 49 | 123.1709 ± 0.0035 | 123.11870115 | ≈ 0.042% | 365/21 → 365/21 |
| 2026-10-18 | 50 | 127.1707 ± 0.0038 | 127.13137078 | ≈ 0.031% | 376/21 → 376/21 |
| 2026-10-18 | 51 | 130.2316 ± 0.0036 | 129.62481511 | ≈ 0.466% | 387/22 → 387/22 |
| 2026-10-18 | 52 | 135.0479 ± 0.0034 | 134.9362 ± 0.0011 | ≈ 0.083% | 395/20 → 395/20 |
| 2026-10-18 | 53 | 138.0453 ± 0.0038 | 137.53314779 | ≈ 0.371% | 411/22 → 411/22 |
| 2026-10-18 | 55 | 147.4487 ± 0.0036 | 147.39656430 | ≈ 0.035% | 432/20 → 432/20 |
| 2026-10-18 | 56 | 152.8920 ± 0.0037 | 152.40655943 | ≈ 0.318% | 438/20 → 438/20 |
| 2026-10-18 | 57 | 155.0971 ± 0.0039 | 154.27518885 | ≈ 0.530% | 454/21 → 454/21 |
| 2026-10-18 | 58 | 160.2563 ± 0.0040 | 160.00230491 | ≈ 0.158% | 465/21 → 465/21 |
| 2026-10-18 | 59 | 163.0882 ± 0.0039 | 162.65622073 | ≈ 0.265% | 476/21 → 476/21 |
| 2026-10-18 | 61 | 169.3583 ± 0.0046 | 168.65349632 | ≈ 0.416% | 497/22 → 497/22 |
| 2026-10-18 | 62 | 174.4571 ± 0.0045 | 173.80426406 | ≈ 0.374% | 506/21 → 506/21 |
| 2026-10-18 | 63 | 179.8926 ± 0.0045 | 178.91981218 | ≈ 0.541% | 515/21 → 515/21 |

¹ For 31 inputs, the new exact-method value (63.74755294) is slightly above the old sampled central value (63.7472 ± 0.0022). That difference is within the displayed uncertainty. This old estimate cannot establish the gain; the contribution is still publicly credited. No positive percentage is inferred from it.

The 26-input row changes comparator count and depth. The 33-input row changes the published depth. These are explicitly shown rather than presented as identical-architecture comparisons.

Machine-readable version: [CSV](../data/average_swap_comparison.csv). Reduction is calculated as `(old central value - new central value) / old central value * 100`.

## Worst-case swaps: 10 inputs

**Public incorporation: October 10, 2026.**

| Metric | Previous network | Contributed network |
| --- | ---: | ---: |
| Comparators | 29 | 29 |
| Layers | 8 | 8 |
| Maximum swaps | 21 | 20 |
| Average swaps | 10.77619048 | 11.49365079 |

Worst-case reduction: **1 swap, or 4.7619%**. Average swaps increase for this particular network; it addresses a different objective. [Pinned before/after diff](https://github.com/bertdobbelaere/SorterHunter/commit/9187435b0eb9ef6761a0a18c56331504d400a1bd).

## Median selection

**Public incorporation: October 5 and October 17, 2026.**

**57 incorporated contributions** across two batches: 19 acknowledged October 5 and 38 additional network files committed October 17. Median selection returns the middle value(s) without fully sorting all inputs. Its size/depth improvements must not be added to a swap-count percentage. These are historical contribution counts, not a claim of 57 currently unbeaten records. [Evidence](EVIDENCE.md).
