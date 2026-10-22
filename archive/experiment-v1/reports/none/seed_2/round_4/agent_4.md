# Computational Challenge: The Quantum-Classical Chasm

## The Fundamental Category Error I'm Making

I'm still trapped in combinatorial thinking when this is fundamentally about **geometric intersection theory**. The KTW puzzles aren't just counting objects—they're encoding **Schubert calculus** on Grassmannians. Each puzzle piece represents a **local intersection condition**.

**What I Actually Need to Compute**: Not whether there's a bijection, but whether the **intersection multiplicities** can be computed row-by-row using **local cohomological data**.

The growth diagram conjecture is asking: *Can Grassmannian intersection theory be decomposed into local row operations?* This is a question about **sheaf cohomology**, not combinatorics.

## The Spectral Sequence Connection I Missed Entirely

Growth diagrams are essentially **spectral sequences** in disguise! The E₁ page corresponds to individual row data, and convergence to E∞ gives the final LR coefficients.

**Critical Oversight**: The "free nabla choices" aren't arbitrary—they're **cocycle representatives** in some cohomology theory. The constraint that they yield valid tableaux is a **coboundary condition**.

**Experiment I: Cohomological Structure**
Using `transfer_operators.py`:
1. Interpret transfer matrices as **boundary operators** d: Cₖ → Cₖ₊₁
2. Check if d² = 0 (exact complex structure)
3. Compute ker(d)/im(d) for each row
4. Test if H*(complex) ≅ space of LR tableaux

## The Torus Action I Completely Ignored

Grassmannians have natural **torus actions**, and both puzzles and tableaux should respect this symmetry. The growth diagram conjecture might be asking whether these actions are **compatible** under row-by-row construction.

**Missing Computational Angle**: 
- Each puzzle has a **weight** under torus action
- Each LR tableau has a **weight** under the same action
- Growth diagrams should preserve weights **additively**

**Experiment J: Weight Preservation**
For c^(3,2,1)_{(2,1),(2,1)} = 2:
1. Compute torus weights of both puzzles
2. Compute torus weights of both LR tableaux  
3. Check if row-by-row puzzle construction preserves weights
4. Test if this forces the bijection

## The Real Computational Bottleneck: Non-Local Constraints

I keep assuming LR tableau constraints are local, but they're **global**! The tableau condition requires the entire filling to increase along rows/columns simultaneously.

**The Deep Problem**: Puzzle solving is **inherently local** (each nabla choice affects only nearby cells), while tableau validity is **inherently global** (word must be Yamanouchi).

**Experiment K: Locality vs. Globality**
Using `solve_puzzle.py`:
1. Implement "partial tableau validity" row-by-row
2. For each puzzle row, determine which choices are **locally consistent**
3. Propagate constraints to next row
4. Test if global validity emerges from local consistency

**Expected Failure Mode**: Local choices that seem valid become globally inconsistent, requiring **backtracking**—destroying the growth diagram structure.

## The Migration Algorithm as Tropical Geometry

I dismissed Purbhoo's migration as "indirect," but it might be **tropical geometry** in disguise! Migration flips could be **tropical rational functions** transforming between different tropical representations of the same algebraic variety.

**Computational Reframing**: 
- Mosaics are **tropical Grassmannians**
- Migration is **tropical intersection theory**
- LR tableaux are **classical limits** of tropical intersections

**Experiment L: Tropical Structure**
Using `mosaic.py` (fixing the migration issues):
1. Assign **tropical coordinates** to each rhombus
2. Implement migration as **tropical matrix multiplication**
3. Take **classical limit** (temperature → 0)
4. Check if result matches classical LR coefficients

## What I Should Actually Compute: Failure Cases

Instead of looking for confirmations, I should be **hunting for counterexamples**:

**Experiment M: Systematic Contradiction Search**
1. Find smallest case where row-by-row construction **cannot** determine unique LR tableau
2. Identify puzzle configurations with **