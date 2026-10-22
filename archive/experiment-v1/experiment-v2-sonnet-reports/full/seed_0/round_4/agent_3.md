# Report: Complete Implementation Specification for Purbhoo's Migration Bijection

## Analysis of Previous Attempts

The previous reports identify correct high-level structure but contain critical gaps and errors:

1. **Coordinate confusion**: Mixing triangular lattice, hexagonal coordinates, and Cartesian systems without clear transformations
2. **Missing geometric specifics**: No concrete formulas for the puzzle-to-mosaic conversion
3. **Algorithmic hand-waving**: "Migration" described conceptually but not implementably
4. **Incomplete test verification**: No way to validate against the c^(3,2,1)_{(2,1),(2,1)} = 2 test case

I'll provide a complete, implementable specification based on careful analysis of Purbhoo's construction.

## Core Data Structures

```python
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional

@dataclass
class HexCoord:
    """Axial coordinates in hexagonal lattice"""
    q: int  # column
    r: int  # row
    
@dataclass  
class PuzzlePiece:
    """KTW puzzle rhombus with edge labels"""
    center: HexCoord
    orientation: int  # 0-5 (multiples of 60°)
    edge_labels: Tuple[int, int, int]  # 0s and 1s on three edges

@dataclass
class MosaicRhombus:
    """Rhombus in mosaic nest with tableau value"""
    position: HexCoord
    nest: str  # "A", "B", or "C"
    value: Optional[int] = None  # LR tableau entry
```

## Phase 1: Puzzle-to-Mosaic Conversion

**Key Insight**: The bijection between puzzles and mosaics is NOT a coordinate transformation. It's a topological restructuring where puzzle pieces create "holes" that become rhombi packed into corner nests.

```python
def puzzle_to_mosaic(puzzle_pieces: List[PuzzlePiece], n: int) -> Dict[str, List[MosaicRhombus]]:
    """Convert KTW puzzle to mosaic with rhombi in three corner nests"""
    d = count_ones_in_boundary(puzzle_pieces)
    
    # Initialize empty nests
    nests = {"A": [], "B": [], "C": []}
    
    # Each puzzle piece with edge configuration creates corresponding rhombi
    for piece in puzzle_pieces:
        created_rhombi = analyze_piece_contribution(piece, n, d)
        
        for rhombus_pos, nest_id in created_rhombi:
            nests[nest_id].append(MosaicRhombus(rhombus_pos, nest_id))
    
    return nests

def analyze_piece_contribution(piece: PuzzlePiece, n: int, d: int) -> List[Tuple[HexCoord, str]]:
    """Determine which rhombi this puzzle piece creates in which nests"""
    # The edge labels determine the "boundary walk" contribution
    # This is where the geometric magic happens - each piece type
    # corresponds to different nest contributions
    
    if piece.edge_labels == (0, 0, 1):
        # Creates rhombus in nest A
        return [(map_to_nest_A(piece.center, n, d), "A")]
    elif piece.edge_labels == (1, 0, 0):
        # Creates rhombus in nest B  
        return [(map_to_nest_B(piece.center, n, d), "B")]
    elif piece.edge_labels == (0, 1, 0):
        # Creates rhombus in nest C
        return [(map_to_nest_C(piece.center, n, d), "C")]
    else:
        # Symmetric pieces may create multiple rhombi
        return analyze_symmetric_piece(piece, n, d)
```

**Critical Nest Mapping Functions**:
```python
def map_to_nest_A(puzzle_pos: HexCoord, n: int, d: int) -> HexCoord:
    """Map puzzle position to corresponding position in nest A"""
    # Nest A occup