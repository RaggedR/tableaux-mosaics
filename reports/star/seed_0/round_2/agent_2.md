# Specialist Report: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Corrections to the Synthesis

The synthesis contains several fundamental errors that would lead to incorrect implementation:

### 1. **Puzzle-to-Mosaic Conversion is Wrong**
The proposed edge-label assignment is incorrect. In Purbhoo's construction:
- The puzzle "straightens" into a mosaic through a physical deformation
- Rhombi with label 0 disappear (become empty space in nests)
- Rhombi with label 1 become unit rhombi in the mosaic
- Puzzle triangles become mosaic triangles/squares

**Correct conversion**: For each puzzle piece at position (i,j,k):
```
if piece is rhombus with label 0:
    → becomes empty space (no tile)
if piece is rhombus with label 1:
    → becomes unit rhombus in appropriate nest
if piece is triangle:
    → becomes triangle or square in mosaic
```

The nest assignment depends on the piece's position relative to the hexagon corners after deformation.

### 2. **Flock Formation Error**
The synthesis suggests arbitrary f-value assignment. This is incorrect - Lemma 2.14 states there's a **unique** function f that makes a valid flock for a given orientation.

**Correct algorithm**:
```
Given rhombi α in nest with orientation (E,N):
1. Sort rhombi by position: furthest E first, then furthest N
2. Assign f-values to maintain:
   - Weakly increasing along E direction
   - Strictly increasing along N direction
   - Content matches the partition ν
```

### 3. **Migration Order Clarification**
The synthesis correctly identifies standard order but needs precision:

**Standard order <_f**: For rhombi X and Y:
- If f(X) < f(Y), then X <_f Y
- If f(X) = f(Y), then X <_f Y iff X is west of Y

For north/east migration: process largest to smallest
For south/west migration: process smallest to largest

## Complete Implementation Specification

### Data Structures
```
Rhombus {
    position: (x, y)  // 2D coordinates in plane
    nest: A|B|C|None  // which nest it belongs to
}

Mosaic {
    hexagon_vertices: [(x,y)]  // A',A,B',B,C',C clockwise
    rhombi: Set<Rhombus>
    triangles: Set<Triangle>
    squares: Set<Square>
}

Flock {
    rhombi: Set<Rhombus>
    orientation: (E_x, E_y, N_x, N_y)  // unit vectors
    f_values: Map<Rhombus, Int>
}
```

### Algorithm Implementation

**Step 1: Puzzle → Mosaic**
```
1. Create hexagon with vertices at standard positions
2. Map puzzle triangular grid to hexagon interior
3. For each puzzle piece:
   - If rhombus with label 1: place rhombus at mapped position
   - If triangle: place triangle/square based on local configuration
   - If rhombus with label 0: leave empty
4. Assign rhombi to nests based on position
```

**Step 2: Form Canonical Flock on α**
```
Given rhombi α in nest A with orientation (-E_A, -N_A):
1. Sort α by position: X before Y if X·(-E_A) > Y·(-E_A) 
   or (X·(-E_A) = Y·(-E_A) and X·(-N_A) > Y·(-N_A))
2. Partition sorted list into groups of size ν_1, ν_2, ...
3. Assign f(rhombus) = i for rhombi in group i
```

**Step 3: Migration (A → B, south direction)**
```
For each rhombus ℓ in decreasing standard order:
    while ℓ not in nest B:
        H = find_minimal_hexagon(ℓ)
        tiles = get_tiles_in_hexagon(H)
        if H has 2-fold symmet