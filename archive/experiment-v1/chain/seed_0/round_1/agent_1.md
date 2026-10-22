I'll analyze the problem of implementing Purbhoo's mosaic migration bijection for KTW puzzles.

## Initial Analysis

### Core Components

The bijection has three main phases:
1. **Puzzle → Mosaic conversion**: Transform a KTW puzzle (tiling with labeled rhombi) into a mosaic (tiling with unit triangles, squares, and rhombi)
2. **Migration algorithm**: Move rhombi through the mosaic via local hexagon rotations
3. **Mosaic → LR tableau extraction**: Read the final configuration as a Littlewood-Richardson tableau

### Key Concepts from the Reference

From the stripped Purbhoo paper, I can extract:

1. **Mosaics** are tilings of a hexagon with angles 150°, 90°, 150°, 90°, 150°, 90° using:
   - Equilateral triangles (side length 1)
   - Squares (side length 1)
   - Rhombi (side length 1, angles 30° and 150°)

2. **Migration** moves rhombi between three "nests" (corners A, B, C) via hexagon rotations:
   - Each rhombus moves individually in "standard order"
   - Local moves are 180° rotations in 2-fold symmetric hexagons or 120° rotations in 3-fold symmetric hexagons
   - The process preserves the content and tableaux properties

3. **Boundary data** correspondence:
   - Puzzle boundary: three 0/1 strings (π, ρ, σ)
   - Mosaic boundary: three collections of rhombi (α, β, γ) in nests
   - LR tableau: shape λ/μ with content ν

### Critical Gaps to Address

1. **Puzzle → Mosaic conversion details**: The paper mentions a "physical" description involving pulling corners and flexing squares into rhombi, but the precise algorithmic steps are unclear.

2. **Coordinate system**: Need to establish how to represent positions and orientations in the mosaic.

3. **Standard order**: The paper mentions rhombi migrate in "standard order" but doesn't fully define this for the mosaic context.

4. **Flock formation**: Before migration, rhombi must be organized into "flocks" with specific orientations.

### Test Case Analysis

For c^(3,2,1)_{(2,1),(2,1)} = 2:
- This is a Littlewood-Richardson coefficient
- We have two puzzles with this boundary data
- Each should produce a distinct LR tableau of shape (3,2,1)/(2,1) with content (2,1)

### Implementation Strategy

I need to provide:
1. **Data structures** for puzzles, mosaics, and tableaux
2. **Conversion algorithm** from puzzle to mosaic
3. **Migration algorithm** with precise local move rules
4. **Extraction algorithm** from final mosaic to LR tableau

The main challenge is filling in the algorithmic details that Purbhoo's paper leaves implicit, particularly for the puzzle-to-mosaic conversion.