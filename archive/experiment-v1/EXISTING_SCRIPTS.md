# Existing Scripts

Four Python scripts for computing with KTW puzzles, Littlewood-Richardson
coefficients, and related structures. These are tools for investigating the
open question, not answers to it.

## lr_coefficients.py

Computes Littlewood-Richardson coefficients c^ν_{λ,μ} by enumerating
KTW puzzle witnesses using a row transfer matrix on trinary-labeled
edges. The transfer decomposes into two commuting operators T̃_+ and
T̃_- (corresponding to the right and left spectral lines of the
puzzle triangle), whose commutativity follows from the Yang-Baxter
equation for the free-fermion vertex model. Each valid path through
the transfer matrix is a puzzle witness. The key structural fact
encoded here is that upward triangles (Δ) are deterministic — given
two of their three edge labels, the third is forced — while downward
triangles (∇) may branch, with up to two valid completions. All
puzzle multiplicity comes from this ∇ branching. The main entry point
is `lr_puzzles(λ, μ, ν)`, which returns a list of Puzzle objects.
Example: `lr_puzzles((2,1), (2,1), (3,2,1))` returns 2 puzzles,
confirming c^{(3,2,1)}_{(2,1),(2,1)} = 2.

## solve_puzzle.py

An independent puzzle solver using the same 3-label edge formulation
(labels 0, 1, 10 where 10 denotes a rhombus). This script approaches
the problem from the tiling perspective rather than the transfer
matrix perspective: it builds the puzzle triangle row by row, tracking
all valid edge assignments at each level. Boundary edges (bottom,
left, right) are determined by the partitions λ, μ, ν via the
standard binary encoding. Internal edges are assigned by exhaustive
enumeration subject to the Δ and ∇ tile rules. The solver also
generates TikZ code for visualising individual puzzles. The main
entry point is `solve(λ, μ, ν)`.

## transfer_operators.py

Implements the transfer matrix operators from Zinn-Justin's 2008
paper "Littlewood-Richardson coefficients and integrable tilings"
(arXiv:0809.2392). Partitions are represented as binary strings in
a fermionic Fock space: the NE boundary of a Young diagram is traced
from (0,0) to (m,k), with 1 for vertical steps and 0 for horizontal
steps. The operators T_free(u) and T̄_free(u) act on these states by
removing horizontal and vertical strips respectively, with each
removed cell contributing a factor of u. The Schur function identity
s_{λ/μ}(u₁,...,uₙ) = ⟨μ|∏T_free(uᵢ)|λ⟩ connects these operators
to symmetric function theory. The coproduct formula
s_λ(u/v) = Σ c^λ_{μ,ν} s_ν(u) s_{μᵀ}(v) recovers
Littlewood-Richardson coefficients from the operator algebra. This
script provides the algebraic backbone that lr_coefficients.py
builds on.

## mosaic.py

Partially implements Purbhoo's mosaic representation from "Puzzles,
Tableaux, and Mosaics" (arXiv:0705.1184). A mosaic is a tiling of
the puzzle triangle by unit triangles and rhombi, where edges labeled
10 are the shared edges of rhombus tiles. The script can convert
puzzles to mosaics, classify rhombus edges by orientation (horizontal,
slash, backslash), and validate mosaic structure. However, the
migration algorithm — which should move colored rhombi through the
mosaic via local hexagonal flips to produce the LR tableau — is
**not working**. The flip detection finds zero available flips for
both puzzles in the minimal nontrivial example, and the flip graph
reports "Puzzle 2 NOT reachable" from Puzzle 1. The bijection
puzzle → mosaic → migration → LR tableau is therefore **not
implemented** in this codebase. Completing this implementation is
itself an open problem that the agents could work on.
