# Synthesis Report: Implementing Purbhoo's Mosaic Migration Bijection

## Executive Summary

The four specialist reports reveal critical disagreements about the puzzle-to-mosaic transformation but converge on the migration algorithm structure. The key tension centers on how puzzle pieces transform: whether rhombi become squares based on edge labels (Reports 2,4) or through coordinate transformation (Reports 1,3). Report 4's correction appears most aligned with Purbhoo's paper.

## Data Structures (Consensus)

```python
# Coordinate systems
PuzzleCoord = tuple[int, int, int]  # Barycentric (i,j,k), i+j+k=n
MosaicCoord = tuple[float, float]    # 2D Cartesian in hexagon

# Pieces
PuzzlePiece = {
    'type': 'triangle' | 'rhombus',
    'position': PuzzleCoord,
    'edge_labels': [int, int, int]  # 0/1 labels clockwise
}

MosaicTile = {
    'type': 'triangle' | 'square' | 'rhombus',
    'position': MosaicCoord,
    'nest': 'A' | 'B' | 'C' | None  # rhombi only
}

Flock = {
    'rhombi': list[MosaicRhombus],
    'orientation': tuple[Vector2D, Vector2D],  # (E, N) unit vectors
    'f_values': dict[rhombus_id, int]  # tableau entries
}
```

## Stage 1: Puzzle-to-Mosaic Conversion

### Critical Resolution

Report 4 provides the clearest correction: the transformation is based on **edge labels**, not just coordinates:

```python
def puzzle_to_mosaic(puzzle_pieces, n, d):
    mosaic = []
    
    for piece in puzzle_pieces:
        # Transform coordinates (all reports agree on hexagon shape)
        mosaic_pos = transform_coords(piece.position, n, d)
        
        if piece.type == 'triangle':
            # Triangles → Triangles (unanimous)
            mosaic.append(MosaicTile('triangle', mosaic_pos))
        
        else:  # rhombus
            # KEY INSIGHT from Report 4:
            if all(label == 0 for label in piece.edge_labels):
                # All 0s → rhombus in nest (based on position)
                nest = determine_nest_from_position(mosaic_pos)
                mosaic.append(MosaicTile('rhombus', mosaic_pos, nest))
                
            elif all(label == 1 for label in piece.edge_labels):
                # All 1s → rhombus in nest (based on position)
                nest = determine_nest_from_position(mosaic_pos)
                mosaic.append(MosaicTile('rhombus', mosaic_pos, nest))
                
            else:
                # Mixed 0/1 → square
                mosaic.append(MosaicTile('square', mosaic_pos))
    
    return mosaic

def transform_coords(puzzle_coord, n, d):
    i, j, k = puzzle_coord
    # Consensus transformation mapping triangle to hexagon
    # Maps (n,0,0)→A', (0,n,0)→B', (0,0,n)→C'
    x = (j * (n-d) + k * d) / n  
    y = k * (n-d) * sqrt(3)/2 / n
    return (x, y)
```

### Hexagon Vertices (All Reports Agree)
```python
A_prime = (0, d)
A = (0, 0)
B_prime = (n-d, 0)
B = (n, 0)
C_prime = (n, n-d)
C = (d, n-d)
```

## Stage 2: Migration Algorithm

### Consensus Implementation

All reports agree on the core migration structure:

```python
def migrate_A_to_B(mosaic):
    # 1. Create flock with specific