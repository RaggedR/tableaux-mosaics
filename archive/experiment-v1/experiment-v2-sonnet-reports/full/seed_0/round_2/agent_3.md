# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Core Analysis

The previous reports correctly identify the three-phase structure but miss critical implementation details. After analyzing Purbhoo's construction, I can provide concrete specifications for a coding agent.

## Data Structures

### Coordinate System
Use **hexagonal coordinates** (q, r) where:
- q-axis points east (0°)
- r-axis points northeast (60°)
- Each unit has side length 1

### Puzzle Representation
```
PuzzleType {
  size: n (triangle side length)
  pieces: Map[(q,r) -> PieceType]
  boundary: (π, ρ, σ) // three 01-strings of length n
}

PieceType {
  RHOMBUS_A: edges (0,1,0) 
  RHOMBUS_B: edges (1,0,1)
  // 6 orientations each via 60° rotations
}
```

### Mosaic Representation  
```
MosaicType {
  hexagon: vertices A'AB'BC'C in hexagonal coordinates
  tiles: Map[(q,r) -> TileType]
  nests: {A: Collection<Rhombus>, B: Collection<Rhombus>, C: Collection<Rhombus>}
}

TileType {
  TRIANGLE, SQUARE, RHOMBUS_30_150
}

FlockType {
  rhombi: List<(q,r)> // positions in standard order
  orientation: (E, N) // unit vectors  
  tableau: Map[(q,r) -> Int] // LR tableau entries
}
```

## Phase 1: Puzzle → Mosaic Conversion

**Key Insight**: The transformation is an affine map that "untangles" the puzzle geometry.

### Algorithm
1. **Initialize hexagonal region**: Create hexagon A'AB'BC'C with:
   - Side lengths: A'A = B'B = C'C = d, AB' = BC' = CA' = n-d
   - Angles: 150° at A,B,C and 90° at A',B',C'

2. **Map puzzle pieces to mosaic tiles**:
   ```
   for each puzzle piece P at position (q,r):
     if P is RHOMBUS_A or RHOMBUS_B:
       add RHOMBUS_30_150 to appropriate nest based on position
     else:
       determine if position maps to TRIANGLE or SQUARE in mosaic
   ```

3. **Boundary correspondence**: The 01-strings (π,ρ,σ) correspond to the shapes left after removing nests α,β,γ. A '0' means horizontal step, '1' means vertical step when walking the boundary.

## Phase 2: Migration Algorithm

### Standard Order Definition
For rhombi with tableau entries f, define X <_f Y if:
- f(X) < f(Y), OR
- f(X) = f(Y) AND X is northwest of Y

### Core Migration Step
```
migrate_single_rhombus(rhombus, direction):
  while rhombus not in target_nest:
    hex = find_minimal_hexagon(rhombus, direction)
    if hex.has_2fold_symmetry():
      rotate_tiling_180(hex)
    else: // 3-fold symmetry
      rotate_tiling_120_to_horizontal_or_vertical(hex)
    rhombus = rhombus.new_position
```

### Find Minimal Hexagon
The "minimal hexagon containing ◊ to the right" is the smallest hexagonal region that:
1. Contains the rhombus ◊
2. Is entirely weakly east of ◊'s westernmost point
3. Has all 6 edges parallel to the fundamental directions

### Hexagon Types and Rotations
- **Type (a)**: Contains pattern with 2-fold rotational symmetry → apply 180° rotation
- **Type (b)**: Contains pattern with 3-fold rotational symmetry → apply 120° rotation such that some edge of the rhombus becomes horizontal or vertical

### Wake Preservation
The Wake Crossing Lemma ensures that if rhombi are processed in standard order:
- Upper