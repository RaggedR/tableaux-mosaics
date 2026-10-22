# Challenging the Growth Diagram Orthodoxy: A Migration-Centric Reframing

The three reports demonstrate sophisticated technical knowledge but collectively **miss the fundamental relationship between jeu de taquin locality and growth diagram structure**. As a specialist in Purbhoo's bijection and migration theory, I must challenge their shared assumption that "local rules" and "growth diagrams" are the correct mathematical framework for understanding this problem.

## The Migration Locality Misunderstanding

All three reports mischaracterize migration as either "globally dependent" (computational) or "automatically local" (Fomin). This reveals a crucial gap in understanding jdt mechanics. **Migration steps are algorithmically local but combinatorially non-trivial**—each jdt slide depends only on adjacent tableau entries, but the *sequence* of slides emerges from global optimization.

The computational report's "backtracking across multiple rows" conflates two distinct processes: **puzzle constraint satisfaction** (which is indeed global) and **migration path determination** (which follows local jdt rules but may require global optimization to find valid paths).

**Critical distinction**: Migration doesn't backtrack through puzzle choices—it follows predetermined jdt slide sequences that are locally determined once the initial mosaic is fixed. The "global dependencies" are in mosaic-to-migration translation, not in jdt execution.

## Growth Diagrams Are the Wrong Question Entirely

The Fomin and Yang-Baxter reports assume growth diagrams are the natural framework for bijection analysis, but this **fundamentally misunderstands what makes Purbhoo's construction work**. The bijection succeeds precisely because it **avoids** the locality constraints that growth diagrams impose.

**Key insight**: The puzzle→mosaic→migration→tableau chain creates a **non-local encoding** of global LR tableau structure through local operations. This is architecturally opposite to growth diagrams, which encode global structure through local consistency.

The "face label" framework assumes we can decompose the bijection into row-by-row operations with local state. But migration explicitly violates this: **tableau entries are determined by jdt slide sequences that can propagate across arbitrary distances**.

## The Schutzenberger Inversion Connection

Here's where all three reports miss the deepest structural insight: **Schutzenberger involution is not peripheral to growth diagram questions—it's the core obstruction**.

Schutzenberger involution acts on LR tableaux through **global evacuation procedures** that reverse all local jdt slide directions simultaneously. If growth diagrams existed for the KTW→LR bijection, they would need to **commute with Schutzenberger evacuation**. But evacuation inherently requires global coordination of all local operations—exactly what growth diagrams cannot provide.

**Concrete obstruction**: Any local face rule system that produces correct LR tableaux must also produce correct Schutzenberger-evacuated tableaux when evacuation is applied to the growth process. But evacuation reverses the temporal order of growth steps, making this requirement **combinatorially impossible** with finite face label alphabets.

## Why the Yang-Baxter Framework Misses the Point

The spectral parameter report correctly identifies that LR coefficients emerge from Yang-Baxter systems, but **confuses integrability with bijection structure**. Yang-Baxter equations govern how transfer matrices commute—they don't govern how combinatorial bijections factor.

**The fundamental error**: Assuming that because LR coefficients satisfy Yang-Baxter relations, combinatorial objects that enumerate these coefficients must also satisfy Yang-Baxter consistency. This is a category error—the objects live in different mathematical universes.

Migration operates in the **combinatorial category** of tableaux and jdt slides. Yang-Baxter operates in the **representation category** of quantum groups and spectral parameters. These categories are connected through **character theory** but not through direct structural correspondence.

## The Computational Evidence Actually Supports Non-Existence

The computational report's complexity analysis provides the strongest evidence **against** growth diagram existence, but draws the wrong conclusions. The P-SPACE complexity of puzzle enumeration versus polynomial complexity of LR coefficient computation reveals that **KTW puzzles are not the natural combinatorial encoding** of LR multiplication.

**Correct interpretation**: The complexity gap shows that puzzles and tableaux represent the **same mathematical objects** (LR coefficients) through **fundamentally different combinatorial structures**. This structural difference is precisely what makes Purbhoo's bijection non-trivial—and precisely what makes growth diagram factorization impossible.

The "backtracking behavior" isn't a bug