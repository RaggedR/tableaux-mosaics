# Computational Analysis: Transfer Matrix vs. Growth Diagram Conjecture

## Core Challenge Assessment

The proposed conjecture attempts to bypass Purbhoo's indirect bijection by establishing a direct growth diagram interpretation of the KTW puzzle transfer matrix. However, this faces **fundamental dimensional mismatches** that require careful computational investigation.

## Critical Gaps in the Formulation

**1. Dimension Mismatch Problem**
The minimal example reveals a structural issue: 2 puzzles with 12 free nabla choices each project to 3 LR tableau entries. This 24→3 compression cannot be "direct" in any meaningful sense without specifying exactly how the growth diagram faces encode this massive information collapse.

**2. Transfer Matrix Construction Ambiguity**
The problem assumes a "row transfer matrix" exists for KTW puzzles, but doesn't specify:
- How puzzle piece constraints translate to matrix entries
- Whether the transfer respects the hexagonal boundary conditions
- How the free nabla degrees of freedom propagate through rows

## Computational Experiments to Test the Conjecture

**Experiment 1: Free Nabla Flow Analysis**
Using `solve_puzzle.py` on c^(3,2,1)_{(2,1),(2,1)}, track how the 12 free nabla choices in each puzzle distribute across rows. If a growth diagram exists, these choices must exhibit structured flow patterns that encode LR tableau data.

**Experiment 2: Face Label Consistency**
Enumerate all valid puzzle completions row-by-row and examine whether face labels between adjacent growth diagram vertices can simultaneously:
- Respect KTW edge constraints
- Generate valid LR tableau entries
- Maintain bijective correspondence

**Experiment 3: Transfer Operator Spectral Analysis**
Use `transfer_operators.py` to compute eigenvalues/eigenvectors of the proposed transfer matrix. Growth diagrams typically exhibit specific spectral signatures - the conjecture is false if these don't emerge.

## Alternative Computational Framework

**Counter-Hypothesis: The Direct Route is Impossible**
The migration algorithm in Purbhoo's construction may be *essential*, not just convenient. The local hexagonal flips could be performing non-local computations that cannot be captured by any growth diagram's local face-labeling rules.

**Test Strategy:** Implement the mosaic representation using `mosaic.py` (fixing the migration issues) and analyze the computational complexity of each flip operation. If flips require global puzzle information, the conjecture fails.

## Specific Computational Predictions

1. **If the conjecture holds:** Transfer matrix eigenvalues should match known LR coefficient generating functions
2. **If it fails:** Free nabla distributions will show non-local correlations incompatible with growth diagram locality

The 24→3 compression ratio in the minimal example strongly suggests the conjecture is false - true growth diagrams preserve more structural information than this compression allows.

## Recommended Computational Path

Start with spectral analysis of the c^(3,2,1)_{(2,1),(2,1)} case using existing scripts, then scale to larger examples. The dimensional mismatch alone may be sufficient to refute the conjecture without deeper investigation.