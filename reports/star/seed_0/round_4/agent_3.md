# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Overview
The generalist's synthesis captures the structure correctly but lacks crucial implementation details. I'll provide the complete algorithm with specific data structures and procedures.

## Data Structures

```python
# Puzzle piece at position (i,j,k) in barycentric coordinates
PuzzlePiece = {
    'position': (i, j, k),  # i+j+k = n
    'type': 'triangle' or 'rhombus',
    'edge_labels': [a, b, c]  # 0s and 1s, read clockwise
}

# Mosaic tile in 2D hexagon coordinates
MosaicTile = {
    'type': 'triangle', 'square', or 'rhombus',
    'position': (x, y),
    'nest': 'A', 'B', 'C', or None  # for rhombi only
}

# Flock (collection of rhombi with tableau structure)
Flock = {
    'rhombi': [list of rhombus positions],
    'orientation': (E, N),  # unit vectors
    'f_values': {position: integer}  # tableau entries
}
```

## Stage 1: Puzzle to Mosaic Conversion

The key insight: puzzle rhombi become squares, and new rhombi are placed based on boundary strings.

```python
def puzzle_to_mosaic(puzzle_pieces, boundary_strings, n, d):
    π, ρ, σ = boundary_strings
    mosaic = []
    
    # 1. Transform puzzle coordinates to mosaic hexagon
    for piece in puzzle_pieces:
        (i, j, k) = piece['position']
        # Map triangle vertices: (n,0,0)→A', (0,n,0)→B', (0,0,n)→C'
        x = (j * (n-d) + k * (n-d/2)) / n
        y = (k * d * sqrt(3)/2) / n
        
        if piece['type'] == 'triangle':
            mosaic.append({'type': 'triangle', 'position': (x, y)})
        else:  # rhombus with mixed labels becomes square
            mosaic.append({'type': 'square', 'position': (x, y)})
    
    # 2. Place rhombi in nests based on boundary strings
    # Nest A: rhombi for 1s in π
    curr_pos_A = (0, 0)  # start at A
    for bit in π:
        if bit == 1:
            mosaic.append({
                'type': 'rhombus',
                'position': curr_pos_A,
                'nest': 'A'
            })
        curr_pos_A = step_along_boundary(curr_pos_A, bit)
    
    # Similar for nests B and C using ρ and σ
    
    return mosaic
```

## Stage 2: Migration Algorithm

Critical: The orientation determines how we read the tableau and process order.

```python
def migrate_flock_A_to_B(mosaic, n, d):
    # 1. Create flock from nest A rhombi with orientation (-E_A, -N_A)
    E_A = (0, 1)  # A to A' direction
    N_A = (cos(60°), sin(60°))  # A to B' direction
    
    flock = create_canonical_flock(
        get_rhombi_in_nest(mosaic, 'A'),
        orientation=(-E_A, -N_A)
    )
    
    # 2. Process rhombi in standard order (largest to smallest)
    ordered_rhombi = sort_by_standard_order(flock)
    
    for rhombus in ordered_rhombi:
        wake = {'upper': set(), 'lower': set(), 'midline': []}
        
        while rhombus['nest'] != 'B':
            hexagon = find_minimal_hexagon_south(rhombus, mosaic)
            
            if hexagon_has_2fold