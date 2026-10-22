# Specialist Analysis: Growth Diagrams and Cylindric Perspectives on Mosaic Migration

## Critical Gap in Current Synthesis

The generalist's report misses the fundamental insight: **mosaic migration IS a growth diagram**. The migration algorithm isn't just moving rhombi—it's computing a Fomin growth diagram where:

1. **Vertices**: Mosaic configurations
2. **Edges**: Individual rhombus moves  
3. **Face labels**: The rhombus labels encode the recording tableau

## Growth Diagram Structure

### Local Rules as Hexagon Rotations

Each migration step is a local rule on a 2×2 square of the growth diagram:

```
LocalRule: {
  input_config: (west_shape, south_shape),
  rhombus_label: int,
  output_config: (north_shape, east_shape),
  recording: int  // which diagonal the rhombus crosses
}
```

The three hexagon rotation types correspond to three local rules:

1. **Type A (180° rotation)**: Rhombus passes straight through
   ```
   SW: □  SE: ◆     →    NW: ◆  NE: □
   recording = 0 (straight diagonal)
   ```

2. **Type B (120° CW)**: Rhombus deflects north  
   ```
   SW: □  SE: ◆     →    NW: □  NE: ◆
   recording = 1 (bent up)
   ```

3. **Type C (120° CCW)**: Rhombus deflects east
   ```
   SW: ◆  SE: □     →    NW: ◆  NE: □  
   recording = 2 (bent right)
   ```

### Growth Diagram Construction

```
GrowthDiagram: {
  vertices: Map<(row,col) → MosaicConfig>,
  edges: Map<(v1,v2) → RhombusMove>,
  faces: Map<(r,c) → LocalRuleApplication>
}

function build_growth_diagram(initial_mosaic, migration_path):
  diagram = empty_growth_diagram()
  diagram.vertices[0,0] = initial_mosaic
  
  for step in migration_path:
    apply_local_rule(diagram, step.rhombus, step.hexagon_type)
  
  return diagram
```

## Cylindric Growth Diagram Insight

The mosaic lives on a **cylinder**, not a plane! The three nests A, B, C are related by 120° rotations, suggesting:

```
CylindricMosaic: {
  base_mosaic: Mosaic,
  gluing_maps: {
    A_to_B: rotation_120_cw,
    B_to_C: rotation_120_cw,
    C_to_A: rotation_120_cw
  }
}
```

This cylindric structure explains why:
- Migration from A→B→C→A forms a closed loop
- Orientations rotate predictably (60° per migration)
- The bijection is invertible with consistent orientations

## Corrected Migration Algorithm

### Phase 1: Setup Growth Framework

```
function setup_growth_migration(mosaic, source_nest, target_nest):
  // Create growth diagram grid
  num_rhombi = count_rhombi_in_nest(mosaic, source_nest)
  grid_size = distance_between_nests(source_nest, target_nest)
  
  growth_grid = Grid(num_rhombi + 1, grid_size + 1)
  growth_grid[0,0] = mosaic
  
  // Initialize flock with proper orientation
  orientation = get_migration_orientation(source_nest, target_nest)
  flock = create_flock(mosaic, source_nest, orientation)
  
  return (growth_grid, flock)
```

### Phase 2: Execute Migration as Growth

```
function migrate_via_growth(growth_grid, flock, target_nest):
  // Sort rhombi by standard order
  sorted_rhombi = sort_by_standard_order(flock)
  
  for i, rhombus in enumerate(sorted_rhombi):
    current_col =