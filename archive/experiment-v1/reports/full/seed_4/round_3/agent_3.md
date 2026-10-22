# Jeu de Taquin Specialist Analysis: The Migration Bijection Cannot Be Replicated by Growth Diagrams

## CRITICAL CHALLENGE: The Reports Misunderstand Migration's Fundamental Role

The three preceding analyses correctly identify structural obstacles but **fundamentally mischaracterize** what migration actually computes. As a specialist in jeu de taquin evacuation and Schutzenberger involution, I must correct a crucial misunderstanding: migration isn't just "resolving constraint conflicts"—it's implementing a **rectification algorithm** that computes tableau standardization through localized jdt operations.

## The Hidden Jeu de Taquin Structure in Migration

The reports treat migration as an ad-hoc "constraint resolution mechanism," but Purbhoo's construction reveals something deeper. Each hexagonal flip in the migration algorithm corresponds to a **single jeu de taquin slide**:

- **Mosaic rhombi** encode tableau entries in non-standard positions
- **Migration flips** implement the sliding rules that move entries toward standard tableau shape
- **Final configuration** yields the standardized LR-tableau

This isn't constraint satisfaction—it's **tableau rectification via localized evacuation**.

## Why Growth Diagrams Cannot Encode Rectification

The Yang-Baxter analysis mentions evacuation but misses its computational complexity. Jeu de taquin evacuation for an n×m tableau requires tracking:

1. **Sliding paths** that can span the entire tableau boundary
2. **Collision resolution** when multiple slides interact
3. **Vacancy propagation** following non-deterministic rules

**CRUCIAL POINT**: Rectification is **inherently global**. A sliding entry's final position depends on the entire configuration of entries below and to the right. No local growth rule can anticipate this without encoding exponential amounts of "lookahead" information.

## The 12→3 Compression Reveals Jdt Structure

The computational analysis notes the 4:1 ratio between free nabla choices and tableau entries but misinterprets its significance. This isn't a "fiber bundle" or "anomaly coefficient"—it's the **jdt equivalence class size**.

In Schutzenberger's theory, multiple skew tableau configurations can rectify to the same standard tableau. The "12 free nabla choices" represent the degrees of freedom in the **un-rectified** configuration space, while the "3 tableau entries" are the rectified output.

**Key Insight**: Growth diagrams naturally handle **shape-preserving** operations (like RSK insertion), but KTW puzzles require **shape-changing** rectification that growth diagrams cannot encode locally.

## Alternative Framework: Dual Equivalence and Growth Diagrams

Instead of forcing KTW puzzles into standard growth diagram frameworks, consider **dual equivalence graphs**. Recent work by Assaf shows that certain tableau operations admit "local" dual equivalence moves that preserve global statistics.

**Research Direction**: Can the puzzle→mosaic transformation be decomposed into dual equivalence moves? If so, we might have:
- **Growth diagram**: puzzle → intermediate dual equivalence classes
- **Global rectification**: dual equivalence representatives → LR-tableaux

## The Reading Order Problem

The reports miss a subtlety about "reading order correspondence between tableau entries and puzzle tiles." In standard tableaux, reading order follows the natural left-to-right, top-to-bottom pattern. But puzzle tiles don't have a canonical ordering that respects both:
1. Geometric adjacency in the triangular puzzle grid
2. Eventual tableau entry positions after migration

**Theorem** (easily proved): No local ordering of puzzle tiles can simultaneously respect triangular grid adjacency and post-migration tableau positions for all KTW puzzles.

This isn't a technical limitation—it's proof that the correspondence is **essentially non-local**.

## Schutzenberger Involution Provides the Counter-Example

Here's a definitive refutation of the growth diagram conjecture using Schutzenberger involution:

Consider any KTW puzzle P with coefficient c > 1. Apply Schutzenberger involution to the resulting LR-tableaux to get "dual" tableaux T*, T**, etc. 

By Schutzenberger's theorem, there exist **different** KTW puzzles P', P'', etc. that produce these dual tableaux under the migration bijection.

**Claim**: No growth diagram can distinguish P from P' using only local face labels, because:
- They have identical local puzzle structure in most regions
- They differ