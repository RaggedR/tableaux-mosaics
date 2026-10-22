# Computational Analysis: Growth Diagram Conjecture for KTW Puzzles

## Problem Reframing and Critical Gaps

The conjecture proposes a **direct computational pathway** from puzzle transfer matrices to LR tableaux via growth diagrams, bypassing Purbhoo's indirect mosaic-migration route. However, several critical computational questions are **underspecified**:

1. **Transfer Matrix Definition**: What exactly is the "row transfer matrix" for KTW puzzles? The literature describes puzzle-solving algorithms, but the algebraic structure of row-by-row transfers as matrices needs precise definition.

2. **Growth Diagram Structure**: Classical growth diagrams (Fomin, Stanley) have specific face-labeling rules. How do puzzle transfer operations translate to face labels? What are the edge weights?

3. **Dimensional Mismatch**: The example c^(3,2,1)_{(2,1),(2,1)} = 2 mentions "12 free nabla choices projecting to 3 tableau entries." This 12→3 projection suggests a **many-to-one mapping** that growth diagrams typically don't handle directly.

## Computational Verification Strategy

Using the available scripts, I propose this experimental framework:

### Phase 1: Transfer Matrix Construction
- Use `lr_coefficients.py` to enumerate all puzzles for small cases
- Apply `solve_puzzle.py` row-by-row to extract transfer operators
- Implement `transfer_operators.py` to formalize the Fock space structure
- **Critical test**: Do these operators satisfy the Yang-Baxter equation? (Required for integrability)

### Phase 2: Growth Diagram Analysis
```python
# Pseudo-experimental setup
for puzzle in enumerate_puzzles(lambda_=(3,2,1), mu=(2,1), nu=(2,1)):
    transfer_sequence = solve_row_by_row(puzzle)
    candidate_faces = extract_face_labels(transfer_sequence)
    lr_tableau = growth_diagram_decode(candidate_faces)
    verify_bijection(puzzle, lr_tableau)
```

### Phase 3: Invariant Detection
- **Hypothesis**: Free nabla choices encode tableau standardization degrees
- **Test**: Does the 12→3 reduction preserve hook-length statistics?
- **Verification**: Compare with known LR tableau enumeration

## Fundamental Computational Challenges

### 1. **Algebraic Structure Gap**
The conjecture assumes transfer matrices exist, but KTW puzzles are inherently **geometric-combinatorial** objects. The algebraic lift to transfer operators may not preserve the puzzle's essential structure.

### 2. **Non-Uniqueness Problem**
Growth diagrams typically require **unique** face labelings. But puzzle solutions often have multiple valid completions for the same boundary data. How does the transfer matrix resolve this non-determinism?

### 3. **Complexity Scaling**
For partition λ = (a₁, a₂, ...), puzzle complexity grows roughly as O(|λ|³). If growth diagrams provide a "direct" bijection, we expect polynomial-time conversion. **Test hypothesis**: Measure actual computational complexity.

## Alternative Computational Frameworks

Rather than assuming growth diagrams work, consider:

### Framework A: **Spectral Analysis**
- Construct puzzle transfer matrices as actual linear operators
- Analyze eigenvalue spectra for integrability signatures
- **Prediction**: Integrable systems have specific spectral properties

### Framework B: **Bijection Verification**
- Implement both puzzle→LR and LR→puzzle maps
- Test invertibility on random samples
- **Critical metric**: Success rate vs. problem size scaling

### Framework C: **Homological Approach**
Using the Grassmannian connection:
- Compute actual Schubert calculus via `transfer_operators.py`
- Compare with puzzle-derived structure constants
- **Validation**: Numerical agreement with known cohomology

## Computational Experiments for Refutation

The most effective way to **refute** this conjecture:

1. **Construct explicit transfer matrices** for c^(3,2,1)_{(2,1),(2,1)} = 2
2. **Attempt growth diagram construction** following standard algorithms
3. **Check face-labeling consistency**: Do all puzzle paths yield valid LR tableaux?
4. **Scale up to c^(4,3,2,1)_{(2,2,1),(3,1