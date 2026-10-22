## Report: Purbhoo Mosaic Migration Implementation

**Building on Prior Work**: The geometric approach correctly identifies the hexagonal flip mechanism, but lacks the crucial growth diagram perspective needed for proper implementation. I'll provide the missing face label structure and local rules.

## Enhanced Data Structures

The previous approach misses that migration is fundamentally about **face labels** propagating through a directed graph, not just geometric transformations:

```
struct FaceLabel {
    int content;          // tableau entry (1,2,3,...)
    Orientation orient;   // (E,N) direction vectors
    int standard_order;   // position in RSK-style ordering
}

struct Mosaic {
    vector<Tile> tiles;
    map<HexCoord, FaceLabel> face_labels;  // key addition
    vector<Flock> nests[3];  // A, B, C nests with flock structure
}

struct Flock {
    vector<RhombusID> rhombi;
    map<RhombusID, int> tableau_entries;  // content function f
    Orientation nest_orientation;         // (E,N) for this nest
    bool is_accessible;                   // can migrate
}
```

## Algorithm 1: Puzzle to Mosaic (Corrected)

The bijection isn't just "unfolding" - it's about **encoding recording tableaux as face labels**:

```
Mosaic puzzle_to_mosaic(Puzzle puzzle) {
    1. Map puzzle boundary strings to partition shapes:
       - String "001101" → partition via horizontal/vertical steps
       - Each nest gets partition shape α, β, γ
    
    2. Create canonical flock in nest A:
       - Pack rhombi according to partition α
       - Assign face labels f(rhombus) = unique tableau content
       - Use orientation (-E_A, -N_A) per Lemma 4.1
    
    3. Fill interior with triangles/squares from puzzle
       - Preserve local matching conditions at boundaries
    
    4. Initialize empty flocks in nests B, C
}
```

**Key insight**: The "unique flock" (Lemma 4.1) means there's exactly one way to assign tableau entries given the rhombi arrangement.

## Algorithm 2: Migration via Local Rules

Migration isn't arbitrary rotation - it follows **Fomin-style local rules** that preserve face labels:

```
bool migrate_step(Mosaic& mosaic, RhombusID rho) {
    HexRegion hex = find_minimal_hexagon(rho);
    Pattern pattern = classify_pattern(hex);
    
    switch(pattern) {
        case PATTERN_2FOLD:  // rhombus + 6 triangles
            rotate_180(hex);
            // face labels automatically preserved
            break;
            
        case PATTERN_3FOLD:  // rhombus + 2 rhombi + 4 triangles
            bool clockwise = should_rotate_clockwise(rho);
            rotate_120(hex, clockwise);
            update_face_labels_3fold(hex);  // critical step
            break;
    }
    
    return rhombus_moved_toward_target(rho);
}
```

**Local rule for 3-fold rotation**: When pattern has 3-fold symmetry, the choice of 120° rotation direction follows Purbhoo's constraint: "whichever way causes some edge to end up exactly horizontal or vertical." This isn't geometric preference - it's the **unique choice that preserves standard order**.

## Algorithm 3: Standard Order Preservation (Critical)

The previous report mentioned standard order but missed its **algebraic significance**:

```
bool preserve_standard_order(vector<RhombusID>& flock) {
    // Standard order: X <_f Y iff f(X) < f(Y) OR
    //                 f(X) = f(Y) AND X is northwest of Y
    
    sort(flock, [&](RhombusID a, RhombusID b) {
        int content_a = get_tableau_entry(a);
        int content_b = get_tableau_entry(b);
        
        if (content_a != content_b) 
            return content_a > content_b;