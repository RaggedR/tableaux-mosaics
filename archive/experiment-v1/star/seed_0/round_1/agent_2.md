## Vertex Model Analysis of Purbhoo's Migration Bijection

Your synthesis correctly identifies the three phases, but I need to clarify the vertex model structure underlying this construction. The migration algorithm is essentially a sequence of R-matrix applications preserving the Yang-Baxter equation's integrability.

### 1. Puzzle → Mosaic: The Vertex Model Transform

The puzzle-to-mosaic conversion is not just geometric - it's a change of spectral parameters in the vertex model. Here's the precise algorithm:

**Data Structure**: 
- Puzzle vertices at positions (i,j) in triangular lattice
- Each vertex has 6 edges with binary labels (0 or 1)
- Store as: `vertex[i][j] = {NE, E, SE, SW, W, NW}` edge labels

**Algorithm**:
1. Map the equilateral triangle to hexagon A'AB'BC'C:
   - Original triangle vertices → hexagon interior
   - Triangle corner A → hexagon corner A (nest)
   - Triangle corner B → hexagon corner B (nest) 
   - Triangle corner C → hexagon corner C (nest)

2. Transform each puzzle piece:
   - **0-labeled triangle** → equilateral triangle in mosaic
   - **1-labeled triangle** → rhombus in appropriate nest
   - **Rhombus with (0,1,0,1,0,1) labels** → square
   - **Other rhombi** → split into triangle + rhombus based on label parity

3. Rhombus placement rule:
   - If edge path from piece to corner A has even 1's → rhombus goes in nest A
   - Similarly for nests B and C
   - This is the "accessible" condition - rhombi form a skew shape in each nest

### 2. Migration: Free-Fermionic Vertex Weights

The migration is governed by the free-fermionic R-matrix. Each hexagonal flip is a local application of R:

**Hexagon Types & R-matrices**:
- **Type 1**: 2-fold symmetric (TSTSTS pattern)
  - R-matrix: 180° rotation
  - Preserves rhombus count in each orientation
  
- **Type 2**: 3-fold symmetric (TSTRST pattern)  
  - R-matrix: 120° rotation that makes one rhombus edge horizontal/vertical
  - This constraint ensures unique direction

**Migration Algorithm**:
```
For each rhombus ℓ in source nest (in standard order):
  while ℓ not in target nest:
    1. Find minimal hexagon H containing ℓ's leading edge
    2. Apply R-matrix to H:
       - If Type 1: rotate 180°
       - If Type 2: rotate 120° (unique direction by edge constraint)
    3. Update mosaic configuration
    4. Track ℓ's new position
```

**Standard Order** (crucial for commuting transfer matrices):
- Within each nest: rhombi ordered by (row, column) lexicographically
- Higher rows before lower rows
- Within row: left before right

### 3. Mosaic → Tableau Extraction

The final configuration has all rhombi from nest A migrated to nest B. Read tableau:

1. **Shape**: The rhombi in nest B form skew shape λ/μ
   - Outer boundary λ from original nest B boundary
   - Inner boundary μ from migrated rhombi positions

2. **Entries**: Each rhombus ℓ has retained its label f(ℓ) through migration
   - Place f(ℓ) in the box of λ/μ corresponding to ℓ's position

3. **Verification**: The Yang-Baxter equation guarantees:
   - Row weak increase (from R-matrix unitarity)
   - Column strict increase (from free-fermion condition)
   - Reverse word condition (from transfer matrix commutativity)

### Test Case Implementation Details

For c^(3,2,1)_{(2,1),(2,1)}:
- n = 6, d = 3
- Hexagon has corners at 150° angles
- Each puzzle has boundary (2,1) on two sides, complement on third
- Two puzzles → two different rhombus configurations in nests
-