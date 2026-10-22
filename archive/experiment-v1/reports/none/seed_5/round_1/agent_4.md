# Initial Analysis: Growth Diagram Conjecture for KTW Puzzles

## Challenging the Problem Framing

The stated conjecture assumes a "direct" bijection via growth diagrams is inherently superior to Purbhoo's mosaic construction, but this framing obscures several computational realities:

1. **What constitutes "directness"?** The puzzle→mosaic→LR tableau path involves well-defined local operations. A growth diagram approach may require equally complex bookkeeping across face labels.

2. **The minimal example reveals hidden complexity**: For c^(3,2,1)_{(2,1),(2,1)} = 2, we have 2 puzzles but 3×3×2 = 18 total tableau entries across both tableaux. The "12 free nabla choices" suggests significant degeneracy in the puzzle→tableau mapping that any direct construction must handle.

## Computational Experiments to Test the Conjecture

### Experiment 1: Transfer Matrix Spectral Analysis
Use `transfer_operators.py` to compute eigenvalues of row transfer matrices for small cases. If growth diagrams exist, the transfer matrix should exhibit specific spectral properties related to the LR coefficient multiplicity.

**Hypothesis**: The transfer matrix for c^(λ)_{μν} should have rank equal to c^(λ)_{μν}, with eigenspaces corresponding to distinct LR tableaux.

### Experiment 2: Face Label Encoding Verification
For the (3,2,1)/(2,1)×(2,1) example:
- Enumerate both puzzles using `lr_coefficients.py`
- Solve row-by-row using `solve_puzzle.py` 
- Track whether intermediate row solutions can uniquely encode partial LR tableau data

**Critical test**: Can face labels at row k unambiguously determine the first k rows of the corresponding LR tableau?

### Experiment 3: Migration Algorithm Reversal
Since `mosaic.py` migration is broken, implement the reverse: start from known LR tableaux and attempt to construct growth diagram faces directly.

**Key insight**: If the conjecture holds, this reverse construction should naturally yield puzzle edge labels.

## Alternative Computational Framework

The problem may be approaching this backwards. Instead of seeking a direct puzzle→LR tableau bijection, consider:

1. **Puzzle multiplication structure**: The transfer matrices naturally encode the associative algebra structure. Growth diagrams might emerge from studying how this algebra acts on the space of boundary conditions.

2. **Fock space perspective**: The `transfer_operators.py` suggests a representation-theoretic viewpoint where puzzles are matrix elements of operators in Fock space. Growth diagrams could correspond to operator decompositions.

3. **Local vs. global coherence**: Purbhoo's migration succeeds because it maintains local hexagonal symmetries. A growth diagram approach must preserve analogous local constraints while building global tableau structure.

## Computational Gaps to Address

1. **Scaling behavior**: Test whether the conjectured direct bijection maintains computational tractability as partition sizes grow.

2. **Uniqueness verification**: For cases with c^(λ)_{μν} > 1, verify that proposed growth diagram faces actually distinguish between different LR tableaux.

3. **Boundary condition sensitivity**: Examine how small changes in puzzle boundary labels affect proposed face label sequences.

## Verdict on the Conjecture

The conjecture is **computationally interesting but likely false** in its strong form. The indirect nature of Purbhoo's bijection may be necessary rather than incidental. However, a weaker version might hold: growth diagrams could provide an efficient algorithm for computing LR coefficients without requiring face labels to directly encode individual tableaux.

The real computational question is not whether such a direct bijection exists, but whether it would be more efficient than existing methods for practical calculations.