# Growth Diagram Specialist Report: Implementing KTW Puzzle Migration

## Critical Assessment: The Framework Needs Fundamental Restructuring

The generalist's synthesis contains several deep conceptual errors that would prevent successful implementation. As a specialist in Fomin growth diagrams and RSK-type correspondences, I must correct the fundamental misunderstanding of what Purbhoo's construction actually does.

## The Real Mathematical Structure

**Key Insight**: Purbhoo's migration is NOT a growth diagram in the Fomin sense. It's a bijection between two different combinatorial structures that preserves certain invariants through local moves.

### Correct Data Structure

```cpp
struct PurbhooMosaic {
    // Hexagonal tiling with three types of unit pieces
    struct Tile {
        enum Type { TRIANGLE, SQUARE, RHOMBUS_30_150 };
        Type type;
        HexCoord position;
        int orientation;  // 0-5 for six possible orientations
    };
    
    // Three corner "nests" containing rhombi collections
    struct Nest {
        vector<HexCoord> rhombi_positions;
        Orientation frame;  // (E,N) vectors defining coordinate system
        bool is_accessible(HexCoord pos) const;
    };
    
    map<HexCoord, Tile> tiling;
    array<Nest, 3> corner_nests;  // A, B, C corners
    BoundaryData boundary_strings;
};
```

## Migration Algorithm: The Real Implementation

The generalist's "local face updates" approach is completely wrong. Here's what actually happens:

```cpp
LRTableau purbhoo_migration(const KTWPuzzle& puzzle) {
    // Step 1: Convert puzzle to mosaic (straightforward geometric transform)
    PurbhooMosaic mosaic = puzzle_to_mosaic(puzzle);
    
    // Step 2: Create flock on rhombi in corner A
    Flock flock = create_canonical_flock(mosaic.corner_nests[0]);  // nest A
    
    // Step 3: Migrate flock from A to B via local hexagon operations
    migrate_flock_A_to_B(mosaic, flock);
    
    // Step 4: Read LR tableau from final flock configuration
    return flock_to_tableau(flock, mosaic.corner_nests[1]);  // nest B
}
```

### The Core Migration Operation

**Critical Error in Synthesis**: Migration doesn't update "face labels" - it performs specific sequences of local hexagonal rotations as described in Purbhoo's paper.

```cpp
void migrate_flock_A_to_B(PurbhooMosaic& mosaic, Flock& flock) {
    // Process rhombi in standard order (this part was correct)
    vector<HexCoord> migration_sequence = compute_flock_standard_order(flock);
    
    for (HexCoord rhombus_pos : migration_sequence) {
        migrate_single_rhombus(mosaic, rhombus_pos);
    }
}

void migrate_single_rhombus(PurbhooMosaic& mosaic, HexCoord start_pos) {
    HexCoord current_pos = start_pos;
    
    while (!in_target_nest_B(current_pos)) {
        // Find minimal containing hexagon
        HexRegion hex = find_minimal_hexagon(mosaic, current_pos);
        
        if (has_2fold_symmetry(hex)) {
            // Rotate tiling by 180°
            rotate_hexagon_180(mosaic, hex);
        } else if (has_3fold_symmetry(hex)) {
            // Rotate by 120° in direction that makes edge horizontal/vertical
            rotate_hexagon_120_constrained(mosaic, hex);
        }
        
        current_pos = track_rhombus_new_position(mosaic, start_pos);
    }
}
```

## Standard Order: The Make-or-Break Implementation Detail

The generalist completely missed this. Standard order is NOT lexicographic sorting - it's the unique total order on rhombi that makes migration preserve the tableau property: