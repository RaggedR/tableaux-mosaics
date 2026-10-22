# Synthesis Report: Implementing Purbhoo's Mosaic Migration Bijection

## Key Mathematical Structure (Resolving Fundamental Confusion)

The specialist reports reveal a critical confusion in the original synthesis: **migration is not about moving geometric rhombi through space**. Instead, it's a **discrete sequence of local combinatorial operations** that can be implemented purely algebraically.

### Correct Mathematical Framework

The bijection operates on three distinct but related levels:

1. **Combinatorial Level**: Face labels in hexagonal regions that encode tableau structure
2. **Geometric Level**: Hexagonal coordinate system for bookkeeping 
3. **Algebraic Level**: Standard order preservation that ensures bijection validity

## Unified Data Structure

```cpp
struct MosaicState {
    // Hexagonal coordinate system
    struct HexCoord {
        int q, r, s;  // cube coordinates with q+r+s=0
        HexCoord(int q, int r) : q(q), r(r), s(-q-r) {}
    };
    
    // Face label encoding (NOT moving rhombi)
    struct Face {
        int label;                    // 0=empty, 1=NE diagonal, 2=NW diagonal, 3=box
        array<int, 6> edge_weights;  // weights on six hex edges
        HexCoord position;
    };
    
    // Three boundary regions as collections of face labels
    map<HexCoord, Face> faces;
    BoundaryData boundary;
    int n, d;
};
```

## Core Algorithm: Migration as Local Face Updates

**Critical Insight from Growth Diagram Specialist**: Migration is a sequence of local face label updates, not geometric movement.

```cpp
LRTableau migrate_via_local_rules(const PuzzleBoundary& puzzle) {
    MosaicState state = initialize_from_puzzle(puzzle);
    
    // Migration = apply local update rules in specific order
    vector<HexCoord> migration_order = compute_standard_order(state);
    
    for (HexCoord coord : migration_order) {
        apply_local_migration_rule(state, coord);
    }
    
    return read_tableau_from_final_state(state);
}
```

### Local Migration Rules (Unified from All Specialists)

The vertex model specialist was correct that these rules must satisfy Yang-Baxter consistency:

```cpp
void apply_local_migration_rule(MosaicState& state, HexCoord pos) {
    Face& face = state.faces[pos];
    
    // Get neighboring edge weights
    auto [N, NE, SE, S, SW, NW] = get_neighbor_weights(state, pos);
    
    // Apply bijection-preserving local rules
    if (N > S && NE == SW) {
        // Corresponds to jeu de taquin slide
        face.label = (face.label == 1) ? 2 : 1;
        update_neighbor_weights(state, pos, {{N, N+1}, {S, S-1}});
    }
    else if (NE > SW && SE == NW) {
        // Different slide direction
        face.label = (face.label == 2) ? 1 : 2;  
        update_neighbor_weights(state, pos, {{NE, NE+1}, {SW, SW-1}});
    }
    // Additional rules for all local configurations
}
```

## Critical Implementation Details

### 1. Standard Order Computation (Resolving Vertex Model Constraint)

The vertex model specialist correctly noted that standard order isn't simple sorting—it must respect combinatorial constraints:

```cpp
vector<HexCoord> compute_standard_order(const MosaicState& state) {
    vector<HexCoord> candidates;
    
    // Collect all non-empty faces in boundary region A
    for (auto& [coord, face] : state.faces) {
        if (face.label > 0 && in_boundary_region_A(coord)) {
            candidates.push_back(coord);
        }
    }
    
    // Sort respecting tableau constraints
    sort(candidates.begin(), candidates.end(), 
         [&](HexCoord a, HexCoord b) {