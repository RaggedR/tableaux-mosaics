## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

I'll complete and correct the previous researcher's work, providing a fully implementable specification.

### Critical Corrections

The previous researcher made progress but has several errors:
1. **Boundary reading is wrong**: π, ρ, σ should be read clockwise from lower-left, not from arbitrary corners
2. **Rhombus placement formula is incorrect**: The coordinate (d-i, k_i-i) doesn't properly embed partitions
3. **Migration details are incomplete**: Missing crucial hexagon identification rules

### Complete Data Structures

```
Puzzle:
  - triangular grid coordinates: (i,j,k) where i+j+k=n
  - tiles: Dict[(i,j,k) -> PuzzlePiece]
  - PuzzlePiece: edges dict with 0/1 labels

Mosaic:
  - hexagon vertices: A'(0,0), A(0,d), B'(n-d,d), B(n,d), C'(n,0), C(n-d,0)
  - tiles: Dict[(x,y) -> 'triangle'|'square'|'rhombus']
  - rhombi_by_nest: {A: set, B: set, C: set}

Rhombus:
  - center: (x,y)
  - nest: 'A'|'B'|'C'
  - orientation: angle in {0°, 60°, 120°}
```

### Step 1: Puzzle to Mosaic (Corrected)

1. **Read boundary strings correctly**:
   - Start at lower-left vertex
   - π: left-to-right along bottom
   - ρ: bottom-to-top along right  
   - σ: top-to-bottom along left (reversed!)
   - Each 0 = step along edge, 1 = step perpendicular

2. **Convert strings to partitions**:
   - For string with 1s at positions i₁ < i₂ < ... < i_d:
   - Partition λ = (i_d-d, i_{d-1}-(d-1), ..., i_1-1)

3. **Place rhombi in nests**:
   - Nest A gets partition from π
   - Nest B gets partition from ρ  
   - Nest C gets complement of partition from σ
   - Stack rhombi in rows according to partition

### Step 2: Create Flock with Correct Orientation

For orientation (-E_A, -N_A) at nest A:
- E_A = (1, 0) pointing from A to A'
- N_A = (1/2, √3/2) pointing from A to B'
- So -E_A = (-1, 0) and -N_A = (-1/2, -√3/2)

**Standard order**: Rhombus r₁ < r₂ if:
1. r₁ is more west (smaller x-coordinate in rotated frame)
2. If same x, then r₁ is more south (smaller y-coordinate in rotated frame)

**Tableau assignment**:
```
Sort rhombi in nest A by standard order
Assign values row by row (bottom to top):
- All rhombi in bottom row get value 1
- Next row gets value 2, etc.
```

### Step 3: Migration Algorithm (Complete)

**Key insight**: We migrate rhombi one at a time from largest to smallest in standard order.

```
For each rhombus ρ (largest to smallest):
  While ρ not in target nest B:
    1. Find minimal hexagon containing ρ:
       - Must contain ρ's center
       - Extends rightward (in migration direction = south)
       - Has vertices from {triangles, squares, rhombi centers}
    
    2. Identify hexagon configuration:
       - Count rhombi: 1 (type A) or 0 (type B)
       - Type A: 180° rotation around hexagon center
       - Type B: 120° rotation, choosing direction that makes
                 one edge of ρ align with hexagon edge
    
    