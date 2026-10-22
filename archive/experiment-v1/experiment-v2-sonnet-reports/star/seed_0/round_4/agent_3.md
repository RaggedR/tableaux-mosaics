# Technical Implementation Report: Purbhoo's Migration as Jeu de Taquin Sequence

## Core Correction: Migration IS Geometric Movement, Not Just Face Updates

The generalist synthesis contains a fundamental error. Migration **is** about moving rhombi through geometric space, but implemented as a **deterministic sequence of jeu de taquin slides**. The geometric intuition is correct and essential—the implementation challenge is encoding this as discrete operations.

## Correct Mathematical Framework

Migration works in three phases that must be implemented sequentially:

### Phase 1: Puzzle → Mosaic Conversion
```cpp
struct Rhombus {
    HexCoord center;
    int orientation;  // 0, 1, 2 for three orientations
    int content;      // tableau entry (initially 0 for empty)
};

struct MosaicState {
    vector<Rhombus> rhombi_A, rhombi_B, rhombi_C;  // three nests
    TriangularGrid triangles;
    SquareGrid squares;
    
    // Boundary shapes as diagrams
    Partition alpha, beta, gamma;  // correspond to puzzle boundary strings
};
```

The conversion removes puzzle edge labels and creates geometric rhombi in three corner regions (nests A, B, C).

### Phase 2: Flock Construction and Migration Order

**Key insight**: Migration processes one rhombus at a time in **standard order**:

```cpp
vector<Rhombus*> compute_migration_order(MosaicState& mosaic) {
    // Start with rhombi in nest A (source)
    auto& source_rhombi = mosaic.rhombi_A;
    
    // Assign tableau entries using canonical flock construction
    assign_canonical_entries(source_rhombi, mosaic.alpha);
    
    // Sort by standard order: (entry_value, spatial_position)
    sort(source_rhombi.begin(), source_rhombi.end(),
         [](const Rhombus& a, const Rhombus& b) {
             if (a.content != b.content) return a.content > b.content;
             return spatial_order(a.center, b.center);  // NW to SE
         });
    
    return get_pointers(source_rhombi);
}
```

### Phase 3: Individual Rhombus Migration (The Core Algorithm)

Each rhombus moves via a sequence of **local hexagonal flips**:

```cpp
void migrate_single_rhombus(MosaicState& mosaic, Rhombus& rhombus, 
                           Direction target_direction) {
    HexCoord current = rhombus.center;
    
    while (!in_target_nest(current, target_direction)) {
        // Find minimal hexagonal region containing rhombus
        HexRegion hex = find_minimal_hex(mosaic, current);
        
        if (hex.has_two_fold_symmetry()) {
            // 180-degree rotation
            apply_rotation_180(mosaic, hex);
            current = hex.get_new_rhombus_position();
        }
        else if (hex.has_three_fold_symmetry()) {
            // 120-degree rotation (direction determined by migration target)
            apply_rotation_120(mosaic, hex, target_direction);
            current = hex.get_new_rhombus_position();
        }
        else {
            throw runtime_error("Invalid hex configuration");
        }
        
        rhombus.center = current;
    }
}
```

## Local Hexagonal Flip Rules

The two types of local regions correspond exactly to jeu de taquin slide types:

```cpp
void apply_rotation_180(MosaicState& mosaic, const HexRegion& hex) {
    // Type: rhombus + 2 triangles + 2 squares + rhombus
    // Effect: swap the two rhombi positions
    auto [rhombus1, rhombus2] = hex.get_rhombi();
    swap(rhombus1.center, rhombus2.center);
    
    // Update triangle/square orientations
    for (auto& tri : hex.triangles) tri.rotate_180();
    for (auto