# Vertex Model Analysis: Yang-Baxter Integrability vs. Growth Diagram Locality

## The Free-Fermionic Constraint Problem

The previous analysis misses a **crucial structural constraint**: KTW puzzles, when viewed as vertex models, are **NOT free-fermionic**. This fundamentally undermines the growth diagram approach.

In free-fermionic vertex models, the R-matrix has the special form R(u) = u·I + P where P is the permutation operator. This gives **binary weights** (0 or 1) and ensures **non-intersecting path representations**. But KTW puzzles involve **rhombus multiplicities** - multiple ways to fill the same local configuration. This breaks the free-fermionic structure entirely.

The reporter's confusion about "12→3 compression" actually reveals something deeper: the **spectral parameter space** of KTW puzzles is inherently **interacting**, not free-fermionic. The 12 nabla choices represent **local interaction degrees of freedom** that don't factorize into independent fermion modes.

## Yang-Baxter Equation: Missing Consistency Check

Neither analysis addresses the **fundamental question**: do KTW puzzle piece transformations satisfy the Yang-Baxter equation? 

For a vertex model interpretation to work, local puzzle piece moves must satisfy:
```
R₁₂(u-v) R₁₃(u-w) R₂₃(v-w) = R₂₃(v-w) R₁₃(u-w) R₁₂(u-v)
```

This isn't just "confluence" - it's a **specific algebraic constraint** on how local transformations compose. The Purbhoo migration algorithm's hexagonal flips need to be checked against this equation.

Without Yang-Baxter consistency, there's no guarantee that **different row-ordering** in a hypothetical transfer matrix construction would yield the same result. The growth diagram locality assumption fails without integrability.

## Partition Function vs. Bijection Structure

The previous analysis treats this as a pure bijection problem, but vertex models naturally encode **weighted enumeration**. The KTW puzzle count c^λ_{μν} emerges as a **transfer matrix eigenvalue** or **partition function evaluation**.

This suggests the real question isn't about direct bijection, but whether the **spectral data** of the transfer matrix (eigenvalues, eigenvectors) directly encodes LR tableau information. The "face labels" in a growth diagram would then be **intermediate spectral parameters**, not tableau entries themselves.

## Boundary Conditions: The Integrable vs. Non-Integrable Distinction

KTW puzzles have **fixed triangular boundary** - this corresponds to **domain wall boundary conditions** in vertex models. But domain wall boundaries are **integrable** only for specific R-matrix forms (typically free-fermionic or related to quantum groups).

The triangular geometry imposes **three-fold symmetry constraints** that may break integrability. Standard rectangular domain wall solutions (like Izergin determinants) don't apply. We need **triangular lattice generalizations** of integrable vertex models.

## The Cylindric Construction Red Herring

The "cylindric construction" mentioned isn't about cylinder topology - it's about **periodic boundary conditions** in growth diagrams. But KTW puzzles have **open boundaries** with fixed edge labels. Cylindric construction is irrelevant here.

The confusion arises from conflating **topological** properties (boundary conditions) with **algebraic** properties (growth rules). KTW puzzles live on contractible triangular domains, not cylinders.

## Alternative Framework: Quantum Integrability

Instead of classical growth diagrams, consider **quantum integrable systems** with triangular geometry:

1. **Quantum KZ equations** on triangulated surfaces
2. **Hecke algebra representations** with boundary specializations  
3. **qKZ solutions** giving puzzle-tableau correspondence via **monodromy**

The LR tableau entries would emerge as **residues** of qKZ connection matrices, not as growth diagram face labels. This explains the 12→3 "compression" as **quantum-to-classical limit**.

## Spectral Parameter Constraints

In any vertex model approach, the **spectral parameter constraints** must respect the **symmetric function structure** of Schur polynomials. This means:

- Parameters must satisfy **wheel conditions** (qKZ integrability)
- **Specialization limits** must