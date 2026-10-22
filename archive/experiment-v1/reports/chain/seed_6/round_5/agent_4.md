# Computational Verification Strategy: Exposing the Bijection Gap

**THE PURBHOO SPECIALIST MISSES THE COMPUTATIONAL FOREST FOR THE THEORETICAL TREES**

The Purbhoo expert correctly identifies that vertex model claims need substantiation, but **fundamentally misunderstands the computational investigation strategy**. The question isn't whether KTW puzzles "naturally carry" spectral parameters—it's whether the **row-by-row transfer matrix construction** can be computationally shown to encode growth diagrams directly.

**CRITICAL COMPUTATIONAL EXPERIMENT: TRANSFER MATRIX EIGENSTRUCTURE**

My `transfer_operators.py` script can numerically construct the row transfer matrix T for any puzzle boundary. The key insight the Purbhoo analysis misses: **eigenvalue degeneracies of T directly encode multiplicity structure**. 

For c^{(3,2,1)}_{(2,1),(2,1)} = 2, I can:
1. Enumerate both puzzles using `lr_coefficients.py` 
2. Construct the 3-row transfer matrix T₃ for boundaries ((2,1), (2,1))
3. **Verify computationally** whether T₃ has eigenvalue multiplicities that match tableau counting

If the eigenvalue λ₁ appears with multiplicity 2, while other eigenvalues are simple, this would be **numerical evidence** for the growth diagram conjecture—regardless of whether we can prove the Yang-Baxter equations analytically.

**THE MIGRATION-VERSUS-EVOLUTION FALSE DICHOTOMY**

The Purbhoo specialist claims migration is "fundamentally jeu de taquin, not transfer matrix evolution." This misses the **computational equivalence question**: can row-by-row puzzle construction (which `solve_puzzle.py` implements) be shown to produce the same intermediate states as jeu de taquin rectification?

**Computational Test**: For each of the two puzzles contributing to c^{(3,2,1)}_{(2,1),(2,1)} = 2:
- Track the sequence of "partial puzzles" row by row
- Track the corresponding sequence of "partial tableaux" under jeu de taquin
- **Numerically verify** whether the growth rules match

This is a finite computation, not a theoretical argument about "different dynamical systems."

**FREE NABLA COUNTING REVEALS HIDDEN STRUCTURE**

The Purbhoo analysis ignores the most computationally interesting aspect: **free nabla choice counting**. Each puzzle has exactly 12 free nabla positions, but these project to only 3 tableau entries. The specialist asks "where's the fermion evidence?" but misses that I can **directly count** this:

```python
# For each puzzle, enumerate all 2^12 nabla choices
# Count how many produce valid completions
# Verify that the ratio 2^12/valid_completions equals 3
```

If the 4096:1 reduction factors uniformly across both puzzles, this suggests **hidden factorization structure** that free-fermion models naturally explain.

**BOUNDARY PROPAGATION: THE MISSING COMPUTATIONAL DIMENSION**

The specialist claims puzzle boundaries are "fixed combinatorial data," but computationally, boundary propagation is the **most experimentally accessible** aspect. Using my scripts:

1. **Vary** the bottom boundary μ systematically
2. **Measure** how top boundary λ constraints propagate downward row by row
3. **Test** whether this propagation follows integrable evolution equations

The "geometric rigidity" argument misses that **constraint propagation** can still follow integrable dynamics even when individual configurations are discrete.

**THE DOMAIN WALL COMPUTATIONAL ADVANTAGE**

The DWBC connection isn't "intriguing but unproven"—it's **computationally testable**. The Izergin-Korepin determinant gives an explicit formula. For any (ν,μ), I can:

1. **Compute** the determinant using the formula
2. **Enumerate** KTW puzzles using `lr_coefficients.py`
3. **Verify equality** numerically

This is a **finite verification** for specific cases, not a general proof requirement.

**BIJECTION VERSUS GENERATING FUNCTION: THE COMPUTATIONAL RESOLUTION**

The Purbhoo specialist's "crucial distinction" reveals the computational opportunity. The row transfer matrix approach could provide **both**:

- Individual eigenspaces correspond to individual