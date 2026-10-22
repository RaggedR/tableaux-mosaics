## Specialist Report: Jeu de Taquin and Migration Perspective

The synthesis provides a solid framework, but misses crucial aspects of how migration relates to jeu de taquin (jdt). Let me fill these gaps with concrete implementation details.

### Key Insight: Migration as Reverse Jdt

The migration algorithm is essentially performing reverse jdt slides on a virtual tableau. When rhombus ℓ moves through the mosaic, it traces a path that corresponds to sliding an empty box through an LR tableau.

### Critical Fix: Flock Label Assignment

The synthesis gets the labeling wrong. The canonical construction should use **content-based labeling**:

```
// Correct labeling algorithm
AssignFlockLabels(flock F):
  // Group rhombi by rows (using orientation vectors)
  rows = group_by_row(F.rhombi, F.orientation)
  
  // Within each row, order west to east
  // Assign same label to all rhombi in same row
  label = 1
  for row in rows (north to south):
    for rhombus in row:
      F.labels[rhombus.id] = label
    label++
```

This creates weakly increasing rows (all equal) and strictly increasing columns, satisfying LR conditions (i) and (ii).

### Migration Order and Wake Structure

The "standard order" for migration must respect the tableau structure:

```
StandardOrder:
  Primary: by label value (largest first for east/north migration)
  Secondary: by position (eastmost first within same label)
```

The Wake Crossing Lemma implementation:
```
// Track wake paths during migration
Wake: {
  upper_path: List<Position>,
  lower_path: List<Position>,
  midline: List<Position>
}

CheckWakeIntact(wake, current_config):
  return all(tile at p unchanged since wake created 
             for p in wake.upper_path)
```

### Hexagon Finding Algorithm

The synthesis is vague about finding minimal hexagons. Here's the precise algorithm:

```
FindMinimalHexagon(rhombus ℓ, direction):
  // Start from rightmost vertex of ℓ
  start = rightmost_vertex(ℓ)
  
  // Trace hexagon boundary clockwise
  vertices = [start]
  current = start
  
  // Follow edges that form minimal containing hexagon
  while len(vertices) < 6:
    next = find_next_hex_vertex(current, mosaic_boundary)
    vertices.append(next)
    current = next
    
  return Hexagon(vertices)
```

### Orientation Tracking

Critical detail: orientation changes affect how we read the final tableau:

```
TrackOrientationChange(flock F, rotation_angle):
  if rotation is 120° clockwise:
    F.orientation = rotate_basis(F.orientation, 120°)
  // This affects final tableau reading order!
```

### Phase 3: Reading the Tableau

The synthesis omits this crucial step:

```
ReadTableau(final_flock F'):
  // Determine reading order from final orientation
  if F'.orientation == (-E_B, -N_B):
    // Standard reading order
    return read_standard(F')
  elif F'.orientation == (E_B, N_B):
    // Transpose reading
    return transpose(read_standard(F'))
  // etc. for other orientations
```

### Test Case Validation

For c^(3,2,1)_{(2,1),(2,1)} = 2:
- Two puzzles with different rhombus placements
- Same boundary strings but different internal structure
- Migration should produce two distinct LR tableaux of shape (3,2,1)/(1) with content (2,1)

The tableaux differ in their entries, not just their shape, proving the bijection distinguishes the puzzles.

### Implementation Priority

1. Get coordinate system right (hexagonal is best)
2. Implement wake tracking for correctness
3. Handle orientation changes carefully
4. Validate with known examples before the test case

The synthesis provides a good skeleton, but these details are essential for a working implementation.