# Specialist Report: The Growth Diagram Impossibility Theorem

## The Synthesis Misses the Fomin Framework Entirely

The generalist's analysis commits a fundamental error by conflating "locality" with Fomin's actual growth diagram structure. **Growth diagrams are not about local rules per se—they are about face labeling schemes that preserve certain commutation relations under directed graph traversal.** The synthesis treats growth diagrams as if they were cellular automata, when they're actually **algebraic encoding systems** for bijective correspondences.

## The Real Obstruction: Face Label Cardinality

The computational "4:1 ratios" that the synthesis dismisses as "exponential growth" actually reveal the **core impossibility**. In Fomin growth diagrams, face labels must have **bounded cardinality** that depends only on the local vertex degrees. For RSK, face labels are Young tableaux entries (cardinality ≤ n), and the growth property ensures this bound is preserved under edge operations.

KTW puzzles fundamentally violate this. Each nabla vertex represents a **3-way branching choice**, but these choices are **globally constrained** by boundary connectivity. The "12 free nablas → 3 tableau entries" pattern shows that face labels would need **exponentially large cardinalities** to encode the global constraint satisfaction. This isn't a technical obstacle—it's a **categorical impossibility**.

## Migration vs. Growth: The Category Error Exposed

The synthesis correctly identifies that migration is "homotopy deformation," but misses why this **excludes** growth diagram structure. Migration preserves puzzle **invariants** (boundary conditions, rhombi counts) while changing local structure. Growth diagrams preserve local **operations** while changing global structure.

**Critical insight**: Migration moves in the **kernel** of the constraint map (boundary → interior), while growth diagrams move in the **image** of the construction map (sequence → tableau). These are **orthogonal directions** in the space of bijective correspondences.

## The Stratification Fallacy

The synthesis proposes "stratified bijections" with "different local rules in different regions." This fundamentally misunderstands growth diagram universality. **Fomin growth diagrams work precisely because they use the same face labeling rules everywhere.** Stratification would break the commutation property that makes growth diagrams bijective.

Moreover, puzzle "stratification" by boundary type creates **exponentially many strata** (one per boundary configuration), defeating any computational advantage. The synthesis conflates finite stratification (manageable) with **combinatorial stratification** (intractable).

## The Spectral Parameter Misconception

Contrary to the synthesis, the Yang-Baxter connection is **not** a red herring. The absence of spectral parameters in KTW puzzles signals that they live in a **different algebraic category** than integrable systems. Growth diagrams for RSK work because tableaux insertion has **quantum group structure** (via crystal bases). KTW puzzles lack this structure.

**Key observation**: The degree-6 constraint isn't just about vertex valency—it encodes **braiding relations** that cannot be realized through face label commutation. This is why puzzle rhombi cannot be "grown" incrementally like tableau boxes.

## The Cylindric Construction: A False Promise

The synthesis doesn't address cylindric growth diagrams, but this extension **cannot save** the KTW case. Cylindric diagrams handle **periodic boundary conditions**, not **constrained boundary conditions**. KTW puzzles have rigid boundary specifications that determine interior structure—the opposite of periodicity.

Furthermore, cylindric face labels encode **translation invariance**, while puzzle face labels would need to encode **connectivity preservation**. These are mathematically incompatible requirements.

## The Correct Mathematical Framework: Why Not Growth Diagrams

The synthesis asks for the "natural categorical framework" but doesn't recognize that **we already know it**: KTW puzzles are **geometric crystals** in the sense of Berenstein-Kazhdan, not combinatorial crystals in the sense of Kashiwara. They live in the **tropicalization** of the Grassmannian coordinate ring, not in the **combinatorialization** of its representation theory.

This explains both the migration algorithm's success (geometric moves preserve tropical structure) and growth diagram's failure (combinatorial rules cannot capture geometric constraints).

## The Impossibility Theorem

**Theorem** (Informal): No growth diagram exists for the KTW puzzle-LR tableau bijection because:

1. **Face label cardinality**: Puzzle constraints require face labels of expon