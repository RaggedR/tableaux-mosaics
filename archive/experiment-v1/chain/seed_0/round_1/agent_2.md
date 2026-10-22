## Yang-Baxter Analysis of Purbhoo's Migration

Your initial analysis correctly identifies the core components, but I'll add the vertex model perspective that's crucial for implementation.

### Key Insight: Migration as Commuting Transfer Matrices

The migration algorithm is fundamentally about **commuting transfer matrices** in a free-fermionic vertex model. Each local hexagon rotation is a Yang-Baxter move that preserves the partition function. This guarantees:

1. **Well-defined growth**: The rhombi flow through the mosaic like particles in an integrable system
2. **Order preservation**: Standard order is maintained because the R-matrices satisfy the Yang-Baxter equation

### Critical Clarifications

**1. Puzzle → Mosaic Conversion Algorithm**

The "physical pulling" description obscures the actual algorithm. Here's what happens:

```
For each vertex (i,j) in the triangular puzzle grid:
- If the vertex has three edges labeled (a,b,c) clockwise from SW
- Place tiles based on the sum a+b+c:
  - Sum 0: Unit triangle pointing up
  - Sum 3: Unit triangle pointing down  
  - Sum 1: Rhombus with 0-labeled edges becoming sides of length 1
  - Sum 2: Rhombus with 1-labeled edges becoming sides of length 1
```

The key: 0-labeled edges contract, 1-labeled edges expand. This creates the hexagonal mosaic boundary.

**2. Coordinate System**

Use the natural hexagonal lattice:
- Origin at corner A
- Basis vectors: e₁ = (1,0) along AB', e₂ = (1/2,√3/2) along AC'
- Each tile occupies specific lattice cells
- Rhombi in nest A have edges parallel to e₁ and e₂

**3. Standard Order for Migration**

For a flock F with orientation (E,N):
- Box X <_f Y if f(X) < f(Y), or f(X) = f(Y) and X is west/northwest of Y
- This translates to mosaic coordinates: compare first by content value, then by position

**4. Flock Formation Details**

Before migration from nest A to B:
1. Give rhombi in nest A orientation (-E_A, -N_A)
2. Assign content f(rhombus) = row number in partition α
3. This creates the unique accessible flock

### Local Move Specifications

**2-fold symmetric hexagon (Type a):**
```
Before:        After:
  T₁ R T₂       T₂ R T₁
   \ / \         / \ /
    S₁-S₂       S₂-S₁
```
Rotate 180° around hexagon center.

**3-fold symmetric hexagon (Type b):**
```
Before:        After:
  T₁            T₃
 / \           / \
T₂ R T₃   →   T₁ R T₂
 \ /           \ /
  S             S
```
Rotate 120° so the rhombus edge becomes horizontal or vertical (not diagonal).

### Vertex Model Structure

Each hexagon rotation corresponds to an R-matrix action:
```
R(λ): V_i ⊗ V_j → V_j ⊗ V_i
```

The free-fermion condition restricts weights:
- Preserves particle number (rhombus count in each row)
- Maintains partial sums (Littlewood-Richardson inequalities)

### Migration Algorithm Refinement

```
1. Form flock on α with orientation (-E_A, -N_A)
2. For each rhombus in decreasing standard order:
   a. Find minimal enclosing hexagon to the right
   b. Apply appropriate rotation (180° or 120°)
   c. Repeat until rhombus reaches nest B
3. Read tableau: position in nest B gives row, original content gives entry
```

### Test Case Verification

For c^(3,2,1)_{(2,1),(2,1)} = 2:
- Two puzzles with boundary (001011, 001011, 001011)
- Each converts to a distinct mosaic
- Migration produces two LR tableaux of shape (3,2