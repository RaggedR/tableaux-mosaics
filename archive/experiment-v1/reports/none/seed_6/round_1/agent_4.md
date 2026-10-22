# Initial Analysis: Challenging the Growth Diagram Conjecture

## Core Technical Gaps

The conjecture fundamentally misunderstands the dimensional mismatch between puzzle enumeration and tableau construction. The claim of a "direct bijection" via growth diagram face labels reveals several critical flaws:

**Dimension Problem**: For c^(3,2,1)_{(2,1),(2,1)} = 2, we have 2 puzzles but allegedly "12 free nabla choices projecting to 3 tableau entries." This 12→3 projection suggests a 4:1 redundancy that contradicts bijection claims. A true bijection requires equal cardinalities, not projections.

**Transfer Matrix Misconception**: The row transfer matrix encodes boundary-to-boundary evolution of rhombus configurations. Its eigenspaces correspond to representation multiplicities, not tableau entries. The conjecture conflates spectral properties (eigenvalues) with combinatorial labels (face weights).

## Computational Verification Strategy

Rather than accepting the conjecture, I propose **falsification experiments**:

1. **Enumerate all 2 puzzles** for c^(3,2,1)_{(2,1),(2,1)} using `lr_coefficients.py`
2. **Extract actual nabla degrees of freedom** - count how many rhombi can flip orientations while preserving boundary conditions
3. **Construct transfer matrices row-by-row** using `solve_puzzle.py` 
4. **Test face label interpretation**: Do matrix entries directly encode LR tableau data?

**Expected Failure Mode**: The transfer matrix will have complex eigenstructure unrelated to tableau combinatorics.

## Alternative Framework: Fock Space Perspective

The real insight lies in `transfer_operators.py`. KTW puzzles are better understood as:
- **Bosonic Fock space sectors** where rhombi = particles with crystal graph statistics
- **Transfer matrices = time evolution operators** in discrete quantum mechanics
- **Growth diagrams = classical shadows** of quantum evolution

This suggests the conjecture backwards-engineers a classical bijection from inherently quantum phenomena.

## Critical Test Cases

Beyond the minimal example, examine:
- **Degenerate cases**: When transfer matrix has repeated eigenvalues
- **Large examples**: Does computational complexity scale as expected for "direct" bijection?
- **Boundary variations**: How do different boundary conditions affect the alleged face labeling?

The `mosaic.py` migration algorithm works precisely because it respects the quantum-to-classical correspondence. A "direct" growth diagram approach likely fails because it ignores this deeper structure.

**Prediction**: Computational experiments will show the growth diagram face labels are non-canonical and fail to encode LR tableaux uniquely, refuting the conjecture.