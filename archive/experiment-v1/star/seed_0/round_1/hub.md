Looking at this problem, I need to understand and explain how to implement Purbhoo's mosaic migration bijection that converts KTW puzzles to Littlewood-Richardson tableaux. Let me break down what I understand and identify the key challenges.

## Core Problem Structure

The bijection has three main phases:
1. **Puzzle → Mosaic conversion**: Transform a triangular puzzle tiling into a hexagonal mosaic
2. **Migration algorithm**: Move colored rhombi through the mosaic using local hexagonal flips
3. **Mosaic → Tableau extraction**: Read off the LR tableau from the final configuration

## Key Concepts from the Reference Material

### Puzzles (Input)
- Triangular tilings with unit pieces (triangles and rhombi)
- Edges labeled 0 or 1, must match where pieces meet
- Boundary data: three binary strings (π, ρ, σ) read clockwise from corners
- For our test case c^(3,2,1)_{(2,1),(2,1)}, we expect puzzles of size n with specific boundary conditions

### Mosaics (Intermediate)
- Tiling of a specific hexagon (not equilateral triangle!) with:
  - Equilateral triangles (unit side)
  - Squares (unit side)  
  - Rhombi (unit side, 30°/150° angles)
- Has three "nests" at alternating corners where rhombi pack
- Boundary data: collections of rhombi (α, β, γ) at the three nests

### Migration
- Takes an "accessible flock" (ordered collection of rhombi with labels)
- Moves rhombi through hexagonal flips in a specific order
- Preserves the standard order and tableau properties
- Direction determined by orientation vectors (E, N)

### LR Tableaux (Output)
- Filling of a skew shape with positive integers
- Must satisfy: weakly increasing rows (west to east), strictly increasing columns (south to north), reverse reading word condition
- Has boundary data (ν, μ, λ^v) corresponding to content and shape

## Critical Implementation Challenges

1. **Coordinate Systems**: Need to handle multiple geometric representations:
   - Puzzle triangular grid
   - Mosaic hexagonal layout
   - Tableau row/column structure

2. **The Puzzle→Mosaic Conversion**: The paper describes this physically as "pulling corners outward" but I need the precise algorithmic steps

3. **Migration Details**: 
   - How to identify "accessible" flocks
   - The exact flip rules for hexagonal rotations
   - How to track orientations through the process

4. **Data Structure Design**: Must support:
   - Efficient local updates (hexagonal flips)
   - Tracking rhombus positions and labels
   - Maintaining ordering invariants

For the test case, I need to verify that two distinct puzzles produce two distinct tableaux, confirming the bijection works correctly.

## Next Steps
I need to fill in the algorithmic details for each phase, particularly:
- The exact geometric transformation from puzzle to mosaic
- The complete migration algorithm with ordering rules
- The tableau extraction procedure