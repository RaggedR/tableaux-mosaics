# Initial Analysis: Purbhoo's Mosaic Migration for KTW Puzzles

## Problem Overview
I need to specify how to implement Purbhoo's bijection from KTW puzzles to Littlewood-Richardson tableaux via mosaic migration. The test case involves computing c^(3,2,1)_{(2,1),(2,1)} = 2, meaning there are two puzzles that should map to distinct LR tableaux.

## Key Technical Challenges

### 1. **Puzzle-to-Mosaic Conversion**
From the reference material, this involves:
- Taking a KTW puzzle (equilateral triangle tiled with labeled rhombi)
- Converting to a hexagonal mosaic with triangles, squares, and rhombi
- The conversion involves "removing rhombi, flexing squares to rhombi, and straightening"
- Rhombi get packed into three corner "nests" of the hexagon

**Implementation gap**: The paper describes this geometrically but doesn't give explicit coordinate transformations or algorithmic steps.

### 2. **Migration Algorithm**
The core algorithm moves rhombi through local hexagonal flips:
- Process rhombi in "standard order" (related to tableau entries)
- For each rhombus, find minimal containing hexagon
- Apply 180° rotation (type a) or 120° rotation (type b) based on local pattern
- Continue until rhombus reaches target nest

**Critical issues**:
- How to determine "standard order" from puzzle labels
- Precise rules for identifying hexagon types (a) vs (b)
- Coordinate system for tracking rhombi positions
- How orientation changes propagate

### 3. **Tableau Readoff**
Final step requires:
- Interpreting migrated rhombi configuration as LR tableau
- Handling orientation changes during migration
- Ensuring the result satisfies LR tableau constraints

## Growth Diagram Connection

The migration process has growth diagram characteristics:
- **Local rules**: The hexagonal flip operations are deterministic local transformations
- **Directed structure**: Migration follows compass directions with consistent ordering
- **Face labeling**: Rhombi carry content information (tableau entries) that's preserved

However, this differs from classical Fomin growth diagrams:
- The underlying graph is a hexagonal tiling, not a square grid
- Local rules involve geometric rotations, not combinatorial updates
- The "growth" is spatial migration rather than insertion

**Key insight**: This might form a growth diagram where:
- Vertices = rhombus positions
- Edges = migration steps  
- Face labels = rhombus contents
- Local rules = hexagonal flip transformations

## Critical Implementation Questions

1. **Coordinate system**: How to represent hexagonal mosaic positions?
2. **Standard order**: How to compute this from puzzle boundary data?
3. **Hexagon detection**: Algorithm to identify minimal containing hexagons?
4. **Orientation tracking**: How orientations change during migration?
5. **Termination**: When has a rhombus reached its target nest?

## Next Steps Required

The paper provides theoretical framework but lacks algorithmic details. I need to:
1. Specify concrete data structures for mosaics
2. Detail the conversion algorithm with worked examples
3. Give step-by-step migration procedure
4. Show how to read off LR tableaux from final configurations

The test case with two puzzles mapping to distinct tableaux will be crucial for validation.