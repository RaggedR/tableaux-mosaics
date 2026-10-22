# Report: Implementing Purbhoo's Mosaic Migration Bijection

## Analysis of Previous Reports

The previous reports provide good structural foundations but miss critical algorithmic details. They correctly identify the three-phase process but lack specificity about coordinate transforms, the hexagonal flip operations, and tableau reconstruction. Most importantly, they don't provide concrete test case verification methods.

## Key Implementation Challenges

1. **Coordinate System Ambiguity**: The puzzle-to-mosaic transformation requires precise geometric mapping between triangular lattice (puzzle) and hexagonal coordinates (mosaic).

2. **Migration Mechanics**: The "minimal hexagon" detection and rotation rules need algorithmic specification.

3. **Standard Order**: Computing the lexicographic ordering that drives migration sequence.

4. **Tableau Reconstruction**: Converting final rhombi positions back to LR tableau format.

## Concrete Implementation Specification

### 1. Data Structures

```python
# Core geometric structures
Point = (float, float)  # Hexagonal coordinates (q, r)

class PuzzlePiece:
    position: Point
    edges: [int, int, int]  # 0/1 labels on three edges (clockwise)
    
class KTWPuzzle:
    size: int  # n
    pieces: List[PuzzlePiece]
    boundary: (str, str, str)  # (π, ρ, σ) - boundary 01-strings

class MosaicTile:
    position: Point
    type: str  # "triangle", "square", "rhombus"
    nest: str  # "A", "B", "C", or None
    
class Mosaic:
    n: int
    d: int  # number of 1s in boundary strings
    tiles: Dict[Point, MosaicTile]
    nests: Dict[str, List[Point]]  # nest -> rhombi positions

class Flock:
    rhombi_positions: List[Point]
    orientation: (Point, Point)  # (E, N) unit vectors
    tableau_values: Dict[Point, int]
    content: List[int]  # partition
```

### 2. Phase 1: Puzzle-to-Mosaic Conversion

**Core Algorithm:**

```python
def puzzle_to_mosaic(puzzle: KTWPuzzle) -> Mosaic:
    # Step 1: Create hexagonal region A'AB'BC'C
    mosaic = create_hexagonal_region(puzzle.size)
    
    # Step 2: Map each puzzle piece
    for piece in puzzle.pieces:
        mosaic_pos = transform_coordinates(piece.position)
        
        if piece_creates_gap(piece):
            # This piece corresponds to "missing space" that becomes a nest rhombus
            nest = determine_nest(mosaic_pos)
            mosaic.nests[nest].append(mosaic_pos)
            mosaic.tiles[mosaic_pos] = MosaicTile(mosaic_pos, "rhombus", nest)
        else:
            # This piece becomes a triangle/square in the mosaic interior
            tile_type = determine_interior_type(piece, mosaic_pos)
            mosaic.tiles[mosaic_pos] = MosaicTile(mosaic_pos, tile_type, None)
    
    return mosaic
```

**Coordinate Transformation:**
The key insight is that the puzzle triangle maps to the mosaic hexagon via an affine transformation. Based on Purbhoo's construction:

```python
def transform_coordinates(puzzle_pos: Point) -> Point:
    # Empirical transformation from triangular to hexagonal lattice
    # This maps equilateral triangle vertices to hexagon A'AB'BC'C
    q, r = puzzle_pos
    
    # Shear transformation that "straightens" the puzzle
    new_q = q + 0.5 * r
    new_r = r * math.sqrt(3) / 2
    
    return (new_q, new_r)
```

**Nest Assignment:**
```python
def determine_nest(pos: Point) -> str:
    # Check which of the three 60° sectors the position falls into
    angle = math.atan2(pos[1], pos[0])
    
    if -math.pi/