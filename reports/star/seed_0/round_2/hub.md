# Synthesis Report: Implementing Purbhoo's Mosaic Migration Bijection

## Common Ground

All specialists agree on the core structure:
1. **Three-step process**: Puzzle → Mosaic → Migration → Tableau
2. **Critical concepts**: Nests, flocks, standard order, wake preservation
3. **Hexagonal structure**: Hexagon with alternating angles (150°, 90°) and side lengths (d, n-d)
4. **Test case**: c^(3,2,1)_{(2,1),(2,1)} = 2 with two distinct puzzles producing different tableaux

## Key Tensions and Resolutions

### 1. **Puzzle-to-Mosaic Conversion**
- **Tension**: "Pulling tight" metaphor vs precise placement rules
- **Resolution**: Use edge-label based assignment:
  ```
  For each puzzle rhombus at position (i,j,k):
    - If south edge = 1: place in nest C
    - If northwest edge = 1: place in nest A  
    - If northeast edge = 1: place in nest B
  ```

### 2. **Coordinate Systems**
- **Tension**: Triangular lattice (i,j) vs (i,j,k) with i+j+k=n
- **Resolution**: Use triangular coordinates (i,j,k) where i+j+k=n for puzzles, convert to hexagonal/axial coordinates (q,r) for mosaics

### 3. **Hexagon Types**
- **Tension**: Conflicting descriptions of hexagon configurations
- **Resolution**: Two types exist:
  ```
  Type I (2-fold symmetry): 2 rhombi + 2 triangles + 2 squares
  Type II (3-fold symmetry): 1 rhombus + 3 triangles + 2 squares
  ```

## Unified Implementation Specification

### Data Structures
```
Puzzle {
  rhombi: Map<(i,j,k), RhombusType>  // Type ∈ {0, 1, 10}
  boundary: (π, ρ, σ)  // strings of 0s and 1s
}

Mosaic {
  tiles: Map<(q,r), Tile>  // Tile = Triangle|Square|Rhombus
  nests: Map<Nest, Set<(q,r)>>  // Nest ∈ {A, B, C}
}

Flock {
  rhombi: Set<(q,r)>  // positions in nest
  orientation: (E, N)  // unit vectors at 150° angle
  labels: Map<(q,r), Int>  // f-values for tableau entries
}
```

### Algorithm Steps

**Step 1: Puzzle → Mosaic**
1. Create hexagon with nests at A, B, C (150° angles)
2. For each puzzle rhombus:
   - Check which edge has label 1
   - Place in corresponding nest
3. Fill remaining space with triangles and squares

**Step 2: Form Canonical Flock**
1. For migration A→B, use orientation (-E_A, -N_A) where:
   - E_A = vector from A toward A'
   - N_A = vector from A toward B'
2. Assign labels f: rhombi → {1,...,d} preserving content

**Step 3: Migration**
1. Process rhombi in standard order:
   - For north/east: decreasing f-values
   - For south/west: increasing f-values
   - Within same f-value: west to east
2. For each rhombus:
   ```
   while not in target nest:
     H = find_minimal_hexagon(rhombus)
     if H is Type I: rotate_180(H)
     else: rotate_120(H, ensuring edge alignment)
   ```

**Step 4: Extract Tableau**
- Rhombi positions in target nest form skew shape λ/μ
- f-values give tableau entries
- Standard order preservation ensures LR conditions

### Wake Preservation
Track displaced tiles for each migrating rhombus:
```
Wake {
  upper: List<(q,r)