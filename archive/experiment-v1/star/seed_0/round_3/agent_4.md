# Computational Mathematics Report: Mosaic Migration Implementation

## Critical Implementation Details

### 1. Coordinate System Precision

The axial coordinate system is correct, but for implementation efficiency:

```
Coordinate operations:
- distance(p1, p2) = (|q1-q2| + |q1+r1-q2-r2| + |r1-r2|) / 2
- rotate_60_ccw(q, r) = (-r, q+r)
- rotate_60_cw(q, r) = (-q-r, q)
```

### 2. Hexagon Construction Algorithm

```
function create_hexagon(n, d):
  // Vertices in CCW order from top-left
  A' = (0, 0)
  A = (d, 0)
  B' = (n, 0)
  B = (n, d)
  C' = (n, n)
  C = (n-d, n)
  
  mosaic = empty_map()
  
  // Fill hexagon with triangles
  for q in 0..n:
    for r in 0..n:
      if inside_hexagon(q, r, vertices):
        mosaic[(q,r)] = Triangle(orientation=0)
  
  // Define nest regions
  nest_A = {(q,r) | 0 ≤ q ≤ d, 0 ≤ r ≤ d, q+r ≤ d}
  nest_B = {(q,r) | n-d ≤ q ≤ n, 0 ≤ r ≤ d}
  nest_C = {(q,r) | n-d ≤ q ≤ n, n-d ≤ r ≤ n, q+r ≥ 2n-d}
  
  return mosaic
```

### 3. Puzzle Transformation Details

The deformation from puzzle to mosaic is non-trivial. Given puzzle coordinates (i,j) in the triangle:

```
function deform_puzzle_to_mosaic(i, j, edge_label):
  // Map based on which edges have 1s
  // This stretches the puzzle to fit the hexagon
  
  // Count 1s before position on each boundary
  π_ones = count_ones_before(π, i)
  ρ_ones = count_ones_before(ρ, j) 
  σ_ones = count_ones_before(σ, n-i-j)
  
  // Linear interpolation
  q = i + (π_ones * d) / total_ones
  r = j + (ρ_ones * d) / total_ones
  
  return (q, r)
```

### 4. Migration Algorithm - Critical Details

The migration must process rhombi in specific order:

```
function migrate_flock(mosaic, source_nest, target_nest, direction):
  rhombi = get_rhombi_in_nest(mosaic, source_nest)
  
  // Sort by standard order
  if direction in [NORTH, EAST]:
    rhombi.sort(key = lambda r: (-r.label, r.position), reverse=True)
  else:  // SOUTH, WEST
    rhombi.sort(key = lambda r: (r.label, r.position))
  
  for rhombus in rhombi:
    while rhombus.nest != target_nest:
      migrate_single_step(mosaic, rhombus, direction)
```

### 5. Hexagon Flip Implementation

```
function migrate_single_step(mosaic, rhombus, direction):
  // Find minimal hexagon to the right (in migration direction)
  hex_center = find_minimal_hexagon(rhombus.position, direction)
  
  tiles = get_hexagon_tiles(mosaic, hex_center)
  
  if is_type_a_hexagon(tiles):  // 2-fold symmetry
    rotate_hexagon_180(mosaic, hex_center)
  else:  // type b, 3-fold symmetry
    // Rotate 120° to make