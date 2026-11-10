# Evidence ledger

Pinned attribution sources rechecked November 9, 2026. Commit links pin the evidence to a specific historical version; live pages may change.

| Claim | Source | What the source establishes |
| --- | --- | --- |
| 19 initial median-network contributions | [99eb2a5](https://github.com/bertdobbelaere/SorterHunter/commit/99eb2a5e7cfec223517a01bc7a80a51ca1b246de) | Maintainer explicitly acknowledges 19 networks, Mason's project direction and submission responsibility, and AI implementation/checking assistance. |
| Worst-case swaps reduced from 21 to 20 at N=10 | [9187435](https://github.com/bertdobbelaere/SorterHunter/commit/9187435b0eb9ef6761a0a18c56331504d400a1bd) | Diff shows both network sequences and metrics. Use the sorting_networks_maxswaps.html diff; other changes in this commit credit Robert Lacroix and are not Mason's contributions. |
| 38 additional median-network files | [4f1b0c9](https://github.com/bertdobbelaere/SorterHunter/commit/4f1b0c9351eb5aa5f2a4b6f582a4e7402cce0f57) | Commit adds 38 JSON networks and credits Mason with AI assistance. |
| Second median batch acknowledgment | [c3cb9f8](https://github.com/bertdobbelaere/SorterHunter/commit/c3cb9f870af085c344f5118d900f07a89e8b8d43) | Maintainer records the contribution. Page history uses October 16; the commits are October 17. |
| 26 average-swap network contributions | [2d3c63b snapshot](https://github.com/bertdobbelaere/SorterHunter/blob/2d3c63b0ca965768243e0e3b1c33b4a030b08613/sorting_networks_avgswaps.html) | 26 network entries explicitly attribute the contribution to Mason; input sizes are listed below. |
| Counting-method idea credit | [2d3c63b message](https://github.com/bertdobbelaere/SorterHunter/commit/2d3c63b0ca965768243e0e3b1c33b4a030b08613) | Maintainer credits an idea proposed by Mason for the three-valued refinement used to compute exact averages for most networks, subject to resource limits. |

The 26 credited average-swap sizes are: **18, 19, 24, 26, 29, 31, 33, 35, 37, 41, 43, 45, 47, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 61, 62, 63**.

## Live public tables

- [Worst-case swaps: N=10, L=29, D=8, maximum 20](https://bertdobbelaere.github.io/sorting_networks_maxswaps.html#N10L29D8WCS20)
- [Average-swap networks](https://bertdobbelaere.github.io/sorting_networks_avgswaps.html)
- [Median-selection networks](https://bertdobbelaere.github.io/median_networks.html)

## Reproduction and limits

The verification suite and archived network inventory were added November 9, 2026 (America/New_York). [VALIDATION.txt](VALIDATION.txt) records actual output; [VERIFICATION.md](VERIFICATION.md) defines each check's scope. The exhaustive checker confirms sorting and worst-case counts for both 10-input networks. The Python identity tests cover 24 small networks; all 84 archived contributed versions receive bounded regression tests. Large-input swap averages and full large-network correctness proofs are not reproduced.

All 84 sequences and layer schedules are in [data/networks.json](../data/networks.json), each with its incorporation date and commit-pinned source. The second median snapshot includes the five surviving first-batch entries; the importer retained those only once, yielding 19 + 38 median versions. The optional `python tools/verify_upstream.py` checks exact layer-by-layer transcription and the named credit on all contributed source rows.

The public incorporation records are third-party evidence of acceptance and attribution. Separately implemented AI checkers are a different kind of evidence; they are not independent human review. The portfolio does not claim journal publication, universal optimality, or engineering performance measurements.

## Historical project material

The original submission material is retained separately. This public repository contains the dated portfolio and new reproduction tools, rather than the full historical search engine. The pinned upstream records above provide public evidence without requiring access to a private archive.

