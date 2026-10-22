## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

Building on the previous researcher's corrections, I'll provide a complete implementation guide with concrete details and fixes to remaining gaps.

### Data Structures

```
Puzzle: Dictionary mapping (i,j,k) → piece_info
  - (i,j,k): barycentric coordinates, i+j+k=n
  - piece_info: {type, edges} where edges maps directions to 0/1

Mosaic:
  - vertices: {A': (0, d√3/2), A: (0, 0), B': (n-d, 0), 
              B: (n-d/2, (n+d)√3/2), C': (-d/2, (n+d)√3/2), 
              C: (-n+d, 0)}
  - tiles: Dictionary mapping positions → {type, orientation}
  - rhombi_in_nests: {A: [], B: [], C: []} 
  
Rhombus: {id, position, orientation_angle, entry_value}
```

### Step 1: Puzzle to Mosaic Conversion

The previous report correctly identifies this as a physical transformation. Here's the precise algorithm:

**Algorithm**:
```
1. Map puzzle triangles to hexagon coordinates:
   For each triangle at (i,j,k):
     hex_pos = (i-k)/(n-d) * B' + j/d * (C-B) + k/n * (A'-C')
     
2. Process rhombi via "straightening":
   a. Track deformation: edges labeled 0 rotate CW, edges labeled 1 rotate CCW
   b. Each rhombus has two 0-edges and two 1-edges
   c. Final orientation determined by which edges align with hex grid
   
3. Pack rhombi into nests:
   - Nest A: rhombi with edges parallel to A-A' and A-B'
   - Nest B: rhombi with edges parallel to B-B' and B-C'
   - Nest C: rhombi with edges parallel to C-C' and C-A'
```

### Step 2: Create Canonical Flock

Key fix: The labeling must respect the **reversed** orientation.

**Algorithm**:
```
1. Sort rhombi in nest A using orientation (-E_A, -N_A):
   - E_A points from A to A' 
   - N_A points from A to B'
   - In reversed orientation: sort by increasing distance along N_A,
     then by increasing distance along E_A
     
2. Assign values 1, 2, ..., maintaining weak increase along -E_A 
   and strict increase along -N_A
   
3. This creates the unique flock with given content
```

### Step 3: Migration Algorithm

Critical clarification on hexagon finding:

**Algorithm**:
```
For each rhombus ρ in standard order:
  while ρ not in nest B:
    1. Find minimal hexagon:
       - Start from rightmost vertex of ρ (in migration direction)
       - Scan right until finding 6 tiles forming a hexagon
       - "Minimal" means no smaller hexagon exists between ρ and this one
       
    2. Classify and rotate:
       Type A (rhombus + 2 triangles + rhombus + 2 triangles):
         - Has 180° symmetry, rotate 180°
       Type B (3 rhombi + 3 triangles alternating):  
         - Has 120° symmetry
         - Rotate ±120° so that some edge of ρ becomes horizontal/vertical
         
    3. Update all tile positions within hexagon
```

**Wake Tracking Implementation**:
```
- upper_wake[ρ]: tiles above ρ's path
- lower_wake[ρ]: tiles below ρ's path
- Check: if ρ₁ migrates before ρ₂, and ρ₂ starts above ρ₁'s midline,
  then ρ₂ cannot cross below midline (ensures standard order preserved)
```

### Step 4: Extract LR-