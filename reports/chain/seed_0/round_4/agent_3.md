## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

The previous researcher provides a solid foundation but has critical gaps and some errors. I'll provide a complete, correct specification.

### Key Corrections and Clarifications

1. **Wake concept is correct but incomplete**: The previous report mentions wakes but doesn't explain how they enforce the partial order during migration.

2. **Partition-to-rhombi mapping needs fixing**: The previous description is too vague about coordinate systems.

3. **Migration direction and orientation relationship**: The report doesn't clearly explain how orientations rotate during migration.

### Complete Algorithm Specification

#### Step 1: Puzzle to Mosaic (Corrected)

The physical transformation is conceptually correct, but here's the precise algorithm:

```
Data structures:
- Puzzle: 2D array of pieces in triangular grid
- Mosaic: Hexagon with three nests at corners A, B, C
- Piece types: Triangle (no edge labels), Square (becomes rhombus), 
               Rhombus (30°/150°, has two 1-edges)

Algorithm:
1. Extract all 30°/150° rhombi from puzzle, recording positions
2. Transform remaining structure:
   - Map puzzle coordinates (i,j) to mosaic coordinates
   - Triangles → triangles, squares → squares
   - This creates a hexagon with three 150° corners (nests)
3. Place rhombi in nests based on boundary strings
```

#### Step 2: Boundary String to Partition to Rhombi

```
Algorithm: Convert boundary string to rhombi placement
Input: String σ = σ₁...σₙ (0s and 1s)
Output: Rhombi arranged in nest

1. Create partition λ from σ:
   - λᵢ = position of i-th 1 from right minus i
   - Example: 01001 → λ = (3,0) (1s at positions 4,1)
2. Place rhombi:
   - In nest at A: use orientation (E_A, N_A)
   - Stack λ₁ rhombi along E_A direction (bottom row)
   - Stack λ₂ rhombi in next row north, etc.
   - Each rhombus has 150° angle pointing into nest
```

#### Step 3: Flock Creation with Orientation

For migration from A to B, create flock with orientation (-E_A, -N_A):

```
Algorithm: Create flock with tableau values
1. Let rhombi in nest A have orientation (-E_A, -N_A)
2. Order rhombi by standard order:
   - Primary: west to east in rotated coordinates
   - Secondary: south to north in rotated coordinates
3. Assign values:
   - Group by rows (constant y-coordinate)
   - Bottom row gets value 1, next row gets value 2, etc.
```

#### Step 4: Migration Algorithm (Complete)

```
Algorithm: Migrate flock F from nest A to nest B
1. Process rhombi in standard order (largest to smallest value,
   west to east within same value)

2. For each rhombus ρ:
   a. Find minimal hexagon H containing ρ on its left edge
   b. Apply rotation:
      - If H has 2-fold symmetry: rotate 180°
      - If H has 3-fold symmetry: rotate 120° to align
        one edge of ρ with hexagon boundary
   c. Track wake:
      - Midline: path of ρ's center
      - Upper/lower wake: tiles displaced above/below midline
   
3. Wake enforcement:
   - If ρ₁ migrates before ρ₂, and ρ₂ starts above ρ₁'s midline,
     then ρ₂ cannot cross below the midline
   - This preserves relative positions needed for LR tableau
```

#### Step 5: Extract LR Tableau

```
Algorithm: Read tableau from migrated flock
1. Flock F' in nest B has rhombi with values
2. These form an LR tableau of shape λ/μ where:
   - λ corresponds to boundary at B (nest shape)
   - μ corresponds