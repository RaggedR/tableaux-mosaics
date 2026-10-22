# Mathematical Synthesis Report: Purbhoo's Mosaic Migration Implementation

## Core Mathematical Structure (Resolving Specialist Tensions)

The specialists reveal fundamental disagreements about the mathematical nature of migration. Let me synthesize the correct picture:

**Key Resolution**: Migration IS geometric movement of rhombi, but implemented as discrete local operations that preserve tableau structure. The growth diagram specialist is wrong about "local face updates"—migration follows deterministic paths. The vertex model specialist correctly identifies Yang-Baxter compatibility but overcomplicates the implementation. The technical specialist correctly emphasizes edge-based representation.

## Unified Data Structure

```cpp
struct MosaicState {
    // Primary: Edge-based representation (resolving face vs edge confusion)
    map<pair<HexCoord, int>, int> edge_labels;  // (position, direction) -> {0,1}
    
    // Secondary: Rhombus tracking for migration
    struct Rhombus {
        HexCoord center;
        int tableau_entry;    // Content value for standard order
        bool in_flock;       // Whether participating in current migration
    };
    map<HexCoord, Rhombus> rhombi;
    
    // Boundary regions (three corner nests)
    set<HexCoord> nest_A, nest_B, nest_C;
    
    int n, d;  // Puzzle parameters
};
```

**Critical Insight**: The edge labels determine everything. Rhombus positions and contents are derived from local edge patterns.

## Migration Algorithm: The Correct Synthesis

### Step 1: Puzzle to Mosaic Conversion
```cpp
MosaicState puzzle_to_mosaic(const vector<string>& boundary_strings) {
    MosaicState state;
    state.n = boundary_strings[0].size();
    state.d = count_ones(boundary_strings[0]);
    
    // Convert boundary strings to edge labels on hexagonal grid
    place_boundary_edges(state, boundary_strings);
    
    // Propagate constraints inward to fill mosaic completely
    solve_edge_constraints(state);
    
    // Identify rhombus positions from edge patterns
    extract_rhombus_positions(state);
    
    return state;
}
```

### Step 2: Standard Order Computation (Critical Implementation Detail)
```cpp
vector<HexCoord> compute_standard_order(MosaicState& state) {
    // Assign canonical tableau entries to rhombi in nest A
    vector<HexCoord> nest_A_rhombi;
    for (const HexCoord& pos : state.nest_A) {
        if (state.rhombi.count(pos)) {
            nest_A_rhombi.push_back(pos);
        }
    }
    
    // Assign entries using shape of nest A (filling by rows, left to right)
    assign_canonical_entries(state, nest_A_rhombi);
    
    // Sort by standard order: tableau entry first, then position
    sort(nest_A_rhombi.begin(), nest_A_rhombi.end(),
         [&](const HexCoord& a, const HexCoord& b) {
             int val_a = state.rhombi[a].tableau_entry;
             int val_b = state.rhombi[b].tableau_entry;
             
             if (val_a != val_b) return val_a > val_b;  // Process largest first
             
             // Geometric tiebreaker (northwest to southeast)
             return northwest_southeast_order(a, b);
         });
    
    return nest_A_rhombi;
}
```

### Step 3: Core Migration Loop
```cpp
LRTableau migrate_A_to_B(MosaicState& state) {
    vector<HexCoord> migration_order = compute_standard_order(state);
    
    for (const HexCoord& rhombus_pos : migration_order) {
        migrate_single_rhombus(state, rhombus_pos);
    }
    
    return extract_tableau_from_nest_B(state);
}
```

### Step 4: Single Rhombus Migration (The Heart of the Algorithm)
```cpp
void migrate_single_