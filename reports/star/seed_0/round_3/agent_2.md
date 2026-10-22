# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Overview

The mosaic migration bijection converts KTW puzzles to LR tableaux through three stages:
1. Puzzle → Mosaic conversion
2. Migration algorithm
3. Tableau extraction

I'll build on the generalist's synthesis, correcting errors and providing concrete implementation details.

## Stage 1: Puzzle to Mosaic Conversion

The generalist misunderstands the puzzle-to-mosaic mapping. Here's the correct interpretation:

**Data Structures:**
```
PuzzleRhombus = {
  position: (i,j,k),  # triangular coords
  labels: {NW: 0/1, NE: 0/1, E: 0/1, SE: 0/1, SW: 0/1, W: 0/1}
}

MosaicTile = {
  type: TRIANGLE | SQUARE | RHOMBUS,
  position: (x,y),    # 2D coords
  nest: A | B | C | NONE  # for rhombi only
}
```

**Conversion Algorithm:**
The "pulling tight" operation transforms the puzzle geometrically:

1. Each puzzle rhombus becomes either a square OR a mosaic rhombus
2. Edge labels determine the transformation:
   - If opposite edges differ (0-1 pattern): → mosaic rhombus
   - If all edges match locally: → square
3. Triangular pieces remain triangular

**Concrete Mapping:**
```
def puzzle_to_mosaic(puzzle):
  # Setup hexagon with angles 150° at A,B,C and 90° at A',B',C'
  mosaic = create_hexagon(n, d)
  
  for piece in puzzle.pieces:
    if piece.type == TRIANGLE:
      mosaic.add_triangle(transform_position(piece.pos))
    else:  # rhombus
      # Check label pattern
      if creates_strain(piece):
        # Place rhombus in appropriate nest based on orientation
        nest = determine_nest(piece.orientation)
        mosaic.add_rhombus(transform_position(piece.pos), nest)
      else:
        mosaic.add_square(transform_position(piece.pos))
        
  return mosaic
```

## Stage 2: Migration Algorithm

**Key Data Structures:**
```
Flock = {
  rhombi: set[MosaicRhombus],
  orientation: (E, N),  # basis vectors
  f: dict[rhombus → int]  # labeling function
}

StandardOrder = {
  # For rhombi r1, r2: r1 <_f r2 if:
  # 1. f(r1) < f(r2), OR
  # 2. f(r1) = f(r2) AND r1 is west of r2
}
```

**Migration Steps:**

1. **Create canonical flock at nest A:**
```
def create_canonical_flock(alpha, orientation=(-E_A, -N_A)):
  # Alpha is the collection of rhombi at nest A
  # Sort rhombi by reading order in the given orientation
  sorted_rhombi = sort_by_position(alpha, orientation)
  
  # Assign f-values to make valid LR tableau
  f = {}
  label = 1
  for rhombus in sorted_rhombi:
    f[rhombus] = label
    # Increment label based on tableau rules
    if should_increment(rhombus, sorted_rhombi):
      label += 1
      
  return Flock(alpha, orientation, f)
```

2. **Migration from A to B:**
```
def migrate(flock, source=A, target=B):
  direction = SOUTH  # for A→B migration
  
  # Process in reverse standard order for south migration
  ordered_rhombi = sort_standard_order(flock, reverse=True)
  
  for rhombus in ordered_rhombi:
    while rhombus.nest != target:
      # Find minimal hexagon to rhombus's right
      hex = find_minimal_hexagon(rhombus, direction)
      