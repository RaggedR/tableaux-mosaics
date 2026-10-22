# Growth Diagram Structure Challenges: Beyond Computational Implementation

## The Migration Failure Reveals Deeper Structural Issues

The computational researcher correctly identifies that migration implementation failures block verification, but this masks a **more fundamental theoretical problem**. Even if migration worked perfectly, it wouldn't resolve whether KTW puzzles admit growth diagram structure. Migration is a **global transformation algorithm**, not a **local rule system**.

**Critical Distinction**: Growth diagrams require **local face labeling rules** that determine labels from immediate neighbors. Migration operates through **non-local hexagonal flips** that can affect distant regions of the mosaic. This is algorithmically incompatible with growth diagram locality requirements.

The computational failure isn't just an implementation bug—it reveals that **migration and growth diagrams are fundamentally different paradigms** for organizing the same combinatorial data.

## Nabla Multiplicities Expose Non-Uniformity That Growth Diagrams Cannot Handle

The researcher's observation about unequal nabla distributions (4 vs 8 free nablas) is **devastating for growth diagram prospects**. In Fomin's framework, face labels must satisfy **weight conservation**: the "mass" flowing into each face must equal the mass flowing out through local rules.

**Theoretical Impossibility**: If puzzles with different nabla counts contribute equally to LR coefficients, then the local rules must somehow **absorb or generate weight non-locally**. This violates the fundamental locality principle of growth diagrams.

**Alternative Interpretation**: The nabla multiplicity disparity suggests we need **weighted growth diagrams** where face labels carry **multiplicity factors**. But such weighted systems lose the elegant bijective property that makes growth diagrams powerful for RSK-type correspondences.

## Spectral Structure Indicates Non-Markovian Information Flow

The computational researcher identifies eigenvalue structure in transfer operators, but **misinterprets its significance** for growth diagrams. Spectral parameters in integrable systems (like Yang-Baxter) encode **particle interactions**, not **constraint propagation**.

**Key Insight**: The eigenvalues likely reflect **global topological constraints** from puzzle boundary conditions, not local face labeling rules. This creates a **hierarchy problem**:
- Local rules must respect global eigenvalue structure
- But eigenvalues emerge from **non-local boundary interactions**
- Growth diagrams cannot naturally encode such multi-scale dependencies

**Growth Diagram Limitation**: Fomin's local rules work when information propagates **monotonically** (like in RSK bumping). Puzzle constraints propagate **bidirectionally** with **retroactive invalidation**—a structure growth diagrams cannot represent.

## The Cylindric Construction Fails for Non-Planar Constraint Graphs

Both researchers miss that KTW puzzles live on **hexagonal lattices** with **non-planar constraint graphs**. Standard growth diagrams work on **rectangular grids** where face labels propagate along **planar directed paths**.

**Topological Obstruction**: Hexagonal puzzle constraints form **six-way intersections** that cannot be decomposed into binary face labeling rules. The constraint graph has **genus > 0**, violating the planar assumptions underlying cylindric growth diagram constructions.

**Technical Problem**: Even if we could define hexagonal face rules, the **non-commutative diagram chasing** required to verify consistency would involve **higher-order compatibilities** that standard growth diagram frameworks don't handle.

## Puzzle Branching Choices Form Constraint Satisfaction, Not Growth Dynamics

The fundamental misframing is treating puzzle construction as **growth dynamics**. KTW puzzles are **constraint satisfaction problems** where:
- Each piece placement constrains future possibilities
- Solutions emerge through **backtracking search**, not forward growth
- Valid completions satisfy **global consistency**, not local rules

**Conceptual Error**: Growth diagrams model **additive processes** (like inserting tableaux entries). Puzzle solving involves **selective processes** (choosing compatible configurations). These require **different mathematical frameworks**.

## Alternative: Puzzle Configuration Spaces as Fiber Bundles

Rather than forcing puzzles into growth diagram structure, consider them as **fiber bundles** over Young diagram data:
- **Base space**: LR coefficient indexing (λ, μ, ν)
- **Fiber space**: Valid puzzle configurations
- **Structure group**: Hexagonal symmetries preserving boundary conditions

**Theoretical Advantage**: This naturally accommodates:
- Non-uniform nabla multiplicities (variable fiber dimensions)
- Non-local constraint propagation (bundle connection structure)  
- Spectral parameters (characteristic classes of the bundle)

## The