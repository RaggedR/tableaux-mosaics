# Initial Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Problem Overview
I need to specify a complete implementation of Purbhoo's bijection between KTW puzzles and Littlewood-Richardson tableaux. The bijection has three phases:

1. **Puzzle → Mosaic conversion**: Transform the triangular puzzle into a hexagonal mosaic
2. **Migration algorithm**: Move rhombi through the mosaic via local hexagonal flips
3. **Mosaic → LR tableau extraction**: Read the final tableau from the migrated configuration

## Key Implementation Challenges

### 1. Data Structures
- **Puzzle representation**: Need to store the triangular tiling with labeled edges (0s and 1s)
- **Mosaic representation**: Hexagonal region with triangles, squares, and rhombi
- **Coordinate systems**: Must handle the geometric transformations between puzzle and mosaic coordinates
- **Tableau representation**: Standard Young tableau format with content tracking

### 2. Puzzle-to-Mosaic Conversion
From Purbhoo's description, this involves:
- Removing rhombi from the puzzle
- "Flexing" squares into rhombi via hinge-like transformations
- Straightening the boundary by pulling corners A', B', C' outward
- The 0/1 labels come from clockwise/counterclockwise edge rotations

**Critical gap**: The paper describes this transformation physically but doesn't give the explicit coordinate mapping formulas.

### 3. Migration Algorithm
The core algorithm processes rhombi in "standard order" and performs local hexagonal flips:
- **Type (a)**: 2-fold rotational symmetry → 180° rotation
- **Type (b)**: 3-fold rotational symmetry → 120° rotation (with orientation constraint)

**Critical specifications needed**:
- Precise definition of "standard order" on rhombi
- How to identify the "smallest hexagon" containing a rhombus
- Exact geometric rules for the 120° rotation constraint

### 4. Tableau Extraction
Must convert the final rhombi positions back to standard LR tableau format, including:
- Shape determination (λ/μ)
- Content assignment
- Verification of LR tableau properties

## Test Case Analysis
For c^(3,2,1)_{(2,1),(2,1)} = 2:
- Input: Two distinct KTW puzzles with specified boundary conditions
- Expected output: Two distinct LR tableaux
- This gives us concrete examples to verify the implementation

## Implementation Strategy
I recommend a coordinate-based approach:
1. Use integer lattice coordinates for both puzzle and mosaic
2. Implement explicit transformation matrices between coordinate systems
3. Store tilings as collections of geometric objects with position and type
4. Implement migration as a sequence of coordinate transformations

The biggest challenge is extracting the implicit coordinate transformations and geometric rules from Purbhoo's geometric descriptions.