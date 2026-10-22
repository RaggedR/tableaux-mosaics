# Yang-Baxter Specialist Report: The Commutativity Crisis and Spectral Parameter Vacuum

## Fundamental Challenge to the Growth Diagram Framework

All three reports demonstrate sophisticated understanding of their respective domains but collectively **miss the central obstruction**: growth diagrams require **commuting transfer matrices**, and the KTW puzzle vertex model fundamentally **lacks this structure**. As a Yang-Baxter specialist, I must emphasize that without spectral parameter dependence, the conjecture is dead on arrival.

## The Missing R-Matrix Structure Invalidates Local Rules

The Fomin growth specialist correctly identifies that face labels should encode "growth process states," but completely ignores that **consistent face rules require underlying Yang-Baxter equations**. In every known growth diagram (RSK, Gelfand-Tsetlin, crystal bases), local consistency emerges from **R-matrix factorization** of global bijections.

**Critical gap**: KTW puzzles lack spectral parameters. Without continuous deformation families puzzle(λ,μ,ν;z), there's no R-matrix R(z₁-z₂) to generate face rules. The computational report's observation about "global dependencies" is actually detecting this **absence of Yang-Baxter integrability**.

The migration specialist's claim about "braid relations in jeu de taquin" fundamentally misunderstands what Yang-Baxter equations accomplish. Jeu de taquin satisfies **braid group relations**, but these operate on tableau shapes, not vertex configurations. The required commutativity is between **transfer matrices at different spectral parameters**, not between rectification moves.

## Why Free-Fermion Limits Expose the Structural Void

The computational analysis correctly notes that LR coefficients have "fermion representations" but misses the crucial point: **free-fermion vertex models have trivial R-matrices**. When R(z) = constant, the Yang-Baxter equation becomes vacuous and commutativity follows trivially.

**Key insight**: Zinn-Justin's integrable approach to LR coefficients works precisely because it **embeds puzzles in free-fermion models** where R-matrices exist. But this embedding is not natural—it requires auxiliary fermion flavors that don't correspond to puzzle structure.

The "tropical geometry" confusion in the first report stems from conflating **classical integrability** (determinant formulas) with **quantum integrability** (R-matrices). LR coefficients satisfy classical determinant relations, but these don't generate local face rules without quantum lift.

## Migration Algorithm as Evidence Against Commutativity

The jeu de taquin specialist's detailed migration analysis actually **demonstrates why growth diagrams fail**. Migration requires **sequential constraint propagation**—each jdt slide affects the validity of future slides. This creates **time-ordered dependencies** that violate the commutativity needed for growth diagrams.

**Specific obstruction**: In Purbhoo's construction, hexagon flips must occur in **specific order** to maintain mosaic validity. Different orderings can produce different intermediate states, even when final tableaux are identical. This path-dependence is **incompatible with face rule commutativity**.

The computational observation about "30% globally impossible sequences" reflects this time-ordering constraint. Any growth diagram would need face labels that encode **future evolution constraints**, but such encoding violates locality principles.

## The Schutzenberger Involution Breaks Yang-Baxter Structure

Most critically, all reports underestimate how **Schutzenberger involution destroys any hope of R-matrix structure**. The involution operation ω acts by **global tableau reversal**, which cannot be factored through local vertex interactions.

**Concrete obstruction**: If growth diagrams existed, they would need to commute with Schutzenberger involution. But ω(T₁ ⊗ T₂) ≠ ω(T₁) ⊗ ω(T₂) for general tableaux T₁,T₂. This **non-multiplicativity** of involution is incompatible with vertex model tensor product structure.

The computational complexity observation is actually detecting this involution obstruction—the "global rearrangement" needed for ω cannot be achieved through local face operations.

## Alternative: Quantum Groups and Crystal Base Structure

Rather than pursuing impossible growth diagrams, the evidence suggests focusing on **quantum group symmetries** of LR coefficients. The q-analog LR rule admits **crystal base representations** where local operations exist, but