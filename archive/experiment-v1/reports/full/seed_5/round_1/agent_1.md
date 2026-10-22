# Analysis: KTW Puzzle Transfer Matrix as Growth Diagram

## CHALLENGE 1: The Transfer Matrix Construction is Fundamentally Different

The premise assumes a "row transfer matrix" exists for KTW puzzles, but this mischaracterizes how puzzles work. Unlike RSK where we have a clear row-by-row insertion process, KTW puzzles are **global constraint satisfaction problems** on triangular grids. The "free nabla choices" mentioned aren't sequential decisions—they're simultaneous assignments subject to vertex constraints.

The analogy to growth diagrams breaks down because:
- Growth diagrams encode **local rules** between adjacent grid positions
- KTW puzzles have **non-local constraints** (boundary conditions, rhombi matching)
- There's no natural "time evolution" direction in a triangular lattice

## CHALLENGE 2: Face Labels Don't Naturally Emerge

In Fomin growth diagrams, face labels arise from **cancellation-free rules** where each local configuration uniquely determines vertex weights. But KTW puzzle vertices have rigid constraints:
- Each vertex must have exactly one of 12 local puzzle pieces
- The choice depends on **all three adjacent rhombi**
- This creates a constraint propagation system, not a local growth rule

The c^(3,2,1)_{(2,1),(2,1)} = 2 example is telling: two puzzles with "12 free nabla choices" suggests 2^12 = 4096 potential configurations collapsing to just 2 valid puzzles. This massive constraint satisfaction doesn't resemble the gentle local updates of growth diagrams.

## ALTERNATIVE FRAMING: Cylindric Growth Diagram Perspective

Instead of forcing KTW into the growth diagram framework, consider **why Purbhoo's bijection works**:

The mosaic construction creates a **rectification process** similar to jeu de taquin. The key insight is that mosaics have:
1. **Regional decomposition** (colored rhombi in hexagonal regions)
2. **Migration dynamics** (local hexagonal flips)
3. **Canonical forms** (standard LR tableaux)

This suggests the correct framework is **rectification diagrams**, not growth diagrams.

## DEEPER QUESTION: What Growth Diagrams Actually Capture

Growth diagrams work for RSK because:
- Insertion is **greedy** (each new element finds its position independently)
- Recording tableau entries are **local labels** on insertion paths
- The bijection preserves **both combinatorial and algebraic structure**

KTW puzzles encode Littlewood-Richardson coefficients through **geometric intersection theory**, not combinatorial insertion. The "direct bijection" sought may be category-theoretically impossible because puzzles and tableaux live in fundamentally different combinatorial universes.

## PROPOSED RESOLUTION

Rather than seeking a growth diagram for KTW puzzles, investigate whether the **dual construction** works: Can LR tableaux be given a "puzzle-like" local rule structure? This would reverse the direction but might yield the desired directness while respecting the natural geometry of both objects.

The cylindric growth diagram machinery might apply to a **hybrid construction** where mosaics themselves form the vertices of a growth diagram, with migration moves as edge labels.