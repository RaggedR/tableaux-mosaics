# Synthetic Analysis: The Growth Diagram Conjecture Under Mathematical Scrutiny

## MATHEMATICAL COHERENCE VERSUS COMPUTATIONAL FANTASY

The most striking tension emerges between rigorous mathematical analysis and computational wishful thinking. The computational specialist provides concrete numbers—2 puzzles, 12 nabla choices, 3 tableau entries—but then leaps to claims about "decidable computational tests" without acknowledging that these same numbers reveal **fundamental incompatibilities** that make direct growth diagrams impossible.

This is not mere implementation difficulty. When 12 binary choices must project to 3 ternary values while preserving Yang-Baxter structure, we're asking for a **12→3 dimensional reduction** that maintains non-commutative algebraic relations. The computational evidence doesn't support the existence of such a reduction—it demonstrates its impossibility.

## THE LOCALITY CONFUSION: THREE INCOMPATIBLE DEFINITIONS

All four specialists invoke "locality" but mean entirely different things:

- **Fomin specialist**: Algebraic consistency conditions checkable with adjacent face labels
- **Vertex model specialist**: Parameter-dependent weights satisfying local Yang-Baxter relations  
- **Tableaux specialist**: Geometric operations with finite propagation distance
- **Computational specialist**: Bounded neighborhood effects in constraint satisfaction

These are **mathematically distinct concepts**. The synthesis attempts to unify them under "bounded locality," but this conflation obscures rather than clarifies. The real question is: which notion of locality is relevant for growth diagram existence?

**Critical gap**: None of the specialists address how these different locality concepts relate to each other. This is not philosophical—it's a concrete mathematical question about which algebraic structures can be realized geometrically.

## THE YANG-BAXTER STRAWMAN: INTEGRABILITY AS RED HERRING

The vertex model specialist's emphasis on Yang-Baxter integrability introduces a sophisticated distraction. While Yang-Baxter equations are mathematically beautiful, they're **not necessary** for growth diagram construction. Many successful growth diagrams (including basic RSK) work without underlying integrable structure.

The real constraint is simpler and more fundamental: **local face labeling consistency**. This requires that when you construct tableaux by different paths through the growth diagram, you get the same result. Yang-Baxter is sufficient for this, but not necessary.

**Unifying insight**: The question isn't whether KTW puzzles have integrable structure, but whether they have **any** consistent local decomposition. The computational evidence suggests they don't—not because of Yang-Baxter failure, but because of more basic combinatorial incompatibilities.

## THE TRIANGULAR LATTICE MISDIRECTION: GEOMETRY VERSUS ALGEBRA

Both the Fomin and computational specialists dismiss triangular lattice approaches, but for different reasons that reveal a deeper mathematical tension:

- **Fomin view**: Triangular puzzles should have hexagonal growth diagrams (dual lattice), requiring six-way rules that don't exist
- **Computational view**: Triangular implementations fail because of cascading dependencies

But this misses the **algebraic core**: tableaux are fundamentally rectangular objects with row/column constraints. Any bijection must ultimately encode this rectangular structure, regardless of intermediate geometric representation.

**The real obstruction**: It's not about lattice geometry—it's about whether rectangular tableau constraints can be **locally encoded** at all. The triangular versus rectangular debate is a geometric red herring obscuring this deeper algebraic question.

## THE MIGRATION ALGORITHM AS EXISTENCE PROOF

The tableaux specialist correctly identifies that migration works through **coordinated global transformation**, not local operations. This is actually the most important insight for understanding why direct growth diagrams fail.

Migration succeeds precisely because it **abandons** local decomposition in favor of global coherence. Each hexagonal flip is determined by global tiling constraints, not local choice data. This is why the puzzle→mosaic→migration→tableau route works—it respects the **inherently global** nature of the combinatorial relationships.

**Critical implication**: The success of migration is not evidence that growth diagrams should exist—it's evidence that they **cannot** exist. Migration works by doing exactly what growth diagrams cannot do: making globally coordinated choices.

## THE FUNDAMENTAL CATEGORY ERROR

The deepest problem with the growth diagram conjecture is a **category error** about what objects are being related:

- **KTW puzzles**: Encode multiplicative structure (Grassmannian intersections)
- **LR tableaux**: Encode additive structure (skew tableau fillings)
- **Growth diagrams**: Construct additive objects through local add