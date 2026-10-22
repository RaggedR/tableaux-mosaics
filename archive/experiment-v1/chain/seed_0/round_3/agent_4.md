# Computational Implementation Report: KTW Puzzle to LR Tableau Bijection

## Overview
Based on the previous researcher's analysis and corrections, I'll provide a concrete computational framework for implementing Purbhoo's migration bijection. This report focuses on data structures, algorithms, and verification procedures.

## Data Structures

### Core Geometric Objects
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Rhombus:
    def __init__(self, center, orientation, content=None):
        self.center = center  # Point
        self.orientation = orientation  # 0, 60, or 120 degrees
        self.content = content  # Integer label
        
class Triangle:
    def __init__(self, center, orientation):
        self.center = center
        self.orientation = orientation  # 0 or 180 degrees

class Mosaic:
    def __init__(self, n, d):
        self.n, self.d = n, d
        self.tiles = {}  # Dict mapping positions to tiles
        self.rhombi_by_nest = {'A': [], 'B': [], 'C': []}
```

### Hexagon Recognition
```python
def find_minimal_hexagon(mosaic, rhombus_pos, direction):
    """Find smallest hexagon containing rhombus in given direction"""
    # Search pattern depends on direction (south for A→B)
    # Return (hex_center, hex_type, entry_edge)
    # hex_type ∈ {'2-fold', '3-fold'}
    # entry_edge indicates which edge rhombus enters from
```

## Phase 1: Puzzle to Mosaic Conversion

### Algorithm
1. Create hexagon with vertices as specified
2. For each puzzle rhombus at position (i,j):
   - If labeled 0: remains as rhombus, place in appropriate nest
   - If labeled 1: becomes square in mosaic interior
3. Fill remaining space with triangles

### Nest Assignment Rules
```python
def assign_to_nest(rhombus_pos, puzzle_boundary):
    # Based on which boundary edge the rhombus is nearest
    # A nest: near left edge
    # B nest: near right edge  
    # C nest: near top edge
```

## Phase 2: Migration Algorithm (Detailed)

### Content Assignment for Nest A
```python
def assign_content_nest_A(rhombi_A, partition_alpha):
    # Sort by x-coordinate (west to east)
    sorted_rhombi = sorted(rhombi_A, key=lambda r: r.center.x)
    
    # Assign content row-by-row (French convention)
    index = 0
    for row_num in range(1, len(partition_alpha) + 1):
        for _ in range(partition_alpha[row_num - 1]):
            sorted_rhombi[index].content = row_num
            index += 1
```

### Migration Order Determination
```python
def get_migration_order(rhombi, orientation, direction):
    if orientation == (-E_A, -N_A) and direction == "south":
        # Higher content first, then eastmost first within content
        return sorted(rhombi, key=lambda r: (-r.content, -r.center.x))
```

### Hexagon Rotation Logic
```python
def rotate_hexagon(hex_config, rhombus, entry_edge):
    if hex_config['type'] == '2-fold':
        return rotate_180(hex_config)
    else:  # 3-fold
        # Determine rotation to make rhombus edge horizontal/vertical
        current_rhomb_orientation = rhombus.orientation
        target_orientations = get_valid_exit_orientations(entry_edge)
        
        for rotation in [0, 120, 240]:
            new_orientation = (current_rhomb_orientation + rotation) % 360
            if results_in_valid_exit(new_orientation, target_orientations):
                return rotate_by(hex_config, rotation)
```

### Wake Tracking (for verification)
```python
class Wake:
    def __init__(self, rhombus_id