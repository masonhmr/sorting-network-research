# Methodology

This is a concise exposition of the project's archived technical note, with a new readable reference implementation. The upstream maintainer credits an idea proposed by Mason Hemmer for the three-valued refinement used in exact average counting. That acknowledgment is not a claim of priority over all prior literature.

## 1. What is being optimized?

For a comparator network $N=(c_1,\ldots,c_s)$ and a uniformly random permutation $x$ of distinct ranks, let $s_k(N,x)$ indicate whether comparator $k$ swaps. Then

$$A(N)=\mathbb{E}\left[\sum_{k=1}^s s_k(N,x)\right]=\sum_{k=1}^s p_k,\qquad p_k=\Pr[s_k(N,x)=1].$$

$$W(N)=\max_x\sum_{k=1}^s s_k(N,x).$$

$A$ measures average swaps; $W$ measures worst-case swaps. Comparisons still execute even when no swap is required. Neither metric alone establishes wall-clock performance.

## 2. Count exactly without enumerating every permutation

Choose a distinguished rank $a$ and map each input value $v$ to a three-valued alphabet:

$$f_a(v)=\begin{cases}0&v<a,\\1&v=a,\\2&v>a.\end{cases}$$

This mapping is monotone and commutes with min/max. Consequently, applying it before or after any prefix of the comparator network gives the same three-valued state.

Let $\mathcal{W}_a$ contain words with $a$ zeros, exactly one 1, and $n-1-a$ twos. Each word represents exactly $a!(n-1-a)!$ distinct input permutations. At a comparator with lower-index wire $i_k$ and upper-index wire $j_k$, count the event $(y_{i_k},y_{j_k})=(1,0)$ immediately before the comparator executes.

$$T_k=\sum_{a=0}^{n-1}a!(n-1-a)!\sum_{w\in\mathcal{W}_a}\mathbf{1}[(y_{i_k},y_{j_k})=(1,0)].$$

Every actual swap is counted exactly once: at the distinguished rank equal to its larger operand. Therefore

$$p_k=\frac{T_k}{n!},\qquad A(N)=\frac{\sum_k T_k}{n!}.$$

There are $n\,2^{n-1}$ words across all choices of marked position and smaller-value positions. A direct implementation takes $O(s\,n\,2^{n-1})$ time, with polynomial space when words are processed one at a time. It is still exponential. The reference script favors clarity and exact Python integers. Bit slicing can improve constant factors, but does not remove the exponential scaling.

For a two-input comparator, only the ternary word `(1,0)` contributes to the numerator. Its weight is 1, giving an exact average of $1/2$ swap.

### Large-input computation is not reproduced here

For 63 inputs, direct enumeration requires 63 × 2^62 = 290,536,219,160,925,437,952 words, before accounting for the comparator work per word. This is not a practical explanation of the published 63-input computation. No claim is made that the included reference script performed it.

The October 18 upstream page states that most values use an exact method, subject to network structure and checker resource limits; the 63-input value is displayed without a sampling uncertainty. We report it as **upstream-reported exact-method output, rounded to eight decimals**. The historical large-input implementation, exact numerator/denominator certificates, hardware, runtime, and resource measurements are not available in this public repository. We cannot reconstruct its acceleration strategy from that acknowledgment alone. This gap remains explicit rather than being filled with an assumed algorithm. The 52-input value remains a sampled estimate.

The new verification command checks the large networks on bounded test inputs; it does not certify their average swap values. A complete large-input reproduction would require the actual scalable counter, its inputs and resource configuration, and exact integer outputs checked by an independent implementation.

## 3. Search through input-order transformations

The project used the classical untangling construction on relabeled starting networks. This preserves correctness, comparator count, and the layer schedule of the chosen base network. For a permutation $\pi$, the transformed network $S_\pi$ satisfies

$$A(S_\pi)=A(N)+\sum_k s_k(N,\pi)(1-2p_k).$$

A flipped comparator replaces probability $p_k$ with $1-p_k$. This turns average-swap search into a weighted optimization over input permutations. The historical search used OR-Tools CP-SAT; worst-case search used counterexamples to refine candidate transformations.

The preservation statement concerns a transformation of one base network. It does not mean every old and new entry in the published tables has the same size or depth: some contributions use a different baseline or represent a tradeoff.

## 4. Separate the claims

- **Correctness:** the output is sorted for all inputs. The 0-1 principle supports binary-input checking of comparator-network sorting correctness; binary testing alone does not establish permutation swap counts.
- **Exact average:** integer counting over weighted ternary words, followed by division by $n!$.
- **Exact worst case:** the included 10-input checker enumerates all $10!$ distinct permutations and finds a maximizing witness.
- **Class optimality:** best among transformations of a particular base network. No class-optimality certificate is included or newly claimed here.
- **Global optimality:** best among all eligible networks. Not established by this portfolio.

## Attribution and scope

Mason Hemmer established and directed the project and coordinated submission. Claude agents implemented and ran the historical search/checking work; ChatGPT and Codex assisted with review and implementation as described in the linked acknowledgments. Starting networks and the public collection are credited to Bert Dobbelaere / SorterHunter. Untangling is classical (Knuth, TAOCP Vol. 3, section 5.3.4, Exercise 16); related exchange-probability ideas appear in [Paeth's NICE networks](https://arxiv.org/abs/1808.05212).

This exposition is based on the archived project technical note. Historical implementation timings and optimality certificates are not presented as newly reproduced results. See [the evidence ledger](EVIDENCE.md) for public incorporation records.

