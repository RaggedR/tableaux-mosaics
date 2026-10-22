## Analysis of Purbhoo's Mosaic Migration Implementation

Building on the previous researcher's work, I'll clarify remaining ambiguities and provide concrete implementation details.

### Key Clarifications and Corrections

#### 1. **Puzzle-to-Mosaic Conversion: The Missing Details**

The previous report correctly identifies that rhombi with different diagonal labels become rhombi in the mosaic, but misses the orientation mapping:

**Correct Algorithm**:
- Each puzzle rhombus has edges labeled 0 or 1
- A rhombus with clockwise edges (a,b,c,d) starting from top maps to:
  - Square: if a=c and b=d (both diagonals same)
  - Rhombus oriented at angle θ: if exactly one diagonal differs
    - θ = 0° if top-bottom diagonal differs (a≠c, b=d)
    - θ = 60° if NE-SW diagonal differs
    - θ = 120° if NW-SE diagonal differs

**Critical insight**: The 150° angles in the mosaic hexagon arise naturally when puzzle triangles at the boundary maintain their edge orientations while the interior "relaxes" according to the above rules.

#### 2. **Flock Labeling: The Correct Orientation**

The previous report has the right idea but needs precision:

**For α at nest A with orientation (-E_A, -N_A)**:
- E_A points from A toward A' (southeast)
- N_A points from A toward B' (northeast)
- So (-E_A, -N_A) means northwest is "north" and southwest is "east"

**Labeling algorithm**:
```
1. Pack rhombi into rows, bottom-to-top in the (-N_A) direction
2. Within each row, order west-to-east in the (-E_A) direction
3. Assign labels:
   Row 1 (bottom): all get label 1
   Row k: for each rhombus at position j:
     label[k][j] = max(label[k][j-1], label[k-1][j] + 1)
```

#### 3. **Migration Mechanics: The Hexagon Finding Algorithm**

The "smallest enclosing hexagon" needs precise definition:

**Finding the migration hexagon**:
1. From rhombus center, cast a ray in the migration direction
2. Find the first point where this ray exits the current tile configuration
3. The minimal hexagon is the smallest regular hexagon that:
   - Contains the rhombus
   - Has boundary passing through this exit point
   - Has edges parallel to the three mosaic directions

**Type B rotation disambiguation**:
When rotating 120° in a type B hexagon, the two choices correspond to whether the rhombus moves clockwise or counterclockwise around the hexagon center. The rule "make an edge horizontal or at ±60°" uniquely determines which rotation based on the rhombus's current orientation.

#### 4. **Wake Mechanics and Order Preservation**

The Wake Crossing Lemma ensures tableau properties:

**Concrete implementation**:
```
For each rhombus ρ in migration order:
  1. Record wake_upper[ρ] = list of tiles above midline
  2. Record wake_lower[ρ] = list of tiles below midline
  3. When migrating later rhombus σ:
     - If σ starts above ρ's midline and wake_upper[ρ] intact:
       σ cannot cross below ρ's midline
     - This preserves σ > ρ in final configuration
```

#### 5. **Reading the Final Tableau**

After migration from A to B:
1. Rhombi at B form a skew shape λ/μ where:
   - λ corresponds to the outer boundary of B's nest
   - μ corresponds to the inner boundary (rhombi positions)
2. The standard order at B: northwest is highest, southeast is lowest
3. The preserved labels form an LR-tableau with:
   - Rows increasing west-to-east (by construction)
   - Columns increasing south-to-north (by wake preservation)
   - LR-word property (by careful analysis of the migration order)

### Complete Algorithm for Test Case

For c^(3,2,1)