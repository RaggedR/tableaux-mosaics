# Vertex Model Critique: Missing the Integrability Framework

## Fundamental Misdiagnosis of the Mathematical Structure

The previous analysis, while identifying legitimate concerns about multiplicity vs. bijection, **completely misses the integrable systems perspective** that makes this problem both well-posed and tractable. The dismissal of "raw KTW multiplicities" ignores that these coefficients arise as **partition functions of exactly solvable vertex models**.

### The Free-Fermion Connection is Key

Zinn-Justin's work reveals that KTW puzzles are **not** arbitrary geometric objects but arise from a specific integrable vertex model at the **free-fermion point**. This transforms the entire framework:

- Puzzle multiplicities become **expectation values** in a quantum integrable system
- The "nabla choices" are **vertex configurations** in a well-defined statistical model
- Growth diagrams naturally emerge from **commuting transfer matrices**

The previous analysis treats puzzles as static geometric objects, missing their dynamic vertex model origin.

### Transfer Matrix Commutativity Guarantees Growth Diagrams

The claim that "growth diagrams require discrete bijective objects" fundamentally misunderstands the **Yang-Baxter framework**. When transfer matrices commute (guaranteed by integrability), they automatically generate consistent growth diagram structures where:

1. **Face labels** encode spectral parameters and vertex weights
2. **Local rules** derive from R-matrix consistency conditions  
3. **Global coherence** follows from transfer matrix commutativity

This is not a "hope" or conjecture—it's a **theorem** for integrable vertex models.

### The Spectral Parameter is the Missing Piece

The original problem formulation overlooks the **spectral parameter dependence** in the vertex weights. Growth diagrams for integrable models require:

```
T(u)T(v) = T(v)T(u)  [commutativity]
T(u) = Tr[R(u,θ₁)...R(u,θₙ)]  [transfer matrix construction]
```

The face labels naturally encode these parameters, resolving the "non-locality" concern.

### Challenging the Purbhoo Detour

The previous analysis accepts Purbhoo's **puzzle→mosaic→migration→tableau** route as inevitable. But from the vertex model perspective, this is likely an **unnecessary detour**. The migration algorithm might be reconstructing what transfer matrix evolution does automatically.

**Counter-hypothesis**: The row-by-row transfer matrix construction directly encodes LR tableau growth without requiring intermediate mosaics. The hexagonal flips in Purbhoo's algorithm are **artifacts** of not working in the natural vertex model coordinates.

### Critical Technical Gap: Free-Fermion Weights

The key missing element is the **explicit form of free-fermion vertex weights** for the KTW puzzle model. Standard six-vertex weights are:

```
a = b = 1, c = 0  [free-fermion point]
```

But KTW puzzles involve **decorated vertices** (rhombi with internal structure). The growth diagram construction requires:

1. **Identifying the spectral parameters** for each vertex type
2. **Computing R-matrix elements** for rhombus-rhombus interactions  
3. **Verifying Yang-Baxter** for the full decorated vertex set

### Where the Previous Analysis Goes Wrong

The claim about "globally coupled constraints" reflects **misunderstanding of integrability**. In vertex models:
- **Global constraints** (like puzzle consistency) emerge from **local Yang-Baxter relations**
- **Long-range correlations** are mediated by **transfer matrix eigenvalues**
- **Non-local observables** have **local representations** in appropriate bases

### Proposed Research Direction

Instead of geometric duality or crystal structures, focus on:

1. **Explicit free-fermion weights** for KTW decorated vertices
2. **Spectral curve analysis** of the resulting transfer matrix
3. **Bethe ansatz construction** of the growth diagram face labels

The example c^(3,2,1)_{(2,1),(2,1)} = 2 should be computed as a **two-eigenvalue degeneracy** in the transfer matrix spectrum, not as "2 distinct puzzles."

### The Real Challenge

The genuine difficulty is not "discrete vs. continuous" but **identifying the correct vertex model** underlying KTW puzzles. Zinn-Justin's framework suggests it exists, but the **explicit construction