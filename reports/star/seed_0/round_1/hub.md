# Report: Implementing Purbhoo's Mosaic Migration Bijection

## Overview

The mosaic migration bijection converts KTW puzzles (triangular tilings with labeled edges) into Littlewood-Richardson tableaux through an intermediate "mosaic" representation. This provides a geometric proof of the Littlewood-Richardson rule.

## Core Data Structures

### 1. KTW Puzzles
- **Structure**: Triangular grid of side length n, tiled by unit rhombi
- **Rhombi types**: 
  - Type 0: edges labeled (0,0,0) clockwise
  - Type 1: edges labeled (1,1,1) clockwise  
  - Type 10: edges labeled (1,0,0) clockwise
- **Boundary data**: Three binary strings (π, ρ, σ) read clockwise from corners

### 2. Mosaics
- **Structure**: Hexagon with angles 150°-90°-150°-90°-150°-90°
- **Tiles**: Unit triangles, unit squares, unit rhombi (30°/150° angles)
- **Nests**: Three 150° corners where rhombi accumulate
- **Key property**: Rhombi only appear in the three nests

### 3. LR Tableaux
- **Structure**: Skew shape λ/μ filled with positive integers
- **Constraints**:
  - Weakly increasing rows (left to right)
  - Strictly increasing columns (bottom to top)
  - Lattice word condition on reverse reading order

## Algorithm Steps

### Step 1: Puzzle to Mosaic Conversion

The conversion uses a "pulling tight" metaphor:
1. Start with the KTW puzzle
2. Each puzzle rhombus becomes a mosaic rhombus (in appropriate nest)
3. The "flexible" region between rhombi becomes squares and triangles
4. Edge labels determine rhombus placement:
   - Label 0 → rhombus absent from that nest
   - Label 1 → rhombus present in that nest

**Implementation**: For each position in the puzzle:
- If occupied by rhombus type k, place corresponding rhombus in nest k
- Fill remaining space with squares/triangles to complete tiling

### Step 2: Migration Algorithm

Migration moves rhombi from one nest to another via local transformations.

**Setup**:
1. Choose source nest A and target nest B
2. Form a "flock" F = (rhombi in A, orientation, labeling function)
3. Process rhombi in "standard order" (specific total order on positions)

**Core operation** - For each rhombus:
1. Find minimal hexagon containing the rhombus
2. Apply rotation based on hexagon type:
   - Type (a): 2-fold symmetric → rotate 180°
   - Type (b): 3-fold symmetric → rotate 120° (direction chosen to align edges)
3. Repeat until rhombus reaches target nest

**Key invariant**: The "wake" (path of displaced tiles) maintains separation between rhombi, preserving their relative order.

### Step 3: Reading the LR Tableau

After migration:
1. Rhombi in target nest form a skew shape
2. The labeling function f on rhombi gives tableau entries
3. Standard order on rhombi ensures tableau inequalities are satisfied

## Test Case Analysis

For c^(3,2,1)_{(2,1),(2,1)} = 2:
- Puzzle size n=6, with d=3 ones per boundary
- Two distinct puzzles with boundary (110100, 110100, 001011)
- Each converts to distinct mosaic
- Migration produces two LR tableaux of shape (3,2,1)/(2,1) with content (2,1)

## Critical Implementation Details

1. **Coordinate system**: Use barycentric coordinates for hexagonal grid
2. **Rhombus tracking**: Maintain bijection between puzzle positions and mosaic rhombi
3. **Standard order**: For positions (i,j), use lexicographic order with specific tie-breaking
4. **Hexagon detection**: Check 6 surrounding positions for minimal containing hexagon
5. **Rotation rules**: Explicit lookup table for each hexagon configuration

## Potential Challenges

1. **Boundary handling**: Edge cases near