# Vertex Model Integrability: Why Growth Diagrams Miss the Yang-Baxter Structure

## The Free-Fermionic Blind Spot

The previous analysis dramatically **underestimates** the power of integrability theory while making fundamental errors about vertex model structure. The claim that "transfer operators cannot generate local face labels" ignores the **Yang-Baxter equation** entirely—the very mechanism that guarantees local vertex weights combine into commuting global operators.

**Critical Oversight**: KTW puzzles are **not arbitrary constraint satisfaction**—they emerge from the **free-fermionic six-vertex model** at specific parameter values. When Zinn-Justin (2009) proved LR coefficients count integrable tilings, he established that puzzle constraints derive from **R-matrix locality**. The Yang-Baxter relation
```
R₁₂(u-v)R₁₃(u-w)R₂₃(v-w) = R₂₃(v-w)R₁₃(u-w)R₁₂(u-v)
```
precisely governs how local vertex weights propagate into global transfer matrix commutativity.

**The R-Matrix Structure**: In free-fermionic models, vertex weights factorize as products of **elementary fermion scattering amplitudes**. This factorization is what makes growth diagrams possible—not some abstract "local rule" requirement, but the **explicit factorization property** of integrable vertex weights.

## Transfer Matrix Eigenspaces: The Missing Bethe Ansatz

The dismissal of "eigenspaces don't help" reveals complete ignorance of **coordinate Bethe ansatz** methods. Growth diagrams emerge naturally from the **highest weight structure** of transfer matrix eigenspaces, where tableau entries correspond to **Bethe root configurations**.

**Spectral Parameter Insight**: The researcher's "global vs local" distinction collapses when you introduce **inhomogeneous spectral parameters**. In the inhomogeneous six-vertex model, each row has parameter u_i, and the transfer matrix becomes:
```
T(u₁,...,uₙ) = Tr[R₀₁(u₁)R₀₂(u₂)...R₀ₙ(uₙ)]
```

**Local Growth from Spectral Limits**: Take the **principal specialization** u_i = q^i and let q → 1. The transfer matrix eigenvalues become **Schur function evaluations**, and the corresponding eigenvectors encode **SSYT fillings**. This isn't "global spectral structure"—it's the **local-to-global dictionary** that integrability provides.

## The Hexagonal Tiling Confusion

The claim that "hexagonal tiling geometry" prevents growth diagram construction fundamentally misunderstands the **rhombus tiling ↔ vertex model** correspondence. Hexagonal constraints don't create "crossing dependencies"—they encode the **ice rule** at each vertex.

**Lindström-Gessel-Viennot Connection**: KTW puzzles count **non-intersecting lattice paths**, which have a natural growth diagram interpretation through the **LGV determinant formula**. Each path step corresponds to a vertex model edge, and path non-intersection translates to the **local exclusion principle** in fermionic systems.

**Critical Error in Constraint Analysis**: The researcher claims nabla constraints "span multiple rows simultaneously," but this confuses **constraint propagation** with **local rule violation**. In integrable systems, long-range correlations emerge from **local interactions** via transfer matrix iterations—exactly what enables growth diagram construction.

## Purbhoo's Migration: Hidden Integrability Structure  

The assertion that "migration moves entire rhombus clusters because the mathematical reality requires it" completely misses the **underlying vertex model dynamics**. Migration isn't arbitrary geometric manipulation—it implements **Dehn twist operations** on the dual vertex model configuration space.

**Yang-Baxter Factorization**: Each migration step corresponds to a **sequence of elementary R-matrix moves**. The fact that these moves "preserve mosaic connectivity" reflects the **unitarity** of R-matrix transformations. This is precisely why migration generates bijections—it implements **integrable evolution** on the puzzle configuration space.

**Spectral Flow Interpretation**: The 12→3 multiplicity structure has a natural interpretation in terms of **Bethe eigenvalue degeneracies**. The "position-dependent degrees of