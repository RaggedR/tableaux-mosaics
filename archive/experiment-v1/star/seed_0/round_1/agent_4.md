## Computational Implementation Report for Mosaic Migration Bijection

### Data Structures

**Coordinate System**: Use axial coordinates (q, r) for hexagonal grid where:
- q increases east/west
- r increases northwest/southeast  
- s = -q - r (implicit third coordinate)

**Core Objects**:
```
Tile: {
  position: (q, r),
  type: TRIANGLE | SQUARE | RHOMBUS,
  orientation: 0..5,  // 60° rotations for triangles/rhombi
  edges: [6 binary values],  // clockwise from east
  rhombus_data: {color: int, nest: A|B|C} if RHOMBUS
}

Mosaic: {
  tiles: Map<(q,r) -> Tile>,
  nests: {A: Set<(q,r)>, B: Set<(q,r)>, C: Set<(q,r)>},
  dimensions: {n, d}  // n = puzzle size, d = #1s per boundary
}

Flock: {
  rhombi: [(q,r)],  // ordered list
  orientation: (E_vec, N_vec),  // unit vectors
  labels: Map<(q,r) -> int>  // tableau entries
}
```

### Phase 1: Puzzle to Mosaic Conversion

**Algorithm**:
1. **Setup hexagon geometry**: Create hexagon with vertices A'AB'BC'C where:
   - Angles: 150° at A,B,C and 90° at A',B',C'
   - Edge lengths: A'A = B'B = C'C = d, AB' = BC' = CA' = n-d
   
2. **Map puzzle coordinates**: 
   - Puzzle position (i,j) in triangle → mosaic position (q,r)
   - Use transformation: q = j - i, r = i
   - Adjust origin to place puzzle content in hexagon interior

3. **Convert pieces**:
   - **0-labeled triangle** → triangle in mosaic (same orientation)
   - **1-labeled triangle** → triangle in mosaic (same orientation)  
   - **Rhombus** → square in mosaic (becomes rhombus after deformation)
   
4. **Fill nests**: For each boundary position with a 1:
   - Place a 150°/30° rhombus in corresponding nest
   - Nest A: gets rhombi for 1s in π
   - Nest B: gets rhombi for 1s in ρ  
   - Nest C: gets rhombi for 1s in σ

### Phase 2: Migration Algorithm

**Setup**:
1. Create initial flock F on nest A rhombi with orientation (-E_A, -N_A)
2. Assign labels via unique flock construction (Lemma 4.3):
   - Process rhombi in reading order (west→east, north→south)
   - Label with smallest valid integer maintaining LR conditions

**Migration Loop** (A→B, south direction):
```
For each rhombus ℓ in F (in reverse standard order):
  While ℓ not in nest B:
    1. Find minimal hexagon H containing ℓ to the right
    2. Identify hexagon type:
       - Type A: 2-fold symmetry → rotate 180°
       - Type B: 3-fold symmetry → rotate 120° 
         (choose rotation making an edge horizontal/vertical)
    3. Apply rotation to all tiles in H
    4. Update ℓ's position
```

**Standard Order**: For rhombi with labels f(X), f(Y):
- X <_f Y if: f(X) < f(Y), or f(X) = f(Y) and X is west of Y

### Phase 3: Extract LR Tableau

1. **Identify shape**: Rhombi in nest B form skew shape λ/μ where:
   - μ corresponds to empty positions (from nest structure)
   - λ determined by mosaic boundary

2. **Read tableau**: For each rhombus at position (q,r) in nest B:
   - Map to tableau position (row, col) using nest orientation
   -