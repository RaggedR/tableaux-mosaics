## Computational Implementation Report: KTW Puzzle to LR Tableau Migration

Building on the previous report, I'll provide concrete algorithms and data structures for implementation.

### 1. Puzzle to Mosaic: Complete Algorithm

The previous report correctly identifies the sum-based rule but needs precision on rhombus placement:

```python
def convert_puzzle_to_mosaic(puzzle_edges):
    """
    Input: Dictionary mapping (vertex1, vertex2) -> {0, 1}
    Output: List of MosaicTiles
    """
    for each triangular cell:
        edges = [bottom_edge, left_edge, right_edge]  # clockwise from bottom
        edge_sum = sum(edges)
        
        if edge_sum in [0, 3]:
            place_triangle(cell_center)
        else:
            # Rhombus orientation determined by unique edge
            if edge_sum == 1:
                unique_edge_idx = edges.index(1)
                orientation = 2 * unique_edge_idx  # 0, 2, or 4
            else:  # edge_sum == 2
                unique_edge_idx = edges.index(0)
                orientation = 2 * unique_edge_idx + 1  # 1, 3, or 5
            
            place_rhombus(cell_center, orientation)
```

### 2. Coordinate System and Data Structures

Use axial coordinates for hexagonal grid:

```python
class HexCoord:
    q: int  # x-axis (rightward)
    r: int  # y-axis (60° from x)
    
    def neighbors(self):
        # Six directions: E, NE, NW, W, SW, SE
        return [(q+1,r), (q+1,r-1), (q,r-1), 
                (q-1,r), (q-1,r+1), (q,r+1)]

class Rhombus:
    pos: HexCoord
    orientation: int  # 0-5
    nest: str  # "A", "B", or "C"
    content: int  # assigned during flock formation
    
    def covers_positions(self):
        # Returns 2 HexCoords this rhombus occupies
        return [self.pos, self.pos.shift(self.orientation)]
```

### 3. Nest Assignment and Flock Formation

```python
def assign_nests(rhombi):
    """Determine which nest each rhombus belongs to based on orientation"""
    for r in rhombi:
        if r.orientation in [0, 3]:  # horizontal
            r.nest = "A"
        elif r.orientation in [1, 4]:  # NE-SW diagonal
            r.nest = "B"
        else:  # orientation in [2, 5], NW-SE diagonal
            r.nest = "C"

def form_flock(nest_rhombi, partition):
    """
    Assign content values according to partition
    Order: top-to-bottom, left-to-right
    """
    # Sort by (-r, q) for reading order
    sorted_rhombi = sorted(nest_rhombi, key=lambda rh: (-rh.pos.r, rh.pos.q))
    
    idx = 0
    for row_num, row_size in enumerate(partition, 1):
        for _ in range(row_size):
            sorted_rhombi[idx].content = row_num
            idx += 1
```

### 4. Migration Algorithm: Precise Hexagon Finding

```python
def find_migration_hexagon(rhombus, direction, mosaic_state):
    """
    Find the minimal hexagon for migration step
    direction: one of six hex directions
    """
    candidates = []
    
    # Check all possible hexagon centers near rhombus
    for neighbor in rhombus.pos.neighbors():
        hex_tiles = get_hexagon_tiles(neighbor)
        
        if rhombus in hex_tiles and is_valid_hexagon(hex_tiles):
            # Score by projection onto migration direction
            score = dot_product(neighbor - rhombus.pos, direction)
            if