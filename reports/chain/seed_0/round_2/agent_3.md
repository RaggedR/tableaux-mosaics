## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

The previous researcher correctly identified several critical errors in the initial report. Building on their corrections, here's a complete implementation guide.

### Data Structures

```
Puzzle: 2D array of pieces {'triangle_0', 'triangle_1', 'rhombus_01', 'rhombus_10'}
Mosaic: 
  - hexagon: vertices A', A, B', B, C', C with coordinates
  - tiles: list of (type, position, orientation) where type ∈ {triangle, rhombus}
  - rhombus_data: map from rhombus_id to (position, label)
```

### Algorithm Overview

1. **Puzzle → Mosaic Conversion**
2. **Create Canonical Flock**
3. **Migrate Flock**
4. **Extract LR-Tableau**

### Step 1: Puzzle to Mosaic Conversion

The previous researcher correctly understood this is a physical transformation, not a piece-by-piece mapping.

**Algorithm**:
```
1. Create hexagon A'AB'BC'C:
   - Place A at origin
   - A' at distance d along direction 150° from A
   - B' at distance (n-d) along direction 30° from A
   - Continue around to complete hexagon
   
2. For each puzzle piece at position (i,j,k) in barycentric coords:
   - If triangle: place directly at corresponding hexagon position
   - If rhombus: 
     a. Track edge orientations in original puzzle
     b. During "straightening", edges rotate CW or CCW
     c. Place rhombus with orientation determined by rotation direction
```

**Key insight**: The rhombi placement preserves the combinatorial structure while adapting to the hexagon geometry.

### Step 2: Create Canonical Flock

The previous researcher correctly identified the orientation reversal.

**Algorithm**:
```
1. Collect all rhombi in nest A (those packed in corner A)
2. Sort rhombi in (-E_A, -N_A) orientation:
   - Primary: by position along N_A direction (SW to NE)  
   - Secondary: by position along E_A direction (SE to NW)
3. Label rhombi 1, 2, ..., k in sorted order
4. Create flock F = (rhombi_set, (-E_A, -N_A), labeling_function)
```

### Step 3: Migration Algorithm

The previous researcher's clarifications about hexagon finding are crucial.

**Algorithm**:
```
For each rhombus ρ in standard order:
  while ρ not in nest B:
    1. Find minimal hexagon H containing ρ:
       - Search in migration direction from leftmost point of ρ
       - H must be entirely weakly right of this point
       - May be above/below, not just directly right
    
    2. Determine hexagon type:
       - Count distinct orientations of edges
       - Type A (2-fold): 2 orientations → rotate 180°
       - Type B (3-fold): 3 orientations → rotate 120°
         * Choose rotation making a ρ edge parallel to hexagon edge
    
    3. Apply rotation to contents of H
    4. Update ρ's position
```

**Wake tracking** (for correctness verification):
```
- Record path of displaced tiles as wake[ρ]
- Split into upper_wake[ρ] and lower_wake[ρ]
- Verify later rhombi don't violate wake crossing lemma
```

### Step 4: Extract LR-Tableau

**Algorithm**:
```
1. Rhombi at B form skew shape λ/μ in (E_B, N_B) orientation
2. Create tableau T:
   For each rhombus ρ at position (r,c) in skew shape:
     T[r,c] = original_label[ρ]
3. Verify LR conditions (should hold by construction)
```

### Test Case: c^(3,2,1)_{(2,1),(2,1)} = 2

For n=6, d=3:
- Two puzzles with boundary (