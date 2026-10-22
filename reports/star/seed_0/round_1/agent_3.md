# Specialist Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Gaps in the Synthesis

The generalist's report misses several crucial implementation details that would block a coding agent:

### 1. **Concrete Puzzle-to-Mosaic Conversion**

The "pulling tight" metaphor is too vague. Here's the precise algorithm:

**Data structures needed:**
- Puzzle: 2D array where `puzzle[i][j]` = rhombus type at position `(i,j)` in triangular lattice
- Mosaic: 2D array on hexagonal lattice with entries in {TRIANGLE, SQUARE, RHOMBUS_A, RHOMBUS_B, RHOMBUS_C}

**Conversion algorithm:**
```
1. Initialize hexagon of size d × (n-d) × d × (n-d) × d × (n-d)
2. For each puzzle rhombus at position (i,j):
   - If type 10: place rhombus in nest A at position (i, n-d-j)
   - If type 01: place rhombus in nest B at position (n-d-i, j)  
   - If type 11: place rhombus in nest C at position (j, i)
3. Fill remaining cells with squares/triangles using deterministic rules
```

### 2. **Precise Migration Mechanics**

The report lacks the actual hexagon configurations and rotation rules:

**Hexagon types (up to rotation/reflection):**
- Type 1: Contains 1 rhombus + 2 triangles + 3 squares
- Type 2: Contains 1 rhombus + 4 triangles + 1 square

**Rotation rules:**
- Type 1: Always rotate 180°
- Type 2: Rotate 120° clockwise if rhombus has horizontal edge, counterclockwise if vertical

### 3. **Standard Order Definition**

The report mentions "standard order" without defining it. From Purbhoo:

For rhombi with labels f(r₁) and f(r₂):
- r₁ <_f r₂ if f(r₁) < f(r₂)
- If f(r₁) = f(r₂), then r₁ <_f r₂ if r₁ is west/northwest of r₂

### 4. **Flock Construction**

Missing details on initial flock formation:
1. Assign orientation (-E_A, -N_A) to nest A
2. Label rhombi by unique function f making accessible flock
3. For nest A with standard orientation, f assigns label k to the k-th rhombus in reading order

### 5. **Wake Tracking Algorithm**

The "wake" concept needs explicit tracking:
```
For each migrating rhombus r:
  wake[r] = list of tiles displaced during r's journey
  upper_wake[r] = tiles above midline of path
  lower_wake[r] = tiles below midline of path
```

## Corrected Test Case Walkthrough

For c^(3,2,1)_{(2,1),(2,1)} = 2:

**Puzzle 1**: 
- Boundary: (110100, 110100, 001011)
- Contains rhombi at positions forming specific pattern
- Converts to mosaic with rhombi distributed in three nests

**Migration sequence**:
1. Form flock on nest A with rhombi labeled 1,2,3
2. Migrate in order: rhombus 3 first (maximal in standard order)
3. Each rhombus follows specific path of hexagon rotations
4. Result: rhombi in nest B form shape (3,2,1)/(2,1)
5. Labels give tableau entries

## Implementation Recommendations

1. **Use integer coordinates**: Represent hexagonal grid using axial coordinates (q,r)
2. **Precompute hexagon patterns**: Store all 12 possible hexagon configurations
3. **Track transformations**: Maintain transformation matrix for each rhombus's journey
4. **Validate invariants**: Check wake non-crossing after each migration step

## Corrected Algorithm Outline

```
function puzzle_to_tableau(puzzle):
    mosaic = puzzle_to