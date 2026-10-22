# Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Problem Overview
I need to specify a concrete algorithm for implementing Purbhoo's bijection that converts KTW puzzles to Littlewood-Richardson (LR) tableaux via mosaic migration. The test case involves computing c^(3,2,1)_{(2,1),(2,1)} = 2, meaning there are exactly 2 puzzles that should map to 2 distinct LR tableaux.

## Key Components to Implement

### 1. Puzzle to Mosaic Conversion
- **Input**: KTW puzzle (triangular grid with 0/1 labeled edges)
- **Output**: Mosaic (hexagonal region tiled by unit triangles, squares, and rhombi)
- **Critical insight**: The paper states this is "straightforward" - remove rhombi from corners, flex squares to become rhombi, and straighten the boundary

### 2. Migration Algorithm
- **Core operation**: Move rhombi through local hexagonal transformations
- **Key constraint**: Must preserve the "standard order" of rhombi based on tableau entries
- **Two transformation types** (from paper):
  - 2-fold rotational symmetry hexagons → 180° rotation
  - 3-fold rotational symmetry hexagons → 120° rotation (with orientation constraint)

### 3. LR Tableau Extraction
- **Input**: Final mosaic configuration after migration
- **Output**: LR tableau with correct shape and entries
- **Requirements**: Must satisfy LR conditions (weakly increasing rows, strictly increasing columns, ballot sequence property)

## Critical Implementation Challenges

### Data Structures Needed
1. **Mosaic representation**: Need to track triangles, squares, and rhombi positions
2. **Rhombi orientation**: Track which "nest" (corner region) each rhombus belongs to
3. **Tableau entries**: Map rhombi to tableau values while preserving standard order
4. **Hexagonal neighborhoods**: Identify minimal hexagons for local transformations

### Algorithm Flow Issues
1. **Standard order preservation**: The paper emphasizes migration must preserve the "standard order" of rhombi, but doesn't give explicit rules for computing this order
2. **Hexagon identification**: Need concrete rules for finding "minimal hexagons" containing each rhombus
3. **Termination condition**: When does migration stop? When all rhombi reach their target nest?

## Missing Concrete Details
The paper is quite abstract. I need to fill critical gaps:

1. **Explicit puzzle-to-mosaic transformation rules**
2. **Concrete hexagon pattern matching for the two transformation types**
3. **Standard order computation algorithm**
4. **Step-by-step migration procedure**
5. **Final tableau reading algorithm**

## Test Case Strategy
For c^(3,2,1)_{(2,1),(2,1)} = 2:
- Generate the 2 distinct KTW puzzles with this boundary data
- Apply the full bijection to each
- Verify we get 2 distinct LR tableaux
- Check that the LR tableaux have the correct shape and satisfy all LR conditions

The coding agent will need concrete algorithms with explicit steps, not the high-level descriptions in the paper. My report must bridge this gap with implementable procedures.