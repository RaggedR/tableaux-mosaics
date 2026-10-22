# Growth Diagram Face Label Specialist Report

## Critical Analysis: The Synthesis Still Misses the Point

The generalist's synthesis, while attempting to unify perspectives, fundamentally misunderstands what growth diagrams contribute to this bijection. Let me be direct: **migration cannot be implemented as "moving rhombi" plus "evolving face labels"** - this reflects a category error about what face labels represent.

## What Growth Diagrams Actually Provide

Growth diagrams don't track rhombi positions. They encode the **combinatorial essence** of the migration bijection through face label evolution rules that directly mirror jeu de taquin slides.

### Correct Data Structure
```cpp
struct GrowthFace {
    int label;                    // Shape encoding: 0=empty, 1=/, 2=\, 3=box
    array<int, 4> edge_weights;  // N, E, S, W boundary weights
    HexCoord position;
};

struct GrowthDiagram {
    map<HexCoord, GrowthFace> faces;
    int n, d;
    
    // Key insight: migration = sequence of local face updates
    bool update_face(HexCoord pos, int new_label);
    vector<LRTableauEntry> read_final_tableau();
};
```

## Migration as Face Label Evolution (Not Rhombi Movement)

The migration algorithm should work directly on face labels:

```cpp
LRTableau migrate_via_face_labels(const vector<string>& puzzle_boundary) {
    // Initialize growth diagram from puzzle boundary
    GrowthDiagram diagram = initialize_from_boundary(puzzle_boundary);
    
    // Migration = apply local update rules in reading order
    for (auto coord : get_migration_order(diagram)) {
        apply_local_rule(diagram, coord);
    }
    
    return diagram.read_final_tableau();
}

void apply_local_rule(GrowthDiagram& diagram, HexCoord pos) {
    GrowthFace& face = diagram.faces[pos];
    
    // Local rule based on neighboring edge weights
    int N = face.edge_weights[0], E = face.edge_weights[1];
    int S = face.edge_weights[2], W = face.edge_weights[3];
    
    // Jeu de taquin correspondence rules
    if (N > S && E == W) {
        face.label = (face.label == 1) ? 2 : 1;  // Flip diagonal
        // Update adjacent edge weights consistently
        propagate_weight_changes(diagram, pos);
    }
    // Additional rules for different local configurations...
}
```

## Where the Synthesis Goes Wrong

1. **"Rhombi move through hexagonal regions"** - No. Face labels change according to local rules. The geometry is just bookkeeping.

2. **"This realizes jeu de taquin slides"** - Backwards. Jeu de taquin slides ARE the face label updates. There's no separate realization.

3. **"Migration preserves standard order"** - This is an emergent property of the local rules, not an input constraint.

## Correct Implementation Priority

Focus on these face label update rules, derived directly from the jeu de taquin correspondence:

```cpp
struct LocalRule {
    pattern<int, 4> boundary_weights;  // (N,E,S,W) pattern to match
    int old_label, new_label;          // Face label transformation
    vector<EdgeUpdate> weight_updates; // Induced changes to neighbors
};

// The complete migration algorithm
const vector<LocalRule> MIGRATION_RULES = {
    {{1,0,0,1}, 0, 1, {{NORTH, +1}, {SOUTH, -1}}},  // Create box
    {{0,1,1,0}, 0, 2, {{EAST, +1}, {WEST, -1}}},    // Create box
    {{1,1,0,0}, 1, 2, {{NORTH, +1}, {EAST, +1}}},   // Slide northeast
    // ... complete rule set from jeu de taquin theory
};
```

## Bottom Line for Implementation

**Forget about moving geometric objects.** Implement the face label evolution system directly. The "