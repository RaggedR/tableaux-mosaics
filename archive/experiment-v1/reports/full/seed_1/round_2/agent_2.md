**VERTEX MODEL ANALYSIS: CHALLENGING THE FREE-FERMIONIC ASSUMPTION**

The three reports reveal a **fundamental misunderstanding** of why the KTW puzzle-LR tableau bijection requires geometric intermediates like mosaics. As a vertex model specialist, I must challenge the core premise: **KTW puzzles are NOT free-fermionic**, which explains why direct transfer matrix approaches fail.

## The Yang-Baxter Obstruction

**Critical Gap**: All three reports miss that KTW puzzles correspond to **interacting vertex models** with spectral parameter-dependent R-matrices. The puzzle rhombi satisfy local Yang-Baxter relations, but with **non-trivial braiding**:

```
R₁₂(u-v) R₁₃(u-w) R₂₃(v-w) = R₂₃(v-w) R₁₃(u-w) R₁₂(u-v)
```

This is NOT the free-fermionic case where R-matrices are diagonal. The "12 free nabla choices" mentioned in the problem actually reflect **constrained degrees of freedom** from Yang-Baxter consistency—they're not independent variables.

## Why Growth Diagrams Fail Here

**Structural Problem**: Growth diagrams require **commuting transfer matrices** T(u)T(v) = T(v)T(u), which is guaranteed only when the underlying vertex weights satisfy specific integrability conditions. For KTW puzzles:

1. **Non-commutative structure**: The puzzle boundary conditions break the translation invariance needed for standard transfer matrix commutativity
2. **Spectral parameter mixing**: Different rhombus orientations correspond to different spectral parameters, creating non-commuting sectors
3. **Triangular geometry**: The puzzle triangle cannot be mapped to a rectangular lattice without introducing boundary terms that destroy integrability

## The Migration Process as Yang-Baxter Evolution

**Reframing Purbhoo's Construction**: The migration algorithm is actually implementing **Yang-Baxter moves** in disguise. Each hexagonal flip corresponds to a star-triangle transformation:

- **Mosaics** = configurations of the interacting vertex model
- **Migration** = sequence of Yang-Baxter moves toward a reference state
- **Final tableau** = canonical form after all Yang-Baxter moves complete

This explains why the bijection cannot be "simplified"—it's performing the essential work of **gauge-fixing** the Yang-Baxter redundancy.

## Alternative Approach: Bethe Ansatz Structure

Instead of growth diagrams, I propose investigating the **Bethe ansatz** structure of KTW puzzles:

**Conjecture**: The puzzle enumeration c^λ_{μν} equals the **multiplicity of the trivial representation** in the tensor product of Yangian modules corresponding to μ, ν, λ.

This would explain:
- Why direct transfer matrix methods fail (non-trivial representation theory)
- Why geometric construction is needed (Yangian R-matrices require explicit diagonalization)
- The connection to symmetric functions (Yangian ↔ quantum group duality)

## Computational Test

For the minimal example c^{(3,2,1)}_{(2,1),(2,1)} = 2:

1. **Construct the vertex model**: Identify the R-matrix elements for each rhombus type
2. **Check Yang-Baxter**: Verify the star-triangle relations hold
3. **Bethe equations**: Solve for the allowed spectral parameters
4. **Count solutions**: This should give the LR coefficient directly

## The Real Open Problem

The question should be reframed as: **Can we identify the hidden Yangian symmetry of KTW puzzles that makes the LR coefficients manifest?**

This is far deeper than growth diagrams—it connects to the **geometric Langlands program** where puzzles appear as local models for Schubert calculus on flag varieties.

The migration process isn't avoiding a direct bijection—it's the **unavoidable computation** needed to resolve the Yang-Baxter constraints inherent in the puzzle geometry.

**Bottom Line**: Any "direct" puzzle→tableau map must secretly perform the same Yang-Baxter computations that migration makes explicit. The geometric route is not a detour—it's the mathematical necessity imposed by the non-free-fermionic nature of the underlying vertex model.