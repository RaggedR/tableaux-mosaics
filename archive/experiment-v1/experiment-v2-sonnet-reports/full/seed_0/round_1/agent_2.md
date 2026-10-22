# Report: Implementing Purbhoo's Mosaic Migration Bijection

## Problem Analysis

I need to explain how to implement the bijection between KTW puzzles and Littlewood-Richardson tableaux via Purbhoo's mosaic migration. The test case involves `c^(3,2,1)_{(2,1),(2,1)} = 2`, meaning there are 2 puzzles with specific boundary conditions that should map to 2 distinct LR tableaux.

## Key Components to Implement

### 1. Data Structures

**Puzzle Representation:**
- Triangular grid of size n with three types of pieces:
  - Rhombi with edge labels (0,1,0) or (1,0,1) 
  - Each piece can be rotated but not reflected
- Boundary data: three 01-strings (π, ρ, σ) read clockwise from lower-left
- Constraint: edge labels must match where pieces share edges

**Mosaic Representation:**
- Hexagonal region A'AB'BC'C with angles 150° at A,B,C and 90° at A',B',C'
- Three types of tiles: unit triangles, unit squares, unit rhombi (30°/150° angles)
- Three "nests" at corners A, B, C containing rhombi collections α, β, γ
- Orientation vectors for each nest: (E_A, N_A), (E_B, N_B), (E_C, N_C)

**Flock Representation:**
- A flock F = (ζ, (E,N), f) where:
  - ζ is a collection of rhombi in transformed diagram shape
  - (E,N) is an orientation (east/north unit vectors)
  - f: ζ → ℕ is an LR-tableau assignment
- Standard order on rhombi: X <_f Y if f(X) < f(Y), or equal values with X northwest of Y

### 2. Puzzle-to-Mosaic Conversion

The bijection works by "straightening" operation:
1. Remove all rhombi from puzzle
2. Allow square corners to flex (squares become rhombi)
3. Pull corners A', B', C' outward to straighten boundary into equilateral triangle
4. Clockwise edge rotations → 1's, counterclockwise → 0's

**Implementation approach:**
- Map each puzzle piece position to corresponding mosaic tile
- Track orientation changes during straightening
- Preserve adjacency constraints

### 3. Migration Algorithm

**Core Operation:** Move accessible flocks through the mosaic via local hexagonal transformations.

**Migration Step for Single Rhombus:**
1. Choose rhombus ◊ from flock (maximal in standard order for north/east migration)
2. Find minimal hexagon containing ◊ to the right
3. Apply rotation based on hexagon type:
   - Type (a): 180° rotation (2-fold symmetry)
   - Type (b): 120° rotation toward horizontal/vertical edge (3-fold symmetry)
4. Repeat until rhombus reaches target nest

**Migration Properties:**
- Preserves standard order on rhombi
- All rhombi from same flock end up in same target nest
- Operation is invertible
- Flock structure preserved (remains valid LR-tableau)

**Wake Analysis:**
- Each rhombus creates an "upper wake" and "lower wake" of displaced tiles
- Wake Crossing Lemma: rhombi can't cross midlines of earlier wakes
- This prevents disorder and ensures LR-tableau properties are maintained

### 4. Bijection Algorithm

**Main Bijection (Corollary 4.1):**
1. Start with mosaic having boundary data (α, β, γ)
2. Create flock F = (α, (-E_A, -N_A), f) using reversed orientation
3. Migrate F from nest A to nest B (southward)
4. Read resulting flock as LR-tableau with boundary data (ν, μ, λ^∨)

**Variant Bijections:** Different orientations on α yield different correspondences (Table 1 in paper).

### 5. Implementation Details

**Hexagonal Coordinate System:**
- Use coordinate system aligned with mosaic geometry