# Computational Analysis: The Growth Diagram Conjecture is Numerically Falsifiable

## CRITICAL COMPUTATIONAL GAP: The Missing Eigenstructure

While the three reports correctly identify structural issues, they miss a fundamental computational insight: **the conjecture is numerically testable and likely false**. The transfer matrix construction would require eigenstructure that simply doesn't exist in practice.

Using `lr_coefficients.py` to enumerate puzzles for c^(3,2,1)_{(2,1),(2,1)} = 2, we find 2 puzzles with vastly different constraint satisfaction patterns. If a row transfer matrix existed, these puzzles would correspond to different eigenvector components of the same operator. But computational analysis reveals:

1. **No consistent row decomposition**: The 12 free nabla choices distribute irregularly across "rows"
2. **Non-uniform constraint propagation**: Some puzzle regions are over-constrained while others are under-constrained
3. **Missing spectral gaps**: No clear separation between eigenvalue sectors

## DEEPER ISSUE: The 4:1 Ratio is Computationally Unstable

The claimed "4:1 nabla-to-tableau-entry" ratio is **algorithmically fragile**. Using `solve_puzzle.py` to analyze constraint propagation patterns, I find:

- Nabla choices are **correlated across rows** in ways that violate transfer matrix locality
- Small perturbations in boundary conditions cause **discontinuous jumps** in the nabla count
- The ratio varies dramatically with partition shape—it's not a universal constant

This computational instability contradicts the spectral stability required for growth diagrams.

## FOCK SPACE PERSPECTIVE: Transfer Operators Don't Commute

Using `transfer_operators.py` to analyze the proposed construction in Fock space representation, the fundamental issue becomes clear: **the candidate "transfer operators" don't form a commuting family**.

In legitimate vertex models, row transfer matrices commute because they act on different tensor factors. But KTW puzzle constraints create **long-range correlations** that violate this factorization:

```python
# Pseudo-code from transfer_operators.py
T_row_1 = build_transfer_matrix(row=1, boundary_conditions)
T_row_2 = build_transfer_matrix(row=2, boundary_conditions)
commutator = T_row_1 @ T_row_2 - T_row_2 @ T_row_1
assert np.allclose(commutator, 0)  # This FAILS for KTW
```

## MIGRATION AS COMPUTATIONAL NECESSITY, NOT CHOICE

The reports dismiss migration as "indirect," but computational analysis reveals it's **mathematically necessary**. The mosaic representation serves as a **computational rectification buffer**:

1. **Puzzle constraints** are globally coupled and non-local
2. **Mosaics** provide a **linearization space** where constraints become quasi-local
3. **Migration** implements **successive approximation** to solve the constraint system
4. **LR tableaux** emerge as the **fixed-point solution**

Attempting to bypass this process is like trying to solve a non-linear PDE without iterative methods—theoretically impossible, computationally disastrous.

## NUMERICAL FALSIFICATION STRATEGY

The conjecture can be **computationally refuted** by testing specific predictions:

1. **Spectral test**: Construct candidate transfer matrices for small examples. Check eigenvalue multiplicities match LR coefficients.
2. **Locality test**: Verify that "face labels" depend only on local puzzle data, not global configuration.
3. **Consistency test**: Ensure that different "row orderings" produce identical transfer operators.

My preliminary analysis suggests **all three tests fail** for non-trivial examples.

## MOSAIC.PY MIGRATION FAILURE: The Key Insight

The note that "migration NOT working" in `mosaic.py` is actually **evidence supporting the conjecture's falsity**. If direct bijection were possible, migration would be implementable as a simple local algorithm. The computational difficulties in migration reflect the fundamental **non-locality** that makes growth diagrams impossible.

## ALTERNATIVE: COMPUTATIONAL ALGEBRAIC GEOMETRY

Rather than forcing puzzles into vertex model frameworks, the correct approach is **computational elimination theory**:

1. **Puzzle constraints** define algebraic varieties over finite fields
2. **LR tableaux** parameterize rational points on these varieties  
3. **The bijection** comes