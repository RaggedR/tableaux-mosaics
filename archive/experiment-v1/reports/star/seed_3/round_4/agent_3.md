# FUNDAMENTAL MISUNDERSTANDING OF THE MIGRATION BIJECTION

## THE SYNTHESIS COMPLETELY MISCHARACTERIZES MIGRATION

The synthesis claims migration works through "bounded local operations (hexagonal flips with finite propagation distance)" and that "global properties emerge through composition of bounded operations." This is **mathematically incorrect** and reveals a fundamental misunderstanding of what migration actually does.

Migration is not a sequence of independent local flips. It is a **coordinated transformation** where the entire pattern of rhombi moves collectively according to global constraints derived from the puzzle boundary conditions. The "hexagonal flips" are not arbitrary local moves—they are **forced reconfigurations** that maintain specific global invariants throughout the process.

**Concrete counterexample**: In a 3×3 rhombus tiling, changing a single nabla choice can force rhombi reconfiguration that propagates across the **entire tiling**. There is no meaningful sense in which this has "finite propagation distance"—the effect is inherently global because the tiling constraints couple distant regions.

## THE READING ORDER INSIGHT THE SYNTHESIS IGNORES

The synthesis focuses on locality and bounded operations but completely ignores the crucial insight from Purbhoo's bijection: the **reading order correspondence** between puzzle tiles and tableau entries.

In the puzzle → mosaic → migration → tableau sequence, the migration preserves a specific reading order on rhombi that directly determines the tableau content. This is not about local vs. global operations—it's about **maintaining a canonical order** on combinatorial objects while transforming their geometric arrangement.

**Critical question**: How does the proposed direct growth diagram construction maintain this reading order correspondence? The synthesis suggests "face labels correspond to nabla choices," but nabla choices don't have a natural ordering that respects tableau construction rules.

## YANG-BAXTER STRUCTURE IS MORE RESTRICTIVE THAN CLAIMED

The synthesis dismisses Yang-Baxter constraints as merely "arithmetic necessities," but this understates their **geometric rigidity**. Yang-Baxter equations don't just constrain which bijections exist—they impose **specific integrability conditions** that severely limit the possible local update rules.

For KTW puzzles, any direct growth diagram construction must respect the **non-commutative geometry** of the puzzle constraints. The rhombus tilings have inherent orientation and chirality that cannot be encoded in standard rectangular growth diagrams without losing essential structural information.

**Specific challenge**: The synthesis claims this is "decidable," but provides no algorithm for checking Yang-Baxter compatibility of proposed face labeling schemes. This is a **non-trivial computational problem** in statistical mechanics, not a routine verification.

## THE "TRIANGULAR LATTICE" PROPOSAL REVEALS DEEPER CONFUSION

The synthesis proposes analyzing "triangular growth structures" instead of rectangular ones, claiming this "changes the computational complexity analysis entirely." This shows **fundamental confusion** about the relationship between puzzle geometry and tableau combinatorics.

Tableaux are inherently **rectangular objects** with row and column constraints. The triangular geometry of puzzles reflects the **boundary conditions** of Littlewood-Richardson coefficients, not the internal structure of tableaux themselves. Any bijection must ultimately encode rectangular tableau data.

**The real challenge**: How do you encode rectangular tableau constraints (row-strictness, column-strictness, skew shape) using triangular geometric operations? This is not a complexity theory question—it's a **structural compatibility problem** that the synthesis completely sidesteps.

## JEU DE TAQUIN SLIDES IMPOSE GLOBAL COHERENCE CONDITIONS

The synthesis claims jdt migration constructs "global consistency through bounded local operations," but this misunderstands how jdt slides work. Each slide is **globally determined** by the requirement to maintain tableau properties under skew-shape modification.

In Schutzenberger's involution, the slide path is **uniquely determined** by global tableau structure—there are no "local choices" that could be encoded in growth diagram face labels. The migration process preserves this determinism, which is why it successfully produces valid LR-tableaux.

**Insurmountable obstacle**: Direct growth diagrams require **local choice data** at each step to determine face labels. But jdt slides have **no local choices**—they are completely determined by global tableau structure. This creates a fundamental incompatibility that the synthesis ignores.

## THE BOUNDED LOCALITY CLAIM FAILS FOR SCHUR FUNCTION MULTIPLICATION

The synthesis argues that "most successful combinatorial algorithms use bounded locality," citing RSK as an example. But this comparison is **categorically incorrect**. RSK constructs tableaux from **