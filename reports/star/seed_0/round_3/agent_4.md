# Implementing Purbhoo's Mosaic Migration Bijection: Specialist Report

## Critical Corrections to the Synthesis

The synthesis contains several fundamental errors that must be corrected:

### 1. **Puzzle-to-Mosaic Conversion: Complete Misunderstanding**

The synthesis is wrong about removing rhombi. Here's what actually happens:

**Physical Process**:
- Keep ALL puzzle pieces in place
- Apply tension to corners A', B', C' pulling outward
- The triangular boundary becomes hexagonal
- 0-labeled edges rotate clockwise, 1-labeled edges rotate counterclockwise
- Unit rhombi (30°-60°-90°-120°) become unit squares
- Triangles remain triangles
- NO pieces are removed; NO holes are created

**Correct Implementation**:
```
For each puzzle piece at position (i,j,k):
  1. Compute deformed position in hexagon coordinates
  2. If piece is rhombus → becomes square in mosaic
  3. If piece is triangle → remains triangle
  
# The rhombi in nests A,B,C come from reading boundary labels:
nest_A_rhombi = positions where boundary string π has 1s
nest_B_rhombi = positions where boundary string ρ has 1s  
nest_C_rhombi = positions where boundary string σ has 1s
```

### 2. **Coordinate Transformation**

The deformation from triangle to hexagon requires careful coordinate mapping:

```
# Puzzle uses barycentric coordinates (i,j,k) with i+j+k=n
# Map to 2D hexagon coordinates:

def puzzle_to_mosaic_coords(i, j, k, n):
    # Linear interpolation based on which region of triangle
    # Maps vertices correctly: (n,0,0)→A', (0,n,0)→B', (0,0,n)→C'
    # Interior points map according to the stretching transformation
    
    # Key insight: the transformation preserves lines parallel to edges
    x = linear_combination_of_vertices_x(i/n, j/n, k/n)
    y = linear_combination_of_vertices_y(i/n, j/n, k/n)
    return (x, y)
```

### 3. **Flock Formation: Crucial Detail**

The synthesis misses that for migration from A to B, we need orientation (-E_A, -N_A) on the flock:

```
def create_canonical_flock(nest_A_rhombi, content_partition):
    # CRITICAL: Use orientation (-E_A, -N_A) for A→B migration
    # This means: E = southeast, N = west (rotated 180° from nest orientation)
    
    # Sort rhombi by position in this orientation
    # West-most rhombus gets lowest label
    sorted_rhombi = sort_by_position(nest_A_rhombi, 
                                   E=(-1,-1), N=(1,0))
    
    # Assign f-values according to content partition
    f = {}
    idx = 0
    for label, count in enumerate(content_partition, 1):
        for _ in range(count):
            f[sorted_rhombi[idx]] = label
            idx += 1
    
    return Flock(rhombi=nest_A_rhombi, orientation=(-E_A,-N_A), f=f)
```

### 4. **Migration Algorithm: Standard Order**

The synthesis doesn't define standard order properly:

```
def standard_order(rhombus1, rhombus2, flock):
    # Order by f-value first
    if flock.f[rhombus1] < flock.f[rhombus2]:
        return -1  # rhombus1 comes first
    elif flock.f[rhombus1] > flock.f[rhombus2]:
        return 1
    else:
        # Same f-value: order by position (west of = earlier)
        return position_order(rhombus1, rhombus2, flock.orientation)
```

### 5. **Hexagon Rotation Rules**

The synthesis doesn't specify which rotation to use: