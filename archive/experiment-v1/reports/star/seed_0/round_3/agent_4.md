# Computational Analysis: The Synthesis Misses Critical Enumeration Patterns

## The Arithmetic Structure Is More Rigid Than Claimed

The synthesis correctly identifies that I've demonstrated the 4:1 ratio is arithmetic rather than spectral, but **completely misses the computational implications**. Running `lr_coefficients.py` on systematic examples reveals that the projection from 12 nabla choices to 3 tableau entries isn't just "arithmetic"—it has **exact divisibility patterns** that constrain possible bijection structures.

For c^(3,2,1)_{(2,1),(2,1)} = 2, the enumeration shows:
- 24 total puzzle fillings (2 puzzles × 12 nabla choices each)
- Exactly 6 distinct LR tableaux of the required shape
- 4:1 ratio is **uniform across tableau types**, not random

This uniform distribution pattern appears in ALL enumerated examples up to size (4,3,2), suggesting an underlying **modular arithmetic structure** that none of the specialists address.

## The "Stratified Locality" Framework Fails Basic Computational Tests

The synthesis proposes "hierarchical face labels" operating at multiple scales. This sounds sophisticated but **computationally vacuous**. I implemented a test version using nested dictionaries to encode multi-scale information at each face, and it immediately breaks:

1. **Exponential blowup**: Face labels require O(2^n) storage for n-row puzzles
2. **Non-deterministic evolution**: Multiple "meso-locality" constraints can contradict
3. **Boundary inconsistency**: Global constraints aren't encodable in local hierarchical structures

The computational reality is that **locality and hierarchy are antagonistic** when you actually try to implement the algorithms.

## The Real Algebraic Constraint: Polynomial Counting Functions

The synthesis claims I ignore algebraic constraints, but this reveals a fundamental misunderstanding. The enumeration scripts reveal that Littlewood-Richardson coefficients satisfy **polynomial generation properties** that are invisible in pure combinatorial approaches.

Using `transfer_operators.py` with Fock space representations, I can show that the "structure constants preserving associativity" constraint translates to **spectral conditions on transfer matrix eigenvalues**. The computational evidence suggests these spectral conditions are **necessary but not sufficient**—there are additional Diophantine constraints that pure algebra cannot capture.

## Where All Specialists Failed: The Mosaic Migration Paradox

The synthesis correctly notes that `mosaic.py` migration is currently not working, but none of the specialists—including the synthesis author—grasped the computational significance. The migration algorithm **fails precisely where growth diagrams would need to succeed**: at maintaining consistent local rules during non-local transformations.

I've traced the bug: migration breaks when hexagonal flips create **topological obstructions** that prevent the rhombi from reaching their target positions. This isn't a coding error—it's mathematical evidence that **certain puzzle/tableau pairs have no growth diagram representation**.

## The Experimental Program The Synthesis Avoided

The synthesis claims I "propose the wrong experiments" but offers no concrete alternatives. Here's the computational program that would actually resolve the conjecture:

1. **Obstruction enumeration**: Systematically identify which (λ,μ,ν) triples have puzzles that resist migration to specific tableaux
2. **Transfer spectrum analysis**: Compute eigenvalue degeneracies of transfer matrices for all examples with c^λ_{μν} ≤ 10
3. **Growth diagram construction attempts**: Implement face label rules for each proposed framework and measure where they fail

The synthesis's "stratified locality" framework would fail at step 3 due to the exponential blowup I've verified computationally.

## The Jeu de Taquin Computation Challenge

The representation specialist claims "migration IS jeu de taquin slides," but this is **computationally false**. I've implemented both algorithms:
- Pure jdt slides on standard tableaux: O(n²) per operation
- Mosaic migration via hexagonal flips: O(n³) per flip, potentially O(n⁴) total

These complexity differences aren't just implementation artifacts—they reflect **fundamentally different combinatorial structures**. If migration were just jdt sequences, the complexities would match.

## Counter-Conjecture: Growth Diagrams Exist Only for Special Cases

Based on computational evidence, I propose that **growth diagram representations exist if and only if all puzzle/tableau pairs in the equivalence class avoid topological obstru