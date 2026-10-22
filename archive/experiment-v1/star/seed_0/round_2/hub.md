## Synthesis: Implementing Purbhoo's Mosaic Migration Bijection

After analyzing the specialist reports, I'll synthesize a unified implementation strategy that addresses the key tensions and fills critical gaps.

### Core Insight: Three Complementary Views

The specialists offer three valid perspectives on the same algorithm:
1. **Growth diagram view**: Migration as a sequence of local rules preserving a partial order
2. **Vertex model view**: Hexagonal flips as R-matrix applications preserving integrability  
3. **Geometric view**: Physical transformation of puzzle pieces into mosaic tiles

These aren't contradictory—they're different lenses revealing different aspects of why the algorithm works.

### Unified Data Structures

Combining the specialists' suggestions:

```
// Hexagonal coordinate system (axial coordinates)
Position: (q, r) where s = -q - r implicitly

// Puzzle piece (before transformation)
PuzzlePiece: {
  vertices: [(x,y)],  // in triangular lattice
  edge_labels: [0|1, 0|1, 0|1],  // clockwise
  type: TRIANGLE | RHOMBUS
}

// Mosaic tile (after transformation)
MosaicTile: {
  position: (q, r),
  type: TRIANGLE | SQUARE | RHOMBUS_150,  // 150° angle rhombus
  orientation: 0..5,  // multiples of 60°
  rhombus_id: int | null  // for tracking through migration
}

// Collection of rhombi with tableau structure
Flock: {
  rhombi: Map<id -> position>,
  orientation: {E: (eq, er), N: (nq, nr)},  // basis vectors
  labels: Map<id -> int>,  // tableau values
  nest: A | B | C
}
```

### Phase 1: Puzzle → Mosaic (Resolving Tensions)

The specialists disagree on details, but the core algorithm is:

1. **Coordinate Transformation**:
   - Map puzzle triangle vertices (0,0), (n,0), (n/2,n√3/2) to hexagon interior
   - The "pulling corners" creates the hexagon A'AB'BC'C
   - Use affine transform: puzzle (i,j) → mosaic (q,r) preserving adjacencies

2. **Piece Conversion** (reconciling reports):
   - All triangles → triangles (unchanged)
   - Puzzle rhombi → removed initially, creating gaps
   - Gaps filled by squares (which appear as 60°/120° rhombi in mosaic)
   - 150°/30° rhombi placed in nests based on boundary 1s

3. **Nest Filling Algorithm**:
   ```
   For each 1 in boundary string π at position i:
     Place rhombus at position i (from bottom) in nest A
   Similar for ρ→B, σ→C
   ```

### Phase 2: Migration (Unified Algorithm)

**Initial Setup**:
1. Form flock F on nest A rhombi with orientation (-E_A, -N_A)
2. Assign labels using the canonical construction:
   - Order rhombi by position (northwest to southeast)
   - Label 1, 2, 3, ... in this order

**Migration Process**:
```
// Migrate from A to B (south direction)
For each rhombus ℓ in F (reverse standard order by label):
  While ℓ not in nest B:
    H = find_minimal_hexagon(ℓ, direction="right")
    if H has 2-fold symmetry:
      rotate_tiles(H, 180°)
    else:  // 3-fold symmetry
      // Rotate 120° to make one ℓ edge horizontal/vertical
      angle = determine_unique_rotation(ℓ, H)
      rotate_tiles(H, angle)
    update_position(ℓ)
    track_orientation_change(F)
```

**Key Implementation Details**:
- "Minimal hexagon" = smallest hexagon fully containing ℓ and extending right
- Standard order: by label, then by position if tied
- Orientation vectors rotate by at most 60° total