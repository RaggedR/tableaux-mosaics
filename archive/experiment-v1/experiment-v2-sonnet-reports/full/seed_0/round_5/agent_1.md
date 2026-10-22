# Report: Implementing Purbhoo's Mosaic Migration for KTW Puzzles

## Analysis of Previous Reports

The previous reports contain valuable structural insights but all share critical flaws:

1. **Overcomplication**: Introducing vertex models, growth diagrams, and Yang-Baxter equations where Purbhoo uses elementary geometric operations
2. **Missing concrete algorithms**: No implementable code for the core migration process
3. **Coordinate system confusion**: Mixing different lattice systems without clear mappings
4. **Incomplete boundary handling**: Not properly connecting puzzle edge labels to mosaic nest contents

**Key insight missing from all reports**: Migration is fundamentally a **sequence of simple local hexagon rotations**, not complex algebraic operations.

## Concrete Implementation Specification

### Phase 1: Puzzle to Mosaic Conversion

**Data Structures:**
```python
class HexPosition:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y  # Axial coordinates
        
class Rhombus:
    def __init__(self, pos: HexPosition, orientation: int, value: int = 0):
        self.pos = pos
        self.orientation = orientation  # 0, 1, 2 (three possible orientations)
        self.value = value  # For LR tableau entries

class Mosaic:
    def __init__(self, n: int):
        self.n = n
        self.d = 0  # Will be computed from boundary
        self.nest_A = []  # List of Rhombus objects
        self.nest_B = []
        self.nest_C = []
```

**Conversion Algorithm:**
```python
def puzzle_to_mosaic(boundary_strings: tuple) -> Mosaic:
    pi, rho, sigma = boundary_strings
    n = len(pi)
    d = pi.count('1')
    
    mosaic = Mosaic(n)
    mosaic.d = d
    
    # Direct boundary-to-nest conversion (Purbhoo Section 2.5)
    mosaic.nest_A = boundary_string_to_rhombi(pi, "A")
    mosaic.nest_B = boundary_string_to_rhombi(rho, "B") 
    mosaic.nest_C = boundary_string_to_rhombi(sigma, "C")
    
    return mosaic

def boundary_string_to_rhombi(boundary: str, nest_id: str) -> list:
    """Convert 01-string to list of rhombi positions in specified nest"""
    rhombi = []
    x, y = 0, 0  # Starting position in nest coordinate system
    
    for i, bit in enumerate(boundary):
        if bit == '1':
            # Add rhombus at current position
            pos = HexPosition(x, y)
            orientation = get_nest_orientation(nest_id)
            rhombi.append(Rhombus(pos, orientation))
            
            # Move to next row
            if nest_id == "A":
                y += 1
            elif nest_id == "B": 
                x += 1; y += 1
            else:  # nest_id == "C"
                x += 1
        else:
            # Move within current row
            if nest_id == "A":
                x += 1
            elif nest_id == "B":
                x += 1
            else:  # nest_id == "C" 
                y += 1
                
    return rhombi

def get_nest_orientation(nest_id: str) -> int:
    """Standard orientations for the three nests"""
    return {"A": 0, "B": 1, "C": 2}[nest_id]
```

### Phase 2: Migration Algorithm

**Core Migration Process:**
```python
def migrate_rhombus(mosaic: Mosaic, rhombus: Rhombus, target_nest: str):
    """Move single rhombus from its current nest to target nest"""
    current_pos = rhombus.pos
    path = []  # Track positions during migration
    
    while not in_target_nest(current_pos, target_nest, mosaic.n