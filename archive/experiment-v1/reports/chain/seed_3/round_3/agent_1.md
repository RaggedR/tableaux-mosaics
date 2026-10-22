# Growth Diagrams vs. Migration: A False Computational Dichotomy

## Fundamental Misframing of the Bijection Problem

The computational colleague frames this as an "efficiency optimization" problem—replacing O(n³) migration with O(n²) face updates—but this **completely misunderstands** what growth diagrams encode. Growth diagrams are not computational shortcuts; they are **structural descriptions of bijective correspondence**.

In Fomin's framework, growth diagrams capture the **local rules that generate global bijections**. The face labels don't "compute" the bijection—they **are** the bijection data encoded geometrically. The colleague's complexity analysis conflates algorithmic implementation with mathematical structure.

## Critical Gap: What Are We Actually Trying to Encode?

The report never addresses what the **face labels should represent**. In classical RSK growth diagrams, face labels record **which element was inserted/deleted** at each step. For puzzle-to-tableau bijections, what plays this role?

Purbhoo's mosaics suggest that **rhombus types and positions** are the elementary data. But KTW puzzle rules operate on **edge orientations and rhombus choices**—a different combinatorial layer. The report's "local face update rules" remain completely unspecified because this fundamental question is unresolved.

## The Transfer Matrix Red Herring  

The colleague's "transfer matrix rank structure" hypothesis reveals deep confusion. Transfer matrices in integrable systems encode **time evolution operators**—they are not combinatorial bijection devices. The eigenvalue analysis proposed would measure **spectral properties of linear operators**, not bijection-counting invariants.

This conflation suggests the colleague has imported intuition from quantum mechanics without understanding that **discrete bijections and continuous evolution are fundamentally different**. Growth diagrams for bijections are **deterministic recursive constructions**, not spectral decompositions.

## Missing the Cylindric Construction Question

The original problem specifically asks whether KTW branching choices form a growth diagram in the **cylindric sense**. The report ignores this entirely. Cylindric growth diagrams (due to Krattenthaler-Müller) handle **periodic boundary conditions** and **wrapping effects**—precisely relevant for puzzle pieces that connect across boundary edges.

Without addressing cylindricity, the entire computational verification strategy is **testing the wrong mathematical object**. The colleague proposes testing planar growth diagram properties when the puzzle geometry is inherently **toroidal**.

## The Migration Algorithm is Not Broken

The report claims "mosaic.py has broken migration functionality" but provides no evidence. Purbhoo's hexagonal flip algorithm is **mathematically well-defined**. If implementation bugs exist, they are coding errors, not conceptual failures.

More critically, the colleague treats migration as a "comparison baseline" when it is actually **the proven bijection method**. The question is whether growth diagrams can **reproduce migration outcomes**, not replace them computationally.

## Information Propagation: The Real Challenge

The colleague mentions "correlation lengths" but misses the deeper issue. In RSK-type growth diagrams, **local insertion rules** have **global consequences** through **path dependencies**. The Littlewood-Richardson tableau structure emerges from **accumulated local decisions**.

For KTW puzzles, the analogous question is whether **nabla choices propagate information consistently** through the puzzle lattice. This is not a computational complexity problem—it is a **structural coherence question** about how local and global constraints interact.

## What Would a Growth Diagram Actually Look Like?

Instead of computational speculation, consider the mathematical requirements:

1. **Vertices**: Partial puzzle configurations up to row k
2. **Edges**: Addition of row k+1 with specific nabla choices  
3. **Face labels**: The specific choices that determine tableau increments
4. **Local rule**: How adjacent face labels determine the next row's tableau contribution

The **real challenge** is defining consistent face labels that encode **which nabla choices correspond to which tableau entries** in each local configuration.

## Testable Specific Conjecture

Rather than algorithmic optimization, here is a **mathematically precise** test:

**Conjecture**: For each nabla choice in a KTW puzzle, there exists a **canonical local rule** that determines its contribution to the corresponding LR tableau **based solely on adjacent row configurations**.

**Test**: Construct explicit local rules for the c^(3,2,1)_{(2,1),(2,1)} = 2 example and verify they reproduce Purbhoo's migration outcomes.

This requires **combinatorial analysis**, not computational complexity theory.