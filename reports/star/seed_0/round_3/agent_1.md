# Implementing Purbhoo's Mosaic Migration Bijection: Specialist Report

## Critical Corrections to the Synthesis

The synthesis contains several fundamental errors that must be corrected:

### 1. **Puzzle-to-Mosaic Conversion: Complete Reversal Needed**

The synthesis misunderstands the puzzle-to-mosaic conversion. The correct process:

**Data Structures**:
```
PuzzleRhombus = {
  position: (i,j,k),  # triangular coords
  edges: {NW: 0/1, NE: 0/1, S: 0/1}  # edge labels
}

MosaicTile = {
  type: 'triangle' | 'square' | 'rhombus',
  position: (x,y),  # 2D coords
  nest: 'A' | 'B' | 'C' | null  # for rhombi only
}
```

**Conversion Algorithm**:
```
1. For each puzzle rhombus at (i,j,k):
   - If all edges same label → becomes mosaic rhombus
   - If edges alternate 0,1,0 or 1,0,1 → becomes triangle
   - If exactly two adjacent edges same → becomes square

2. Rhombus placement rules:
   - Label pattern 0,0,1 → place in nest A
   - Label pattern 1,0,0 → place in nest B  
   - Label pattern 0,1,0 → place in nest C
   
3. The "pulling tight" operation:
   - Map puzzle boundary to hexagon boundary
   - Interior tiles deform according to local geometry
```

### 2. **Coordinate Mapping**

For n=6, d=3:
```
Hexagon vertices:
A' = (0, 3)      B' = (3, 0)
A  = (0, 0)      B  = (6, 0)
                 C' = (6, 3)
                 C  = (3, 6)

Puzzle (i,j,k) → Mosaic (x,y):
x = j + k/2
y = k * sqrt(3)/2
```

### 3. **Flock Formation and Orientation**

The synthesis oversimplifies. For migration from A to B:

```
def create_initial_flock(rhombi_at_A, boundary_string_pi):
  # Orientation (-E_A, -N_A) means:
  # E_A points from A to A' (straight up)
  # N_A points from A to B' (northeast)
  # So -E_A points down, -N_A points southwest
  
  # Convert boundary string to partition
  partition = string_to_partition(pi)
  
  # Sort rhombi by position in nest
  sorted_rhombi = sort_by_coordinates(rhombi_at_A, 
                                    west_to_east=True,
                                    south_to_north=True)
  
  # Assign f-values according to partition
  f_values = {}
  rhombus_index = 0
  for part_index, part_size in enumerate(partition):
    for i in range(part_size):
      f_values[sorted_rhombi[rhombus_index]] = part_index + 1
      rhombus_index += 1
      
  return Flock(rhombi_at_A, (-E_A, -N_A), f_values)
```

### 4. **Migration Algorithm Details**

```
def migrate_south(flock, from_A_to_B):
  # Process in REVERSE standard order for south migration
  ordered_rhombi = sort_by_standard_order(flock, reverse=True)
  
  for rhombus in ordered_rhombi:
    current_pos = rhombus.position
    
    while not in_nest_B(current_pos):
      # Find minimal hexagon to the south
      hex_tiles = find_hexagon_south(current_pos)
      
      if hex_tiles.has_2fold_symmetry():
        rotate_180(hex_tiles)
      elif hex