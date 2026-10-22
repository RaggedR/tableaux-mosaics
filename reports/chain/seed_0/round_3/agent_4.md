## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

I'll build on the previous researcher's corrections and provide a complete, implementable specification.

### Key Insights from Previous Work

The previous researcher correctly identified crucial misconceptions:
1. The puzzle-to-mosaic conversion is a **deformation**, not direct mapping
2. Mosaic rhombi come from **boundary data**, not puzzle pieces
3. Standard order with orientation (-E_A, -N_A) goes **west** and **south**

However, their report has gaps in the migration algorithm and lacks concrete examples. I'll complete these details.

### Data Structures

```
Puzzle:
  - size: n
  - tiles: Dict[(i,j) -> (type, edge_labels)]
  - type: 'triangle' | 'rhombus'
  - edge_labels: Dict[direction -> 0/1]

Mosaic:
  - hexagon_tiles: Dict[(x,y) -> ('triangle' | 'square' | 'empty')]
  - nest_rhombi: {A: List[Rhombus], B: List[Rhombus], C: List[Rhombus]}
  - Rhombus: (position, id)

Flock:
  - rhombi: List[Rhombus]
  - orientation: (E, N) unit vectors
  - tableau_values: Dict[rhombus_id -> int]
```

### Algorithm Steps

#### Step 1: Puzzle to Mosaic

1. **Extract boundary strings**: Read edges clockwise starting from corners:
   - π: bottom edge (left to right)
   - ρ: right edge (bottom to top)
   - σ: left edge (top to bottom)

2. **Deform puzzle to hexagon**:
   - Create hexagon A'AB'BC'C with |A'A|=|B'B|=|C'C|=d, |AB'|=|BC'|=|CA'|=n-d
   - Each puzzle triangle → mosaic triangle (preserving relative positions)
   - Each puzzle rhombus → empty space in mosaic
   - Fill gaps with squares to complete tiling

3. **Place boundary rhombi in nests**:
   - For string π with 1s at positions k₁,...,k_d:
     - Place rhombus i at coordinate (d-i, k_i-i) relative to nest A's corner
   - Similar placement for ρ→B and σ→C using rotated coordinates

#### Step 2: Create Initial Flock

With orientation (-E_A, -N_A) on nest A:
- E_A points from A toward A' (northeast)
- -E_A points southwest, -N_A points southeast

**Standard order**: For rhombi r₁=(x₁,y₁) and r₂=(x₂,y₂):
- r₁ < r₂ if y₁ > y₂ (further south)
- r₁ < r₂ if y₁ = y₂ and x₁ < x₂ (further west)

**Assign tableau values**:
```
Sort rhombi by standard order
current_row = 1
for i = 0 to d-1:
  tableau[rhombi[i]] = current_row
  if i+1 < d and rhombi[i+1] is in a different row:
    current_row += 1
```

#### Step 3: Migration (South from A to B)

Process rhombi in **reverse standard order** (largest to smallest):

```
for each rhombus ρ from largest to smallest:
  while ρ not in nest B:
    1. Find minimal hexagon H containing ρ and extending rightward
    2. Determine hexagon type:
       - Type A: 2-fold rotational symmetry → rotate 180°
       - Type B: 3-fold rotational symmetry → rotate 120°
         (choose rotation making ρ's edge horizontal/vertical)
    3. Update mosaic tiles and ρ's position
```

**Wake preservation**: The algorithm maintains that each rhombus's "wake" (path of disturbed tiles) doesn't interfere with previously moved rh