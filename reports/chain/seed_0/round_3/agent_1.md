## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

I'll build on the previous researcher's work, fixing critical errors and filling gaps for a complete implementation.

### Key Corrections to Previous Report

1. **Hexagon Coordinates Error**: The mapping formula is incorrect. In a mosaic, rhombi occupy specific positions based on the puzzle-to-mosaic bijection, not arbitrary interpolations.

2. **Migration Direction**: The previous report misses that migration from A to B goes *south* (not east), per Corollary 3.2's proof.

3. **Flock Creation**: The orientation (-E_A, -N_A) is correct, but the sorting description is backwards.

### Complete Implementation Guide

#### Data Structures

```
Puzzle: 
  - pieces: Dict[(i,j,k) -> {edges: {dir -> 0/1}}]
  - size: n (side length)

Mosaic:
  - hexagon: vertices as given
  - tiles: Dict[center_point -> {type: 'triangle'|'rhombus', orientation}]
  - rhombi_by_nest: {A: [], B: [], C: []}

Rhombus:
  - id: unique identifier
  - center: (x, y) position
  - nest: 'A'|'B'|'C'
  - tableau_value: integer (assigned during flock creation)
```

#### Step 1: Puzzle to Mosaic

The bijection works by "pulling apart" the puzzle:

```
1. Initialize empty mosaic hexagon
2. For each puzzle piece at (i,j,k):
   a. If triangle: place in corresponding mosaic position
   b. If rhombus: 
      - Track which edges have 0s (these edges align with nest directions)
      - Determine target nest based on edge alignments
      - Add to appropriate rhombi_by_nest list
3. Fill remaining hexagon space with triangles
```

**Key insight**: A rhombus goes to nest A if its 0-edges align with directions A-A' and A-B' after straightening.

#### Step 2: Create Canonical Flock

```
For rhombi α in nest A:
1. Give orientation (-E_A, -N_A) where:
   - E_A = unit vector from A toward A'
   - N_A = unit vector from A toward B'
   
2. Sort rhombi by standard order in this orientation:
   - Primary: position along N_A (increasing)
   - Secondary: position along E_A (decreasing, since orientation is reversed)
   
3. Assign tableau values:
   row = 1
   for each rhombus ρ in sorted order:
     ρ.tableau_value = row
     if next rhombus is strictly north of ρ:
       row += 1
```

#### Step 3: Migration (South from A to B)

```
For each rhombus ρ in standard order:
  while ρ.nest != 'B':
    1. Find minimal hexagon H containing ρ:
       - Search in direction approximately 240° from north
       - H is the first complete hexagon of tiles encountered
       
    2. Identify hexagon type and rotate:
       if H has 2-fold symmetry (type A):
         rotate_180(H)
       else: # 3-fold symmetry (type B)
         # Rotate ±120° so an edge of ρ becomes axis-aligned
         if ρ needs to go more south: rotate_120_ccw(H)
         else: rotate_120_cw(H)
         
    3. Update ρ.center and check if now in nest B
    
    4. Track wakes for order preservation:
       - upper_wake[ρ] = tiles north of ρ's path
       - lower_wake[ρ] = tiles south of ρ's path
```

#### Step 4: Read LR Tableau

```
1. Rhombi in nest B form shape λ/μ where:
   - λ corresponds to original nest C boundary
   - μ corresponds to final nest A contents
   
2. Create tableau:
   for each rhombus ρ in nest B: