# Specialist Analysis: The Migration Fallacy and Forgotten Fundamentals

## The Central Misconception: Migration ≠ Growth Diagram

The synthesis commits a **fundamental error** in claiming "Purbhoo's migration algorithm IS a growth diagram—just not in the plane." This reveals a profound misunderstanding of what migration actually accomplishes versus what growth diagrams encode.

Migration is a **sequence of jeu de taquin slides** applied to transform a mosaic into standard form. Each hexagonal flip corresponds to a specific jdt operation with well-defined evacuation paths. This is **categorically different** from growth diagram face labels, which encode insertion/recording data at each step of a bijective construction.

The synthesis conflates **process** (migration algorithm) with **encoding** (growth diagram labels). Migration transforms one combinatorial object into another through local moves. Growth diagrams encode the **entire bijection** through face label arithmetic. These are distinct mathematical operations that cannot be unified by appealing to "dual complexes."

## The Schutzenberger Constraint: Deeper Than Acknowledged

The synthesis mentions Schutzenberger equivariance but misses the crucial point: **jeu de taquin and Schutzenberger involution have a specific commutation relationship** that any growth diagram encoding must preserve. 

In LR-tableaux, Schutzenberger involution acts by evacuation followed by rotation. Under jdt slides, this becomes a **controlled interaction** between slide directions and reading orders. Any face label encoding must respect this interaction locally, which places **much stronger constraints** than the synthesis suggests.

The computational "topological obstructions" are likely manifestations of **Schutzenberger non-commutativity**: places where the local face label updates cannot simultaneously preserve jdt slide validity and Schutzenberger evacuation paths.

## The 4:1 Ratio: Missed Connections to Tableau Combinatorics

The synthesis accepts the computational specialist's 4:1 ratios as mysterious "branching multiplicities" without connecting them to **known tableau phenomena**. In LR-tableau theory, systematic 4:1 ratios appear in **standard/non-standard pairs** under certain skew shape configurations.

Specifically, when a skew shape λ/μ has multiple inside corners, the number of standard tableaux often relates to non-standard tableaux by small integer ratios reflecting **promotion operator orbits**. The observed 4:1 pattern likely reflects cases where exactly 4 puzzle configurations map to each tableau configuration under the bijection.

This suggests the growth diagram question should focus on **promotion-equivariant encodings**: can face labels track not just tableau entries, but their promotion classes?

## The Spectral Parameter Relevance: Understated

The synthesis dismisses Yang-Baxter connections as "contextually misplaced," but this ignores **established connections** between jeu de taquin and quantum group actions. The tropicalization of crystal graph operations naturally leads to Yang-Baxter equations in specific limits.

More critically, the "non-integrability" argument is backwards. The fact that migration encounters obstructions doesn't prove non-integrability—it suggests we're looking at **boundary effects** of an integrable system. Many integrable systems have singular loci where standard solution methods fail.

The quartic minimal polynomials and S₄ orbit structures aren't "massive machinery"—they're **natural invariants** of the A₂ root system that governs degree-6 puzzle vertices. Ignoring this connection loses essential structural information.

## The Dual Complex Claim: Category Error

The synthesis's "dual complex" framework confuses **geometric duality** with **combinatorial duality**. Migration operates on mosaics through hexagonal flips, but these live in the **same combinatorial space** as the original puzzle, just with a different local equivalence relation.

There is no meaningful sense in which migration is "3-dimensional" while growth diagrams are "planar projections." Both operate through **discrete local updates** on planar graph-like structures. The apparent non-locality of migration comes from the fact that hexagonal flips can propagate effects across **disconnected puzzle regions**, not from higher-dimensional embedding.

## The Stratification Reality: More Complex Than Dismissed

The synthesis dismisses "stratified locality" as causing "exponential blowup," but misses that **stratification might be necessary**. Growth diagrams work for RSK because tableau insertion has uniform local rules. Puzzle→tableau bijections might require **different local rules** in different regions of the