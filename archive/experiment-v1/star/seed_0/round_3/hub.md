# Unified Implementation Report: Purbhoo's Mosaic Migration Bijection

## Overview

The mosaic migration bijection converts KTW puzzles to Littlewood-Richardson (LR) tableaux through three phases:
1. **Puzzle → Mosaic**: Transform the triangular puzzle into a hexagonal tiling
2. **Migration**: Move rhombi through the mosaic via local hexagon flips
3. **Reading**: Extract the LR tableau from the final configuration

## Core Data Structures

### Coordinate System
Use axial hexagonal coordinates (q,r) with implicit s = -(q+r):
```
Coordinate: (q: int, r: int)
Direction: enum {E=0, NE=1, NW=2, W=3, SW=4, SE=5}
neighbors(q,r) = [(q+1,r), (q+1,r-1), (q,r-1), (q-1,r), (q-1,r+1), (q,r+1)]
```

### Mosaic Structure
```
Mosaic: {
  tiles: Map<Coordinate → Tile>,
  nests: {A: Set<Coordinate>, B: Set<Coordinate>, C: Set<Coordinate>},
  dimensions: {n: int, d: int}  // n = puzzle size, d = #1s in boundary
}

Tile: {
  type: TRIANGLE | SQUARE | RHOMBUS,
  orientation: 0..5,  // multiples of 60°
  rhombus_id: int | null
}

Rhombus: {
  id: int,
  position: Coordinate,
  label: int,  // tableau entry (1 to d)
  nest: A | B | C,
  orientation: (E: Direction, N: Direction)  // basis vectors
}
```

## Phase 1: Puzzle to Mosaic Conversion

### Algorithm
```
function puzzle_to_mosaic(puzzle):
  // 1. Parse boundary strings
  (π, ρ, σ) = extract_boundaries(puzzle)
  d = count_ones(π)  // same as count_ones(ρ) and count_ones(σ)
  
  // 2. Create hexagon frame
  mosaic = create_hexagon(n, d)
  
  // 3. Transform puzzle interior
  for each piece in puzzle:
    if piece is unit_triangle:
      place_triangle(mosaic, deform(piece.position))
    else:  // piece is 30°-60° rhombus
      // Replace with square in mosaic
      place_square(mosaic, deform(piece.position))
  
  // 4. Pack rhombi into nests based on boundaries
  pack_nest_A(mosaic, π)  // northwest corner
  pack_nest_B(mosaic, ρ)  // east corner
  pack_nest_C(mosaic, σ)  // southwest corner
  
  return mosaic
```

### Nest Packing
Each boundary string determines rhombus placement:
```
function pack_nest_A(mosaic, π):
  row = 0
  for i in 0..len(π)-1:
    if π[i] == '1':
      // Place rhombus in nest A at position determined by row
      pos = nest_A_corner + row * E_A + (count_ones(π[0:i]) - row) * N_A
      place_rhombus(mosaic, pos, nest=A)
      if i+1 < len(π) and π[i+1] == '0':
        row++
```

## Phase 2: Migration Algorithm

### Flock Creation and Labeling
```
function create_flock(mosaic, nest, orientation):
  rhombi = get_rhombi_in_nest(mosaic, nest)
  
  // Group rhombi by rows (perpendicular to E direction)
  rows = group_by_row(rhombi, orientation.E)
  
  // Label: same within row, increasing north
  label = 1
  for row in rows (sorted south to north):
    for rhombus in row:
      rhombus.label = label