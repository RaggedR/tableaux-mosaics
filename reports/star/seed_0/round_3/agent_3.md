# Implementation Report: Purbhoo's Mosaic Migration Bijection

## Overview
The bijection converts KTW puzzles to LR tableaux via an intermediate mosaic representation. The key insight is that puzzles encode the same combinatorial data as tableaux, just in different geometric forms.

## Step 1: Puzzle-to-Mosaic Conversion

The generalist's synthesis contains a critical error. The "pulling tight" operation does NOT create holes where rhombi are removed. Instead:

**Correct Algorithm:**
1. Each puzzle piece maps directly to mosaic tiles:
   - Puzzle triangle → Mosaic triangle (unchanged)
   - Puzzle rhombus → Mosaic square OR rhombus (depending on edge labels)

2. **Key insight**: A puzzle rhombus with edge labels determines its mosaic fate:
   ```
   If northeast edge = 0 and northwest edge = 0: → Square
   If northeast edge = 1 and northwest edge = 0: → Rhombus in nest C
   If northeast edge = 0 and northwest edge = 1: → Rhombus in nest A
   If northeast edge = 1 and northwest edge = 1: → Rhombus in nest B
   ```

3. **Coordinate mapping**: For puzzle position (i,j,k) where i+j+k=n:
   ```
   # Puzzle uses barycentric coords in equilateral triangle
   # Mosaic uses 2D coords in hexagon
   
   x = j + (k-i)/2
   y = √3/2 * k
   ```

## Step 2: Migration Algorithm

### Data Structures
```
Rhombus:
  position: (x,y)
  nest: A/B/C
  f_value: int (assigned during flock formation)

Flock:
  rhombi: list[Rhombus]
  orientation: (E,N) vectors
  
Wake:
  midline: list[(x,y)]  # path centers
  upper_tiles: set[Tile]
  lower_tiles: set[Tile]
```

### Migration Process

1. **Create canonical flock** at nest A:
   ```
   # For boundary (α,β,γ), α determines the flock
   # Use orientation (-E_A, -N_A) for A→B migration
   
   def create_flock(rhombi_in_A, partition_alpha):
     # Sort rhombi by lexicographic position in orientation
     sorted_rhombi = sort_by_position(rhombi_in_A, -E_A, -N_A)
     
     # Assign f-values according to partition
     index = 0
     for part_num, part_size in enumerate(partition_alpha):
       for i in range(part_size):
         sorted_rhombi[index].f_value = part_num + 1
         index += 1
   ```

2. **Migration order**: Process rhombi in REVERSE standard order for A→B:
   ```
   # Standard order: first by f-value, then by position
   def standard_order(r1, r2):
     if r1.f_value != r2.f_value:
       return r1.f_value < r2.f_value
     return position_less_than(r1.pos, r2.pos, orientation)
   ```

3. **Local hexagon flips**:
   ```
   def migrate_rhombus(rhombus, direction):
     while not in_target_nest(rhombus):
       hex = find_minimal_hexagon(rhombus, direction)
       if hex.type == "2-fold":
         rotate_180(hex)
       else:  # 3-fold
         # Rotate 120° to make rhombus edge horizontal/vertical
         if makes_horizontal(120_cw):
           rotate_120_cw(hex)
         else:
           rotate_120_ccw(hex)
       update_position(rhombus)
       record_wake(rhombus)
   ```

## Step 3: Extract LR Tableau

After migration to nest B:
1. Rhombi positions encode the tableau shape
2. f-values become tableau entries
3. Read entries in French notation (bottom