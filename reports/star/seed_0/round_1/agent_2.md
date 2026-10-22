# Specialist Report: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Gaps and Corrections in the Synthesis

The generalist's report captures the high-level structure but lacks crucial implementation details and contains some inaccuracies. Here's my specialist analysis:

## Precise Data Structures

### 1. KTW Puzzles
- **Grid representation**: Store as 2D array indexed by (row, col) in triangular lattice
- **Rhombus encoding**: Each rhombus has orientation ∈ {0°, 120°, 240°} and type ∈ {0-blue, 1-red, 10-white}
- **Edge labeling**: Derive from rhombus types at adjacent positions
- **Boundary extraction**: Read counterclockwise (not clockwise as stated) starting from each corner

### 2. Mosaics
- **Hexagon dimensions**: Side lengths d, n-d, d, n-d, d, n-d (alternating)
- **Tile representation**: 
  ```
  Triangle: {position, orientation ∈ {up, down}}
  Square: {position}
  Rhombus: {position, nest ∈ {A, B, C}}
  ```
- **Nest structure**: Each nest is a 150° wedge containing rhombi packed in rows

### 3. Flocks and Migration
- **Flock**: F = (ζ, (E,N), f) where:
  - ζ = set of rhombi positions
  - (E,N) = orientation vectors (150° angle between them)
  - f: ζ → ℕ assigns entries based on content
- **Standard order**: For rhombi at positions p, q:
  - p <_f q if f(p) < f(q), or f(p) = f(q) and p is west of q

## Corrected Algorithm

### Step 1: Puzzle → Mosaic

The "pulling tight" metaphor is misleading. The correct bijection:

1. **Initialize hexagon** with the three nests at alternating vertices
2. **For each puzzle rhombus** at position (i,j):
   - Determine which nest it belongs to based on edge labels
   - Place in corresponding row/column of that nest
3. **Fill remaining space** with squares and triangles to complete tiling

**Key insight**: A puzzle rhombus with edges (a,b,c) goes to nest X if the edge pointing toward X has label 1.

### Step 2: Migration Algorithm

**Initialization**:
1. Form canonical flock on nest A with orientation (-E_A, -N_A)
2. Assign f(rhombus) = k if it's the i-th rhombus in row k

**Migration process** (A → B):
1. Process rhombi in decreasing standard order
2. For each rhombus:
   ```
   while rhombus not in nest B:
     H = find_minimal_hexagon(rhombus)
     if H has 2-fold symmetry:
       rotate_180(H)
     else: # 3-fold symmetry
       rotate_120(H, direction_toward_B)
   ```

**Hexagon types**:
- Type (a): Contains 2 rhombi + 2 triangles
- Type (b): Contains 1 rhombus + 3 triangles + 2 squares

### Step 3: Extract LR Tableau

1. Rhombi in nest B form skew shape λ/μ
2. Entry at position p is f(p) from the flock
3. The migration preserves standard order, ensuring tableau conditions

## Test Case Specifics

For c^(3,2,1)_{(2,1),(2,1)}:
- Each puzzle has specific rhombus placement
- Puzzle 1 migrates to tableau: 
  ```
  . . 1
  . 1 2
  1 2 3
  ```
- Puzzle 2 migrates to:
  ```
  . . 1
  . 2 2
  1 2 3
  ```

## Implementation Priorities

1. **Coordinate system**: Use (x,y,z) with x+y+z=0