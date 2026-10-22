I'll analyze Purbhoo's mosaic migration bijection for converting KTW puzzles to Littlewood-Richardson tableaux.

## Initial Analysis

### Core Concepts

**KTW Puzzles**: Triangular tilings with edge-labeled rhombi, where edges are labeled 0 or 1, and labels must match across shared edges. The boundary data (π, ρ, σ) are binary strings read clockwise from the three sides.

**Mosaics**: Tilings of a specific hexagon using:
- Unit equilateral triangles
- Unit squares  
- Rhombi with angles 30°/150°

The hexagon has angles 150° at corners A, B, C and 90° at corners A', B', C', with specific side lengths based on parameters d and n.

**Migration**: The key algorithm that moves rhombi through the mosaic via local transformations.

### The Three-Step Process

**Step 1: Puzzle → Mosaic**
Purbhoo describes this physically: remove rhombi, let squares flex into rhombi, and pull the corners to straighten the boundary. The 0/1 labels correspond to clockwise/counterclockwise rotations of edges.

**Step 2: Migration Algorithm**
- Start with rhombi packed in nest A (corner with 150° angle)
- Form a "flock" F = (α, orientation, labeling function)
- Move rhombi one by one to nest B via local hexagon rotations
- Process rhombi in "standard order" (specific ordering based on labels)

**Step 3: Mosaic → LR Tableau**
The final configuration of rhombi in nest B, with their labels, directly corresponds to an LR tableau.

### Key Implementation Challenges

1. **Puzzle-to-Mosaic Conversion**: The paper gives a physical intuition but not explicit coordinates. Need to determine:
   - How puzzle coordinates map to mosaic coordinates
   - How 0/1 edge labels determine rhombus placement
   - Initial positioning of triangles and squares

2. **Standard Order**: Critical for migration but definition is scattered. From Section 2.2: "X <_f Y iff either f(X) < f(Y), or f(X) = f(Y) and X is west (or northwest) of Y."

3. **Local Hexagon Operations**: Two types:
   - Type (a): 2-fold rotational symmetry → rotate 180°
   - Type (b): 3-fold rotational symmetry → rotate 120° to make rhombus edge horizontal/vertical

4. **Orientation Tracking**: Each nest has an orientation (E,N) that can rotate during migration. Critical for determining which hexagon operation to apply.

### Test Case Analysis

For c^(3,2,1)_{(2,1),(2,1)} = 2:
- n = 6 (total size), d = 3 (number of 1s)
- Two puzzles with same boundary but different internal structure
- Each should produce a distinct LR tableau of shape (3,2,1)/(2,1) with content (2,1)

### Critical Missing Details

1. **Coordinate System**: Need explicit formulas for:
   - Hexagon vertex positions
   - Tile positions in the mosaic
   - How puzzle triangular grid maps to mosaic hexagonal grid

2. **Flock Formation**: The "unique flock" with orientation (-E_A, -N_A) mentioned in Corollary proof needs explicit construction rules.

3. **Hexagon Detection**: Algorithm for finding the "smallest hexagon" containing a rhombus during migration.

4. **Wake Tracking**: The "wake" concept is crucial for correctness but needs data structure design.

### Next Steps

To make this implementable, I need to:
1. Derive explicit coordinate transformations
2. Design data structures for tiles, flocks, and wakes
3. Specify the hexagon-finding algorithm precisely
4. Work through the test case manually to verify understanding

The paper provides beautiful theory but leaves significant implementation gaps. The physical intuition helps but needs translation to discrete algorithms.