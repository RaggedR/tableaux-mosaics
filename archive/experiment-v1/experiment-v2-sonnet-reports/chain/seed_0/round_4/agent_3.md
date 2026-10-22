# Report: Implementing Purbhoo's Migration Bijection for KTW Puzzles

## Executive Summary

The previous analysis correctly identifies fundamental gaps in the free-fermionic approach but **overcomplicates the implementation**. Purbhoo's migration is not a Yang-Baxter vertex model - it's a **sequence of deterministic local moves** that can be implemented directly from the geometric description. The "free-fermionic" terminology is a red herring for coding purposes.

## Implementation Architecture

### Core Data Structures

```cpp
struct HexCoord {
    int x, y;  // Triangular lattice coordinates
};

struct RhombusState {
    HexCoord position;
    int tableau_entry;  // Content value (1,2,3,...)
    Orient orientation; // One of 3 rhombus orientations
};

struct Mosaic {
    unordered_set<HexCoord> triangles;
    unordered_set<HexCoord> squares; 
    vector<RhombusState> rhombi;
    array<Nest, 3> nests;  // A, B, C corners
};

struct Flock {
    vector<RhombusState> rhombi_subset;
    Orient standard_orientation;
    vector<int> reading_order;  // Standard tableau order
};
```

### Migration Algorithm (Corrected)

The previous report correctly identifies that migration preserves standard order, but the implementation strategy is wrong. Here's the correct approach:

```cpp
bool migrate_rhombus_step(Mosaic& mosaic, RhombusState& rho) {
    HexCoord pos = rho.position;
    
    // Find minimal containing hexagon to the right
    HexPattern pattern = identify_hex_pattern(mosaic, pos);
    
    switch (pattern.type) {
        case HEX_2FOLD:  // Symmetric case
            rotate_180_degrees(mosaic, pattern.region);
            break;
            
        case HEX_3FOLD:  // Choose rotation to make edge horizontal/vertical
            if (can_make_horizontal(rho.orientation))
                rotate_120_ccw(mosaic, pattern.region);
            else
                rotate_120_cw(mosaic, pattern.region);
            break;
    }
    
    return rho_moved_rightward(rho);
}
```

## Key Correction: Standard Order is Geometric, Not Algebraic

The previous report's fundamental error is treating standard order as an algebraic sorting problem. In Purbhoo's system:

**Standard order = geometric domination in the skew shape**
- Box X <_f Box Y iff f(X) < f(Y), OR f(X) = f(Y) and X is northwest of Y
- This order is **preserved by migration geometry**, not maintained by Yang-Baxter relations

```cpp
bool preserves_standard_order(const Flock& before, const Flock& after) {
    // Migration moves rhombi in standard order sequence
    // Later rhombi cannot "overtake" earlier ones due to wake constraints
    for (int i = 0; i < before.reading_order.size(); i++) {
        for (int j = i + 1; j < before.reading_order.size(); j++) {
            if (crosses_wake(before.rhombi[i], after.rhombi[j])) {
                return false;  // Wake Crossing Lemma violation
            }
        }
    }
    return true;
}
```

## Test Case Implementation

For c^(3,2,1)_{(2,1),(2,1)} = 2:

```cpp
void test_migration_bijection() {
    // Two KTW puzzles with boundary (2,1), (2,1), (3,2,1)
    auto puzzle1 = parse_puzzle("001101|010101|011001");  
    auto puzzle2 = parse_puzzle("010101|001101|011001");  // Different internal config
    
    // Convert to mosaics
    Mosaic mosaic1 = puzzle_to_mosaic(puzzle1);
    Mosaic mosaic2 = puzzle_to_mosaic(puzzle2);
    
    