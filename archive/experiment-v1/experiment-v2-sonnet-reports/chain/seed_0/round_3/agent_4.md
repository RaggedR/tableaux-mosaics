## Implementation Report: Purbhoo's Mosaic Migration Algorithm

**ANALYSIS OF PREVIOUS APPROACH**: The Yang-Baxter analysis correctly identifies the core geometric operations but overcomplicates with unnecessary algebraic machinery. I'll provide concrete geometric algorithms and data structures.

## Core Data Structures

```
struct HexCoord {
    int q, r;  // axial coordinates for hexagonal tiling
}

struct Tile {
    TileType type;        // TRIANGLE, SQUARE, RHOMBUS
    HexCoord position;
    int label;           // 0 or 1 for puzzle edges
    Orientation orient;   // one of 6 orientations
}

struct Mosaic {
    vector<Tile> tiles;
    map<HexCoord, Tile*> grid;  // spatial lookup
    vector<Rhombus> nest_A, nest_B, nest_C;  // rhombi in each nest
}
```

## Algorithm 1: Puzzle to Mosaic Conversion

**Key insight**: Purbhoo's bijection works by "unfolding" the equilateral triangle into a hexagon, with rhombi collecting in corner "nests".

```
Mosaic puzzle_to_mosaic(Puzzle puzzle) {
    1. Create hexagonal grid with corners A, B, C
    2. For each puzzle piece at position (i,j):
       - If piece is rhombus with edge labels (a,b,c):
         * Determine target nest based on label pattern
         * Place rhombus in nest with orientation preserving labels
       - If piece is triangle:
         * Place triangle/square in hexagon interior
    3. Return mosaic with rhombi sorted by "standard order" in each nest
}
```

**Standard order**: Within each nest, rhombi are ordered lexicographically by (row, column) in the nest's local coordinate system. This is crucial for migration.

## Algorithm 2: Migration Core Operation

**The minimal hexagon rule**: For a rhombus R, find the smallest hexagon that:
1. Contains R entirely within its interior
2. Has at least one vertex strictly to the "right" of R's leftmost point
3. Is tiled by exactly 7 pieces (1 center + 6 neighbors)

```
bool migrate_rhombus(Mosaic& mosaic, RhombusID rhombus) {
    1. Find minimal hexagon H containing rhombus
    2. Extract 7-tile pattern from H
    3. If pattern matches TYPE_A (2-fold symmetric):
       - Rotate entire pattern 180°
    4. Else if pattern matches TYPE_B (3-fold symmetric):
       - Rotate 120° in direction that makes rhombus edge horizontal/vertical
    5. Place rotated pattern back into hexagon
    6. Update rhombus position
    7. Return true if rhombus moved toward target nest
}
```

**Pattern recognition**: Only two hexagon patterns occur:
- **TYPE_A**: Rhombus surrounded by 6 triangles/squares (2-fold symmetry)
- **TYPE_B**: Rhombus with 2 other rhombi, 4 triangles (3-fold symmetry)

## Algorithm 3: Full Migration Sequence

```
Mosaic migrate_flock(Mosaic mosaic, vector<RhombusID> flock, NestID target) {
    1. Sort flock by standard order (largest first for north/east migration)
    2. For each rhombus R in sorted order:
       a. While R not in target nest:
          - migrate_rhombus(mosaic, R)
          - Verify R moved closer to target
       b. Update R's orientation vectors (E,N) after migration
    3. Return final mosaic
}
```

**Critical ordering**: Migration must process rhombi in standard order to preserve the LR tableau structure (Theorem 5.1). Wrong order breaks the bijection.

## Algorithm 4: Extract LR Tableau

```
LRTableau mosaic_to_tableau(Mosaic mosaic) {
    1. Identify the "active" nest (contains migrated rhombi)
    2. Extract rhombi from nest, preserving spatial arrangement
    3. Read tableau entries:
       - Each rhombus carries its original "content"