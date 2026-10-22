## Analysis and Complete Implementation Report for Purbhoo's Mosaic Migration Bijection

The previous report has the right overall structure but contains critical gaps and some conceptual errors. Here's my complete specification:

### Data Structures

```
Puzzle: {
  size: n,
  pieces: Array<{
    row: int, col: int,  // triangular lattice coordinates
    type: '0-triangle' | '1-triangle' | '0-rhombus' | '1-rhombus' | '10-rhombus',
    orientation: 0 | 60 | 120 | 180 | 240 | 300  // degrees
  }>
}

Mosaic: {
  hexagon: {
    vertices: {A', A, B', B, C', C},  // with coordinates
    d: int,  // number of 1s per boundary
    n: int   // puzzle size
  },
  tiles: Map<(x,y) → {
    type: 'triangle' | 'square' | 'rhombus',
    orientation: angle
  }>,
  nests: {
    A: Set<Rhombus>,  // rhombi at corner A
    B: Set<Rhombus>,  // rhombi at corner B
    C: Set<Rhombus>   // rhombi at corner C
  }
}

Rhombus: {
  id: int,  // unique identifier
  position: (x, y),
  orientation: angle
}

Flock: {
  rhombi: Array<Rhombus>,  // ordered by standard order
  orientation: (E, N),      // basis vectors
  tableau: Map<rhombus_id → int>  // LR tableau entries
}
```

### Step 1: Puzzle to Mosaic Conversion

The key insight from Purbhoo: puzzles are projections of piecewise linear surfaces, and the transformation "straightens" the puzzle boundary into a hexagon.

```
Algorithm: ConvertPuzzleToMosaic
Input: Puzzle of size n
Output: Mosaic

1. Count d = number of 1s on any boundary edge

2. Create hexagon vertices:
   - Place A', B', C' at corners of equilateral triangle
   - Extend by distance d to get A, B, C
   - Angles at A, B, C are 150°; at A', B', C' are 90°

3. For each puzzle piece at triangular coordinates (i, j):
   a. Apply transformation that maps:
      - Lower-left puzzle corner → A'
      - Lower-right puzzle corner → B'
      - Top puzzle corner → C'
   
   b. Transform pieces:
      - 0-triangle → equilateral triangle
      - 1-triangle → unit square
      - Rhombus with two 0-edges → stays inside hexagon
      - Rhombus with two 1-edges → becomes 150°/30° rhombus in a nest
      - Rhombus with one 0 and one 1 edge → split into triangle + square

4. Pack boundary rhombi into nests based on which puzzle edges they touched
```

### Step 2: Flock Creation

```
Algorithm: CreateInitialFlock
Input: Rhombi in nest A from partition π
Output: Flock F ready for migration

1. Convert 01-string π to partition λ:
   - Start at origin, go right on 0, up on 1
   - Partition parts λᵢ = horizontal distance at height i

2. Arrange rhombi in standard tableau shape:
   - Row i (from bottom) has λᵢ rhombi
   - Left-justify all rows

3. Set orientation (-E_A, -N_A) where:
   - E_A = unit vector from A toward A'
   - N_A = unit vector from A toward B'
   - This makes the flock "face northeast" for southward migration

4. Assign tableau values:
   - All rhombi get value 1 (for initial flock)
   - Order rhombi by standard order: west-to-east, then south-to-north
```

### Step 3: Migration Algorithm

```
Algorithm: MigrateFlock