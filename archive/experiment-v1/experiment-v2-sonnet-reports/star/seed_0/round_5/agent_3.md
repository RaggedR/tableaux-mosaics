# Technical Implementation Report: Purbhoo's Mosaic Migration Bijection

## Executive Summary for Coding Agent

The generalist correctly identifies the core structure but makes critical errors in migration mechanics. Migration is NOT arbitrary movement of rhombi—it's a deterministic sequence of jeu de taquin slides following specific geometric rules. I'll provide the precise algorithmic specification.

## Core Data Structures (Corrected)

```cpp
struct HexCoord {
    int x, y;  // Triangular lattice coordinates
    
    // Six neighbors in hexagonal directions
    vector<HexCoord> neighbors() const {
        return {{x+1,y}, {x-1,y}, {x,y+1}, {x,y-1}, {x+1,y-1}, {x-1,y+1}};
    }
};

struct MosaicTile {
    enum Type { TRIANGLE, SQUARE, RHOMBUS };
    Type type;
    HexCoord position;
    int orientation;  // 0-5 for different rotations
    int tableau_label;  // For rhombi: their reading order value
};

struct MosaicState {
    map<HexCoord, MosaicTile> tiles;
    vector<HexCoord> nest_A_rhombi, nest_B_rhombi, nest_C_rhombi;
    int n, d;
    
    // Critical: track which rhombi belong to current migration flock
    set<HexCoord> active_flock;
};
```

## Algorithm 1: Puzzle to Mosaic Conversion

**Key Insight**: Use Knutson-Tao's lifting to R^4 surface, then project to hexagonal tiling.

```cpp
MosaicState puzzle_to_mosaic(const PuzzleData& puzzle) {
    MosaicState mosaic;
    mosaic.n = puzzle.n;
    mosaic.d = puzzle.d;
    
    // Step 1: Create hexagonal boundary of correct size
    create_hexagonal_boundary(mosaic);
    
    // Step 2: Place corner rhombi based on boundary strings
    place_corner_rhombi(mosaic, puzzle.boundary_strings);
    
    // Step 3: Fill interior with triangles/squares via constraint propagation
    fill_interior_tiles(mosaic);
    
    return mosaic;
}

void place_corner_rhombi(MosaicState& mosaic, const vector<string>& boundary) {
    // Convert boundary 01-strings to rhombus patterns
    for (int corner = 0; corner < 3; corner++) {
        string boundary_str = boundary[corner];
        vector<HexCoord> corner_positions = get_corner_positions(corner);
        
        // Each '1' in boundary string corresponds to rhombus
        int rhombus_count = 0;
        for (char c : boundary_str) {
            if (c == '1') {
                HexCoord pos = corner_positions[rhombus_count];
                mosaic.tiles[pos] = create_rhombus_tile(pos);
                
                // Assign to appropriate nest
                if (corner == 0) mosaic.nest_A_rhombi.push_back(pos);
                else if (corner == 1) mosaic.nest_B_rhombi.push_back(pos);
                else mosaic.nest_C_rhombi.push_back(pos);
                
                rhombus_count++;
            }
        }
    }
}
```

## Algorithm 2: Standard Order Computation

**Critical Correction**: Standard order is determined by tableau reading order, NOT geometric position.

```cpp
vector<HexCoord> compute_standard_order(MosaicState& mosaic) {
    // Assign canonical tableau entries to nest A rhombi
    assign_canonical_tableau_entries(mosaic.nest_A_rhombi, mosaic);
    
    // Sort by tableau value (descending), then by position (northwest precedence)
    sort(mosaic.nest_A_rhombi.begin(), mosaic.nest_A_rhombi.end(),
         [&](const HexCoord& a, const HexCoord