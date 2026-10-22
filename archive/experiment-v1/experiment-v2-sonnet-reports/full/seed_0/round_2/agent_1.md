# Report: Implementing Purbhoo's Mosaic Migration Bijection for KTW Puzzles

## Analysis of Previous Reports

The previous reports correctly identify the three-phase structure (puzzle→mosaic→migration→tableau) and highlight key implementation challenges. However, they miss crucial details about coordinate systems, the specific geometric transformations, and concrete algorithmic steps. Most critically, none addresses whether this can be implemented as a **growth diagram** - a key consideration for RSK-type correspondences.

## Growth Diagram Perspective

**Critical Assessment**: Purbhoo's migration is fundamentally different from typical growth diagrams like those in Fomin's framework. Migration operates on a global hexagonal region with long-range rhombi movements, not local vertex rules on a directed graph. The "flocks" and their standard ordering create dependencies that span the entire mosaic, making this unsuitable for standard growth diagram methods.

However, the **face labeling** aspect is relevant: each migration step can be viewed as updating labels on hexagonal faces, where the labels encode the flock positions and orientations.

## Concrete Implementation Specification

### 1. Coordinate System and Data Structures

```
PuzzlePiece {
    type: RHOMBUS_01, RHOMBUS_10, RHOMBUS_11  // edge label patterns
    position: (row, col)  // triangular lattice coordinates
    orientation: 0..5     // rotation state (60° increments)
}

MosaicTile {
    type: TRIANGLE, SQUARE, RHOMBUS_30_150
    position: (x, y)     // hexagonal lattice coordinates  
    nest: A, B, C, NONE  // which corner nest (if rhombus)
}

Flock {
    rhombi: Set<RhombusId>
    orientation: (east_vector, north_vector)
    tableau_function: Map<RhombusId, Integer>
    content: Partition
}
```

### 2. Puzzle-to-Mosaic Conversion Algorithm

**Key insight**: The conversion uses a shear transformation that maps the triangular puzzle lattice to hexagonal mosaic coordinates.

```
puzzle_to_mosaic(puzzle):
    mosaic = empty_hexagon(n, d)
    
    for each piece in puzzle:
        if piece.type == RHOMBUS:
            # Rhombi are "removed" - become empty space in mosaic
            continue
        else:
            # Squares become rhombi via coordinate transform
            mosaic_pos = shear_transform(piece.position)
            
            if is_in_nest_region(mosaic_pos):
                # This square becomes a rhombus in a nest
                new_rhombus = MosaicTile(RHOMBUS_30_150, mosaic_pos, get_nest(mosaic_pos))
                mosaic.add(new_rhombus)
            else:
                # Central squares remain as triangles/squares
                new_tile = MosaicTile(infer_type(mosaic_pos), mosaic_pos, NONE)
                mosaic.add(new_tile)
    
    return mosaic

shear_transform(row, col):
    # Maps triangular lattice to hexagonal lattice
    # This is the key geometric transformation - needs empirical derivation
    x = col + 0.5 * row  
    y = row * sqrt(3)/2
    return (x, y)
```

### 3. Migration Algorithm Implementation

**Critical specification**: Migration processes rhombi in **standard order** - ordered by tableau values, with position as tiebreaker.

```
migrate_flock(mosaic, flock, direction):
    # Direction: NORTH, EAST, SOUTH, WEST
    rhombi_ordered = sort_by_standard_order(flock.rhombi, direction)
    
    for rhombus_id in rhombi_ordered:
        migrate_single_rhombus(mosaic, rhombus_id, direction)
    
    # Update flock orientation (rotates by at most 60°)
    flock.orientation = rotate_orientation(flock.orientation, direction)
    
    return updated_mosaic, updated_flock

migrate_single_rhombus(mosaic, rhombus_id, direction):
    current