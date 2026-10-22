# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Overview
The mosaic migration bijection transforms KTW puzzles into Littlewood-Richardson tableaux through three stages: puzzle-to-mosaic conversion, rhombi migration, and tableau extraction.

## Stage 1: Puzzle-to-Mosaic Conversion

### Data Structures
```python
class PuzzlePiece:
    type: str  # 'triangle' or 'rhombus'
    position: (i, j, k)  # barycentric coordinates, i+j+k=n
    edge_labels: dict  # maps edge directions to 0/1

class MosaicTile:
    type: str  # 'triangle', 'square', or 'rhombus'
    position: (x, y)  # 2D coordinates in hexagon
    nest: str  # 'A', 'B', 'C', or None
```

### Algorithm
```python
def puzzle_to_mosaic(puzzle, n, d):
    # Step 1: Transform puzzle geometry
    mosaic_tiles = []
    for piece in puzzle.pieces:
        # Convert barycentric to hexagon coordinates
        x = piece.j + piece.k/2 - (piece.j + piece.k) * d/n
        y = piece.k * sqrt(3)/2 * (1 - d/n)
        
        if piece.type == 'triangle':
            mosaic_tiles.append(MosaicTile('triangle', (x,y)))
        else:  # rhombus with mixed labels becomes square
            mosaic_tiles.append(MosaicTile('square', (x,y)))
    
    # Step 2: Add nest rhombi from boundary data
    # Read boundary strings π, ρ, σ from puzzle edges
    for i, bit in enumerate(π):
        if bit == '1':
            # Position rhombus at nest A
            x_A = i * cos(150°)  # along A-A' direction
            y_A = i * sin(150°)
            mosaic_tiles.append(MosaicTile('rhombus', (x_A, y_A), 'A'))
    
    # Similar for ρ→B and σ→C
    return mosaic_tiles
```

## Stage 2: Migration Algorithm

### Core Data Structures
```python
class Flock:
    rhombi: list[Rhombus]  # ordered by standard order
    orientation: (E, N)  # unit vectors defining compass
    f_values: dict  # rhombus → integer label
    
class Rhombus:
    id: int
    position: (x, y)
    wake: Wake  # tracks displacement path
    
class Wake:
    midline: list[(x,y)]  # path center
    upper_tiles: set[Tile]
    lower_tiles: set[Tile]
```

### Migration Process
```python
def migrate_flock(flock, source_nest, target_nest):
    # Set migration direction based on nest pair
    if source_nest == 'A' and target_nest == 'B':
        direction = 'south'  # using (-E_A, -N_A) orientation
        
    # Process rhombi in standard order
    for rhombus in flock.rhombi:
        rhombus.wake = Wake()
        
        while rhombus.nest != target_nest:
            # Find minimal containing hexagon to the right
            hex = find_minimal_hexagon(rhombus, direction)
            
            if hex.symmetry == 2:  # 180° rotational symmetry
                rotate_tiles_180(hex)
            else:  # 120° rotational symmetry
                # Rotate to make rhombus edge horizontal/vertical
                angle = choose_rotation_angle(rhombus, hex)
                rotate_tiles_120(hex, angle)
            
            # Update wake tracking
            rhombus.wake.add_displaced_tiles(hex.tiles)
            
    return flock
```

### Critical Implementation Details

1. **Standard Order Comparison**:
```python
def compare_rhombi(r1, r2, f