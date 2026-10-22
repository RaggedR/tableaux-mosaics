# Analysis: The Migration Algorithm as the Missing Link

The three reports collectively misunderstand the fundamental nature of Purbhoo's bijection and consequently misframe the growth diagram question. As a specialist in jeu de taquin and migration algorithms, I see critical gaps in their analysis that require immediate correction.

## Migration ≠ Generic "Indirect" Construction

All three reports treat Purbhoo's puzzle→mosaic→migration→tableau construction as merely "indirect," but this reveals a profound misunderstanding. **Migration IS a sequence of local jeu de taquin slides**, each determined by reading order and vacancy propagation rules. The reports miss that migration already exhibits the local-to-global structure that growth diagrams formalize.

The key insight they overlook: when we perform migration on a mosaic, each jdt slide creates **local recording data** - specifically, which rhombus moves and how the vacancy propagates. This recording data is precisely what growth diagram face labels should encode.

## Critical Error: Dimensional Analysis

The computational report's "4:1 reduction" analysis (12 nabla choices → 3 tableau entries) fundamentally misunderstands what the face labels should count. They're not counting tableau entries - they're counting **migration step choices**. Each migration produces a sequence of jdt slides, and the face labels should encode the local decisions at each slide.

For c^(3,2,1)_{(2,1),(2,1)} = 2, there are exactly 2 mosaics, each generating a specific migration sequence. The growth diagram question is whether these migration sequences can be generated row-by-row through local face label rules.

## The Yang-Baxter Report's Category Error

The integrability analysis completely misses the point. KTW puzzles don't need to satisfy Yang-Baxter equations directly - **the migration algorithm does**. Migration is a sequence of commuting jdt operations, and jdt slides satisfy braid relations (a discrete analogue of Yang-Baxter). The growth diagram structure should emerge from this commutativity, not from puzzle tiling constraints.

The spectral parameter objection fails because migration doesn't require spectral parameters - it uses **vacancy tracking** and **reading order**, both of which are discrete and local.

## What Face Labels Actually Should Encode

None of the reports correctly identify what face labels should represent. Based on jdt theory, they should encode:

1. **Vacancy position** after each migration step
2. **Direction of rhombus movement** (which neighbor the vacancy came from)  
3. **Reading order increment** (how the tableau reading advances)

This creates a natural correspondence: puzzle → mosaic → migration sequence → face label sequence → tableau.

## The Schutzenberger Connection Ignored

Most critically, all reports ignore the role of Schutzenberger involution in the migration process. The LR tableau reading order corresponds directly to how Schutzenberger involution acts on the migration sequence. Growth diagram face labels should encode the **involution action** at each step.

This connection suggests the growth diagram exists but requires understanding migration as **Schutzenberger-compatible jdt sequences**, not generic local rules.

## Computational Framework Correction

The third report's computational approach is backwards. Instead of enumerating puzzles and checking for patterns, we should:

1. **Implement correct migration** (fixing the broken mosaic.py)
2. **Record migration sequences** for all mosaics in small examples
3. **Extract local rules** from how migration steps depend on boundary data
4. **Test if these rules satisfy Fomin consistency**

The transfer matrix structure should emerge from migration commutativity, not puzzle constraint propagation.

## Alternative Conjecture: Migration Growth

Based on my understanding of jdt and migration, here's the correct conjecture:

**Migration Growth Conjecture**: There exist local rules such that row-by-row construction of migration sequences (via face labels encoding jdt slide choices) produces exactly the same tableau outcomes as Purbhoo's full migration algorithm.

This respects the actual structure of the bijection rather than trying to bypass it.

## Research Direction: Tableau Path Independence  

The real test is **path independence in tableau construction via migration**. If we build a tableau by performing partial migrations on mosaic rows, do different row orders yield the same result? If yes, growth diagrams exist. If no, the migration structure is inherently non-local.

This is experimentally testable with the corrected mosaic implementation and would settle the conjecture definitively.

## Conclusion

The reports collectively fail because they don't engage