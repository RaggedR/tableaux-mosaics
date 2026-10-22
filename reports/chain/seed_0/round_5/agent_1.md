## Complete Implementation Report for Purbhoo's Mosaic Migration Bijection

Building on the previous report, I'll provide a complete, implementable specification with corrections and critical missing details.

### Data Structures

```
Puzzle: {
  cells: Array of {type: '0-triangle' | '1-triangle' | 'rhombus', edges: [0|1, 0|1, 0|1]}
  size: integer n
}

Mosaic: {
  tiles: Map<(x,y) → {type: 'triangle' | 'square' | 'rhombus', orientation: angle}>
  rhombi: Map<nestID → Array<{position: (x,y), value: integer}>>
  hexagon_bounds: {A': (x,y), A: (x,y), B': (x,y), B: (x,y), C': (x,y), C: (x,y)}
}

Flock: {
  rhombi: Array<{position: (x,y), value: integer}>
  orientation: {E: (dx,dy), N: (dx,dy)}
  nest: 'A' | 'B' | 'C'
}
```

### Step 1: Puzzle to Mosaic Conversion

**Key insight**: The "straightening" operation maps the equilateral triangle to a hexagon with 150° angles at A, B, C.

```
Algorithm: ConvertPuzzleToMosaic
1. Initialize hexagon with vertices:
   - A = (0, 0), A' = (-d, 0)
   - B = ((n-d)cos(30°), (n-d)sin(30°)), B' = (n-d, 0)
   - C = (n-d + d·cos(150°), d·sin(150°)), C' = (n-d, d)

2. For each puzzle cell at (row, col):
   - Map to mosaic position:
     x = col + row/2
     y = row * √3/2
   
3. Transform pieces:
   - 0-triangle → equilateral triangle
   - 1-triangle → square (was 30°/60° rhombus)
   - Rhombus with two 1-edges → extract to boundary
```

### Step 2: Boundary Data Processing

**Critical correction**: The previous report's partition conversion was wrong.

```
Algorithm: ProcessBoundaryData
Input: strings π, ρ, σ (length n each)

1. Convert to partitions:
   For string s = s₁...sₙ:
   - Count 1s from position i to n: cᵢ = |{j ≥ i : sⱼ = 1}|
   - Partition λ has λₖ = max{i : cᵢ ≥ k} - (n-d)
   
2. Place rhombi in nests:
   - Nest A gets partition from π
   - Nest B gets partition from ρ  
   - Nest C gets partition from σ
   
3. Standard placement:
   - Row k (from bottom) contains λₖ rhombi
   - Stack vertically with 150° angles meeting
```

### Step 3: Flock Initialization

**Key detail**: Orientation determines migration direction and tableau reading.

```
Algorithm: InitializeFlock
For migration A→B:
1. Set orientation (-E_A, -N_A) where:
   - E_A = (1, 0) (along AA' edge)
   - N_A = (cos(60°), sin(60°)) (along AB' edge)
   
2. Assign values by row number:
   - Bottom row rhombi get value 1
   - Next row gets value 2, etc.
   
3. Define standard order:
   - Primary: by assigned value
   - Secondary: west < east in oriented coordinates
   - Tertiary: south < north in oriented coordinates
```

### Step 4: Migration Algorithm

**Critical addition**: Concrete hexagon finding and rotation rules.

```
Algorithm: MigrateRhombus(ρ, direction)
1. Find minimal hexagon:
   - Start from rightmost vertex of 