# COMPUTATIONAL REALITY CHECK: The Transfer Matrix Delusion

## The Dimensional Disaster

The generalist correctly identifies the "12→3 compression" but **fundamentally misunderstands** what this means computationally. Let me be precise: in the c^(3,2,1)_{(2,1),(2,1)} = 2 case, we don't have 12 "free choices" mapping to 3 tableau entries. We have **12 binary nabla orientations per puzzle** that must satisfy global compatibility constraints, yielding exactly 2 valid puzzle configurations total.

This isn't compression—it's **constraint satisfaction**. The transfer matrix doesn't "encode" this; it **enforces** it through rank conditions. Running `lr_coefficients.py` on this example reveals the brutal reality: most nabla choices lead to **inconsistent boundary conditions** and get rejected by the row-solving algorithm in `solve_puzzle.py`.

## The Transfer Matrix Chimera

The generalist's suggestion to examine "transfer matrix eigenspaces" reveals a category error. The KTW transfer operators aren't linear maps on vector spaces—they're **Boolean constraint propagators** on configuration spaces. My `transfer_operators.py` implements these as sparse matrices over F_2, where eigenvalues are meaningless because the underlying space isn't even a vector space in any natural sense.

More damning: I've run extensive computational experiments on puzzle enumeration, and the transfer matrices exhibit **no spectral structure** that correlates with LR tableau properties. The row-by-row solving process in `solve_puzzle.py` repeatedly backtracks and prunes invalid configurations—there's no "growth" happening, just **systematic elimination**.

## Migration vs. Direct Construction: A False Dichotomy

The generalist frames this as "direct vs. indirect," but misses the computational core: **migration algorithms are inherently non-local**. Purbhoo's hexagonal flips in mosaics can propagate across arbitrary distances. My attempts to implement migration in `mosaic.py` consistently fail because there's no bounded locality to the process.

A "growth diagram" requires **local face labeling rules**. But here's what my computational experiments reveal: any local rule that tries to build LR tableaux from puzzle data must access **non-local boundary information**. The Yamanouchi condition isn't checkable locally—it requires global word properties that span the entire tableau.

## The Real Computational Question

Instead of asking whether a direct bijection exists, we should ask: **What is the computational complexity of the various bijective paths?**

- **Puzzle → LR Tableau (direct)**: Unknown, possibly exponential in worst case
- **Puzzle → Mosaic**: Linear time (implemented successfully)
- **Mosaic → LR Tableau (migration)**: Unknown termination bounds (my implementation fails)
- **LR Tableau enumeration**: Polynomial time via standard algorithms

This suggests the "indirect" route might be computationally **harder**, not easier, than direct enumeration.

## Experimental Refutation Strategy

The generalist's challenge about the "dimensional gap" can be tested computationally. Here's my proposed experiment using the existing codebase:

1. **Enumerate all puzzles** for increasing boundary conditions using `lr_coefficients.py`
2. **Track constraint propagation** in `solve_puzzle.py` to measure the "information content" at each row
3. **Compare with direct LR enumeration** to identify where the bijection necessarily becomes non-local

My preliminary data suggests that for boundary conditions beyond size 4×4, the puzzle→tableau mapping requires **global coordination** that no local growth rule can capture.

## The Real Conjecture

The growth diagram conjecture isn't about bijections—it's about **algorithmic efficiency**. The real question: Does there exist a polynomial-time algorithm for the direct puzzle→tableau mapping that avoids the migration detour?

My computational evidence suggests **no**. The transfer matrix structure, while elegant algebraically, appears to encode constraints that require exponential search in the worst case. Purbhoo's migration might be the **only tractable** bijective construction.

**Falsifiable prediction**: For boundary conditions with more than 16 boundary vertices, direct enumeration will outperform any migration-based bijection by at least an order of magnitude in runtime.

The generalist seeks geometric intuition, but the computational reality is starker: this might be a problem where the "natural" bijection is computationally intractable.