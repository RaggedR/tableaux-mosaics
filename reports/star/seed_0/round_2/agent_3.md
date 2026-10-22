# Specialist Analysis: Mosaic Migration Implementation

## Critical Corrections and Clarifications

### 1. **Puzzle-to-Mosaic Conversion is Wrong**

The synthesis misunderstands the fundamental conversion. The "pulling tight" operation is **not** about placing puzzle rhombi into nests based on edge labels. Instead:

**Correct Process:**
1. Remove ALL rhombi from the puzzle (leaving holes)
2. Transform the triangular grid into a hexagonal grid by:
   - Straightening the three sides into the hexagon A'AB'BC'C
   - Converting puzzle rhombi (30°-150° angles) into squares
   - Triangles remain triangles
3. The HOLES left by removed rhombi determine nest placement:
   - Holes near corner A → rhombi in nest A
   - Holes near corner B → rhombi in nest B  
   - Holes near corner C → rhombi in nest C

### 2. **Coordinate System Clarification**

For implementation, use:
- **Puzzles**: Triangular coordinates (i,j,k) with i+j+k=n
- **Mosaics**: Standard 2D coordinates (x,y) for tile centers
  - Each tile occupies a specific polygon in the plane
  - Nests are cones with apex at corners A, B, C

### 3. **Flock Formation for A→B Migration**

The canonical flock orientation is correct: (-E_A, -N_A) where:
- E_A points from A toward A' (along hexagon edge)
- N_A points from A toward B' (along hexagon edge)

**Critical**: The f-values are assigned by treating the rhombi collection α as a partition:
1. Order rhombi by their position in the nest (using the orientation)
2. Assign f-values to match the partition content

### 4. **Migration Algorithm Refinements**

**Hexagon Finding:**
```
find_minimal_hexagon(rhombus_pos):
  # Look in migration direction from rhombus
  # Find smallest hexagon containing rhombus
  # Two cases based on rhombus orientation in hexagon
```

**Rotation Rules:**
- Type I (2-fold): Always rotate 180°
- Type II (3-fold): Rotate 120° such that one rhombus edge becomes parallel to migration direction

**Standard Order During Migration:**
For orientation (E,N) and migration north:
1. Process rhombi with highest f-values first
2. Within same f-value, process westernmost first
3. This ensures wake preservation

### 5. **Wake Tracking Implementation**

```python
class Wake:
    def __init__(self, rhombus_path):
        # Path is sequence of positions during migration
        self.midline = compute_midline(rhombus_path)
        self.upper = tiles_above(self.midline)
        self.lower = tiles_below(self.midline)
    
    def is_intact(self, current_config):
        # Check if all wake tiles are in original positions
```

### 6. **Test Case Verification**

For c^(3,2,1)_{(2,1),(2,1)} = 2:
- Two puzzles with boundary (001, 01, 01)
- Each produces a distinct 2×2 tableau with entries from {1,2}
- The migration must preserve the distinction

### 7. **Critical Implementation Details**

**Mosaic Validity:**
- After placing rhombi in nests, fill remaining space uniquely with triangles and squares
- No degrees of freedom in this filling

**Migration Termination:**
- Rhombus reaches target nest when it enters the cone at B
- Orientation may rotate by 0° or 60° during migration

**Tableau Extraction:**
- Final rhombi positions in nest B form shape λ/μ
- The f-values give tableau entries
- Verify LR conditions: rows weakly increasing, columns strictly increasing

## Implementation Recommendations

1. **Start with 2D visualization** - Draw the hexagon and nests explicitly
2. **Test hexagon rotations** independently before full migration
3. **Verify wake preservation** at each step
4. **Check bijection property**: Migration A→B followed by B→A returns original mosaic

The key insight