# Computational Mathematics Report: Purbhoo Mosaic Migration Implementation

## Critical Gaps in the Synthesis

The generalist's synthesis has several implementation flaws that will cause algorithmic failures:

1. **Edge constraint propagation is underdetermined** - You cannot "solve_edge_constraints" from boundary data alone without the actual puzzle pieces
2. **Standard order computation is wrong** - The canonical entry assignment doesn't match Purbhoo's definition
3. **Single rhombus migration is incomplete** - The core hexagonal flip operations are missing

## Correct Implementation Strategy

### Data Structure: Tile-Based Representation

```cpp
enum TileType { TRIANGLE_UP, TRIANGLE_DOWN, SQUARE, RHOMBUS_A, RHOMBUS_B, RHOMBUS_C };

struct Tile {
    TileType type;
    HexCoord position;
    map<int, int> edge_labels;  // direction -> {0,1}
    int tableau_entry;          // for rhombi only
};

struct MosaicState {
    map<HexCoord, Tile> tiles;
    vector<HexCoord> nest_A_rhombi, nest_B_rhombi, nest_C_rhombi;
    int n, d;
};
```

### Algorithm 1: Puzzle to Mosaic (Correct Version)

```cpp
MosaicState puzzle_to_mosaic(const PuzzleData& puzzle) {
    MosaicState mosaic;
    
    // Step 1: Place puzzle pieces directly as mosaic tiles
    for (const auto& piece : puzzle.pieces) {
        Tile tile = convert_puzzle_piece_to_tile(piece);
        mosaic.tiles[piece.position] = tile;
    }
    
    // Step 2: Add corner rhombi to complete hexagonal tiling
    add_corner_rhombi(mosaic);
    
    // Step 3: Classify rhombi by nest
    classify_rhombi_by_nest(mosaic);
    
    return mosaic;
}
```

### Algorithm 2: Standard Order (Purbhoo's Definition)

```cpp
void assign_standard_order(MosaicState& mosaic) {
    // Nest A has specific geometric shape - identify its Young diagram
    YoungDiagram nest_shape = extract_nest_A_shape(mosaic);
    
    // Fill tableau entries using standard Young tableau rules
    int entry = 1;
    for (int row = nest_shape.num_rows - 1; row >= 0; row--) {
        for (int col = 0; col < nest_shape.row_length[row]; col++) {
            HexCoord rhombus_pos = nest_to_hex_coord(row, col);
            if (mosaic.tiles.count(rhombus_pos)) {
                mosaic.tiles[rhombus_pos].tableau_entry = entry++;
            }
        }
    }
}

vector<HexCoord> compute_migration_order(const MosaicState& mosaic) {
    vector<HexCoord> order = mosaic.nest_A_rhombi;
    
    sort(order.begin(), order.end(), [&](const HexCoord& a, const HexCoord& b) {
        int entry_a = mosaic.tiles.at(a).tableau_entry;
        int entry_b = mosaic.tiles.at(b).tableau_entry;
        return entry_a > entry_b;  // Largest tableau entry first
    });
    
    return order;
}
```

### Algorithm 3: Hexagonal Flip Operations (The Core)

```cpp
enum FlipType { TYPE_A_ROTATION, TYPE_B_ROTATION };

struct HexRegion {
    HexCoord center;
    array<Tile, 6> tiles;  // Clockwise from top
};

bool attempt_flip(MosaicState& mosaic, HexCoord center, FlipType type) {
    HexRegion region = extract_hex_region(mosaic, center);
    
    if (type == TYPE_A_ROTATION) {
        // 180-degree rotation for 2-fold symmetric patterns
        if (is_2