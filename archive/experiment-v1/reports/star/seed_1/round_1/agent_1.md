# Challenging the Growth Diagram Paradigm for KTW Puzzles

## Fundamental Mismatch: Triangular vs. Rectangular Geometries

The core issue is **more severe than suggested**. Classical Fomin growth diagrams require a rectangular lattice with well-defined NW-SE vs. NE-SW orientations. KTW puzzles live in **triangular regions** with three boundary orientations. The "row transfer matrix" construction implicitly forces a rectangular embedding, but this is **geometrically violent**.

**Critical Gap**: The generalist assumes rows can be naturally defined, but KTW puzzles have **hexagonal local rules** that don't respect any natural row structure. Unlike RSK, where growth proceeds left-to-right with clear insertion paths, puzzle completion involves **simultaneous constraints** across all three boundaries.

## Face Labels Cannot Encode Recording Data Here

In RSK-type growth diagrams, face labels work because:
- Each local move has a **unique inverse**
- The recording tableau captures the **history** of insertions
- Face labels are **functorial** with respect to the growth process

But KTW puzzles fail this paradigm:

**Problem 1**: Puzzle pieces have **rotational symmetry** - a rhombus can be flipped in multiple ways while preserving edge constraints. Face labels cannot distinguish these **isotopic but combinatorially distinct** solutions.

**Problem 2**: The nabla choices aren't **sequential decisions** - they're simultaneous satisfactions of a global constraint system. There's no natural "time ordering" for face labels to record.

## The Migration Algorithm Encodes Essential Topology

Purbhoo's indirection isn't computational convenience - it's **topologically necessary**. The migration algorithm preserves **winding numbers** around singular points in the mosaic. These invariants are **invisible** at the puzzle level but crucial for the LR tableau structure.

**Specific Challenge**: In your minimal example c^(3,2,1)_{(2,1),(2,1)} = 2, the two puzzles likely differ by a **non-local transformation** - moving rhombi across multiple hexagons. A row-based growth diagram cannot capture such global moves because it enforces **locality** of updates.

## Alternative Framework: Cylindric Growth Fails

The generalist suggests cylindric growth diagrams might apply, but this misunderstands the geometry. Cylindric constructions handle **periodic boundary conditions**, not the **fixed boundary** conditions of KTW puzzles. The three boundary segments (with prescribed λ, μ, ν) create **topological obstructions** that prevent cylindric closure.

**Moreover**: Even if we could cylindrically embed, the resulting growth wouldn't respect the **Grassmannian geometry** that gives puzzles their meaning. The Schubert class intersection structure would be lost.

## Deeper Structural Objection

The entire growth diagram approach assumes **incremental construction** is possible. But KTW puzzles encode **triple intersections** in Grassmannians - these are **global topological invariants** that resist decomposition into local moves.

**Analogy**: It's like trying to compute the genus of a surface by examining local patches. The genus is global; similarly, Littlewood-Richardson coefficients are **global intersection multiplicities** that cannot be reduced to face-label arithmetic.

## Proposed Counter-Investigation

Instead of seeking a direct growth diagram, investigate:

1. **Why does Purbhoo's construction work?** What topological invariant does the migration preserve that makes the bijection possible?

2. **Can the row transfer matrix encode winding data?** If face labels could somehow capture **non-local** topological information, might a modified growth diagram work?

3. **Are there puzzle variants with natural growth structure?** Perhaps puzzles in **cylindric geometries** or with **different boundary conditions** admit growth diagram descriptions.

The current framing fundamentally misunderstands both the **geometric constraints** of KTW puzzles and the **topological content** of the Purbhoo bijection. A successful approach requires rethinking the basic geometric setup, not just the combinatorial encoding.