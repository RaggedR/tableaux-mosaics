# Specialist Report: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Gaps and Corrections

The generalist's report misses several crucial implementation details. Here's what a coding agent actually needs:

### 1. Puzzle-to-Mosaic Conversion: The Real Algorithm

The "pulling tight" metaphor is too vague. Here's the precise transformation:

**Coordinate Systems**:
- Puzzle: Triangular lattice with vertices at positions (i,j) where 0 ≤ i,j ≤ n-i
- Mosaic: Hexagonal grid embedded in plane with three nests at vertices A, B, C

**Conversion Algorithm**:
1. Map puzzle vertices to mosaic vertices via affine transformation:
   - Southwest corner → A'
   - Southeast corner → B' 
   - North corner → C'
   
2. For each puzzle rhombus at position (i,j):
   - Read its type from edge labels (0→white, 1→black edges)
   - If northwest edge is black: place rhombus in nest A
   - If northeast edge is black: place rhombus in nest B
   - If south edge is black: place rhombus in nest C
   
3. Fill remaining hexagon with squares and triangles following the tiling rules

**Data Structure**: 
```
Mosaic {
  tiles: Map<(x,y), TileType>  // TileType = Triangle|Square|Rhombus
  rhombi_in_nest: Map<Nest, Set<(x,y)>>
  rhombus_labels: Map<(x,y), Integer>  // for tableau entries
}
```

### 2. Migration Algorithm: Precise Implementation

**Flock Formation**:
- A flock is NOT just "rhombi in a nest" - it requires specific orientation
- Orientation determines which rhombi are "accessible" (can migrate)
- For migration from A to B, use orientation (-E_A, -N_A) where E_A, N_A are the edge vectors of nest A

**Standard Order** (critical!):
For rhombi in a flock with content k:
1. Primary sort: by entry value k (ascending for north/east migration, descending for south/west)
2. Secondary sort: within same entry, by position (west to east, then south to north)

**Hexagon Rotation Details**:
The two hexagon types have specific configurations:
- Type (a): Contains 2 triangles, 2 squares, 2 rhombi in alternating pattern
- Type (b): Contains 3 triangles, 3 rhombi in alternating pattern

For type (b), the 120° rotation direction is determined by ensuring the migrating rhombus's edge becomes axis-aligned (parallel to nest edges).

### 3. Wake Preservation (Missing from Generalist Report)

This is CRUCIAL for correctness:

**Wake Tracking**:
```
Wake {
  upper_path: List<(x,y)>  // tiles above midline
  lower_path: List<(x,y)>  // tiles below midline
  midline: List<(x,y)>     // edge between upper/lower
}
```

**Wake Rules**:
- When rhombus ℓ migrates, it creates a wake
- Later rhombi must respect existing wakes
- If rhombus starts above a wake's midline, it stays above throughout migration
- This preserves the relative order needed for valid LR tableaux

### 4. Test Case Clarification

For c^(3,2,1)_{(2,1),(2,1)}, the two puzzles have boundaries:
- Puzzle 1: Creates tableau with entries in specific positions
- Puzzle 2: Creates tableau with different entry positions

The mosaic intermediate will show:
- 3 rhombi in nest A (from puzzle rhombi with south edge = 1)
- Different distributions in nests B and C for each puzzle

### 5. Implementation Pitfalls

1. **Orientation Confusion**: The paper uses four possible orientations per nest. For A→B migration specifically, use (-E_A, -N_A), not the standard orientation.

2. **Accessible vs All Rhombi**: Only rhombi forming a "straight shape" from the nest