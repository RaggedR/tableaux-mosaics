# Analysis: Challenging the Growth Diagram Conjecture for KTW Puzzles

## FUNDAMENTAL MISDIRECTION: The Transfer Matrix Doesn't Exist

The three reports collectively miss a crucial point: **KTW puzzles don't naturally admit row transfer matrices**. Unlike vertex models on rectangular lattices, KTW puzzles live on **triangular grids** where "rows" don't have uniform length or consistent neighbor relationships. 

The conjecture assumes we can construct a transfer matrix by processing puzzle pieces "row-by-row," but this ignores that:
- Triangular lattice vertices have **varying coordination numbers**
- Boundary effects propagate **diagonally**, not horizontally  
- The constraint satisfaction is **globally coupled**, not decomposable into row operations

The reports discuss eigenanalysis and spectral parameters for a mathematical object that **doesn't exist in the proposed form**.

## DEEPER ISSUE: Jeu de Taquin Structure vs. Growth Diagrams

As a specialist in jdt and migration, I must emphasize that Purbhoo's bijection works precisely because it **respects the natural geometry** of both puzzles and tableaux:

1. **Puzzles** encode rhombi tilings with color constraints
2. **Mosaics** create a rectification target via hexagonal regions  
3. **Migration** uses local moves that preserve LR-tableau combinatorics
4. **Reading order** emerges from the jdt sliding sequence

The migration algorithm is essentially a **sequence of jdt slides** applied to the mosaic's rhombus arrangement. Each slide corresponds to moving a tableau entry to its correct position under the reading order.

**Critical insight**: The reading order of tableau entries corresponds directly to the **temporal sequence** of rhombus migrations, not to spatial "face labels" in some growth diagram.

## CATEGORY ERROR: Growth vs. Rectification

Growth diagrams encode **insertion processes** where new elements are added incrementally. But KTW puzzles are **constraint satisfaction problems** with fixed boundary data. The correct analogy is:

- **RSK insertion**: Add elements sequentially → Growth diagram natural
- **KTW puzzles**: Satisfy global constraints → Rectification process natural  

The bijection puzzle↔tableau doesn't involve "growth"—it involves **rectifying** a constrained tiling into canonical form through jdt-like moves.

## MIGRATION AS THE TRUE BIJECTION MECHANISM

The reports miss that migration **is already the direct bijection**. Here's why:

In migration, each hexagonal flip corresponds to:
1. Moving a rhombus past a color boundary  
2. This generates a **bump** in the evolving tableau
3. The bump propagates via jdt until reaching the correct position
4. The final positions give the LR-tableau entries

The "indirectness" mentioned in the problem statement is illusory. Migration directly encodes the **jdt rectification path** from the mosaic's initial configuration to standard LR form.

## SCHUTZENBERGER INVOLUTION PERSPECTIVE  

Under Schützenberger involution, LR tableaux have a natural **evacuation sequence** that mirrors the temporal order of migration moves. This suggests:

**Conjecture**: The migration sequence for a puzzle's mosaic is the **time-reversed evacuation** of the corresponding LR tableau under Schützenberger involution.

If true, this would explain why migration "works"—it's following the natural combinatorial dynamics of tableau evacuation, just in reverse.

## ALTERNATIVE RESEARCH DIRECTION

Instead of forcing puzzles into growth diagrams, investigate:

1. **Can we characterize which jdt sequences arise from migration?**  
2. **How does the evacuation order relate to puzzle tile positions?**
3. **What invariants are preserved between puzzle constraints and jdt moves?**

The "direct bijection" already exists—it's the migration algorithm viewed as jdt rectification. The real question is understanding **why this particular rectification process preserves all the necessary combinatorial structure**.

## CONCLUSION

The growth diagram conjecture is based on a category error. KTW puzzles and LR tableaux connect via **rectification geometry**, not **insertion dynamics**. The migration bijection is already optimal—the challenge is understanding its **jdt-theoretic foundations**, not replacing it with an incompatible framework.