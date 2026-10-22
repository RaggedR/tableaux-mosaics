# Specialist Report: Implementing Purbhoo's Mosaic Migration Bijection

## Critical Gaps and Corrections

The generalist report misses several crucial details that will block implementation. I'll provide the concrete specifications needed.

## 1. Puzzle → Mosaic Conversion (Correcting Step 1)

The "pulling tight" metaphor is too vague. Here's the precise algorithm:

**Input**: KTW puzzle with boundary strings (π, ρ, σ)
**Output**: Mosaic in hexagon A'AB'BC'C

**Algorithm**:
1. The hexagon has vertices with angles:
   - A, B, C: 150° (these become nests)
   - A', B', C': 90°
   - Side lengths: A'A = B'B = C'C = d, AB' = BC' = CA' = n-d

2. For each puzzle rhombus at position (i,j,k) where i+j+k=n:
   - If edge from (i,j,k) toward (i+1,j,k-1) is labeled 1: place rhombus in nest A
   - If edge toward (i,j+1,k-1) is labeled 1: place rhombus in nest B  
   - If edge toward (i-1,j+1,k) is labeled 1: place rhombus in nest C

3. Fill remaining space with unit squares and triangles to complete tiling

**Key insight**: The bijection maps 0/1 edge labels to absence/presence of rhombi touching those edges in the mosaic.

## 2. Migration Algorithm Details

### Flock Formation
Before migration, form a flock F = (α, (E,N), f) where:
- α = rhombi in source nest
- (E,N) = orientation vectors (not just "orientation")
- f: α → ℕ assigns labels preserving content

For the canonical flock with orientation (-E_A, -N_A):
- E_A points from A toward A'
- N_A points from A toward B'
- f assigns entries 1,2,...,d to maintain LR tableau properties

### Standard Order (Critical!)
For rhombi in a nest with orientation (E,N):
- Primary: by f-value (ascending for north/east migration, descending for south/west)
- Secondary: among equal f-values, by position (west to east in the nest)

### Migration Mechanics

**Hexagon types** (the report's (a) and (b) are insufficient):
```
Type I (2-fold):    Type II (3-fold):
  □---△              △---□
 / \ / \            / \ / \
△---◇---△          □---◇---△
 \ / \ /            \ / \ /
  △---□              △---□
```

**Rotation rules**:
- Type I: Always rotate 180°
- Type II: Rotate 120° such that one rhombus edge becomes horizontal OR vertical
  - If migrating north/south: resulting rhombus has horizontal edge
  - If migrating east/west: resulting rhombus has vertical edge

## 3. Reading the Tableau

After migration to nest B:
1. The rhombi form a skew shape λ/μ where:
   - λ corresponds to the boundary string at B' (reading north)
   - μ corresponds to the boundary string at A' (reading west)
   
2. The f-values on rhombi give the tableau entries

3. The preserved standard order ensures tableau inequalities

## 4. Test Case Worked Example

For one puzzle with boundary (110100, 110100, 001011):

1. **Mosaic**: d=3 rhombi each in nests A and B, specific pattern in nest C

2. **Migration A→B**:
   - Process rhombi with f-values in order 3,2,1
   - Each follows specific path through hexagon rotations
   - Final configuration: 3 rhombi in nest B forming shape (3,2,1)/(2,1)

3. **Tableau**: Read f-values in their final positions

## 5. Implementation Recommendations

### Data Structures
```
Mosaic = {
  tiles: Map<(x,y), TileType>,