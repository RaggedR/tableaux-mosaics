# Analysis: Transfer Matrix Structure vs. Growth Diagram Bijections

## Critical Issues with the Proposed Direct Route

The problem assumes that KTW puzzles admit a natural **row transfer matrix** structure, but this is fundamentally problematic. Let me explain why:

### 1. **Geometric Obstruction: No Natural Row Structure**

KTW puzzles live on **triangular domains**, not rectangular grids. The puzzle pieces (unit triangles and rhombi) don't align with horizontal "rows" in any canonical way. Unlike ASMs or domino tilings on rectangular grids, there's no obvious way to define a "row-by-row" transfer matrix for triangular puzzles.

The standard vertex models that admit natural transfer matrices (six-vertex, five-vertex, etc.) are defined on square lattices where horizontal rows are geometrically evident. For triangular domains, any row decomposition would be artificial.

### 2. **Spectral Parameter Issues in Free-Fermionic Context**

Even if we could define a transfer matrix, the **commutativity** requirement poses deeper issues. In Zinn-Justin's work, the Yang-Baxter equation ensures commuting transfer matrices, but this relies on:

- **Uniform spectral parameters** along each row
- **Free-fermionic weights** that factor through determinants
- **Boundary conditions** compatible with the R-matrix structure

KTW puzzles have **heterogeneous constraints**: different boundary labels (ν, μ, λ) impose different local rules. This breaks the spectral parameter uniformity needed for standard commutation proofs.

### 3. **The Migration Algorithm Reveals the True Structure**

Purbhoo's migration algorithm isn't just a computational trick—it reveals that the **natural dynamics** occur in the mosaic representation, not the original puzzle. The hexagonal flips correspond to elementary moves in a more fundamental vertex model.

**Key insight**: The mosaics are where the integrable structure lives. The puzzle → mosaic transformation eliminates the geometric irregularities that prevent direct transfer matrix treatment.

## Alternative Framework: Mosaic Transfer Matrices

Instead of forcing puzzles into a transfer matrix framework, consider:

1. **Define transfer matrices on the mosaic lattice** (which has regular hexagonal structure)
2. **Use the known puzzle ↔ mosaic bijection** to pull back the dynamics
3. **Show that mosaic transfer matrices encode growth diagrams** whose face labels give LR tableaux

This respects the natural geometry while potentially achieving the desired directness.

## Challenge to the c^(3,2,1)_{(2,1),(2,1)} = 2 Example

The claim that each puzzle has "12 free nabla choices projecting to 3 tableau entries" needs verification. In vertex models, the number of local configurations must be consistent with:

- **Ice rule constraints** (arrow conservation)
- **Boundary condition compatibility**
- **Partition function factorization** through free-fermionic weights

The specific numbers (12 → 3) suggest a 4:1 compression that should emerge from underlying representation theory, not ad hoc counting.

## Recommended Approach

Rather than seeking a direct puzzle transfer matrix, investigate:
1. **Hexagonal vertex model on mosaic lattices** with appropriate boundary conditions
2. **Growth diagram interpretation** of the resulting commuting transfer matrices
3. **Bijective proof** that the growth dynamics recover both LR coefficients and tableaux

This leverages established integrable structures while maintaining geometric naturality.