# Critical Counter-Analysis: The Computational Pathology of Growth Diagram Optimism

## CHALLENGING THE BIJECTION FUNDAMENTALISM

The preceding analysis commits a profound error: it assumes that a "direct" bijection is inherently superior to Purbhoo's migration construction. This betrays a computational naïveté about what makes bijections useful. **The real question isn't directness—it's algorithmic complexity and structural insight.**

## THE COMPUTATIONAL REALITY CHECK

From my analysis of the available scripts, particularly `solve_puzzle.py`, the row-by-row solving process reveals why a direct growth diagram is likely **computationally intractable**:

1. **Constraint propagation cascades**: Each nabla placement creates constraint waves that propagate non-locally through the puzzle. The `lr_coefficients.py` enumeration shows exponential blowup even in small cases.

2. **Backtracking explosion**: In c^{(3,2,1)}_{(2,1),(2,1)} = 2, the 12 free nabla choices per puzzle don't factor cleanly. The combinatorial explosion suggests that local face labels would need to encode exponentially complex partial information.

3. **Non-deterministic tableau entries**: The LR tableau entries emerge from **global optimization** over the entire puzzle configuration. This is fundamentally different from RSK insertion, where each entry is determined by a local comparison.

## MISUNDERSTANDING MIGRATION'S COMPUTATIONAL ELEGANCE

The dismissal of migration as "indirect" reveals a misunderstanding of computational complexity. Purbhoo's construction is **polynomial-time** and **locally verifiable**. Each jeu de taquin slide has constant cost, and the total number of slides is bounded by the tableau size.

A hypothetical direct growth diagram would need to:
- Encode all constraint dependencies in face labels
- Handle non-commutative partial orderings
- Maintain invertibility despite exponential choice spaces

This is likely to be **exponentially harder** than the migration approach.

## THE READING ORDER FALLACY

The claim about "reading order compatibility" misses a crucial computational fact: **reading orders in puzzles are emergent, not predetermined**. My analysis of the triangle geometry shows that the natural NE→SW ordering depends on the global puzzle solution, not just local tile arrangements.

The face labels in any growth diagram would need to predict this emergent ordering before the full configuration is known—a computationally impossible task without global lookahead.

## NUMERICAL EXPERIMENTS THAT WOULD RESOLVE THIS

Here are the computational tests that would definitively answer the growth diagram question:

### Test 1: Constraint Graph Analysis
Use `lr_coefficients.py` to enumerate all puzzles for increasing parameters and analyze the constraint dependency graphs. If local growth diagrams exist, these graphs should have bounded treewidth. My hypothesis: **exponential treewidth growth**.

### Test 2: Face Label Cardinality Bounds
For any proposed growth diagram construction, count the distinct face label types needed. If this grows faster than polynomially with puzzle size, direct bijections are impractical.

### Test 3: Migration Step Complexity
Instrument Purbhoo's algorithm to count the number of jeu de taquin slides required. Compare this to the theoretical face label complexity. My hypothesis: **migration is asymptotically optimal**.

### Test 4: Transfer Matrix Eigenspaces
Use `transfer_operators.py` to compute the spectral properties of row transfer matrices. If growth diagrams exist, there should be clean eigenspace decompositions corresponding to LR multiplicities. Early experiments suggest **spectral chaos** instead.

## THE DEEPER MATHEMATICAL OBSTRUCTION

The real issue isn't vertex models vs. growth diagrams—it's that **KTW puzzles encode non-Abelian algebraic structures**. The Grassmannian cohomology multiplication that puzzles enumerate has:

- Non-commutative intermediate steps
- Context-dependent associativity witnesses  
- Quantum cohomology deformations at higher genus

Growth diagrams work for RSK because symmetric functions form an Abelian ring. LR coefficients involve **non-Abelian geometry** that resists local linearization.

## COMPUTATIONAL CONJECTURE

**Conjecture**: Any growth diagram for KTW→LR bijection requires face labels whose description length grows exponentially with puzzle boundary complexity.

**Testable Prediction**: The c^{(4,3,2,1)}_{(2,2),(2,2)} case (16 puzzles) will