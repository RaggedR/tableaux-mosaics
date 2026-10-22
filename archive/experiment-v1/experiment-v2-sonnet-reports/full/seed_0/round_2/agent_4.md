# Report: Implementing Purbhoo's Mosaic Migration Bijection

## Executive Summary

I'm providing concrete implementation details for Purbhoo's bijection between KTW puzzles and LR tableaux. The previous reports correctly identified the three phases but lacked crucial algorithmic specifics. My analysis fills these gaps with explicit data structures, geometric transformations, and step-by-step procedures suitable for direct implementation.

## Core Data Structures

### 1. Coordinate System
Use **axial coordinates** (q, r) for hexagonal grids:
- q-axis points east-northeast (30° from horizontal)
- r-axis points north-northwest (150° from horizontal)
- Each unit rhombus occupies one hexagonal cell
- Triangles and squares occupy fractional positions

### 2. Puzzle Representation
```
struct PuzzlePiece {
    type: {RHOMBUS_A, RHOMBUS_B, RHOMBUS_C}  // The three rhombus types
    position: (int, int)  // Triangle grid coordinates
    rotation: int         // 0-5 (60° increments)
}

struct Puzzle {
    pieces: List[PuzzlePiece]
    boundary: (String, String, String)  // (π, ρ, σ) - the 01-strings
}
```

### 3. Mosaic Representation
```
struct Rhombus {
    position: (float, float)  // Axial coordinates
    orientation: int          // 0-2 (120° increments for 30°/150° rhombi)
    nest: {A, B, C}          // Which corner nest contains this rhombus
}

struct Flock {
    rhombi: List[Rhombus]
    east_vector: (float, float)   // E direction
    north_vector: (float, float)  // N direction  
    tableau_values: Map[Rhombus -> int]  // f: ζ → ℕ
}

struct Mosaic {
    triangles: List[(float, float)]
    squares: List[(float, float)]
    rhombi_A: List[Rhombus]  // Nest A
    rhombi_B: List[Rhombus]  // Nest B  
    rhombi_C: List[Rhombus]  // Nest C
}
```

## Algorithm 1: Puzzle-to-Mosaic Conversion

**Key Insight**: The bijection preserves combinatorial structure while changing geometry. Each puzzle piece maps to a mosaic tile configuration.

```python
def puzzle_to_mosaic(puzzle):
    mosaic = Mosaic()
    
    # Phase 1: Map each puzzle piece to mosaic tiles
    for piece in puzzle.pieces:
        if piece.type == RHOMBUS_A:
            # Creates specific pattern of triangles + one rhombus
            add_rhombus_A_pattern(mosaic, piece.position, piece.rotation)
        # Similar for RHOMBUS_B, RHOMBUS_C
    
    # Phase 2: Identify nest assignments
    for rhombus in mosaic.all_rhombi():
        rhombus.nest = determine_nest_from_position(rhombus.position)
    
    # Phase 3: Set canonical orientations
    set_nest_orientations(mosaic)
    
    return mosaic
```

**Critical Implementation Detail**: The "straightening" operation maps puzzle coordinates (i,j) in the triangular grid to mosaic coordinates via:
- (i,j) → (i - j/2, j * √3/2) in Cartesian coordinates
- Then convert to axial coordinates for the hexagonal mosaic

## Algorithm 2: Migration Implementation

**Core Operation**: Move rhombi through hexagonal transformations while preserving flock structure.

```python
def migrate_flock(mosaic, flock, target_nest):
    # Step 1: Order rhombi by standard order
    ordered_rhombi = sort_by_standard_order(flock)
    
    for rhombus in ordered_rhombi:
        while rhombus.nest != target_nest:
            # Step 2: Find minimal containing hexagon
            hexagon = find_minimal