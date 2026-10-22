# Computational Implementation Report: Purbhoo Mosaic Migration Bijection

## Executive Summary

The generalist's synthesis correctly identifies that migration is **not geometric movement** but discrete local operations. However, the proposed algorithm oversimplifies critical aspects. I'll provide concrete data structures and algorithms that handle the computational complexity properly.

## Core Data Structures

### Hexagonal Coordinate System
```cpp
struct HexCoord {
    int q, r;  // axial coordinates (s = -q-r implicit)
    
    HexCoord operator+(const HexCoord& other) const {
        return {q + other.q, r + other.r};
    }
    
    // Six hexagonal directions
    static const vector<HexCoord> DIRECTIONS;
    // {{1,0}, {1,-1}, {0,-1}, {-1,0}, {-1,1}, {0,1}}
    
    bool operator<(const HexCoord& other) const {
        return tie(q, r) < tie(other.q, other.r);
    }
};
```

### Mosaic State with Edge Labels
```cpp
struct MosaicState {
    // Edge-based representation (NOT face-based)
    map<pair<HexCoord, int>, int> edge_labels;  // coord, direction -> {0,1}
    
    // Boundary regions as coordinate sets
    set<HexCoord> region_A, region_B, region_C;
    
    // Content tracking for standard order
    map<HexCoord, int> rhombus_labels;  // tableau entry at each position
    
    int n, d;
};
```

**Critical Fix**: The generalist's face-based approach misses that puzzle edges carry the {0,1} labels, not faces. Migration operates on edge configurations.

## Puzzle-to-Mosaic Conversion

```cpp
MosaicState puzzle_to_mosaic(const vector<string>& puzzle_boundary) {
    MosaicState state;
    state.n = puzzle_boundary[0].size();
    state.d = count(puzzle_boundary[0].begin(), puzzle_boundary[0].end(), '1');
    
    // Initialize hexagonal regions
    initialize_boundary_regions(state);
    
    // Convert each boundary string to edge labels
    for (int side = 0; side < 3; side++) {
        convert_boundary_to_edges(state, puzzle_boundary[side], side);
    }
    
    // Fill interior using local consistency constraints
    propagate_edge_constraints(state);
    
    return state;
}
```

### Boundary Conversion Algorithm
```cpp
void convert_boundary_to_edges(MosaicState& state, const string& boundary, int side) {
    HexCoord start = get_boundary_start(side);
    HexCoord direction = get_boundary_direction(side);
    
    for (int i = 0; i < boundary.size(); i++) {
        HexCoord pos = start + direction * i;
        int edge_dir = (side * 2) % 6;  // Which edge of hexagon
        
        state.edge_labels[{pos, edge_dir}] = boundary[i] - '0';
    }
}
```

## Migration Algorithm Implementation

### Standard Order Computation (Addressing Critical Gap)
```cpp
vector<HexCoord> compute_migration_order(const MosaicState& state) {
    vector<pair<HexCoord, int>> candidates;
    
    // Collect rhombi in region A with their tableau values
    for (const HexCoord& pos : state.region_A) {
        if (state.rhombus_labels.count(pos)) {
            candidates.push_back({pos, state.rhombus_labels.at(pos)});
        }
    }
    
    // Sort by tableau standard order: first by value, then by position
    sort(candidates.begin(), candidates.end(), 
         [](const auto& a, const auto& b) {
             if (a.second != b.second) return a.second > b.second;  // Larger values first
             // Within same value: lexicographic by NW-SE, then NE-SW
             return