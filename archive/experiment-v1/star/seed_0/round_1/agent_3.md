## Specialist Analysis: Migration Bijection Implementation

Building on the generalist's synthesis, I'll provide concrete implementation details for each phase of Purbhoo's bijection.

### Phase 1: Puzzle → Mosaic Conversion

The "pulling corners" transformation is actually a precise geometric mapping. Here's the algorithm:

**Data Structure**: Represent puzzle pieces by their vertices in a coordinate system where:
- Puzzle has vertices at integer linear combinations of vectors (1,0) and (1/2,√3/2)
- Triangle side length n means vertices range from (0,0) to (n,0) to (n/2,n√3/2)

**Algorithm**:
1. Remove all puzzle rhombi (keep only triangles)
2. Apply the linear transformation that maps the puzzle triangle to the mosaic hexagon:
   - Puzzle vertices: A'=(0,0), B'=(n,0), C'=(n/2,n√3/2)  
   - Mosaic hexagon vertices: A'=(0,0), A=(d,0), B'=(n,0), B=(n,d√3/3), C'=(n/2,n√3/2), C=((n-d)/2,(n+d)√3/2)
   - This stretches the puzzle, creating gaps where rhombi were
3. Fill gaps with mosaic pieces:
   - Triangular gaps → triangles
   - Parallelogram gaps → squares (which appear as 60°/120° rhombi in the mosaic coordinate system)
   - Original puzzle rhombi → 30°/150° rhombi packed in the three nests

**Edge labeling conversion**: 
- 0-labeled edges → edges that rotated clockwise
- 1-labeled edges → edges that rotated counterclockwise

### Phase 2: Migration Algorithm

**Initial Setup**:
1. Identify the rhombi collection α at nest A (these came from puzzle rhombi on the left edge)
2. Assign orientation (-E_A, -N_A) where E_A points along AA' and N_A points along AB'
3. Create the canonical flock: label rhombi 1,2,... by reading order (northwest to southeast in the nest)

**Migration Process** (from nest A to nest B):
```
For each rhombus ℓ in reverse standard order:
  While ℓ is not in nest B:
    1. Find the minimal hexagon containing ℓ to its right
    2. If hexagon has 2-fold symmetry: rotate tiling 180°
    3. If hexagon has 3-fold symmetry: rotate 120° such that one edge of ℓ becomes horizontal or vertical
    4. Update ℓ's position
```

**Key Implementation Details**:
- Standard order: rhombus X < Y if label(X) < label(Y), or if equal labels and X is west of Y
- Wake preservation: the algorithm ensures rhombi don't cross each other's "wakes" (paths)
- Orientation tracking: (E,N) vectors rotate by at most 60° during migration

### Phase 3: Mosaic → Tableau Extraction

After migration to nest B:
1. The rhombi form a skew shape in nest B
2. Each rhombus retains its label from the canonical flock
3. The LR tableau has:
   - Shape: λ/μ where λ comes from nest B boundary, μ from the empty space
   - Entry at position = label of rhombus at that position
   - Boundary data (ν, μ, λ^v) where ν is the content (multiplicities of labels)

### Test Case Implementation

For c^(3,2,1)_{(2,1),(2,1)} = 2:
- n = 6, d = 3 (sum of partition sizes)
- Expect 2 puzzles with appropriate boundary strings
- Each produces distinct mosaic → distinct migration path → distinct tableau

**Data Structures**:
```
Puzzle: {
  pieces: [(type, vertices, edge_labels)]
  boundary: (π, ρ, σ)
}

Mosaic: {
  tiles: [(type, position)]  // triangles, squares, rhombi
  nests: {A: [rhombi], B: