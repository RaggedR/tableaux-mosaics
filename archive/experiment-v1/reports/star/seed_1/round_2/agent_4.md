# Computational Challenge: The Synthesis Misses the Scaling Catastrophe

The synthesis contains a critical mathematical error that undermines its central "constraint hierarchy" framework. As a computational specialist, I must correct this and propose experiments that actually test the right mathematical objects.

## The Fundamental Scaling Error

The synthesis proposes measuring "constraint distance" - how far a single nabla choice affects other choices. This **completely misses the point**. The issue isn't constraint propagation distance; it's **constraint density explosion**.

In KTW puzzles, constraints aren't linear chains - they form **dense intersection patterns**. For the minimal example c^(3,2,1)_{(2,1),(2,1)} = 2:
- Each puzzle has 12 free nabla choices
- These project to 3 LR tableau entries  
- The projection is 12→3, not a "propagation distance"

The synthesis confuses **spatial extent** with **combinatorial complexity**. Growth diagrams fail because of **exponential degeneracy**, not because constraints travel too far.

## What "Hierarchical Constraint Structure" Actually Means

The synthesis correctly identifies scale-dependent phenomena but mischaracterizes them:

- **Local scale**: Individual rhombus orientations (2 choices each)
- **Global scale**: Boundary compatibility (exponentially constrained)
- **Missing intermediate scale**: **Constraint intersection geometry**

The real mathematical obstruction is that puzzle constraints form **non-planar intersection graphs**. Row-by-row construction requires planar decomposability, which puzzles provably lack.

## The Migration Algorithm Isn't "Jeu de Taquin in Disguise"

This analogy is mathematically incorrect. Jeu de taquin operates on **existing tableaux** through local sliding moves. Migration operates on **colored rhombi** through hexagonal flips in triangular geometry.

The correct analogy: migration is **tropical geometric deformation**. The mosaic represents a tropical curve, and migration deforms it while preserving certain intersection multiplicities. This is why it works - it's using **algebraic geometry**, not combinatorial sliding.

## Critical Experiment: Test the Degeneracy Conjecture

Instead of measuring "constraint distances," test this hypothesis:

**Degeneracy Conjecture**: For puzzle boundary parameters (λ,μ,ν), if the number of free nabla choices exceeds the number of LR tableau entries by a factor > log(puzzle size), then no growth diagram bijection exists.

Computational test:
1. Generate all puzzles for increasing boundary sizes
2. Count free nabla choices vs. final tableau entries
3. Compute the degeneracy ratio
4. Test whether high degeneracy correlates with constraint intersection complexity

This tests whether the obstruction is **information-theoretic** (too much freedom collapsing to too few outcomes) rather than geometric.

## The Spectral Parameter Red Herring

The synthesis elevates the "spectral parameter mystery" to a research direction. This is backwards. The free-fermionic property **guarantees** that puzzles have the right combinatorial structure to encode LR coefficients. Deforming away from integrability would break this connection entirely.

The real question: **Can we deform the puzzle geometry while preserving LR combinatorics?** This isn't about Yang-Baxter equations - it's about whether alternative geometric realizations of the same combinatorial constraints exist.

## Missing Mathematical Framework: Constraint Graph Planarity

The synthesis completely misses the most testable aspect of the growth diagram obstruction. Growth diagrams require that constraint interactions decompose into **planar layers**. 

Computational test:
1. For each puzzle, construct the **constraint intersection graph**: vertices = nabla choices, edges = mutual constraints
2. Test whether this graph admits a **planar drawing** consistent with row-by-row ordering
3. If not, growth diagrams are impossible for that puzzle type

This is a **finite, algorithmic test** that would definitively resolve the conjecture for specific cases.

## The Real Computational Question

The synthesis asks "What makes some bijections direct while others require intermediate constructions?" The computational answer is precise:

**Direct bijections exist when the constraint intersection graph admits efficient decomposition algorithms.**

For puzzles→tableaux:
- Constraint graph is **non-planar** and **highly connected**
- Decomposition requires exponential algorithms
- Migration provides a **different geometric embedding** where constraints become tractable

This isn't about "constraint languages" - it's about **computational complexity classes**.

##