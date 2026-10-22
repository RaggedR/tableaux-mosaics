## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

I'll build on the previous researcher's work, providing crucial corrections and concrete implementation details.

### Critical Corrections

1. **Puzzle-to-Mosaic Conversion**: The previous report misunderstands the fundamental transformation. Purbhoo describes a **physical deformation**, not a direct mapping. The puzzle's equilateral triangle is stretched into a hexagon by pulling corners A', B', C' outward, converting:
   - Puzzle rhombi → Empty spaces in mosaic
   - Unit triangles → Unit triangles (unchanged)
   - NOT directly placing rhombi into nests

2. **Rhombus Placement**: The mosaic rhombi come from the **boundary data**, not from puzzle pieces. For boundary string π with d ones, we place d rhombi in nest A according to partition structure.

3. **Standard Order**: With orientation (-E_A, -N_A), rhombi increase **westward** in rows and **southward** between rows, not northward as claimed.

### Correct Implementation

#### Data Structures

```
Puzzle:
  - size: n
  - pieces: List[(pos, type, edges)]
  - pos: (i,j) with 0 ≤ i,j ≤ n-1, i+j ≤ n-1
  - edges: {dir -> 0/1} for each edge

Mosaic:
  - hexagon with vertices A'AB'BC'C
  - tiles: Dict[(x,y) -> Tile]
  - Tile: 'triangle' | 'square' | 'rhombus'
  - nests: {A: Set[Rhombus], B: Set[Rhombus], C: Set[Rhombus]}

Flock:
  - rhombi: Set[Rhombus] 
  - orientation: (E,N) vectors
  - tableau: Rhombus -> Integer
```

#### Step 1: Puzzle to Mosaic

```
1. Extract boundary strings:
   - π: bottom edge, left to right
   - ρ: right edge, bottom to top  
   - σ: left edge, top to bottom

2. Create hexagon frame:
   - Place unit triangles/squares following deformation rules
   - Puzzle rhombus at (i,j) → gap in mosaic

3. Place rhombi in nests from boundary data:
   For π = π₁...πₙ with d ones at positions k₁ < ... < kₐ:
   - Rhombus i goes at position (n-d-kᵢ+i-1, d-i) in nest A
   - Similarly for ρ→B, σ→C using appropriate coordinates
```

#### Step 2: Create Flock with Orientation (-E_A, -N_A)

```
1. Standard order on nest A rhombi:
   Rhombus (x₁,y₁) < (x₂,y₂) iff:
   - y₁ < y₂ (south is smaller), OR
   - y₁ = y₂ AND x₁ > x₂ (west is smaller when tied)

2. Assign tableau values:
   row = 1
   for i from 0 to d-1:
     rhombi[i].value = row
     if i+1 < d and rhombi[i+1].y < rhombi[i].y:
       row += 1
```

#### Step 3: Migration South (from A to B)

```
for rhombus ρ in standard order:
  while ρ.nest ≠ B:
    1. Find minimal hexagon H rightward of ρ:
       - Start from ρ's rightmost vertex
       - Expand until hitting 6 boundary tiles
       
    2. Identify hexagon type and rotate:
       if H has 2-fold symmetry:
         rotate_180(H)  # ρ moves right
       else:  # 3-fold symmetry
         # Choose rotation placing ρ's edge horizontal/vertical
         if angle(ρ.edge, horizontal) ∈ {30°, 