# Specialist Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Gaps in the Synthesis

The synthesis provides a good framework but misses crucial implementation details. Let me fill these gaps with concrete specifications.

## Precise Coordinate Systems and Conversions

### Puzzle Coordinates
Use barycentric coordinates (i,j,k) where i+j+k=n:
- i = distance from right edge
- j = distance from bottom edge  
- k = distance from left edge

Each rhombus has three vertices; use the centroid coordinates.

### Mosaic Hexagon Layout
The hexagon has vertices at:
- A' = (0, 0)
- A = (d, 0)
- B' = (d+n-d, 0) = (n, 0)
- B = (n+d·cos(30°), d·sin(30°))
- C' = (n-d+d·cos(150°), (n-d)·sin(60°)+d·sin(30°))
- C = ((n-d)·cos(60°), (n-d)·sin(60°))

### Nest Placement Rules
For puzzle rhombus with edges labeled (e_bottom, e_left, e_right):
```
if e_bottom == 1:
    place rhombus in nest C at position based on (i,j,k)
elif e_left == 1:
    place rhombus in nest A at position based on (i,j,k)
elif e_right == 1:
    place rhombus in nest B at position based on (i,j,k)
else:
    # All edges 0 - this rhombus becomes squares/triangles
```

## Migration Algorithm Details

### Standard Order Definition
For rhombi with labels f(r₁), f(r₂):
1. If f(r₁) < f(r₂), then r₁ <_f r₂
2. If f(r₁) = f(r₂) and r₁ is west of r₂, then r₁ <_f r₂

### Hexagon Finding Algorithm
```
find_minimal_hexagon(rhombus_pos):
    # Start from rhombus center
    # Search in migration direction for tiles forming hexagon
    # Key: hexagon must be entirely "weakly right" of leftmost rhombus point
    
    if migration_direction in [north, east]:
        search_vector = migration_direction
    else:
        search_vector = -migration_direction
    
    # Find 6 tiles forming hexagon boundary
    # Check tile types to determine Type I or II
```

### Rotation Rules
**Type I (2-fold symmetry):**
- Always rotate 180°
- Swaps rhombi positions

**Type II (3-fold symmetry):**
- Rotate 120° such that one rhombus edge becomes horizontal or vertical
- This uniquely determines rotation direction

## Wake Tracking Implementation

```
Wake {
    midline: List<Edge>  // sequence of tile edges
    upper_tiles: Set<TilePos>
    lower_tiles: Set<TilePos>
}

track_wake(rhombus_journey):
    wake = new Wake()
    for each hexagon rotation in journey:
        displaced_tiles = get_displaced_tiles(rotation)
        classify_tiles_relative_to_midline(displaced_tiles, wake)
    return wake
```

## Canonical Flock Construction

For nest A with rhombi α:
1. Use orientation (-E_A, -N_A) for migration A→B
2. Assign labels f: α → {1,...,d} such that:
   - Each value 1,...,d appears exactly once
   - Labels increase from southwest to northeast in nest
   - This matches the content ν of the target tableau

## Test Case Verification

For c^(3,2,1)_{(2,1),(2,1)} = 2:

**Puzzle 1**: Should produce tableau with entries arranged as:
```
  2
1 2
```

**Puzzle 2**: Should produce tableau with entries arranged as:
```
  1
2 2
```

The migration must preserve these distinct configurations through wake preservation.

## Critical