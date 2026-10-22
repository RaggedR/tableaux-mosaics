# Migration Algorithm Report for KTW Puzzle-Tableau Bijection

## Executive Summary
I can implement Purbhoo's bijection, but with a critical insight: **the coordinate transformations and physical deformations are red herrings for implementation**. The real algorithm operates on combinatorial structures that can be implemented directly without geometric calculations.

## Data Structures

### Core Objects
```python
class Tile:
    type: str  # "triangle", "square", "rhombus"
    position: (int, int)  # discrete grid coordinates
    orientation: int  # 0-5 for 6 possible orientations
    label: int  # for rhombi in flocks

class Mosaic:
    tiles: List[Tile]
    boundary_rhombi: Dict[str, List[Tile]]  # "A", "B", "C" -> rhombi lists
    
class Flock:
    rhombi: List[Tile]
    orientation: (int, int)  # (E, N) direction indices
    tableau_values: Dict[Tile, int]
```

### Coordinate System
- Use **discrete hexagonal coordinates** (not continuous geometry)
- Puzzle triangles map to specific grid positions
- Each position can hold exactly one tile type

## Algorithm Implementation

### Step 1: Puzzle to Mosaic Conversion

**Key Insight**: Don't compute geometric transformations. Instead:

```python
def puzzle_to_mosaic(puzzle_pieces):
    # Direct combinatorial mapping based on paper's bijection
    mosaic_tiles = []
    
    for piece in puzzle_pieces:
        if piece.type == "rhombus_with_0":
            # Becomes square in mosaic
            mosaic_tiles.append(Tile("square", piece.position, piece.orientation))
        elif piece.type == "rhombus_with_1":
            # Becomes triangle in mosaic  
            mosaic_tiles.append(Tile("triangle", piece.position, piece.orientation))
        # Corner regions become boundary rhombi collections
    
    return Mosaic(mosaic_tiles, extract_boundary_rhombi(mosaic_tiles))
```

**Boundary Data Extraction**: The 01-strings from puzzle boundaries directly encode which rhombi belong to each corner nest A, B, C.

### Step 2: Migration Algorithm Core

**Critical Resolution**: The "standard order" isn't circular - it comes from the **input boundary partition structure**, not the final tableau.

```python
def migrate_flock(mosaic, source_nest, target_nest, flock):
    # Flock rhombi already have tableau values from boundary partition
    ordered_rhombi = sort_by_standard_order(flock.rhombi, flock.tableau_values)
    
    for rhombus in ordered_rhombi:
        migrate_single_rhombus(mosaic, rhombus, target_nest)
    
    return updated_mosaic

def migrate_single_rhombus(mosaic, rhombus, target_direction):
    current_pos = rhombus.position
    
    while not in_target_nest(current_pos, target_direction):
        # Find 6-tile hexagonal neighborhood
        hex_tiles = get_hexagonal_neighborhood(mosaic, current_pos)
        
        # Pattern matching for flip type
        if is_symmetric_2fold(hex_tiles):
            rotate_tiles_180(hex_tiles)
        elif is_symmetric_3fold(hex_tiles):
            rotate_tiles_120(hex_tiles, get_direction_constraint(target_direction))
        
        current_pos = rhombus.position  # Updated by rotation
```

### Step 3: Hexagonal Pattern Recognition

**Two patterns to detect**:

```python
def is_symmetric_2fold(tiles):
    # Pattern (a): rhombus + triangle + square + triangle + square + rhombus
    # Symmetric under 180° rotation
    return check_pattern_a(tiles)

def is_symmetric_3fold(tiles):  
    # Pattern (b): rhombus + square + square + square + square + square
    # Symmetric under 120° rotation
    return check_pattern_b(tiles)

def rotate_tiles_120(tiles, direction_constraint):
    # "whichever way