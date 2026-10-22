## Analysis of Previous Report and Complete Implementation Specification

The previous researcher made a good start but left critical gaps. I'll build on their work and provide the complete, corrected specification.

### Critical Issues with Previous Report

1. **Incomplete extraction of LR tableau** - The report cuts off mid-sentence in Step 5
2. **Vague coordinate transformations** - No concrete formulas for puzzle→mosaic mapping
3. **Missing orientation tracking** - Doesn't explain how orientations rotate during migration
4. **Wake enforcement underspecified** - Needs concrete rules for hexagon selection

### Complete Algorithm Specification

#### Step 1: Puzzle to Mosaic (Precise Algorithm)

```
Data Structure:
- Puzzle: Array of triangular cells, each containing piece type and edge labels
- Coordinate system: (row, col) where row 0 is bottom, col increases rightward

Algorithm:
1. For each cell (r,c) in puzzle:
   - If contains 30°/150° rhombus with two 1-edges:
     * Record in boundary rhombi list
     * Mark cell as empty
   - Transform coordinates:
     * x = c - r/2
     * y = r * √3/2
     * This maps equilateral triangle to hexagon

2. Identify nests:
   - A: bottom-left corner (120° opening northeast)
   - B: top corner (120° opening southwest)  
   - C: bottom-right corner (120° opening northwest)
```

#### Step 2: Boundary Reading and Rhombi Placement

```
Algorithm: Place rhombi in nests from boundary data
Input: Boundary strings (π, ρ, σ) read clockwise from corners

1. For nest A (string π):
   - Convert π to partition λ:
     * Scan right-to-left, recording positions of 1s
     * λᵢ = (position of i-th 1 from right) - i
   - Place rhombi in rows:
     * Row k contains λₖ rhombi
     * Stack north with 30° angles touching

2. Orient nest A with (E_A, N_A) where:
   - E_A points along bottom edge (northeast)
   - N_A points along left edge (north)
   - Similar for nests B, C
```

#### Step 3: Flock Creation for Migration

```
Algorithm: Create migratable flock
1. For migration A→B, use orientation (-E_A, -N_A) on rhombi in A
   - This makes rhombi "face" the correct direction for migration

2. Assign tableau values:
   - Order rhombi by standard order in chosen orientation
   - Standard order: compare by (f(X), position) where:
     * f(X) = assigned value
     * Position: west < east, south < north in oriented coordinates
   - Assign f(X) = row number (1 for bottom row, 2 for next, etc.)
```

#### Step 4: Migration Algorithm (Complete)

```
Algorithm: Migrate rhombus ρ
1. Find minimal hexagon:
   - Scan rightward from ρ's rightmost vertex
   - Find first hexagon H fully containing ρ on its boundary
   - H contains 2 triangles + 1 rhombus (2-fold) or 3 rhombi (3-fold)

2. Apply rotation:
   - 2-fold case: Rotate tiling of H by 180°
   - 3-fold case: Rotate 120° clockwise if ρ's top edge becomes horizontal,
                 else 120° counterclockwise

3. Wake tracking:
   - Upper wake: all tiles displaced above ρ's path
   - Lower wake: all tiles displaced below ρ's path
   - Wake Crossing Rule: If ρ₂ starts above midline of previously
     migrated ρ₁, then ρ₂ cannot cross below that midline
```

#### Step 5: Extract LR Tableau (Complete)

```
Algorithm: Read tableau from migrated flock
1. Flock F' now in nest B with standard orientation (E_B, N_B)
2. Rhombi positions form skew shape λ/μ where:
   - λ = partition