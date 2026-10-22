## Migration Implementation Report: Building on Vertex Model Insights

The vertex model perspective is valuable but needs correction and completion. Here's my analysis building on what works and fixing critical gaps.

### 1. Puzzle → Mosaic Conversion: Corrected Algorithm

The sum-based rule is close but incomplete. The correct algorithm:

```
For each triangular cell in the puzzle:
1. Sum the three edge labels (0 or 1) around the cell
2. Place tile based on sum AND orientation:
   - Sum 0: Equilateral triangle (all edges were 0)
   - Sum 3: Equilateral triangle (all edges were 1)  
   - Sum 1: Rhombus - the single 1-edge determines orientation
   - Sum 2: Rhombus - the single 0-edge determines orientation
```

**Critical detail**: For rhombi, the orientation matters. The rhombus is placed so that:
- Sum 1: The edge labeled 1 in the puzzle becomes a diagonal of the rhombus
- Sum 2: The edge labeled 0 in the puzzle becomes a side of the rhombus

### 2. Data Structure for Implementation

```python
class MosaicTile:
    type: "triangle" | "rhombus"
    position: (x, y)  # hexagonal coordinates
    orientation: int  # 0-5 for 6 possible orientations
    
class Rhombus(MosaicTile):
    nest: "A" | "B" | "C"
    content: int  # which row in partition
```

### 3. Flock Formation: Complete Algorithm

The report correctly identifies orientation (-E_A, -N_A) but misses key details:

```
1. Identify all rhombi in nest A
2. Order them by position (reading order in nest):
   - Primary: top to bottom (decreasing y)
   - Secondary: left to right (increasing x)
3. Assign content f(r) based on this order:
   - First d₁ rhombi get content 1
   - Next d₂ rhombi get content 2
   - etc. (where α = (d₁, d₂, ...))
```

### 4. Migration Path Finding

The "minimal hexagon to the right" is imprecise. Correct algorithm:

```
For rhombus at position (x,y):
1. Check the 6 adjacent positions for tiles
2. Identify which form a valid hexagon containing the rhombus
3. Valid hexagons have either:
   - 2-fold symmetry: rhombus + 2 triangles + 2 rhombi
   - 3-fold symmetry: rhombus + 3 triangles
4. If multiple valid hexagons exist, choose the one whose center
   is furthest in the migration direction
```

### 5. Reading the LR Tableau

After migration to nest B:

```
1. Rhombi are now arranged in rows and columns in nest B
2. For each rhombus r with content f(r):
   - Its row position in nest B determines which row of the tableau
   - Place entry f(r) in that row
   - Within each row, entries appear left-to-right by x-coordinate
```

### 6. Test Case Worked Example

For boundary (001011, 001011, 001011):

**Puzzle 1** has rhombi arranged to give mosaic where:
- Nest A contains 3 rhombi forming partition (2,1)
- After migration: rhombi land in configuration producing tableau:
  ```
  1 1
  2
  ```

**Puzzle 2** produces different mosaic leading to:
  ```
  1 2
  1
  ```

### 7. Key Implementation Checks

1. **Orientation tracking**: Each rhombus maintains orientation through migration
2. **Collision detection**: Rhombi cannot overlap during migration
3. **Termination**: Migration ends when rhombus cannot move further right
4. **Order preservation**: Process rhombi in decreasing standard order

### 8. Vertex Model Correction

The R-matrix description is conceptually right but practically complex. For implementation:
- Think of each hexagon rotation as swapping positions while preserving local constraints
- The 120° rotation choice (horizontal vs vertical)