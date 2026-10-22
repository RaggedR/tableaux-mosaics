# Implementation Report: Purbhoo's Mosaic Migration Algorithm

## Executive Summary

I'll specify a concrete algorithm for implementing Purbhoo's puzzle-to-tableau bijection. The key insight is that "migration" is a deterministic sequence of local hexagonal rotations that moves rhombi from one corner nest to another while preserving tableau properties.

## Data Structures

### Coordinate System
Use a triangular lattice with basis vectors `e1 = (1,0)` and `e2 = (1/2, √3/2)`. Every position is `(i,j)` where the actual coordinate is `i*e1 + j*e2`.

```
struct Position {
    int i, j;  // lattice coordinates
}

struct Rhombus {
    Position center;
    int orientation;  // 0,1,2 for 60° rotations
    int label;        // which nest it belongs to (A=0, B=1, C=2)
}

struct Mosaic {
    vector<Rhombus> rhombi;
    int n, d;  // puzzle parameters
}
```

### Puzzle Representation
A puzzle is a list of pieces with positions and 0/1 boundary labels. For the test case c^(3,2,1)_{(2,1),(2,1)} = 2, we expect n=5, d=2.

## Phase 1: Puzzle → Mosaic Conversion

**Algorithm**: The paper states this is a "physical transformation" - pull corners A', B', C' outward to straighten the triangle into a hexagon.

**Implementation**:
1. Parse puzzle boundary to extract the three 01-strings (π, ρ, σ)
2. For each 01-string, convert to a "nest shape" - this is a Young diagram-like arrangement of rhombi
3. Position the three nests at 120° intervals around the hexagon
4. Fill interior with triangles and squares

**Critical Detail**: The bijection between 01-strings and rhombi arrangements follows the partition correspondence from Section 1. A string like "01101" corresponds to a specific staircase pattern of rhombi.

**Concrete Steps**:
```
convert_puzzle_to_mosaic(puzzle):
    boundary_strings = extract_boundary(puzzle)  // (π, ρ, σ)
    
    // Convert each boundary string to rhombi arrangement
    nest_A = string_to_rhombi(boundary_strings[0], corner_A)
    nest_B = string_to_rhombi(boundary_strings[1], corner_B) 
    nest_C = string_to_rhombi(boundary_strings[2], corner_C)
    
    // Fill remaining hexagon with triangles/squares
    interior = fill_interior(nest_A, nest_B, nest_C)
    
    return Mosaic(nest_A + nest_B + nest_C + interior)
```

## Phase 2: Migration Algorithm

**Core Insight**: Migration moves rhombi from nest A to nest B by a sequence of local "hexagonal flips". Each flip rotates a small hexagonal region by 60° or 180°.

**Migration Direction**: The paper specifies moving in "standard order" - this means process rhombi from largest to smallest in the tableau ordering.

**Local Flip Rules**: When a rhombus encounters a hexagon, there are two cases:
- **Type (a)**: 2-fold symmetric hexagon → rotate 180°
- **Type (b)**: 3-fold symmetric hexagon → rotate 120° (in direction that makes an edge horizontal/vertical)

**Algorithm**:
```
migrate_rhombi(mosaic, source_nest, target_nest):
    // Get rhombi from source nest in standard order (largest first)
    rhombi_to_migrate = get_rhombi_in_standard_order(mosaic, source_nest)
    
    for rhombus in rhombi_to_migrate:
        while not_in_target_nest(rhombus):
            hexagon = find_minimal_hexagon_to_right(rhombus)
            
            if hexagon.is_2fold_symmetric():
                rotate_hexagon_180(hexagon)
            else if hexagon.is_3fold_symmetric():