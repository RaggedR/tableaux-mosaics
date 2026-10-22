# Yang-Baxter Implementation Report: Mosaic Migration Bijection

## Critical Vertex Model Structure

The migration algorithm operates on a **staggered six-vertex model** where rhombi carry fermionic degrees of freedom. The key insight: Purbhoo's hexagon flips are R-matrix evaluations ensuring commutativity of transfer matrices.

## Phase 1: Puzzle-to-Mosaic Mapping (Corrected)

The generalist's approach misunderstands the geometric transformation. The correct procedure:

```
function puzzle_to_mosaic(puzzle):
  // Extract boundary as 01-strings
  (π, ρ, σ) = read_boundaries_clockwise(puzzle)
  n = len(π)
  d = count_ones(π)
  
  // Create hexagon A'AB'BC'C with angles
  // 150° at A,B,C (nests) and 90° at A',B',C'
  mosaic = create_hexagon_frame(n, d)
  
  // Transform puzzle pieces
  for each tile at (i,j,k) in puzzle:  // barycentric coords
    edge_labels = get_edge_labels(tile)
    
    if all edges have same label:
      // Unit triangle → stays triangle
      place_triangle(mosaic, transform_coords(i,j,k))
    else:
      // 30-60 rhombus → becomes square
      // Critical: track edge rotation directions
      clockwise_edges = count_clockwise_rotations(tile)
      place_square(mosaic, transform_coords(i,j,k), 
                  rotation_data=clockwise_edges)
  
  // Pack rhombi based on boundary complement
  pack_rhombi_from_boundaries(mosaic, π, ρ, σ)
  
  return mosaic
```

### Boundary-to-Partition Conversion

The boundary strings encode partitions via their complement structure:

```
function boundary_to_partition(boundary_string):
  // boundary_string of length n with d ones
  partition = []
  ones_seen = 0
  
  for i from n-1 downto 0:
    if boundary_string[i] == '1':
      ones_seen++
      partition.append(n - d - i + ones_seen - 1)
  
  return reverse(partition)
```

## Phase 2: Migration via R-Matrices

### Hexagon Flip as Six-Vertex Configuration

Each hexagon contains a configuration from the six-vertex model. The flip operation evaluates the R-matrix:

```
function migrate_rhombus(mosaic, rhombus, direction):
  path = []
  current_pos = rhombus.position
  
  while not in_target_nest(current_pos):
    hex = find_minimal_hexagon_in_direction(current_pos, direction)
    
    // Identify vertex configuration
    config = get_hexagon_configuration(hex)
    
    if config.type == "symmetric":  // 2-fold symmetry
      // R-matrix: swap opposite edges
      flip_180_degrees(hex)
    else:  // 3-fold symmetry  
      // R-matrix: rotate to maintain horizontal/vertical edge
      flip_120_degrees(hex, preserve_axis=true)
    
    path.append(hex)
    current_pos = rhombus.new_position
  
  return path
```

### Free-Fermionic Weights and Order Preservation

The free-fermionic condition ensures that the Yang-Baxter equation holds with spectral parameters determined by rhombus labels:

```
function migrate_flock(mosaic, source_nest, target_nest):
  rhombi = get_rhombi_in_nest(mosaic, source_nest)
  
  // Critical: orientation determines standard order
  orientation = get_nest_orientation(source_nest)
  if migration_direction in [SOUTH, WEST]:
    orientation = reverse_orientation(orientation)
  
  // Sort by standard order (lexicographic in oriented coordinates)
  ordered_rhombi = sort_by_standard_order(rhombi, orientation)
  
  // Migrate preserving relative order
  for rhombus in ordered_