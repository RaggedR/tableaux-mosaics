# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Synthesis and Unified Algorithm

After reviewing the specialist reports, I've identified several **critical gaps and tensions** that need resolution for a working implementation. The specialists disagree on fundamental aspects while missing key algorithmic details.

## Major Tensions to Resolve

**Tension 1**: What is migration mechanically?
- Generalist: "hexagonal flips" 
- Vertex model specialist: "Yang-Baxter moves"
- Tableaux specialist: "jeu de taquin slides"
- Combinatorics specialist: "local rotations"

**Resolution**: Migration is **sequential transport of individual rhombi** via local hexagonal rotations. Not bulk operations.

**Tension 2**: How do we determine migration paths?
- Multiple specialists mention "minimal hexagons" but none specify the algorithm
- No one explains how to handle the geometric complexity

**Critical Gap**: None of the reports provide the **concrete test case implementation** for c^(3,2,1)_{(2,1),(2,1)} = 2.

## Unified Implementation Strategy

### Data Structures (Simplified)

```cpp
struct HexCoord {
    int q, r;  // axial coordinates
    HexCoord operator+(const HexCoord& other) const;
};

struct Rhombus {
    HexCoord pos;
    int orientation;  // 0, 1, 2 (60-degree increments)
    int tableau_value;
    int nest_id;  // 0=A, 1=B, 2=C
};

struct Mosaic {
    vector<Rhombus> rhombi;
    map<HexCoord, char> tiles;  // 'T'=triangle, 'S'=square, 'R'=rhombus
    int n, d;
};
```

### Phase 1: Puzzle → Mosaic (Concrete Algorithm)

**Key insight**: The puzzle-to-mosaic conversion is **deterministic** once we understand the boundary correspondence.

```cpp
Mosaic puzzle_to_mosaic(const vector<string>& boundary_data) {
    // boundary_data = [π, ρ, σ] - the three boundary strings
    Mosaic mosaic;
    mosaic.n = boundary_data[0].length();
    mosaic.d = count(boundary_data[0].begin(), boundary_data[0].end(), '1');
    
    // Convert each boundary string to rhombus arrangement
    vector<Rhombus> nest_rhombi[3];
    for (int nest = 0; nest < 3; nest++) {
        nest_rhombi[nest] = boundary_to_rhombi(boundary_data[nest], nest);
    }
    
    // Combine and position in hexagon
    position_nests_in_hexagon(mosaic, nest_rhombi);
    fill_interior_tiles(mosaic);
    
    return mosaic;
}
```

**Critical implementation detail**: `boundary_to_rhombi()` converts a 01-string to a Young diagram packed with rhombi:
- Each '1' corresponds to a "northern step" → rhombus placed north in the nest
- Each '0' corresponds to a "western step" → rhombus placed west in the nest
- The resulting shape is the Young diagram corresponding to the partition

### Phase 2: Migration Algorithm (The Core)

**Filling the critical gap**: Here's the precise migration procedure:

```cpp
vector<Rhombus> migrate_flock(vector<Rhombus>& source_rhombi, 
                               int target_nest, 
                               Mosaic& mosaic) {
    // Sort rhombi in "standard order" - this is tableau order
    sort(source_rhombi.begin(), source_rhombi.end(), 
         [](const Rhombus& a, const Rhombus& b) {
             if (a.tableau_value != b.tableau_value) 
                 return a.tableau_value > b.tableau_value;  // larger first
             return geometric_precedence(a, b);
         });
    
    vector<Rhombus> migrated;
    
    for (Rhombus& rhom