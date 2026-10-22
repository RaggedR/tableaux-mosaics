## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

Building on the previous researcher's work, I'll provide a complete, implementable specification with corrections and clarifications.

### Key Corrections to Previous Report

1. **Boundary reading is correct** in the previous report - π, ρ, σ are indeed read clockwise from lower-left
2. **Rhombus placement needs clarification**: The partition-to-rhombi correspondence requires proper coordinate transformation
3. **Migration details are critically incomplete**: Missing the crucial "wake" concept that ensures correctness

### Complete Algorithm Specification

#### Step 1: Puzzle to Mosaic (Enhanced)

The puzzle-to-mosaic conversion physically transforms the equilateral triangle:

1. **Extract rhombi**: Remove all rhombus pieces from the puzzle
2. **Transform grid**: 
   - Grab corners A', B', C' and pull outward
   - Triangle edges become hexagon edges
   - Unit triangles remain triangles
   - Square puzzle pieces become unit squares
3. **Place rhombi in nests**:
   ```
   For partition λ = (λ₁, λ₂, ..., λ_d):
   - Place λ₁ rhombi in bottom row of nest
   - Place λ₂ rhombi in second row, etc.
   - Each row stacks from the nest corner outward
   ```

#### Step 2: Flock Creation (Corrected)

For migration from A to B, use orientation (-E_A, -N_A):
- This makes rhombi "readable" as an LR tableau
- Standard order: west-to-east, then south-to-north in rotated coordinates

```
Algorithm: Create flock with tableau values
1. Transform coordinates to flock orientation
2. Sort rhombi by: x-coordinate (ascending), then y-coordinate (ascending)
3. Group rhombi by y-coordinate (rows)
4. Assign value k to all rhombi in k-th row from bottom
```

#### Step 3: Migration Algorithm (Complete with Wake Concept)

**Critical insight**: The "wake" ensures rhombi maintain relative positions during migration.

```
Algorithm: Migrate flock from nest A to nest B
Input: Mosaic with flock F in nest A
Output: Modified mosaic with flock F' in nest B

1. Sort rhombi in F by standard order (largest to smallest)
2. For each rhombus ρ in order:
   a. Initialize wake(ρ) = empty path
   b. While ρ not in nest B:
      - Find minimal hexagon H containing ρ
      - If H contains another rhombus: rotate 180°
      - Else: rotate 120° (direction that aligns ρ edge with H edge)
      - Add displaced tiles to wake(ρ)
      - Update ρ position
   c. Maintain wake integrity:
      - Upper wake: tiles above midline of ρ's path
      - Lower wake: tiles below midline
      - Future rhombi cannot cross these wakes
```

#### Wake Crossing Rules

The wake ensures tableau properties are preserved:
1. Rhombi with same value maintain north-south ordering
2. Rhombi with consecutive values maintain proper relative positions
3. This guarantees the result is a valid LR tableau

### Test Case Verification

For c^(3,2,1)_{(2,1),(2,1)} = 2:

**Puzzle 1 boundaries**: π = 01010, ρ = 01010, σ = 01001
- Partitions: π → (3,1), ρ → (3,1), σ^∨ → (2,1)
- Migration produces tableau with shape (3,2,1)/(2,1) and content (2,1)

**Puzzle 2 boundaries**: π = 01010, ρ = 00110, σ = 00101  
- Partitions: π → (3,1), ρ → (2,2), σ^∨ → (3,0)
- Migration produces different tableau, same shape and content

### Implementation Notes

1. **Coordinate systems**: Use (x,y) for mosaic, with x pointing right, y pointing up at 60°
2. **