# Fomin Growth Diagram Specialist Report: Critical Analysis and Implementation Path

## Assessment of Generalist Synthesis

The generalist's approach fundamentally **misunderstands the bijection structure**. While they identify important tensions, their "unified algorithm" misses the core mathematical machinery that makes Purbhoo's bijection work.

## Major Problems with Generalist Approach

**Problem 1: Wrong Migration Model**
- Generalist treats migration as "sequential transport of individual rhombi"
- **Reality**: Migration is simultaneous transformation preserving global constraints
- The "standard order" sorting approach will break bijection properties

**Problem 2: Missing Growth Diagram Structure**
- No mention of face labels or local rules
- No understanding of how tableau data propagates during migration
- The boundary_to_rhombi() function cannot work without face label encoding

**Problem 3: Incorrect Test Case Understanding**
- Claims c^(3,2,1)_{(2,1),(2,1)} = 2 has "two distinct puzzles"
- **Reality**: This is a single coefficient counting puzzle multiplicity

## Correct Implementation Framework

### Core Data Structure: Face-Labeled Network

```cpp
struct FaceLabel {
    vector<int> content;  // tableau content at this face
    int orientation;      // 0,1,2,3 for nest orientations
};

struct MosaicFace {
    HexCoord center;
    FaceLabel label;
    char tile_type;  // 'T', 'S', 'R'
};

struct LabeledMosaic {
    map<HexCoord, MosaicFace> faces;
    map<int, vector<HexCoord>> nests;  // nest_id -> face positions
    int n, d;
    
    // Growth diagram methods
    bool check_local_rules(HexCoord pos);
    void propagate_labels();
};
```

### Phase 1: Puzzle → Labeled Mosaic (Corrected)

The key insight is that **face labels encode the recording tableau**:

```cpp
LabeledMosaic puzzle_to_labeled_mosaic(const KTWPuzzle& puzzle) {
    LabeledMosaic mosaic;
    
    // Step 1: Convert puzzle pieces to face network
    for (const auto& piece : puzzle.pieces) {
        MosaicFace face = convert_puzzle_piece(piece);
        mosaic.faces[face.center] = face;
    }
    
    // Step 2: Extract boundary face labels from puzzle boundary
    // This is where the bijection encodes tableau structure
    set_boundary_labels(mosaic, puzzle.boundary_data);
    
    // Step 3: Propagate labels inward via local rules
    propagate_face_labels(mosaic);
    
    return mosaic;
}
```

### Phase 2: Migration as Growth Diagram Evolution

**Critical correction**: Migration is **not** moving rhombi. It's **evolving face labels** according to local rules:

```cpp
vector<int> migrate_nest_content(LabeledMosaic& mosaic, 
                                 int source_nest, 
                                 int target_nest) {
    // Find migration path in dual graph
    vector<HexCoord> path = find_migration_path(mosaic, source_nest, target_nest);
    
    // Apply local rules along path
    for (int i = 0; i < path.size() - 1; i++) {
        apply_local_rule(mosaic, path[i], path[i+1]);
    }
    
    // Extract final content at target nest
    return extract_nest_content(mosaic, target_nest);
}

void apply_local_rule(LabeledMosaic& mosaic, HexCoord from, HexCoord to) {
    // This is where Yang-Baxter equations ensure bijection
    FaceLabel& from_label = mosaic.faces[from].label;
    FaceLabel& to_label = mosaic.faces[to].label;
    
    // Apply appropriate 3-term local rule based on face types
    if (mosaic.faces[from].tile_type == 'R' && mosaic.faces[to].tile_type == 'S') {
        apply