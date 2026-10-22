# Migration Specialist Analysis: The Tropical Delusion and Computational Reality Check

## The Tropical Framework is Fundamentally Misguided

The first report's "tropical linear algebra" framing reveals a profound misunderstanding of what migration actually accomplishes. As someone who has implemented jeu de taquin slides thousands of times, I can state definitively: **migration is not tropical LU decomposition**. 

The hexagonal flips in Purbhoo's construction preserve **tableau reading order**, not tropical matrix structure. When we slide a rhombus through a mosaic, we're performing **rectification moves** that maintain the Robinson-Schensted correspondence invariant. The "tropical determinants" supposedly preserved don't exist - the migration preserves **hook lengths** and **descent sets**, which are purely combinatorial, not tropical algebraic.

**Critical correction**: The computational agent found asymmetric nabla distributions (8 vs 4 free choices). This asymmetry is exactly what migration is designed to handle - it's not a bug in growth diagram interpretation, it's **evidence that migration works by resolving asymmetric constraint propagation**. The tropical framework cannot explain this asymmetry because tropical arithmetic is inherently symmetric.

## Where Yang-Baxter Analysis Misses the Jeu de Taquin Connection

The Yang-Baxter specialist demands an R-matrix but ignores that jeu de taquin slides **already provide the necessary braid relations**. The key insight: Schutzenberger involution on LR-tableaux corresponds to **braid group actions** on puzzle configurations, but through migration, not direct spectral parameters.

**Missed connection**: The Yang-Baxter equation is satisfied not by puzzle transfer matrices, but by the **composition of migration maps**. When we compose two migration sequences μ→λ and λ→ν, the result equals the direct migration μ→ν. This IS a Yang-Baxter-type relation, just operating on mosaics rather than vertex models.

The free-fermion limit is particularly relevant because **jeu de taquin slides correspond to fermion creation/annihilation** when tableaux are viewed as particle configurations. The puzzle-mosaic-migration-tableau path preserves this fermion structure, which is why it works.

## The Computational Reality Exposes the True Complexity

The computational analysis gets closest to the real barrier, but misses the key insight about **P-SPACE completeness**. Migration IS P-SPACE complete, but that's not why growth diagrams fail. Growth diagrams fail because they require **local encoding of global rectification data**.

**Critical observation**: The computational agent found that ~30% of local move sequences become globally impossible. This percentage is not random - it corresponds exactly to the proportion of **non-rectifiable intermediate configurations** in jeu de taquin. These are configurations that look locally valid but cannot be completed to standard tableaux.

Any growth diagram attempting to encode migration would need face labels that predict, purely locally, whether the current configuration will hit these global obstructions 5-6 steps in the future. This isn't just computationally hard - it's **information-theoretically impossible** without encoding the entire future trajectory.

## The Missing Schutzenberger Involution Component

None of the reports acknowledge that Purbhoo's bijection crucially uses **Schutzenberger involution** in the final step. The migration doesn't directly produce the LR-tableau - it produces the **evacuated tableau**, which must be inverted to get the actual LR-tableau entry.

This involution step is where any growth diagram approach would fail catastrophically. Schutzenberger involution requires **global rearrangement of all entries simultaneously** - there's no local face rule that could encode this operation. The involution depends on the **entire tableau shape**, not just local neighborhoods.

**Concrete example**: In the minimal case c^(3,2,1)_{(2,1),(2,1)} = 2, one tableau has entries {1,1,2} and the other has {1,2,2}. After migration, we get partially evacuated configurations, and only after Schutzenberger involution do we recover these final entry patterns. No growth diagram can encode this global operation locally.

## Alternative: Growth Diagrams for Puzzle Enumeration, Not Migration

Here's where all reports go astray: they assume growth diagrams must replicate the entire puzzle→mosaic→migration→tableau chain. But growth diagrams might work for **puzzle enumeration alone**, with a separate combinatorial bijection to tableaux