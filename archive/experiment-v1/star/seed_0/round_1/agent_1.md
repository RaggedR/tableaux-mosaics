## Specialist Analysis: Growth Diagrams and Migration Implementation

Looking at this problem through the lens of growth diagrams and local rules, I see several critical insights that will help implement this bijection correctly.

### 1. The Puzzle-to-Mosaic Conversion is a Coordinate Transform

The key insight is that puzzles and mosaics are different projections of the same piecewise-linear surface in ℝ⁴. The conversion isn't just geometric - it's fundamentally about reinterpreting the combinatorial data.

**Implementation approach:**
- Puzzles use triangular coordinates with vertices at 120° angles
- Mosaics use a hexagonal frame with three nests at vertices A, B, C
- The transformation maps puzzle edges to mosaic boundaries:
  - Edge labels 0/1 become steps west/north in the boundary walk
  - Each puzzle piece maps to specific mosaic tiles based on its edge labels

**Data structures needed:**
```
PuzzlePiece: {type: triangle/rhombus, edges: [0/1, 0/1, 0/1], position}
MosaicTile: {type: triangle/square/rhombus, position, orientation}
```

### 2. Migration as a Growth Diagram Process

Migration is essentially running a growth diagram algorithm where:
- **Vertices**: Positions where rhombi can be placed
- **Directed edges**: Valid migration paths between positions
- **Face labels**: The rhombus values (1, 2, 3, ...) that determine migration order
- **Local rules**: The hexagonal flip operations

The "accessible flock" concept corresponds to the initial configuration in a growth diagram where rhombi form a valid Young diagram shape.

**Critical implementation detail:** Migration proceeds in standard order:
- For north/east migration: process largest-valued rhombi first
- For south/west migration: process smallest-valued rhombi first
- This ensures the Wake Crossing Lemma holds (rhombi don't illegally cross paths)

### 3. The Hexagonal Flip Rules

Each rhombus migration step involves finding the minimal enclosing hexagon and applying one of two rotations:

**Type A (2-fold symmetry)**: Rotate 180°
```
Before:    After:
  /□\       \□/
 /ρ  \  →  /  ρ\
```

**Type B (3-fold symmetry)**: Rotate 120° to make one rhombus edge horizontal/vertical
```
The rotation direction is uniquely determined by which edge becomes aligned
```

### 4. Orientation Tracking Through Migration

This is crucial and often missed: orientations (E,N) rotate predictably:
- Maximum 60° rotation per complete migration
- The induced orientation (E',N') determines how to read the final tableau
- For the standard bijection: use orientation (-E_A, -N_A) on the initial flock

### 5. Algorithm for the Complete Bijection

**Step 1: Puzzle → Mosaic**
```
1. Create hexagon with nests at A, B, C
2. For each puzzle piece at position (i,j,k):
   - Map to mosaic coordinates using affine transform
   - Triangle → triangle (direct mapping)
   - Rhombus with edges (a,b,c,d,e,f) → rhombus if it belongs to a nest
   - Otherwise → appropriate square/triangle configuration
3. Pack rhombi into nests based on boundary conditions
```

**Step 2: Migration**
```
1. Form initial flock F on α (rhombi at nest A) with orientation (-E_A, -N_A)
2. Assign values f(ρ) based on standard Young tableau order
3. For each rhombus in standard order:
   a. Find minimal enclosing hexagon to the right
   b. Apply appropriate rotation (Type A or B)
   c. Update position, repeat until reaching target nest B
4. Track orientation changes throughout
```

**Step 3: Extract Tableau**
```
1. Final flock F' has rhombi in nest B forming shape λ/μ
2. The function f': rhombi → values gives the tableau entries
3. The shape and entries fully determine the LR tableau
```

### 6. Test Case Verification

For c^(3,2,1)_{(2,1),(2,