## Computational Analysis: Growth Diagram Conjecture for KTW Puzzles

### Critical Assessment of the Conjecture

The proposed conjecture contains a fundamental **dimensional mismatch** that requires immediate attention. The claim that "12 free nabla choices project to 3 tableau entries" for c^(3,2,1)_{(2,1),(2,1)} = 2 suggests a 4:1 reduction ratio, but this oversimplifies the actual correspondence structure.

**Key Issue**: The transfer matrix operates on puzzle configurations row-by-row, but LR tableaux have fundamentally different combinatorial constraints. A direct bijection through face labels would require the growth diagram to preserve both:
1. Local puzzle consistency (hexagon vertex conditions)
2. Global tableaux properties (ballot sequences, content restrictions)

### Computational Verification Strategy

Using the available scripts, I propose this experimental framework:

**Phase 1: Transfer Matrix Structure**
- Use `lr_coefficients.py` to enumerate all puzzles for c^(3,2,1)_{(2,1),(2,1)} = 2
- Apply `solve_puzzle.py` row-by-row to extract the transfer matrix eigenspaces
- Map each "free nabla choice" to specific matrix elements using `transfer_operators.py`

**Phase 2: Growth Diagram Construction**
- For each puzzle, construct the proposed growth diagram where faces encode intermediate states
- Test whether face labels can be interpreted as Young tableau entries
- Verify that the final configuration matches known LR tableaux

**Phase 3: Bijection Testing**
- Compare direct face-label mapping against Purbhoo's mosaic→migration route
- Check if both paths yield identical LR tableaux for all test cases
- Identify failure modes where the direct mapping breaks down

### Alternative Computational Framing

The conjecture assumes the transfer matrix naturally induces growth diagrams, but this may be **backwards**. Instead of seeking direct bijection through face labels, consider:

1. **Spectral Analysis**: The transfer operators may reveal hidden symmetries that explain the 4:1 reduction without requiring face-label interpretation
2. **Local-to-Global Problem**: Each row operation might preserve some invariant that accumulates into tableau properties, but not through simple face labeling

### Technical Challenges

**Mosaic Integration**: The `mosaic.py` script has migration issues, but this is precisely where the computational experiment should focus. If direct growth diagrams exist, they should **replace** migration entirely.

**Scale Testing**: The minimal example (2 puzzles, 12 choices) is insufficient. I recommend extending to c^(4,3,2)_{(3,2),(2,1)} and larger cases to test scaling behavior.

### Computational Predictions

If the conjecture holds, we should observe:
- **Rank compatibility**: Transfer matrix rank equals tableau count
- **Factorization property**: Row operations compose to give global bijection
- **Local constraint preservation**: Each growth step maintains puzzle validity

If it fails, likely failure modes include:
- **Non-unique face labels**: Multiple puzzle configurations mapping to same intermediate states
- **Constraint violation**: Growth process producing invalid tableau configurations
- **Dimension explosion**: Intermediate states growing faster than final tableau count

### Research Extension

The most critical gap is the **computational verification of constraint propagation**. The scripts can enumerate states but need enhancement to track how local puzzle rules translate through the proposed growth diagram into global tableau properties. This is where the conjecture will likely succeed or fail definitively.

**Bottom Line**: The conjecture is testable but requires careful attention to the constraint propagation mechanism, not just counting arguments.