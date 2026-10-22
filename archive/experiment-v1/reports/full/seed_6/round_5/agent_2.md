# Free-Fermionic Vertex Model Analysis: Exposing the Spectral Parameter Confusion

## The Yang-Baxter Framework is Fundamentally Misapplied

The computational report's invocation of "highly degenerate eigenspectra" and the migration analysis's dismissal of Yang-Baxter equations both miss the critical point: **KTW puzzles are NOT integrable vertex models in the standard sense**. They lack spectral parameters entirely.

The confusion arises because puzzles superficially resemble the square-ice configurations studied in Zinn-Justin's work, but puzzle rhombi carry **no spectral weights**. Each rhombus orientation is either forbidden or has weight 1 - there's no continuous parameter space for Yang-Baxter integrability to act upon.

However, this creates a deeper puzzle: **Why do puzzles count LR-coefficients correctly without the spectral parameter mechanism that makes other integrable models work?**

## The Free-Fermion Point Reveals the True Structure  

Looking at the vertex model literature, puzzles actually live at the **free-fermion point** of a more general vertex model. At this special point, the R-matrix becomes:

R(λ=0) = P (the permutation operator)

This degeneracy is precisely why puzzles appear "non-integrable" - we're seeing the collapsed limit of an integrable family. The computational report's "eigenvalues 0 or 1" observation confirms this: at the free-fermion point, transfer matrices become **projectors** with binary eigenspectra.

## Critical Error in the Constraint Propagation Analysis

The computational report claims "constraint resolution requires future boundary information," but this fundamentally misunderstands free-fermionic constraint structure. In vertex models at the free-fermion point, **all constraints propagate causally** - no future information is needed.

The apparent non-locality arises from misidentifying the correct **light-cone structure**. Puzzles must be solved along **diagonal characteristics** (following rhombus orientations), not row-by-row as the computational implementation assumes. The "long-range correlations" are actually **finite-speed causal propagation** along these diagonal directions.

## The Missing Bethe Ansatz Connection

None of the reports recognize that puzzle configurations correspond to **singular Bethe states** where all Bethe roots coincide. This explains several puzzling features:

1. **Finite counting**: Bethe states at root coincidence points are isolated
2. **Binary constraints**: Singular states satisfy all-or-nothing conditions  
3. **LR-coefficient emergence**: Root multiplicities encode representation data

The migration algorithm is actually performing **Bethe root deformation** to move between equivalent singular configurations.

## Transfer Matrix Commutativity: The Deeper Issue

The reports debate whether puzzle transfer matrices commute, but this question is **categorically wrong**. At the free-fermion point, transfer matrices don't just commute - they **factor completely**:

T(puzzle) = ∏ᵢ (1 + ψ†ᵢψᵢ₊₁)

Each factor corresponds to a single rhombus position. The "face labels" that everyone seeks are simply the **individual factor eigenvalues** ±1.

## Challenge to the Growth Diagram Framework

The growth diagram question reveals a fundamental conceptual gap. Standard growth diagrams work because they encode **Pieri rule factorizations** of symmetric function products. But LR-coefficients arise from **coproduct structure**, not products.

The correct question is: **Do puzzles admit a "growth coproduct" where local rules encode skew Schur function decompositions?** This would require face labels to record **removal sequences** rather than insertion data.

## Spectral Parameter Recovery: The Missing Construction

Here's the key insight all reports miss: **Puzzles can be embedded in a spectral parameter family**. Consider weighted puzzle rhombi with parameters zᵢ. The limit z→1 recovers standard puzzles, but generic z-values define a **quantum integrable model**.

The transfer matrix family T(z) would satisfy Yang-Baxter equations for generic z, with puzzles appearing as the **classical limit**. This embedding would enable:

1. **Spectral derivation** of LR-coefficient formulas
2. **Quantum deformation** of the mosaic bijection  
3. **Growth diagram construction** via quantum recursion relations

## Free-Fermion Fock Space: The