# Analysis: Growth Diagrams for KTW Puzzles - Critical Gaps and Extensions

## Core Challenge to the Proposed Framework

The fundamental issue with seeking a "direct" growth diagram bijection puzzle → LR-tableau is that it misunderstands the essential role of **local moves** in Purbhoo's construction. The migration step isn't an inefficient detour—it's the crucial component that resolves the **non-uniqueness problem** inherent in puzzle-to-tableau mappings.

## The Nabla Choice Problem

The example c^(3,2,1)_{(2,1),(2,1)} = 2 reveals the core issue: each puzzle contains multiple "free nabla choices" that don't affect the puzzle's validity but must be consistently resolved to produce a unique LR-tableau. The 12 free nablas projecting to 3 tableau entries suggests a 4-to-1 local correspondence that requires **global coordination**.

A row-by-row transfer matrix approach cannot resolve this non-locality because:
- Nabla orientations in different regions of the puzzle interact non-trivially
- The jeu de taquin structure emerges from these interactions, not from local face labels
- Growth diagrams work when local choices aggregate independently—but puzzle nablas don't

## Missing Connection to Schutzenberger Involution

The problem statement ignores how migration relates to **Schutzenberger involution**. In standard jeu de taquin theory, the involution provides the key insight that sliding paths can be reversed and reordered. Purbhoo's migration leverages this by:
1. Converting puzzle rhombi to a "taquin-ready" mosaic format
2. Using hexagonal flips as generalized jeu de taquin slides
3. Exploiting the involution to ensure path-independence

A growth diagram approach would need to encode this involutive structure directly in its face labels—but transfer matrices are inherently **non-involutive** (they represent directed processes).

## Alternative Framing: Tropical Geometry Perspective

Rather than seeking direct growth diagrams, consider the **tropical geometric** interpretation of puzzles. KTW puzzles can be viewed as:
- Piecewise-linear functions on the Newton polytope
- With local constraints encoded by the puzzle piece rules
- Where LR-tableaux correspond to particular **tropical bases**

From this view, migration isn't a detour but a **change of tropical coordinates**. The question becomes: can we find tropical coordinates where the puzzle-to-tableau map is coordinate-wise linear?

## Extension: What Growth Diagrams Actually Capture

If we insist on growth diagrams, the right question is: **What intermediate objects do growth diagram face labels naturally encode?**

I propose they should encode **partially-completed mosaics** rather than tableau entries. The face labels would track:
- Local rhombus orientations resolved so far  
- Pending constraints from unresolved nabla choices
- Compatibility data for future hexagonal flips

This shifts the bijection to: puzzle → growth-diagram-mosaic → LR-tableau, where the second arrow uses standard migration.

## The Reading Order Fallacy

The problem assumes "reading order of tableau entries corresponds to an order on puzzle tiles." This is incorrect. The Standard Young Tableau reading order (top-to-bottom, left-to-right within rows) has **no natural correspondence** to any geometric ordering on puzzle pieces. The correspondence emerges only after migration resolves the global constraint interactions.

This suggests that any growth diagram approach must either:
1. Abandon natural geometric orderings on puzzles, or  
2. Accept that face labels encode migration-intermediate objects

## Conclusion

The search for a "direct" growth diagram bijection puzzle → LR-tableau is likely **categorically impossible** because it attempts to eliminate the essential non-local coordination that migration provides. The productive direction is understanding what intermediate structures growth diagrams can naturally capture in this context.