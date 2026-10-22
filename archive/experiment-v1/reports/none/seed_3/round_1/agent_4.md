# Initial Analysis: Growth Diagram Conjecture for KTW Puzzles

## Gaps in the Problem Statement

The problem statement makes a critical leap that needs scrutiny. While Purbhoo's bijection puzzle → mosaic → migration → LR tableau is indeed established, the claim that "row transfer matrix" construction could yield a "growth diagram" is **unsupported**. 

**Key Missing Elements:**
1. What exactly is the "row transfer matrix" for KTW puzzles? This isn't standard terminology in the literature.
2. How would face labels in such a growth diagram encode tableau entries?
3. Why should we expect this construction to exist at all?

## Computational Approach to the Conjecture

Given the minimal example c^(3,2,1)_{(2,1),(2,1)} = 2, I can design experiments using the available scripts:

### Phase 1: Enumeration Analysis
```python
# Using lr_coefficients.py
puzzles = enumerate_puzzles((2,1), (2,1), (3,2,1))
# Verify we get exactly 2 puzzles
# Extract free nabla positions for each puzzle
```

### Phase 2: Row-by-Row Decomposition  
```python
# Using solve_puzzle.py
for puzzle in puzzles:
    row_data = solve_row_by_row(puzzle)
    # Track how choices at each row level constrain subsequent rows
    # Look for patterns that might correspond to tableau growth
```

### Phase 3: Transfer Operator Investigation
The transfer_operators.py script for Fock space operators is intriguing here. **This suggests a connection I need to explore**: Are the "transfer operators" actually related to row-wise puzzle construction? This could be the missing link.

## Alternative Framings

**Reframe 1: Lattice Path Perspective**
Instead of seeking face labels directly encoding tableaux, consider: Do the constraint patterns in row-by-row puzzle solving create a natural lattice structure whose paths correspond to LR tableaux?

**Reframe 2: Symmetric Function Connection**
The 12 free nabla choices projecting to 3 tableau entries suggests a 4-to-1 mapping. This ratio might reflect underlying symmetric function identities that could be computationally verified.

## Critical Computational Questions

1. **Constraint Propagation**: How do free nabla choices in row i constrain choices in row i+1? Can this be encoded as matrix operations?

2. **Bijection Verification**: The current mosaic.py has "migration NOT working" - this is actually crucial! I need to implement the migration algorithm to verify the known bijection before proposing alternatives.

3. **Growth Pattern Recognition**: For larger examples, do the row-wise constraint patterns exhibit the recursive structure characteristic of growth diagrams?

## Proposed Experiments

1. **Implement missing migration algorithm** in mosaic.py to establish baseline
2. **Extract constraint matrices** for each row level in the minimal example
3. **Test scaling behavior** with larger Littlewood-Richardson coefficients
4. **Search for matrix factorizations** that might reveal hidden growth structure

The conjecture is ambitious but premature without understanding what "row transfer matrix" actually means in this context. My computational focus will be on making this concrete before testing the growth diagram hypothesis.