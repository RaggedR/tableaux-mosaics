# Initial Analysis: Purbhoo's Mosaic Migration for KTW Puzzles

## Problem Understanding

I need to provide implementation details for a bijection that transforms KTW (Knutson-Tao-Woodward) puzzles into Littlewood-Richardson tableaux via Purbhoo's mosaic migration algorithm. The test case involves computing $c^{(3,2,1)}_{(2,1),(2,1)} = 2$, meaning there are two distinct KTW puzzles that should map to two distinct LR tableaux.

## Three-Phase Algorithm Structure

### Phase 1: Puzzle → Mosaic Conversion
- **Input**: KTW puzzle (triangular tiling with labeled edges)
- **Output**: Mosaic (hexagonal tiling with triangles, squares, rhombi in designated "nests")
- **Key insight**: The paper describes this as "removing rhombi, flexing squares to rhombi, pulling corners tight"

### Phase 2: Migration Algorithm
- **Core operation**: Local hexagonal flips that move rhombi through the mosaic
- **Direction**: Moves "flocks" (collections of labeled rhombi) from one nest to another
- **Preservation**: Maintains the combinatorial structure needed for LR tableaux

### Phase 3: Mosaic → LR Tableau Reading
- **Input**: Migrated mosaic with rhombi in target nest
- **Output**: Standard LR tableau with proper shape and content

## Critical Implementation Questions

1. **Hexagon geometry**: How exactly are the "nests" positioned and oriented?
2. **Local rules**: What are the precise hexagonal flip operations?
3. **Migration order**: In what sequence should rhombi be moved?
4. **Termination**: How do we know when migration is complete?

## Data Structure Needs

- Coordinate system for hexagonal tiling
- Representation of oriented rhombi with labels
- Tracking of "flocks" and their standard order
- Hexagonal neighborhood operations

## Gaps to Address

The paper is quite abstract about the geometric details. I need to extract:
- Explicit coordinate representations
- Step-by-step local flip rules
- Clear termination conditions
- Concrete worked examples beyond the figures

This is a complex geometric algorithm that requires careful attention to orientation, ordering, and local transformation rules.