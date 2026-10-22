# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Overview

I need to specify the complete implementation of Purbhoo's bijection that converts KTW puzzles to LR tableaux via mosaic migration. Based on my analysis of the paper and the previous reports, I'll focus on the concrete algorithmic details needed for implementation.

## Phase 1: Puzzle-to-Mosaic Conversion

### Data Structures

**Puzzle Representation:**
```
struct PuzzleTile {
    position: (int, int)  // triangular lattice coordinates
    type: {type0, type1, type2}  // three rhombus types from paper
    orientation: int  // 0-5 for six possible orientations
}

struct KTWPuzzle {
    size: int  // n = side length
    tiles: List[PuzzleTile]
    boundary: (string, string, string)  // (π, ρ, σ) - the 01-strings
}
```

**Mosaic Representation:**
```
struct MosaicTile {
    position: (float, float)  // hexagonal coordinates
    type: {triangle, square, rhombus}
    orientation: int
    nest: {A, B, C, none}  // which nest the tile belongs to
}

struct Mosaic {
    d: int, n: int  // parameters
    tiles: List[MosaicTile]
    nests: {A: List[rhombi], B: List[rhombi], C: List[rhombi]}
}
```

### Conversion Algorithm

The key insight from Purbhoo is that puzzles and mosaics are related by a coordinate transformation. The conversion works as follows:

1. **Remove all rhombi** from the puzzle, leaving just the triangles
2. **Transform coordinates**: Each triangle becomes either a triangle or square in the mosaic
3. **Add corner rhombi**: The "missing" rhombi get packed into the three nests

**Concrete steps:**
```python
def puzzle_to_mosaic(puzzle):
    mosaic = empty_hexagonal_region(puzzle.n, count_ones(puzzle.boundary[0]))
    
    # Transform each triangle tile
    for tile in puzzle.tiles:
        if tile.type == "triangle":
            new_pos = transform_coordinates(tile.position)
            new_tile = MosaicTile(new_pos, determine_type(tile), tile.orientation, none)
            mosaic.tiles.append(new_tile)
    
    # Pack rhombi into nests based on boundary strings
    pack_rhombi_into_nests(mosaic, puzzle.boundary)
    return mosaic
```

The coordinate transformation maps the equilateral triangle to the hexagon A'AB'BC'C. The exact transformation depends on the geometric relationship described in Purbhoo's Section 2.5.

## Phase 2: Migration Algorithm

### Flock Data Structure
```
struct Flock {
    rhombi: List[rhombus]  // subset of rhombi in a nest
    orientation: (Vector2D, Vector2D)  // (E, N) basis vectors
    tableau: Map[rhombus -> int]  // LR-tableau entries
    content: Partition  // content of the tableau
}
```

### Standard Order

The crucial concept is the "standard order" on rhombi within a flock. From the paper:
- Primary: tableau entry value (smaller entries come first)
- Secondary: position (lexicographic order in the given orientation)

```python
def standard_order(flock):
    def compare(rhombus1, rhombus2):
        entry1, entry2 = flock.tableau[rhombus1], flock.tableau[rhombus2]
        if entry1 != entry2:
            return entry1 < entry2
        # Same entry: use position in (E,N) coordinates
        return lexicographic_compare(rhombus1.pos, rhombus2.pos, flock.orientation)
    
    return sorted(flock.rhombi, key=compare)
```

### Migration Core Algorithm

The migration moves rhombi one-by-one in standard order:

```python
def migrate_flock(mosaic, flock, direction