# Specialist Report: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Analysis of the Synthesis

The synthesis correctly identifies the key disagreement about puzzle-to-mosaic transformation. However, it misinterprets Report 4's correction. Let me clarify based on careful reading of Purbhoo's paper.

## Correct Puzzle-to-Mosaic Transformation

The transformation is **geometric**, not based on edge labels. Here's what actually happens:

```python
def puzzle_to_mosaic(puzzle_pieces, n, d):
    """
    Transform puzzle to mosaic via geometric deformation:
    1. Remove all rhombi from puzzle
    2. Apply affine transformation that maps triangle to hexagon
    3. Rhombi become gaps that must be filled
    """
    mosaic_tiles = []
    
    # Step 1: Transform coordinate system
    # Puzzle uses barycentric (i,j,k) with i+j+k=n
    # Mosaic uses 2D coordinates in hexagon
    
    for piece in puzzle_pieces:
        if piece.type == 'triangle':
            # Triangles stay triangles
            mosaic_pos = transform_to_hexagon(piece.position, n, d)
            mosaic_tiles.append({
                'type': 'triangle',
                'position': mosaic_pos
            })
    
    # Step 2: Fill gaps with squares and mosaic rhombi
    gaps = identify_gaps(mosaic_tiles)
    
    for gap in gaps:
        if gap.near_corner():
            # Gaps near corners A, B, C become rhombi
            nest = gap.closest_corner()
            mosaic_tiles.append({
                'type': 'rhombus',
                'position': gap.position,
                'nest': nest
            })
        else:
            # Interior gaps become squares
            mosaic_tiles.append({
                'type': 'square',
                'position': gap.position
            })
    
    return mosaic_tiles
```

The key insight from Purbhoo: "squares will become 30°/60°-rhombi" under the deformation. This means puzzle rhombi → mosaic squares (not the other way around).

## Detailed Migration Algorithm

```python
def migrate_flock(mosaic, source_nest, target_nest):
    """
    Migration moves rhombi from source_nest to target_nest
    via sequence of local hexagon rotations
    """
    # Step 1: Create flock with orientation (-E_A, -N_A)
    rhombi_in_A = [tile for tile in mosaic if tile.nest == 'A']
    
    # Orientation vectors for nest A
    E_A = vector(1, 0)  # Points along AA'
    N_A = vector(-0.5, sqrt(3)/2)  # Points along AB'
    
    flock = {
        'rhombi': rhombi_in_A,
        'orientation': (-E_A, -N_A),
        'f_values': assign_tableau_values(rhombi_in_A, (-E_A, -N_A))
    }
    
    # Step 2: Process rhombi in standard order
    # For south migration: process from max to min
    sorted_rhombi = sort_by_standard_order(flock)
    
    for rhombus in sorted_rhombi:
        migrate_single_rhombus(rhombus, mosaic, target_direction='south')
    
    return mosaic
```

## Single Rhombus Migration

```python
def migrate_single_rhombus(rhombus, mosaic, direction):
    """
    Move one rhombus via hexagon rotations
    """
    while not rhombus.in_target_nest():
        # Find minimal hexagon containing rhombus
        hex_tiles = find_minimal_hexagon(rhombus, mosaic, direction)
        
        if hex_pattern_is_symmetric_2fold(hex_tiles):
            # Rotate 180°
            rotate_tiles(hex_tiles, angle=180)
        elif hex_pattern_is_symmetric_3fold(hex_tiles):
            #