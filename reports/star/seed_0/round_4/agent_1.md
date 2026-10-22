# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Overview
The migration bijection transforms KTW puzzles into Littlewood-Richardson tableaux via an intermediate mosaic representation. The key insight is that rhombi flow through the mosaic via local hexagon rotations, preserving a labeling that becomes the tableau entries.

## Data Structures

```python
# Core geometric types
Point = tuple[float, float]
Edge = tuple[Point, Point, int]  # endpoints and label (0 or 1)

# Puzzle pieces
Triangle = namedtuple('Triangle', ['vertices', 'edge_labels'])
Rhombus = namedtuple('Rhombus', ['vertices', 'edge_labels', 'nest'])

# Mosaic pieces  
MosaicTriangle = namedtuple('MosaicTriangle', ['vertices'])
MosaicSquare = namedtuple('MosaicSquare', ['vertices'])
MosaicRhombus = namedtuple('MosaicRhombus', ['vertices', 'nest', 'label'])
```

## Stage 1: Puzzle to Mosaic Conversion

The "pulling tight" operation maps puzzle coordinates to hexagon coordinates:

```python
def puzzle_to_mosaic(puzzle, n, d):
    # Hexagon vertices (clockwise from lower-left)
    A_prime = (0, d)
    A = (0, 0)  
    B_prime = (n-d, 0)
    B = (n, 0)
    C_prime = (n, n-d)
    C = (d, n-d)
    
    mosaic_tiles = []
    
    # Map puzzle triangles to mosaic triangles
    for triangle in puzzle.triangles:
        new_vertices = [map_coordinate(v, n, d) for v in triangle.vertices]
        mosaic_tiles.append(MosaicTriangle(new_vertices))
    
    # Map puzzle rhombi to mosaic squares
    for rhombus in puzzle.rhombi:
        new_vertices = [map_coordinate(v, n, d) for v in rhombus.vertices]
        mosaic_tiles.append(MosaicSquare(new_vertices))
    
    # Add boundary rhombi from puzzle boundary data
    pi, rho, sigma = puzzle.boundary_data
    
    # Nest A rhombi from π string
    for i, bit in enumerate(pi):
        if bit == 1:
            pos = A + i * (B_prime - A) / (n-d)
            rhombus = create_rhombus_at(pos, orientation='A')
            mosaic_tiles.append(MosaicRhombus(rhombus.vertices, 'A', None))
    
    # Similarly for nests B (from ρ) and C (from σ)
    
    return mosaic_tiles

def map_coordinate(puzzle_coord, n, d):
    # Barycentric (i,j,k) to hexagon coordinates
    i, j, k = puzzle_coord  # i+j+k = n
    
    # Map triangle vertices to hexagon vertices
    x = (j*(n-d) + k*d) / n
    y = k*(n-d) / n
    
    return (x, y)
```

## Stage 2: Migration Algorithm

Migration moves rhombi from nest A to nest B via local hexagon rotations:

```python
def migrate_A_to_B(mosaic, alpha_rhombi):
    # Create flock with orientation (-E_A, -N_A)
    E_A = normalize((0, 1))  # A to A'
    N_A = normalize((1, 1))  # A to B'
    
    flock = Flock(
        rhombi=alpha_rhombi,
        orientation=(-E_A, -N_A),
        f_values=assign_canonical_labels(alpha_rhombi, (-E_A, -N_A))
    )
    
    # Sort by standard order (largest first for south migration)
    sorted_rhombi = sorted(flock.rhombi, key=lambda r: 
        