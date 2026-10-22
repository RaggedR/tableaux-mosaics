# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Executive Summary for Coding Agent

You need to implement a bijection that transforms KTW puzzles into LR tableaux via mosaic migration. This is **not a growth diagram** in the Fomin sense - there are no face labels or local rules on directed graphs. Instead, this is a geometric bijection using hexagonal tiling transformations.

The key insight: rhombi in mosaics carry tableau entries and migrate through local hexagonal flips while preserving tableau structure via a "standard order" relation.

## Data Structures

### Coordinate System
Use axial coordinates for the hexagonal mosaic:
```
struct HexCoord { int q, r; }  // axial coordinates
struct Point { double x, y; }  // for geometric calculations
```

The hexagon has vertices at positions that form 60°/120° angles. Use a coordinate system where the hexagon center is origin.

### Puzzle Representation
```
struct PuzzleEdge {
    int label;  // 0 or 1
    HexCoord pos;
    int direction;  // 0-5 for six directions
}

struct Puzzle {
    vector<PuzzleEdge> edges;
    vector<int> boundary[3];  // three boundary strings π, ρ, σ
}
```

### Mosaic Representation  
```
enum TileType { TRIANGLE, SQUARE, RHOMBUS }
enum Nest { A, B, C }  // three corner nests

struct Rhombus {
    HexCoord center;
    int orientation;  // 0-2 for three orientations
    int tableau_entry;  // the LR tableau value
    Nest current_nest;
}

struct Mosaic {
    vector<Rhombus> rhombi;
    map<HexCoord, TileType> tiles;
    vector<Rhombus> nest_contents[3];  // rhombi in each nest
}
```

## Algorithm Step 1: Puzzle → Mosaic Conversion

**Critical geometric transformation**: The paper describes this as "grabbing corners A', B', C' and pulling tight" to straighten the hexagon into triangle.

### Implementation Approach:
1. **Boundary Analysis**: For each boundary segment, count 0s and 1s to determine rhombi shapes
2. **Nest Population**: Place rhombi in corner nests A, B, C according to boundary data
3. **Interior Filling**: Fill hexagon interior with triangles/squares

```python
def puzzle_to_mosaic(puzzle):
    mosaic = Mosaic()
    
    # Extract boundary data (π, ρ, σ) from puzzle edges
    boundaries = extract_boundaries(puzzle)
    
    # Convert each boundary string to rhombus collection
    for nest_id, boundary_string in enumerate(boundaries):
        rhombi = boundary_to_rhombi(boundary_string, nest_id)
        mosaic.nest_contents[nest_id] = rhombi
    
    # Fill interior with triangles/squares
    fill_interior(mosaic)
    
    return mosaic
```

**Key insight from paper**: The bijection is "straightening" - 0s correspond to westward steps, 1s to northward steps in the boundary walk.

## Algorithm Step 2: Migration Process

This is the core algorithm. Migration moves rhombi from one nest to another via local hexagonal transformations.

### Standard Order on Rhombi
The paper defines a "standard order" ≺ on rhombi within each nest based on tableau structure:
- For northward/eastward migration: start with maximal rhombus  
- For southward/westward migration: start with minimal rhombus

```python
def compute_standard_order(rhombi, nest_orientation):
    # Order based on tableau values and geometric positions
    # Entry k comes before entry k+1
    # Among equal entries, use geometric precedence
    return sorted(rhombi, key=lambda r: (r.tableau_entry, geometric_order(r)))
```

### Local Hexagonal Transformations
**Critical detail from paper**: Migration proceeds by examining the "smallest hexagon" containing each rhombus and applying rotational transformations:

```python
def migrate_rhombus(rhombus,