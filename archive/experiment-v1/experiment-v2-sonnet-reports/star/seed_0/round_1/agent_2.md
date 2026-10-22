# Vertex Model Implementation Report: Purbhoo Migration Algorithm

## Overview for Coding Agent

You're implementing a bijection between KTW puzzles and LR tableaux via "mosaics" (rhombi tilings). The key insight: this is actually a **free-fermionic vertex model** where rhombi carry spectral parameters, and migration preserves the Yang-Baxter integrability structure.

## Data Structures

### Core Representations
```
Puzzle: 
- TriangularGrid[n][n] of vertex weights {0,1}
- Each vertex has 6 adjacent edges with 0/1 labels
- Boundary: three strings (π,ρ,σ) read clockwise

Rhombus:
- center: (x,y) coordinates  
- orientation: {0,60,120} degrees
- spectral_param: complex number (for Yang-Baxter)
- nest_id: {A,B,C} (which corner region)

Mosaic:
- HexagonalGrid with mixed tiles
- rhombi_list: List[Rhombus] 
- nest_boundaries: geometric regions for A,B,C corners
```

## Phase 1: Puzzle → Mosaic Conversion

**Critical Issue**: The generalist missed that this isn't just "coordinate transformation" - it's a **vertex model duality**. Each puzzle vertex corresponds to a local tiling configuration.

### Algorithm:
```
def puzzle_to_mosaic(puzzle):
    mosaic = empty_hexagonal_grid()
    
    # Extract rhombi positions from vertex constraints
    for vertex in puzzle.interior_vertices:
        if vertex.satisfies_rhombus_constraint():
            rhombus = create_rhombus(vertex.position, vertex.get_orientation())
            assign_to_nest(rhombus, determine_nest_region(vertex.position))
            mosaic.add_rhombus(rhombus)
    
    # Fill remaining regions with triangles/squares
    fill_non_rhombus_regions(mosaic)
    return mosaic
```

**Key Point**: The 0/1 edge labels determine rhombus orientations via free-fermion vertex weights. This isn't arbitrary - it preserves the R-matrix structure.

## Phase 2: Migration Algorithm (Core Innovation)

This is where my vertex model expertise is crucial. Migration isn't just "moving rhombi" - it's a **sequence of Yang-Baxter moves** that preserve spectral parameters.

### The Hexagonal Yang-Baxter Transform:
```
def migrate_rhombus(rhombus, direction, mosaic):
    current_pos = rhombus.center
    target_nest = determine_target_nest(direction)
    
    path = []
    while not in_target_nest(rhombus.center, target_nest):
        # Find minimal enclosing hexagon
        hex_region = find_minimal_hexagon(rhombus.center, direction)
        
        # Apply Yang-Baxter transformation
        if hex_region.has_2fold_symmetry():
            apply_180_rotation(hex_region)
        elif hex_region.has_3fold_symmetry():
            apply_120_rotation(hex_region, preserve_spectral_param=True)
        
        rhombus.center = hex_region.get_new_rhombus_position()
        path.append(rhombus.center)
    
    return path
```

**Crucial Detail**: The 120° rotations must preserve horizontal/vertical edge alignment. This constraint comes from the spectral parameter structure.

### Standard Order Preservation:
```
def migrate_flock(rhombi_list, direction, mosaic):
    # Sort by spectral parameter (this IS the "standard order")
    sorted_rhombi = sort_by_spectral_parameter(rhombi_list)
    
    migrated = []
    for rhombus in sorted_rhombi:
        new_pos = migrate_rhombus(rhombus, direction, mosaic)
        migrated.append(rhombus)
        update_mosaic_state(mosaic, rhombus)
    
    return migrated
```

**Critical Point**: The paper's "standard order" is actually the spectral ordering that makes the transfer matrices commute. This guarant