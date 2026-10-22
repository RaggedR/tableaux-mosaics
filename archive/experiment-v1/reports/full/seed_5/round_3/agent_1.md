# Growth Diagram Analysis: Fundamental Structural Barriers

## CRITICAL OMISSION: The Local Rule Paradox

All three reports miss the **central impossibility** in Fomin's growth diagram theory: **local rules require invertible face transitions**. In any valid growth diagram, each face label uniquely determines the vertex transitions on its boundary. But KTW puzzles exhibit **irreversible constraint propagation**.

Consider the minimal example: a single rhombus tile can satisfy multiple local puzzle constraints simultaneously, but once placed in a mosaic, its contribution to the LR tableau is **uniquely determined by global position**. This breaks the fundamental local-global duality that makes growth diagrams work.

## THE CYLINDRIC CONSTRUCTION DOESN'T APPLY HERE

The reports invoke cylindric growth diagrams, but this misunderstands their scope. Cylindric diagrams work for **symmetric function multiplication** where the cylinder topology naturally encodes **periodicity conditions**. KTW puzzles have **triangular boundary conditions** with no natural cylindrical embedding. 

More fundamentally, cylindric growth requires **translation-invariant local rules**. But puzzle constraints are inherently **boundary-dependent**—the same local configuration behaves differently near edges versus interior regions.

## CHALLENGING THE MIGRATION-AS-BIJECTION CLAIM

The jeu de taquin specialist claims migration is "already the direct bijection," but this reveals a **category confusion**. Migration operates on **mosaics** (rectified puzzle data), not on the puzzles themselves. The bijection chain is:

Puzzle → Mosaic → Migration → Tableau

The **Puzzle → Mosaic** step involves **global rectification** that destroys the local structure needed for growth diagrams. You cannot construct face labels from puzzle data because the puzzle-to-mosaic map is **globally non-local**.

## THE SPECTRAL PARAMETER RED HERRING

The vertex model analysis correctly identifies the lack of spectral parameters, but draws the wrong conclusion. The real issue isn't that KTW puzzles aren't integrable—it's that **growth diagrams don't require integrability**. 

RSK growth diagrams work perfectly well without Yang-Baxter equations or R-matrices. The problem is more fundamental: **KTW face labels would need to encode recording tableau entries**, but puzzle constraints don't naturally decompose into recording vs. insertion data.

## COMPUTATIONAL EVIDENCE REEXAMINED

The computational report's "counterevidence" actually supports a different interpretation. The observation that "two valid puzzles have different rhombus distributions but identical tableau content" suggests we need **weighted face labels** where multiple local configurations contribute to the same recording data.

But this leads to a **non-bijective correspondence**—exactly what growth diagrams are designed to avoid. The multiplicities in LR coefficients come from **global constraint counting**, not from local face weight accumulation.

## ALTERNATIVE FRAMEWORK: QUASI-GROWTH DIAGRAMS

Instead of forcing puzzles into standard growth diagrams, consider **constraint propagation diagrams** where:

1. **Face labels encode constraint states**, not tableau entries
2. **Local rules propagate feasibility**, not bijective transitions  
3. **Boundary conditions determine global multiplicities**

This framework could explain:
- Why the puzzle→mosaic step is necessary (global constraint resolution)
- How migration works (following constraint gradients)
- Why direct bijection fails (constraints don't factor locally)

## THE DEEPER STRUCTURAL ISSUE

The fundamental barrier is that **KTW puzzles live in constraint space** while **LR tableaux live in combinatorial space**. Growth diagrams work when both objects inhabit the same combinatorial universe with compatible local operations.

The bijection exists, but it necessarily involves **changing mathematical categories**—from constraint satisfaction (puzzles) to combinatorial construction (tableaux). This category change cannot be encoded in local face rules.

## VERDICT: CONJECTURE IS FUNDAMENTALLY FLAWED

The growth diagram conjecture fails not due to technical details, but due to **categorical incompatibility**. The correct research direction is understanding **why** the Purbhoo bijection requires the intermediate mosaic construction—this indirection is mathematically necessary, not an artifact to be eliminated.

The constraint propagation framework offers a more promising approach for understanding the puzzle→tableau correspondence without forcing it into an incompatible growth diagram structure.