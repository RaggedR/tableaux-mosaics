# Migration Bijection Specialist Report: The Growth Diagram Chimera

## Fundamental Challenge: The Reports Misunderstand Migration as Computation

The computational report's "spectral projection" interpretation fundamentally misframes migration. Migration is **not** eigenspace decomposition—it's a **geometric transformation** of tiling patterns that preserves combinatorial invariants through controlled topology changes. The eigenvalue discussion reveals a category error: confusing discrete bijections with continuous spectral analysis.

The critical insight missing from all reports: **migration operates in the mosaic dual space**, not the puzzle constraint space. Face labels cannot encode this bijection because they live in the wrong geometric category.

## The Hexagonal Flip Causality Problem

The Yang-Baxter report correctly identifies non-locality but misses the geometric core: hexagonal flips in migration create **temporary non-orientable regions** in the mosaic. This isn't a bug in computational implementation—it's the fundamental reason why row-by-row growth diagrams cannot encode migration.

Growth diagrams assume **planar causality**: information flows in a directed acyclic pattern. But migration requires **controlled passage through non-orientable intermediate states** where the usual notion of "before/after" breaks down topologically. Face labels cannot encode information that exists in temporarily non-orientable space.

## Jeu de Taquin: The Missing Algorithmic Connection

All reports ignore the deeper connection to jeu de taquin that makes migration work. Migration is **not** arbitrary hexagonal flipping—it's a **sequence of standardized jdt slides** applied to the mosaic's dual tableau structure. Each migration step corresponds to a specific jdt rectification move that preserves Robinson-Schensted-style invariants.

The crucial insight: **migration face labels would need to encode jdt slide sequences**, not static configuration data. But jdt slides have **unbounded interaction distance**—a single slide can propagate changes across the entire tableau. This violates the finite-locality requirement for growth diagram face labels.

## Schutzenberger Involution: The Hidden Global Symmetry

The computational report's "correlation decay" analysis misses the fundamental symmetry structure. Puzzle configurations aren't just constrained by local rules—they exhibit **global Schutzenberger duality** inherited from the underlying LR-tableau structure.

Under Schutzenberger involution, the reading order of tableau entries **reverses globally**. This creates **global anti-correlation** in puzzle tile arrangements that cannot be captured by local face labels. Any growth diagram attempting to encode this would require face labels that "know" about the global reversal structure.

## The Reading Order Correspondence: Why Local Rules Cannot Work

Here's the technical core that all reports miss: the bijection between puzzle tiles and tableau entries depends on **reading order**, which is a **global property** of the tableau shape. Two puzzles with identical local structure can map to different LR-tableaux if their reading orders differ.

**Concrete Example**: In c^{(3,2,1)}_{(2,1),(2,1)}, the two puzzles differ only in a single nabla orientation, but this changes the **entire reading order** of the corresponding tableau entries. No local face label can encode a global permutation of entry positions.

## Migration Irreversibility: The Direction-Dependent Encoding Problem

The computational report notes "non-unique migration sequences" but doesn't understand the implication. Migration is **irreversible by design**—different migration paths can lead from the same mosaic to different intermediate configurations, even though they reach the same final tableau.

This **path-dependence** is what makes migration work as a bijection: it resolves the many-to-one mapping from mosaics to tableaux by **choosing canonical paths**. But path-dependence cannot be encoded in static face labels, which must represent **states**, not **processes**.

## Challenge to the Spectral Analysis Framework

The computational report's eigenspace analysis fundamentally misunderstands the bijection structure. The relevant mathematical object is **not** the transfer matrix spectrum—it's the **fiber bundle structure** over the LR-tableau space.

Each LR-tableau is the base of a fiber containing all puzzles/mosaics that map to it. Migration provides a **canonical section** of this bundle—a systematic way to choose one representative from each fiber. But bundle sections are **global geometric objects** that cannot be encoded in local chart data (face labels).

## The Topological Obstruction: Genus and Growth Diagrams

The computational bug report mentions "genus-1 structures" but doesn't realize this reveals the fundamental obstruction