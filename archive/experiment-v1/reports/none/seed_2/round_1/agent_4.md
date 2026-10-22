# Initial Analysis: Growth Diagram Conjecture for KTW Puzzles

## Computational Perspective on the Conjecture

The proposed growth diagram conjecture suggests a direct algebraic pathway from puzzle enumeration to LR tableaux, bypassing Purbhoo's mosaic construction. However, several computational concerns immediately arise that challenge the feasibility of this approach.

## Critical Gaps in the Formulation

**1. Dimension Mismatch Problem**
The conjecture assumes face labels in a growth diagram can "directly encode LR tableau entries," but this faces a fundamental counting issue. For c^(3,2,1)_{(2,1),(2,1)} = 2:
- We have 2 puzzles × 12 free nabla choices = 24 total configurations
- But only 3 LR tableau entries per puzzle
- This 24→6 compression must lose structural information

The transfer matrix operates on puzzle boundary conditions, not internal tableau structure. How can row-by-row operations preserve the skew tableau's content constraints?

**2. Algebraic Structure Concerns**
Growth diagrams typically work because they preserve certain invariants at each step. For LR tableaux, these invariants include:
- Yamanouchi word property for reading sequences
- Strict increase within rows, weak increase within columns
- Proper skew shape filling

The puzzle transfer matrix, however, is designed around rhombus tilings and boundary hexagon constraints. There's no obvious reason why these linear algebraic operations would naturally respect tableau combinatorics.

## Computational Experiments to Test the Conjecture

**Experiment 1: Transfer Matrix Eigenstructure Analysis**
Using `transfer_operators.py`, compute the transfer matrix for the minimal case and examine:
- Are eigenvalues/eigenvectors related to LR tableau generating functions?
- Do matrix powers reveal hidden tableau-counting structure?
- Can we identify a natural basis where face labels become tableau entries?

**Experiment 2: Free Nabla Choice Distribution**
Using `solve_puzzle.py` on the c^(3,2,1)_{(2,1),(2,1)} example:
- Map each of the 24 free choice configurations to specific puzzle solutions
- Check if the 12→3 projection from choices to tableau entries has consistent patterns
- Test whether different puzzles with same LR coefficient share structural properties

**Experiment 3: Boundary-to-Interior Information Flow**
The growth diagram would need to propagate boundary information inward to generate tableau content. Test:
- How much tableau structure is determined by puzzle boundary data?
- Can we reconstruct the entire LR tableau from partial boundary information?
- Is there a natural "completion" algorithm that mimics growth diagram behavior?

## Alternative Framings

**Reframe 1: Dual Approach**
Instead of puzzle→tableau growth diagrams, consider tableau→puzzle growth diagrams. This reversal might be more natural since LR tableaux have inherent growth properties (adding boxes via Yamanouchi words), while puzzles are more rigid tiling objects.

**Reframe 2: Intermediate Structure**
The conjecture might require an intermediate combinatorial object—neither mosaic nor pure transfer matrix, but something that bridges the algebraic and combinatorial structures more naturally.

## Fundamental Challenge

The deeper issue is that **puzzle transfer matrices encode linear algebra over boundary conditions**, while **LR tableaux encode combinatorial constraints on content filling**. A growth diagram connecting these would need to translate between fundamentally different mathematical languages.

The Purbhoo construction works precisely because mosaics provide this translation layer—they maintain enough geometric structure to connect to puzzles while having sufficient combinatorial flexibility to generate tableaux via migration.

## Computational Verdict

Without a clear mechanism for preserving tableau invariants through transfer matrix operations, the direct growth diagram conjecture appears unlikely. The computational experiments above would likely reveal either dimension mismatches or broken combinatorial structure, suggesting that Purbhoo's indirect route may be mathematically necessary rather than merely convenient.

The next computational priority should be Experiment 2—mapping free nabla configurations—to understand whether the required 12→3 compression preserves any meaningful structure.