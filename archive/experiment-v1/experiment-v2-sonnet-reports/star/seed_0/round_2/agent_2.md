# Vertex Model Specialist Report: Critical Corrections and Implementation Framework

## Major Problems with the Generalist's Approach

The generalist fundamentally misunderstands the mathematical structure. Their "unified algorithm" contains several **fatal errors** that will produce incorrect results.

## Critical Error 1: Migration is NOT Individual Rhombus Transport

The generalist writes: "Migration is sequential transport of individual rhombi via local hexagonal rotations."

**This is wrong.** Migration operates on **entire flocks** (collections of rhombi forming tableau shapes) as coherent units. The Yang-Baxter equation guarantees that when we migrate a flock, all rhombi in that flock move together while preserving their relative tableau structure.

**Correct understanding**: A flock F = (ζ, (E,N), f) where:
- ζ is a collection of rhombi forming a skew Young diagram
- (E,N) is the orientation 
- f assigns tableau entries to rhombi

Migration moves the entire flock ζ from one nest to another, not individual rhombi.

## Critical Error 2: Misunderstanding the Hexagonal Flip Operation

The generalist mentions "hexagonal flips" but doesn't understand the vertex model structure. The correct operation is:

For each minimal hexagon containing part of the migrating flock, we apply one of two Yang-Baxter moves:
- **Type A**: 180° rotation (2-fold symmetry case)
- **Type B**: 120° rotation with orientation constraint (3-fold symmetry case)

The choice depends on the local tiling pattern, not arbitrary decisions.

## Critical Error 3: Wrong Data Structure for Rhombi

```cpp
struct Rhombus {
    HexCoord pos;
    int orientation;  // 0, 1, 2 (60-degree increments)
    int tableau_value;
    int nest_id;  // 0=A, 1=B, 2=C
};
```

**This is insufficient.** Rhombi don't have independent "tableau_value" - their values come from the flock structure. The correct representation needs:

```cpp
struct Flock {
    vector<HexCoord> rhombi_positions;
    pair<Vector2D, Vector2D> orientation;  // (E,N) vectors
    map<HexCoord, int> tableau_function;   // f: rhombi -> ℕ
    int nest_id;
};

struct Mosaic {
    array<Flock, 3> nest_flocks;  // A, B, C nests
    set<HexCoord> interior_tiles;  // triangles and squares
    int n, d;
};
```

## Correct Implementation Framework

### Phase 1: Puzzle to Mosaic (Corrected)

The boundary correspondence is correct, but the implementation must respect flock structure:

```cpp
Mosaic puzzle_to_mosaic(vector<string> boundary) {
    Mosaic M;
    M.n = boundary[0].length();
    M.d = count_ones(boundary[0]);
    
    // Convert each boundary string to a flock
    for (int nest = 0; nest < 3; nest++) {
        M.nest_flocks[nest] = boundary_string_to_flock(
            boundary[nest], nest_orientation(nest));
    }
    
    // Fill interior with canonical mosaic
    fill_canonical_interior(M);
    return M;
}
```

### Phase 2: Migration (Corrected Algorithm)

```cpp
void migrate_flock(Mosaic& M, int source_nest, int target_nest) {
    Flock& source = M.nest_flocks[source_nest];
    if (source.rhombi_positions.empty()) return;
    
    // Determine migration direction
    Vector2D direction = get_migration_direction(source_nest, target_nest);
    
    // Process rhombi in standard tableau order
    vector<HexCoord> ordered_rhombi = get_standard_order(source);
    
    for (HexCoord rhombus_pos : ordered_rhombi) {
        migrate_single_rhombus(M, rhombus_pos, direction);
    }
    
    // Update flock