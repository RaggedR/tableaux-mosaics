# Synthesized Report: Implementing Purbhoo's Mosaic Migration Bijection

## Core Agreement: Three-Stage Pipeline

All researchers agree on the basic structure:
1. **Puzzle → Mosaic**: Geometric transformation
2. **Migration**: Local hexagon flips moving rhombi between nests
3. **Tableau Extraction**: Reading final configuration

## Critical Clarifications

### 1. Puzzle-to-Mosaic Conversion

**Consensus**: The "pulling tight" operation is a continuous deformation, NOT removal of pieces.

**Correct Algorithm**:
```python
def puzzle_to_mosaic(puzzle, n, d):
    # Create hexagon with angles 150° at A,B,C and 90° at A',B',C'
    # Vertices: A'=(0,d), A=(0,0), B'=(n-d,0), B=(n,0), 
    #          C'=(n,d), C=(n-d,n-d)
    
    mosaic = []
    
    # 1. Transform all puzzle pieces (no removal!)
    for piece in puzzle.pieces:
        new_pos = transform_coordinates(piece.pos, n)
        if piece.type == TRIANGLE:
            mosaic.append(Triangle(new_pos))
        else:  # puzzle rhombus
            mosaic.append(Square(new_pos))
    
    # 2. Place boundary rhombi in nests based on boundary strings
    # Boundary string π determines nest A rhombi positions
    for i, bit in enumerate(π):
        if bit == 1:
            pos = boundary_position_A(i)
            mosaic.append(Rhombus(pos, nest='A'))
    
    # Similarly for ρ→B and σ→C
    
    return mosaic
```

**Key Insight**: Puzzle rhombi with alternating 0/1 edge labels experience stress during deformation and become squares. The mosaic rhombi come from reading boundary data, not from puzzle rhombi.

### 2. Coordinate Systems

**Agreed Mapping**:
```python
def puzzle_to_mosaic_coords(i, j, k, n, d):
    # Puzzle: barycentric (i,j,k) with i+j+k=n
    # Mosaic: 2D coordinates in hexagon
    
    # Linear interpolation preserving edge parallelism
    # Maps (n,0,0)→A', (0,n,0)→B', (0,0,n)→C'
    
    # Simplified for implementation:
    x = j + k * 0.5
    y = k * sqrt(3) / 2
    
    # Adjust for hexagon geometry
    return scale_to_hexagon(x, y, n, d)
```

### 3. Migration Algorithm

**Data Structures**:
```python
class Flock:
    rhombi: list[Rhombus]  # subset of rhombi in nest
    orientation: (E, N)     # basis vectors
    f_values: dict[Rhombus, int]  # labeling function

class Wake:
    midline: list[Point]
    upper_tiles: set[Tile]
    lower_tiles: set[Tile]
```

**Critical Details**:

1. **Orientation for A→B migration**: Use (-E_A, -N_A)
   - E_A points from A to A' (up)
   - N_A points from A to B' (northeast)
   - So -E_A points down, -N_A points southwest

2. **Standard Order**:
```python
def compare_standard_order(r1, r2, flock):
    if flock.f_values[r1] != flock.f_values[r2]:
        return flock.f_values[r1] - flock.f_values[r2]
    else:
        # Same f-value: compare positions
        # "West of" in flock orientation = earlier
        return position_compare(r1.pos, r2.pos, flock.orientation)
```

3. **Migration Process**:
```python
def migrate_A_to_B(flock):
    