# Initial Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Overview
I need to explain how to implement the three-step bijection: Puzzle → Mosaic → Migration → LR-tableau. The test case c^(3,2,1)_{(2,1),(2,1)} = 2 means there are exactly 2 puzzles with boundary strings corresponding to partitions (2,1), (2,1), (3,2,1), and each should yield a distinct LR-tableau.

## Step 1: Puzzle to Mosaic Conversion

**Data Structure for Puzzles:**
- Triangular grid with side length n
- Each cell contains one of three rhombi types with edge labels 0/1
- Boundary data: three binary strings (π, ρ, σ) read clockwise

**Data Structure for Mosaics:**
- Hexagonal region A'AB'BC'C with specific angles and side lengths
- Tiled by: unit triangles, unit squares, unit rhombi (30°/150° angles)  
- Three "nests" at corners A, B, C containing collections of rhombi (α, β, γ)
- Standard orientations (E_A, N_A), (E_B, N_B), (E_C, N_C) at each nest

**Conversion Algorithm:**
The paper describes this as a physical "straightening" process:
1. Remove all rhombi from mosaic, leaving triangles and squares
2. Allow square corners to flex (squares become rhombi)
3. Pull corners A', B', C' outward to straighten the boundary into equilateral triangle
4. Edge rotations during straightening determine the 0/1 labels

**Implementation Challenge:** The paper doesn't give the explicit inverse mapping. I need to work out how to construct the unique mosaic from a given puzzle's boundary data.

## Step 2: Migration Algorithm

**Core Concept:**
Migration moves accessible rhombi from one nest to another via local hexagonal transformations. A "flock" is a subset of rhombi with tableau structure that preserves this structure during migration.

**Key Components:**
- **Accessible flocks:** Collections of rhombi in transformed Young diagram shapes
- **Standard order:** Total ordering on rhombi based on tableau entries and positions
- **Local moves:** Two types of hexagonal rotations (2-fold and 3-fold symmetry)
- **Wake tracking:** Upper/lower wakes determine which rhombi can pass each other

**Algorithm Structure:**
1. Identify accessible flock with specific orientation
2. Process rhombi in standard order (largest to smallest for north/east migration)
3. For each rhombus, find minimal containing hexagon and apply appropriate rotation
4. Continue until rhombus reaches target nest
5. Verify flock property is preserved

## Step 3: Reading LR-tableau

**Final Configuration:**
After migration, rhombi end up packed in a different nest with induced orientation. The positions and the preserved tableau entries directly give the LR-tableau.

**Key Issue:** The paper gives multiple bijection variants (Table 1) depending on initial orientation choices. Need to specify which one to implement.

## Implementation Gaps to Address

1. **Explicit puzzle-to-mosaic conversion:** Paper only describes the inverse direction clearly
2. **Hexagonal coordinate system:** Need concrete coordinates for all hexagonal operations  
3. **Orientation tracking:** How exactly do orientations rotate during migration?
4. **Boundary data correspondence:** Precise mapping between binary strings and rhombi collections
5. **Test case verification:** Generate the two expected LR-tableaux for c^(3,2,1)_{(2,1),(2,1)} = 2

## Next Steps
I need to fill these gaps with concrete algorithms and data structures that a coding agent can implement directly. The focus should be on the first bijection variant (orientation (-E_A, -N_A), migrate A→B) as it preserves boundary data structure.