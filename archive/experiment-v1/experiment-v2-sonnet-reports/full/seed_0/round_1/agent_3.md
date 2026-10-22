# Initial Analysis: Purbhoo's Mosaic Migration Bijection

## Overview of the Problem

I need to provide implementation details for Purbhoo's bijection that converts KTW puzzles to Littlewood-Richardson tableaux via mosaics and migration. The bijection has three main phases:

1. **Puzzle → Mosaic conversion**: Transform the triangular puzzle tiling into a hexagonal mosaic
2. **Migration algorithm**: Move rhombi through the mosaic using local hexagonal flips
3. **Mosaic → LR tableau extraction**: Read the final tableau from the migrated configuration

## Key Data Structures Needed

### Puzzle Representation
- **Triangular grid**: Equilateral triangle of side length n
- **Tile types**: Three rhombus types with edge labels (0,1,0), (1,0,1), (0,1,1)
- **Boundary data**: Three strings (π, ρ, σ) of 0s and 1s read clockwise from corners

### Mosaic Representation  
- **Hexagonal region**: Hexagon A'AB'BC'C with specific angle/side length constraints
- **Tile types**: 
  - Unit equilateral triangles
  - Unit squares  
  - Unit rhombi (30°/150° angles)
- **Nests**: Three corner regions A, B, C where rhombi are "packed"
- **Boundary data**: Collections of rhombi (α, β, γ) in each nest

### Flock Structure
- **Definition**: A flock F = (ζ, (E,N), f) consists of:
  - ζ: subset of rhombi forming a transformed diagram
  - (E,N): orientation vectors (east/north directions)
  - f: LR-tableau labeling function on the rhombi
- **Standard order**: Ordering on rhombi based on tableau entries and position

## Critical Implementation Challenges

### 1. Puzzle-to-Mosaic Bijection
The paper describes this as a "straightening" operation - pulling corners A', B', C' outward while squares flex into rhombi. I need to understand:
- How exactly the coordinate transformation works
- How edge labels (0s/1s) correspond to rhombus orientations
- The precise geometric relationship between puzzle tiles and mosaic tiles

### 2. Migration Algorithm Core
Migration moves an accessible flock in a chosen compass direction through these steps:
- Find the maximal/minimal rhombus in standard order (depending on direction)
- For each rhombus in sequence, locate the "smallest hexagon" containing it
- Apply 180° rotation (2-fold symmetry) or 120° rotation (3-fold symmetry)
- Continue until rhombus reaches a new nest

**Key questions:**
- What exactly constitutes the "smallest hexagon"?
- How do we determine 2-fold vs 3-fold symmetry cases?
- How does the "standard order" work in practice?

### 3. Flock Construction and Orientation
- How to identify "accessible flocks" in a mosaic
- How orientations (E,N) vectors rotate during migration (at most 60°)
- The relationship between flock content and LR-tableau structure

## Test Case Analysis
For c^(3,2,1)_{(2,1),(2,1)} = 2, I need to:
1. Identify the two distinct KTW puzzles with this boundary data
2. Show how each converts to a different mosaic
3. Demonstrate migration producing two different LR tableaux
4. Verify the tableaux have the correct shape/content

## Next Steps Needed
1. Clarify the exact geometric transformations in puzzle-to-mosaic conversion
2. Detail the hexagonal flip rules in migration
3. Specify how to read LR tableaux from final mosaic configurations
4. Work through the test case step-by-step

The paper provides the theoretical framework, but I need to bridge from the mathematical description to concrete algorithmic steps suitable for implementation.