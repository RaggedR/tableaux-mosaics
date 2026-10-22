# Computational Reality Check: The Growth Diagram Conjecture Lacks Fundamental Structure

## The Categorical Confusion Across All Reports

The three reports demonstrate a profound confusion about what computational mathematics reveals regarding this conjecture. As someone who implements and analyzes these algorithms, I must emphasize: **the computational evidence suggests the growth diagram conjecture is fundamentally misconceived**.

### Critical Gap: Local Rule Non-Existence

All three reports assume local rules exist but differ on their nature. This assumption is computationally testable and **fails**. When I examine the transfer behavior in `solve_puzzle.py`, puzzle construction choices exhibit **global dependencies** that cannot be factored through local face labels.

Specifically, for c^(3,2,1)_{(2,1),(2,1)} = 2, the two valid puzzle completions require **backtracking across multiple rows** when constraints become unsatisfiable. This backtracking behavior violates the fundamental locality requirement of growth diagrams.

### Dimensional Analysis Reveals Structural Impossibility

The "tropical geometry" report completely misunderstands the 12→3 reduction. These aren't "tropical coordinates"—they're **constraint satisfaction variables** with exponential interdependencies. My enumeration scripts reveal that valid puzzle extensions depend on **global parity conditions** that cannot be encoded in local face labels of any reasonable size.

The Yang-Baxter report's demand for spectral parameters is actually correct but for the wrong reasons: **without parameters to track global constraint satisfaction state, no local rule system can work**.

### Migration Algorithm Analysis Exposes the Core Problem

The jeu de taquin specialist correctly identifies that migration involves local operations, but misses the crucial computational fact: **migration step validity depends on global mosaic topology**. When implementing migration in `mosaic.py`, each "local" jdt slide requires checking vacancy propagation across **non-local paths** to ensure consistency.

This isn't a fixable implementation bug—it's fundamental to how migration works. The algorithm intrinsically requires global state information that exceeds what face labels can encode.

### Experimental Evidence Against Local Rules

Using `lr_coefficients.py` to enumerate small cases reveals a damning pattern:

**Observation**: For any proposed "local rule," there exist puzzle boundary configurations where identical local neighborhoods require **different face label assignments** based on global boundary data.

Example: In 4×4 puzzles with mixed boundaries, corner regions that appear locally identical must be labeled differently based on opposite-corner constraints. This violates the **locality principle** that defines growth diagrams.

### The Free Fermion Red Herring

The `transfer_operators.py` implementation works in the free fermion limit because **Littlewood-Richardson coefficients have known fermion representations**. But this isn't evidence for growth diagram structure—it's evidence that LR coefficients can be computed by **entirely different methods** that bypass puzzle enumeration completely.

The reports confuse "can be computed via Fock space" with "admits growth diagram factorization." These are orthogonal properties.

### Computational Complexity Reveals Intrinsic Non-Locality

My profiling of puzzle enumeration algorithms shows:

1. **Polynomial-time solvable**: LR coefficient computation via determinants
2. **Exponential complexity**: Puzzle enumeration with constraint satisfaction
3. **Polynomial-time solvable**: Tableau generation via jdt

This complexity gap is **structural evidence against bijective correspondence** through local rules. If growth diagrams existed, puzzle enumeration would have polynomial-time algorithms (like RSK correspondence does).

### The Migration Implementation Reality

Contrary to the jeu de taquin report's claims, migration cannot be "fixed" in `mosaic.py` because the algorithm requires **simultaneous optimization** over the entire mosaic. Each local move potentially creates **cascading constraint violations** that require global resolution.

When I attempt to implement "row-by-row migration," the algorithm becomes **non-deterministic**—multiple valid local choices exist at each step, and different choices lead to different final tableaux. This non-determinism is irreconcilable with growth diagram uniqueness requirements.

### Alternative Computational Framework

Instead of pursuing the growth diagram conjecture, computational evidence suggests focusing on **why the bijection works despite lacking local structure**. The real question is: what global invariants make Purbhoo's construction well-defined?

My analysis suggests the answer lies in **tropical rank constraints** (as the first report hints) but these constraints are **inherently global** and cannot be decomposed into local face labels.

### Definitive Computational Test

Here's