# Specialist Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Implementation Details

### 1. **Coordinate System Conversion**
The synthesis correctly identifies the need for coordinate conversion. Here's the precise mapping:

**Puzzle coordinates** (i,j,k) with i+j+k=n map to **hexagonal/axial coordinates** (q,r):
```
q = j - k
r = i
```

This places:
- Origin at hexagon center
- Nest A at approximately (-n/2, 0)
- Nest B at approximately (n/2, 0)  
- Nest C at approximately (0, n)

### 2. **Nest Placement Rules**
The synthesis oversimplifies. The correct rule from Purbhoo:

For puzzle rhombus at (i,j,k):
- **Type 0** (both edges 0): Becomes square in mosaic
- **Type 1** (north edge 1): Place in nest B
- **Type 10** (west edge 1): Place in nest A
- **Type 11** (both edges 1): Becomes triangle in mosaic

The "which edge has label 1" determines nest placement, not just any edge.

### 3. **Flock Formation**
The canonical flock at nest A needs:
```
Flock {
  rhombi: α (all rhombi in nest A)
  orientation: (-E_A, -N_A)  // opposite of nest orientation
  labels: f where f(rhombus) = row_index_from_bottom
}
```

The label assignment must respect the partition structure. If α corresponds to partition (2,1), place rhombi in rows with 2 in bottom row, 1 in top row.

### 4. **Migration Algorithm Precision**

**Finding minimal hexagon**: Start from rhombus position (q,r), scan in migration direction:
```
For each position p in direction D from (q,r):
  Check if forms valid hexagon containing rhombus
  Return first valid hexagon found
```

**Rotation rules**:
- Type I (2-fold): Swap rhombi positions
- Type II (3-fold): Rotate 120° clockwise if it moves rhombus in migration direction

**Standard order during migration**:
```
Compare(rhombus1, rhombus2):
  if f(rhombus1) ≠ f(rhombus2):
    return f(rhombus1) > f(rhombus2)  // for north/east
  else:
    return west_position(rhombus1) < west_position(rhombus2)
```

### 5. **Wake Tracking**
Essential for correctness:
```
Wake {
  midline: Path<(q,r)>  // center path of displaced tiles
  upper: Set<(q,r)>     // tiles above midline
  lower: Set<(q,r)>     // tiles below midline
}
```

After each rhombus migrates, check that subsequent rhombi don't violate wake crossing rules.

### 6. **Test Case Verification**

For c^(3,2,1)_{(2,1),(2,1)} = 2:

**Puzzle 1**: Should have rhombi forming specific pattern that migrates to tableau:
```
3 3
2
```

**Puzzle 2**: Different rhombi pattern migrating to:
```
3 2
3
```

The migration must preserve these distinct outcomes.

## Implementation Risks

1. **Hexagon detection**: Must handle edge cases where hexagon extends beyond mosaic boundary
2. **Orientation tracking**: Each nest has 4 possible orientations; migration can rotate orientation
3. **Wake preservation**: Failing to track wakes correctly will produce invalid tableaux

## Algorithm Correctness Check

After migration, verify:
1. All rhombi reached target nest
2. Standard order preserved: if rhombus1 <_f rhombus2, then rhombus1' <_f' rhombus2'
3. Resulting arrangement forms valid skew shape
4. Labels satisfy LR conditions (weak increase in rows, strict in columns, ballot property)

This implementation requires ~500 lines of careful code with extensive validation. The wake preservation logic is particularly subtle and