# Synthesis Report: Implementing Purbhoo's Mosaic Migration Bijection

## Core Algorithm Overview

The reports agree on the three-step process:
1. Convert KTW puzzle to mosaic
2. Migrate rhombi using local hexagonal flips
3. Extract LR tableau from final configuration

However, there are critical disagreements about the details.

## Key Tensions and Resolutions

### 1. **Puzzle-to-Mosaic Conversion**

**Tension**: Reports disagree fundamentally on how puzzle pieces map to mosaic tiles.

**Resolution**: The third report is correct. The physical "pulling tight" operation works as follows:
- Remove ALL rhombi from the puzzle (creating holes)
- Deform the triangular grid into the hexagon
- Puzzle rhombi with 30°-150° angles become squares
- Triangles remain triangles
- The HOLES determine where to place mosaic rhombi in nests

**Implementation**:
```
For each puzzle rhombus at position (i,j,k):
  if north edge labeled 1: create hole → place rhombus in nest B
  if west edge labeled 1: create hole → place rhombus in nest A  
  if both edges labeled 1: becomes triangle (no hole)
  if both edges labeled 0: becomes square (no hole)
```

### 2. **Coordinate Systems**

**Consensus**: Use triangular coordinates (i,j,k) for puzzles, convert to 2D for mosaics.

**Implementation**:
```
PuzzleCoord = (i, j, k)  # where i+j+k=n
MosaicCoord = (x, y)      # standard 2D plane

# Hexagon vertices (with n=6, d=3 for example):
A' = (0, 0)
A = (3, 0)
B' = (6, 0)  
B = (7.5, 2.6)
C' = (4.5, 6.5)
C = (1.5, 2.6)
```

### 3. **Flock Formation**

**Tension**: Reports differ on how to assign f-values to rhombi.

**Resolution**: For the canonical flock at nest A with orientation (-E_A, -N_A):
1. Sort rhombi by position in the nest
2. Group rhombi to match the partition structure
3. Assign f(rhombus) = group_number

**Implementation**:
```
def create_canonical_flock(rhombi_alpha, partition_nu):
  # Sort by position using orientation (-E_A, -N_A)
  sorted_rhombi = sort_by_position(rhombi_alpha, -E_A, -N_A)
  
  # Assign labels matching partition
  current_label = 1
  for part_size in partition_nu:
    for i in range(part_size):
      f[sorted_rhombi[...]] = current_label
    current_label += 1
```

### 4. **Migration Algorithm**

**Consensus**: Process rhombi in standard order, performing local hexagon rotations.

**Key Details**:
```
def migrate(flock, source_nest, target_nest):
  # Determine migration direction
  direction = get_direction(source_nest, target_nest)
  
  # Sort by standard order
  if direction in [NORTH, EAST]:
    rhombi = sort_descending_standard_order(flock)
  else:
    rhombi = sort_ascending_standard_order(flock)
  
  for rhombus in rhombi:
    while not in_nest(rhombus, target_nest):
      hex = find_minimal_hexagon(rhombus, direction)
      rotate_hexagon(hex)
      update_wake(rhombus)
```

### 5. **Wake Preservation**

**Consensus**: Critical for correctness. Track displaced tiles to ensure proper ordering.

**Implementation**:
```
class Wake:
  def __init__(self):
    self.midline = []  # path of rhombus centers
    self.upper_tiles = set()
    self.lower_tiles = set()
  
  def check_crossing(self, other