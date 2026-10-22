# Initial Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Problem Overview
I need to specify how to implement a bijection from KTW (Knutson-Tao-Woodward) puzzles to Littlewood-Richardson tableaux via Purbhoo's "mosaic migration" algorithm. The bijection has three phases:
1. **Puzzle → Mosaic conversion**: Transform the triangular puzzle tiling into a hexagonal mosaic
2. **Migration algorithm**: Move rhombi through local hexagonal flips following specific rules
3. **Mosaic → Tableau extraction**: Read the final LR tableau from the migrated configuration

## Key Technical Components from the Paper

### Mosaic Structure
- **Hexagon**: Vertices A'AB'BC'C with specific angle/length constraints (150° at A,B,C; 90° at A',B',C')
- **Three tile types**: Unit triangles, unit squares, unit rhombi (30°/150° angles)
- **Nests**: Rhombi are "packed" into three corner regions (A, B, C)
- **Boundary data**: Collections of rhombi (α, β, γ) at each nest

### Migration Mechanics
The paper describes migration as moving rhombi through sequences of local rotations in minimal hexagons:
- **Type (a)**: 2-fold symmetry → 180° rotation
- **Type (b)**: 3-fold symmetry → 120° rotation (with orientation constraint)
- **Standard order**: Based on tableau entries and geometric position
- **Wake tracking**: Upper/lower wakes of migrating rhombi must not cross

## Critical Implementation Challenges

### 1. Geometric Representation
The paper uses continuous geometric transformations, but implementation needs discrete data structures. Key questions:
- How to represent the non-orthogonal hexagonal coordinate system?
- How to track rhombi positions and orientations during migration?
- How to identify "minimal hexagons" algorithmically?

### 2. Migration Order and Constraints  
The algorithm processes rhombi in "standard order" but this depends on:
- Current tableau values (which change as rhombi move)
- Geometric positioning in non-orthogonal coordinates
- Wake interference patterns between multiple moving rhombi

### 3. Puzzle-Mosaic Correspondence
The paper states there's a "natural bijection" via a physical deformation process, but doesn't give the explicit algorithmic mapping between:
- Puzzle edge labels (0s and 1s) ↔ Mosaic tile configurations
- Triangular puzzle boundary ↔ Hexagonal mosaic boundary

## Test Case Requirements
For c^(3,2,1)_{(2,1),(2,1)} = 2:
- Input: Two distinct KTW puzzles with boundary data ((2,1), (2,1), (3,2,1))
- Output: Two distinct LR tableaux 
- The bijection must be deterministic and produce different results for different puzzles

## Next Steps Needed
I need to develop concrete algorithms for:
1. **Coordinate systems**: How to represent hexagonal/rhombic tilings discretely
2. **Puzzle parsing**: Extract boundary data from KTW puzzle edge labels
3. **Migration rules**: Precise algorithmic versions of the geometric transformations
4. **Tableau extraction**: Map final rhombi positions to LR tableau entries

The main challenge is translating Purbhoo's continuous geometric descriptions into discrete algorithmic steps suitable for implementation.