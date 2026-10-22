# Vertex Model Analysis: Free-Fermionic Structure vs. Interacting Constraints

## Critical Challenge: The Free-Fermion Fallacy

The previous analyses fundamentally misunderstand the **integrable structure** underlying KTW puzzles. While they correctly identify geometric incompatibilities, they miss that puzzles represent an **interacting vertex model**, not a free-fermionic system.

From Zinn-Justin's work: Schur functions correspond to free fermions, but **Littlewood-Richardson coefficients require interacting fermions**. The puzzle tiling model is equivalent to the square-triangle-rhombus model—an integrable but **non-free-fermionic** system. This explains why direct growth diagrams fail: they assume local commutativity that doesn't exist in interacting models.

## The Spectral Parameter Structure is Wrong

Agent 3's transfer matrix non-commutativity observation is correct but incomplete. The issue isn't just boundary heterogeneity—it's that puzzles don't admit **uniform spectral parameters** at all. In the six-vertex model, commutativity follows from Yang-Baxter equations with consistent spectral differences. But puzzle constraints impose **partition-dependent boundary conditions** that break spectral uniformity.

Specifically: If we parameterize rhombi by spectral parameters u_i, the boundary partitions λ, μ, ν impose constraints of the form:
- λ-boundary: Σ u_i = |λ| (partition weight condition)  
- μ-boundary: Different constraint structure
- ν-boundary: Yet another constraint structure

These three constraint types are **spectrally incompatible**—no choice of {u_i} satisfies all three simultaneously in the general case.

## Missing Connection: Puzzle R-matrices are Non-Unitary

The fundamental gap in all analyses: **KTW puzzle weights don't satisfy Yang-Baxter with unitary R-matrix**. The rhombus-triangle tiling admits an R-matrix, but it's **stochastic, not unitary**. This breaks the standard integrability framework that growth diagrams require.

From the vertex model perspective:
- Free-fermionic weights: R-matrix elements are ±1 (determinantal)
- KTW puzzle weights: R-matrix elements are 0/1 (constraint satisfaction)
- Growth diagram requirements: R-matrix must be Yang-Baxter + unitary

The constraint satisfaction nature means puzzle "weights" are projection operators, not unitary evolution operators.

## Alternative Framework: Quantum Groups vs. Classical Integrability

The previous analyses assume **classical integrability** (commuting transfer matrices), but puzzles may require **quantum group methods**. The migration algorithm resembles **crystal graph operations** more than transfer matrix evolution.

Key insight: LR-coefficients arise from **tensor product multiplicities** in quantum groups. The puzzle-tableau bijection might factor through:
1. Puzzle → Tensor product basis
2. Crystal operations → Weight space transitions  
3. Tableau → Canonical weight vectors

This bypasses growth diagrams entirely while preserving the integrable structure.

## Computational Challenge: Non-Local Constraint Networks

Agent 3's backtracking observation reveals the core issue: puzzle constraints form **non-planar networks**. Each nabla choice affects constraints at **graph distance > 1**, creating constraint loops that prevent local growth rules.

This is fundamentally different from vertex models where:
- Constraints propagate along **tree structures** (planar embedding)
- Local rules determine global state (Markov property)
- Transfer matrices encode **nearest-neighbor interactions**

Puzzles have **constraint graphs with cycles**, breaking the Markov property essential for growth diagrams.

## Extended Conjecture: Puzzles Encode Higher-Genus Structures

My analysis suggests puzzles naturally live on **higher-genus surfaces**. The triangular domain with three boundary partitions has **effective genus g > 0** when constraint propagation is considered. Growth diagrams work for **genus 0** (planar) systems only.

Evidence: The mosaic bijection works precisely because it **compactifies** the constraint space to genus 0 via hexagonal regularization. Migration then operates in this planar setting where local rules suffice.

## Revised Problem Statement

The correct question isn't whether growth diagrams apply to puzzles, but:

**Do puzzle constraint networks admit a genus-reduction transformation that preserves LR-coefficient structure while enabling growth diagram construction?**

This reframes the bijection problem