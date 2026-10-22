# Vertex Model Analysis: The Yang-Baxter Obstruction Runs Deeper

## Fundamental Mischaracterization of Free-Fermion Structure

The reports fundamentally misunderstand the **free-fermionic correspondence** for LR coefficients. Zinn-Justin's construction doesn't make individual puzzles into vertex configurations - it embeds the **entire LR coefficient generating function** into a free-fermion correlation function. The puzzles themselves remain **classical geometric objects**.

**Critical Point**: The "12 free nabla choices → 3 tableau entries" is not about spectral parameters or transfer eigenvalues. It's about **constraint elimination in overcomplete coordinate systems**. Each puzzle has multiple nabla parameterizations that project to the same geometric configuration - this is **gauge redundancy**, not quantum structure.

## The Commuting Transfer Matrix Illusion

The growth diagram conjecture assumes we can construct **commuting transfer matrices** for puzzle enumeration. But here's the Yang-Baxter reality check:

**Obstruction**: KTW puzzles have **boundary conditions** that break translation invariance. Standard transfer matrix commutation requires **periodic boundaries** or **infinite system limits**. The triangular domain with fixed boundary data cannot support the spectral parameter families needed for commutation.

Even if we could construct row-wise transfer operators, they would satisfy **different** Yang-Baxter equations at different rows due to the changing boundary geometry. This violates the **uniformity condition** essential for integrable structure.

## Where the Migration Algorithm Actually Lives

The reports miss that Purbhoo's migration algorithm implements **jeu de taquin rectification** - but this process has its own Yang-Baxter structure! The hexagonal flips in mosaics correspond to **braid group actions** on crystal operators.

**Key Insight**: The "integrability" is not in the puzzles themselves, but in the **rectification dynamics**. Each migration step satisfies local Yang-Baxter relations, but these operate on the **mosaic crystal** rather than the puzzle geometry.

This suggests the growth diagram exists, but at the **wrong level**: it's a growth diagram for **migration paths**, not for puzzle-to-tableau bijection.

## The Spectral Parameter Question is Backwards

The computational report dismisses spectral parameters as irrelevant, but this misses the deeper issue. The question isn't "Do puzzles have spectral parameters?" but "What plays the role of spectral parameters in the **partition function**?"

**Answer**: The boundary conditions themselves! Each boundary configuration corresponds to an **inhomogeneity pattern** in the associated vertex model. The "row transfer matrix" would have position-dependent weights determined by the boundary data.

But this creates a **non-uniform** system where Yang-Baxter relations **vary by position** - exactly the obstruction to standard integrability.

## Computational Reality Check: The Enumeration Problem

Here's what the computational analysis missed: even if the transfer matrix existed, computing it would require solving the **inverse problem**:

Given: Puzzle configurations and their LR tableau images
Find: Transfer matrix elements such that eigenvalue multiplicities equal LR coefficients

This is **harder than the original enumeration problem**! The transfer matrix approach only helps if we can construct the matrices **independently** of complete enumeration.

## Alternative: Quasi-Local Yang-Baxter Structure

Instead of seeking standard integrability, consider **boundary Yang-Baxter equations**:

**Conjecture**: There exists a **boundary R-matrix** R_boundary(boundary data) such that:
- Local moves satisfy modified Yang-Baxter: R₁₂R₁₃R₂₃ = R₂₃R₁₃R₁₂ near boundaries
- Bulk moves satisfy standard Yang-Baxter
- The boundary/bulk interface has **matching conditions**

This would explain why puzzles admit **local move sequences** (migration) but not **global transfer structure**.

## The Real Vertex Model Connection

The correct question is not about puzzle transfer matrices, but about **boundary correlation functions** in free-fermion models. The LR coefficients appear as:

c^λ_{μ,ν} = ⟨boundary state μ | boundary state ν⟩_λ

where the inner product is taken in a **boundary-modified** free-fermion Fock space.

The "growth diagram" would then be the **correlation function expansion** in terms of intermediate boundary states, not a direct combinatorial construction.

## Fundamental Verdict: The Conj