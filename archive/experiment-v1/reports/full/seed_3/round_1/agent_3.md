# Analysis of KTW Puzzle Growth Diagrams and LR Tableau Bijection

## Critical Gaps in the Problem Formulation

The problem statement contains a fundamental misconception about the nature of Purbhoo's bijection that must be addressed. The claim that the known route is "puzzle → mosaic → migration → LR tableau" oversimplifies the actual construction and misrepresents where the computational complexity lies.

## The Real Structure of Purbhoo's Construction

Purbhoo's bijection is **puzzle ↔ mosaic**, followed by a **migration algorithm** that transforms the mosaic into an LR tableau. The migration is not merely "moving colored rhombi" but a systematic application of jeu de taquin slides in a specific order determined by the mosaic's geometry. This is computationally direct—the complexity lies in understanding how the local hexagonal moves correspond to global jdt behavior.

The problem's framing suggests that "local hexagonal flips" are somehow less direct than "growth diagram face labels," but this misunderstands what makes a bijection computationally tractable.

## Why the Transfer Matrix Approach is Problematic

The proposal to use "row transfer matrix" construction faces several fundamental obstacles:

1. **Puzzle constraints are global**: KTW puzzles must satisfy the "no holes" condition across the entire triangular region. A row-by-row construction cannot easily enforce these global constraints while maintaining bijectivity.

2. **Reading order mismatch**: In Purbhoo's construction, the tableau entries emerge from migration in a specific order that respects both the jdt sliding sequence and the final tableau's reading order. A growth diagram would need to produce entries in row-by-row reading order, which conflicts with the natural emergence order from puzzle geometry.

3. **Face label dimensionality**: The c^(3,2,1)_{(2,1),(2,1)} = 2 example mentions "12 free nabla choices projecting to 3 tableau entries." But growth diagram face labels typically encode single tableau entries or simple local data, not complex global constraint satisfaction.

## A More Promising Direction

Instead of seeking a row-transfer approach, consider this alternative: Can we construct a **reverse migration** that builds puzzles from LR tableaux? This would involve:

- Starting with an LR tableau
- Using reverse jdt to construct a mosaic
- Converting the mosaic to a puzzle

This preserves the natural order relationships that make Purbhoo's bijection work while potentially offering computational advantages.

## Technical Challenge: The Schutzenberger Connection

The problem ignores a crucial aspect: Purbhoo's bijection is intimately connected to Schutzenberger involution properties. The migration algorithm's jdt slides preserve certain symmetries that would be difficult to capture in face labels of a growth diagram. How would the proposed face labeling respect evacuation properties?

## Conclusion

The proposed growth diagram approach faces structural obstacles that the current problem formulation doesn't acknowledge. The "indirectness" of Purbhoo's construction is actually a feature—it respects the natural geometric and combinatorial constraints that make the bijection work. A more promising research direction would explore computational optimizations within Purbhoo's framework rather than seeking an entirely different approach.