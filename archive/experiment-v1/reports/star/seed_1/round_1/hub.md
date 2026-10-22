# Initial Framing: The Hidden Geometry of Bijective Constructions

## Core Tension: Direct vs. Indirect Bijections

The problem exposes a fundamental tension between **computational convenience** and **structural clarity**. Purbhoo's mosaic construction works by introducing an intermediate object (mosaics) that mediates between puzzles and tableaux through local operations. But this raises a deeper question: **Is this indirection essential, or does it obscure a more fundamental geometric relationship?**

## Critical Gaps in the Framing

**1. What exactly is a "growth diagram" here?** The problem mentions face labels but doesn't specify the growth model. In classical growth diagrams (Fomin, Krattenthaler), we typically have:
- A planar network with vertices labeled by partitions
- Edge weights determining local growth rules  
- Face labels recording the "growth history"

But KTW puzzles live in triangular regions, not rectangular grids. How does the "row transfer matrix" decompose this triangular structure into rows?

**2. The example seems underconstrained.** We have c^(3,2,1)_{(2,1),(2,1)} = 2 with "12 free nabla choices projecting to 3 tableau entries." This suggests some 4-to-1 correspondence, but without seeing the explicit puzzles and tableaux, it's unclear what structure is being preserved or lost.

## Alternative Geometric Perspective

Rather than asking whether a direct bijection exists, consider this reframing: **What geometric invariant is preserved by Purbhoo's migration algorithm that might be lost in a direct construction?**

Mosaics naturally encode **local orientations** through their rhombus colorings. The migration algorithm preserves certain topological properties as it moves these orientations. A direct puzzle→tableau map might need to somehow "remember" this intermediate topological data.

## Algebraic Connection

From a representation theory viewpoint, both puzzles and LR tableaux encode the same tensor product multiplicities, but they emphasize different aspects:
- Puzzles highlight the **geometric intersection theory** (Schubert calculus)  
- LR tableaux highlight the **combinatorial recursion** (bumping algorithms)

The question becomes: **Can the row transfer matrix interpolate between these two perspectives without losing essential information?**

## Proposed Investigation Strategy

Instead of directly seeking the bijection, first examine:
1. What invariants does the migration algorithm preserve that aren't obvious from puzzle/tableau definitions?
2. Can these invariants be computed directly from the row transfer matrix structure?
3. Does the triangular→rectangular transformation introduce artificial degrees of freedom?

This might reveal whether the indirection is a bug (unnecessarily complex) or a feature (capturing hidden geometry).