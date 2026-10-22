# Specialist Report: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Corrections to the Synthesis

The synthesis contains several fundamental errors that must be corrected for a working implementation.

### 1. Puzzle-to-Mosaic: Complete Misconception

The synthesis fundamentally misunderstands the transformation. It's NOT about "stress" or rhombi becoming squares.

**Correct Algorithm**:
```python
def puzzle_to_mosaic(puzzle):
    # Key insight: The transformation is purely geometric
    # Each puzzle piece maps to a mosaic piece based on edge labelings
    
    mosaic_pieces = []
    
    for piece in puzzle.pieces:
        if piece.is_triangle():
            # Triangles remain triangles
            mosaic_pieces.append(Triangle(transform_position(piece)))
        else:  # puzzle rhombus
            edge_labels = piece.get_edge_labels()
            
            if all_edges_same(edge_labels):
                # Becomes a mosaic rhombus (30°/150°)
                # Goes into appropriate nest based on position
                nest = determine_nest(piece.position)
                mosaic_pieces.append(Rhombus(transform_position(piece), nest))
            else:
                # Mixed 0/1 labels → becomes square
                mosaic_pieces.append(Square(transform_position(piece)))
    
    return Mosaic(mosaic_pieces)
```

The transformation maps:
- Puzzle triangles → Mosaic triangles
- Puzzle rhombi with all 0s or all 1s → Mosaic rhombi (in nests)
- Puzzle rhombi with mixed 0/1 → Mosaic squares

### 2. Coordinate Transform

```python
def transform_coordinates(puzzle_coord, n, d):
    # Puzzle: Equilateral triangle, side n
    # Mosaic: Hexagon with specific angles
    
    # The transformation "pulls" vertices:
    # - Lower-left stays at origin
    # - Other vertices move to form hexagon
    
    # For piece at barycentric (i,j,k) in puzzle:
    # 1. Convert to Cartesian in triangle
    x_tri = j + 0.5*k
    y_tri = (sqrt(3)/2)*k
    
    # 2. Apply the "pulling" transformation
    # This is a piecewise linear map that:
    # - Maps triangle vertices to hexagon vertices
    # - Preserves edge directions within regions
    
    return apply_hexagon_transform(x_tri, y_tri, n, d)
```

### 3. Migration Algorithm - Critical Details

**Flock Initialization for Corollary 3.2**:
```python
def create_initial_flock(mosaic):
    # For the A→B migration in the bijection:
    alpha_rhombi = mosaic.get_nest_rhombi('A')
    
    # CRITICAL: Use orientation (-E_A, -N_A)
    E_A = vector_from_A_to_A_prime()
    N_A = vector_from_A_to_B_prime()
    
    orientation = (-E_A, -N_A)
    
    # Lemma 2.7: Unique labeling for this orientation
    f_values = compute_unique_labeling(alpha_rhombi, orientation)
    
    return Flock(alpha_rhombi, orientation, f_values)
```

**Migration Process**:
```python
def migrate_single_rhombus(rhombus, mosaic, direction):
    while not in_target_nest(rhombus):
        # Find minimal hexagon to the right (in migration direction)
        hex = find_minimal_hexagon(rhombus, mosaic, direction)
        
        if hex.has_2fold_symmetry():
            # Type (a): 180° rotation
            rotate_hexagon_contents(hex, 180)
        else:  # 3-fold symmetry
            # Type (b): 120° rotation
            # CRITICAL: Choose rotation that makes rhombus edge
            # horizontal or vertical
            angle = choose_rotation_angle(rhombus, hex)