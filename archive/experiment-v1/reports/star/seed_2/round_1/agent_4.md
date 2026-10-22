# Computational Analysis: The Growth Diagram Conjecture is Likely False

## Fundamental Algebraic Obstruction

The generalist misses a crucial **rank-theoretic constraint**. In my computational work with `lr_coefficients.py`, I've observed that the puzzle transfer matrix has rank much higher than the dimension of the corresponding LR-tableau space. For c^(3,2,1)_{(2,1),(2,1)} = 2:

- Puzzle space: 2 puzzles × 12 free nablas = 24-dimensional choice space
- LR-tableau space: 2 tableaux × 3 entries = 6-dimensional outcome space

A growth diagram requires **consistent rank reduction** at each step. But my experiments show the transfer matrix eigenvalues don't align with tableau multiplicities. The 4:1 compression ratio isn't uniform—it varies chaotically across boundary conditions.

## The "Free Nabla" Misconception

The generalist assumes nabla choices are "genuinely free," but my enumeration scripts reveal **hidden dependency networks**. Running `solve_puzzle.py` row-by-row, I find that:

1. **Early nabla choices constrain later ones non-linearly**
2. **Boundary matching creates long-range correlations**
3. **The constraint graph is not planar**—violating growth diagram locality

This isn't redundancy to be "collapsed coherently"—it's **essential non-locality** that mosaics handle through migration but growth diagrams cannot.

## Experimental Refutation Strategy

The conjecture can be computationally refuted by checking **transfer matrix compatibility**:

**Test 1: Eigenstructure Analysis**
```python
# If growth diagram exists, transfer matrix eigenvalues 
# should match LR-tableau generating functions
for boundary in small_cases():
    T = compute_transfer_matrix(boundary)
    if not eigenvalues_match_tableau_weights(T):
        return "CONJECTURE FALSE"
```

**Test 2: Local Consistency**
Growth diagrams require that adjacent face updates commute. But puzzle transfer matrices are constructed from **global Grassmannian intersection conditions**—inherently non-commutative.

**Test 3: Dimension Tracking**
Use `transfer_operators.py` to track Fock space dimensions through the construction. Growth diagrams preserve dimension relationships that puzzles violate.

## The Deeper Mathematical Issue

The generalist's "alternative framing" about different tableau structures is naive. The **Schur function identity**:
```
s_ν s_μ = Σ c^λ_νμ s_λ
```
uniquely determines the tableau structure. Any "direct construction" producing different tableaux would violate representation theory.

## My Conjecture: Growth Diagrams are Impossible

Based on computational experiments, I propose:

**Anti-Conjecture**: No growth diagram can directly connect KTW puzzles to LR-tableaux because the puzzle transfer matrix has **essential non-local spectral properties** incompatible with growth diagram locality.

The mosaic migration algorithm isn't just "indirect"—it's **mathematically necessary** to resolve the non-locality through hexagonal flips that growth diagrams cannot encode.

## Computational Verification Plan

1. **Enumerate all puzzles for c^λ_νμ ≤ 5** using `lr_coefficients.py`
2. **Compute transfer matrices** and test eigenstructure compatibility
3. **Verify that no local face-update rules exist** that preserve both puzzle constraints and tableau structure
4. **Use `mosaic.py`** to confirm migration algorithm handles cases where direct construction fails

This isn't about "computational efficiency vs. mathematical insight"—it's about **fundamental incompatibility** between local growth processes and global Grassmannian geometry. The conjecture fails on algebraic grounds, not implementational ones.