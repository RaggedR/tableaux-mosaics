# Specialist Report: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Analysis of the Synthesis

The synthesis correctly identifies the key disagreement about puzzle-to-mosaic transformation but makes a crucial error in the resolution. Report 4's approach is **incorrect** according to Purbhoo's paper.

## Correct Puzzle-to-Mosaic Transformation

From Purbhoo's paper (page 14): "The boundary will straighten into an equilateral triangle... the squares will become 30°/60°-rhombi. Finally note that some line segments will have rotated clockwise, while others will have rotated counterclockwise. This distinction gives the 0s and 1s on the puzzle, respectively."

This means:
1. **All** puzzle rhombi become mosaic squares (not based on edge labels)
2. Edge labels determine rotation direction during transformation
3. Mosaic rhombi come from the **empty spaces** in the mosaic packing

### Correct Implementation

```python
def puzzle_to_mosaic(puzzle_pieces, n, d):
    mosaic_tiles = []
    
    # Transform all pieces
    for piece in puzzle_pieces:
        mosaic_pos = transform_to_hexagon(piece.position, n, d)
        
        if piece.type == 'triangle':
            mosaic_tiles.append(MosaicTile('triangle', mosaic_pos))
        else:  # puzzle rhombus
            # ALL puzzle rhombi → squares
            mosaic_tiles.append(MosaicTile('square', mosaic_pos))
    
    # Pack rhombi into empty spaces at nests
    rhombi = pack_rhombi_at_nests(mosaic_tiles, n, d)
    mosaic_tiles.extend(rhombi)
    
    return mosaic_tiles

def transform_to_hexagon(barycentric, n, d):
    """Map puzzle coordinates to hexagon coordinates"""
    i, j, k = barycentric
    # Linear transformation that maps:
    # (n,0,0) → A'(0, d)
    # (0,n,0) → B'(n-d, 0)  
    # (0,0,n) → C'(n, n-d)
    x = (n-d)*j/n + n*k/n
    y = d*i/n + (n-d)*k/n
    return (x, y)
```

## Migration Algorithm Details

### Key Data Structure Corrections

```python
Rhombus = {
    'id': int,
    'position': MosaicCoord,
    'nest': 'A' | 'B' | 'C',
    'orientation': int  # 0, 60, or 120 degrees
}

Flock = {
    'rhombi': list[Rhombus],
    'orientation': tuple[Vector2D, Vector2D],  # (E, N) vectors
    'f_values': dict[rhombus_id, int],  # LR-tableau entries
    'content': list[int]  # partition [4,4,2,1,1] means content
}
```

### Migration Implementation

```python
def migrate_flock(mosaic, source_nest, target_nest):
    # 1. Create canonical flock at source
    flock = create_canonical_flock(mosaic, source_nest, orientation=(-E, -N))
    
    # 2. Order rhombi by standard order
    ordered_rhombi = sort_by_standard_order(flock)
    
    # 3. Migrate each rhombus in order
    for rhombus in ordered_rhombi:
        path = []
        current_pos = rhombus.position
        
        while not in_nest(current_pos, target_nest):
            # Find minimal hexagon to the right
            hex_center, hex_type = find_minimal_hexagon(mosaic, current_pos)
            
            # Perform rotation
            if hex_type == 'symmetric':  # 2-fold symmetry
                rotate_180(mosaic, hex_center)
            else:  # 3-fold symmetry
                rotate_120_to_align