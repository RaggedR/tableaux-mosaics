# Report: Implementing Purbhoo's Mosaic Migration Bijection for KTW Puzzles

## Executive Summary

I'm providing complete implementation specifications for Purbhoo's bijection converting KTW puzzles to LR tableaux. The previous reports captured the high-level structure but missed crucial geometric details and algorithmic specifics. This report provides concrete data structures, explicit coordinate transformations, and step-by-step procedures ready for direct implementation.

## Critical Observations from Paper Analysis

**Key Issue with Previous Reports**: They underspecified the geometric transformations and missed Purbhoo's crucial insight that mosaics are "crooked drawings" of puzzles with extra corner rhombi. The bijection isn't just coordinate mapping—it's a fundamental restructuring that makes flock migration possible.

**Core Geometric Insight**: Puzzles use triangular lattice coordinates; mosaics use a hexagonal region with three distinguished corner "nests" where rhombi pack into Young diagram shapes.

## Phase 1: Puzzle-to-Mosaic Conversion

### Data Structures
```
struct PuzzlePiece {
    type: enum {RHOMBUS_0, RHOMBUS_1, RHOMBUS_01} // Three edge-labeled types
    center: (int, int)  // Triangular lattice coordinates  
    orientation: int    // 0-5 (60° rotations)
}

struct Rhombus {
    position: (float, float)  // Hexagonal coordinates
    value: int               // Will hold LR tableau entry
}

struct Mosaic {
    hexagon_bounds: HexRegion
    triangles: Set[(float, float)]
    squares: Set[(float, float)]  
    nest_A: List[Rhombus]    // Southwest corner
    nest_B: List[Rhombus]    // Southeast corner  
    nest_C: List[Rhombus]    // North corner
}
```

### Conversion Algorithm
The key insight from Purbhoo Section 2.5: "Take a mosaic, remove all rhombi, grab corners A', B', C' and pull tight outward. The boundary straightens into an equilateral triangle."

**Implementation Steps**:
1. **Initialize hexagonal region**: Create hexagon A'AB'BC'C with vertices at:
   - A' = (-d, 0), A = (0, 0), B' = (n-d, 0)  
   - B = (n-d, d), C' = (n-2d, d), C = (-d, d)

2. **Map puzzle pieces**: For each puzzle rhombus, the "straightening" operation distributes it into:
   - Interior triangle/square tiles
   - Boundary rhombi that get packed into nests

3. **Boundary correspondence**: The 01-strings (π,ρ,σ) encode the nest shapes:
   - Walk from A' to B': 0 = unit step east, 1 = unit step northeast
   - This determines which rhombi belong to each nest

```python
def puzzle_to_mosaic(puzzle):
    d = count_ones(puzzle.boundary[0])  # All three strings have same # of 1s
    n = len(puzzle.boundary[0])
    
    mosaic = initialize_hexagon(d, n)
    
    # The straightening bijection maps each puzzle piece
    for piece in puzzle.pieces:
        if piece_creates_interior_tiles(piece):
            add_interior_tiles(mosaic, piece)
        else:
            add_to_appropriate_nest(mosaic, piece)
    
    return mosaic
```

## Phase 2: Flock Initialization

**Critical Detail**: Each nest gets a canonical "flock"—a Young diagram of rhombi with LR tableau structure.

### Standard Orientation Setup
From Purbhoo: each nest has canonical orientation vectors:
- Nest A: E_A = direction AA', N_A = direction AB'  
- Nest B: E_B = direction BB', N_B = direction BC'
- Nest C: E_C = direction CC', N_C = direction CA'

### Canonical Flock Construction
```python
def create_canonical_flock(nest_rhombi, boundary_string):
    # Convert boundary string to partition shape