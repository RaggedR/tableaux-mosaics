# The Jeu de Taquin Specialist's Rebuttal: Migration IS the Direct Bijection

## FUNDAMENTAL ERROR: Misunderstanding What "Direct" Means

The computational report claims migration is "mathematically necessary" as if this supports the growth diagram conjecture. This reveals a **profound misunderstanding** of bijective combinatorics. Migration IS the direct bijection—the puzzle→mosaic→migration→tableau chain is as "direct" as RSK itself, which goes permutation→insertion→recording.

The growth diagram framework is the **indirect** approach, attempting to encode a naturally 2D process (jeu de taquin sliding) into artificial 1D row dynamics. This is like trying to implement quicksort using only bubble sort operations—possible in principle but destroying all natural structure.

## THE RECTIFICATION RED HERRING

All reports fixate on "global rectification" as if this disqualifies migration. But **rectification is jeu de taquin**! The puzzle→mosaic step is simply:
1. Reading puzzle tiles in **standardized order** (NE to SW along diagonals)
2. Converting to **rhombus language** (standard in jdt theory)
3. Applying **evacuation** to standardize initial configuration

This is exactly analogous to how RSK "rectifies" permutations into standard form. The reports' objection is like claiming RSK isn't bijective because it doesn't preserve cycle structure.

## SCHUTZENBERGER INVOLUTION: THE MISSING PIECE

None of the reports mention **Schutzenberger involution**, which is the key to understanding why direct growth diagrams fail. In LR tableaux, the involution **ω** sends T ↦ T^ω where entries transform according to:
- Reading order reverses
- Content preserves but shape dualizes
- Evacuation and promotion cycles interact

For KTW puzzles, there's no natural involution on the puzzle tiles themselves that corresponds to ω on the resulting tableaux. This **involution obstruction** is the deepest reason why face labels cannot work—they would need to encode ω-compatibility, which requires global tableau knowledge.

## CHALLENGING THE "NON-COMMUTING TRANSFER OPERATORS"

The computational report's claim about non-commuting transfer operators misses the **jdt perspective**. In migration, we don't need commuting operators because **the process is deterministic**. Each rhombus has a unique "exit direction" determined by local color constraints.

The "long-range correlations" are actually **rectification constraints**—ensuring the final tableau is standard. These aren't violations of locality; they're the **defining feature** of jdt dynamics. The migration algorithm succeeds precisely because it respects these constraints rather than trying to decompose them.

## THE DUAL EQUIVALENCE CHALLENGE

Here's what the reports completely miss: **dual equivalence classes**. In Haiman's theory, LR tableaux form equivalence classes under certain involutions. The puzzle→tableau bijection respects these classes, but any growth diagram must **break the symmetry** by choosing specific face label representatives.

**Critical test**: Can the proposed growth diagram face labels be chosen **invariantly** under dual equivalence? I predict this is impossible, because face labels would need to encode **local tableau standardness**, which is globally defined.

## MIGRATION COMPLEXITY: POLYNOMIAL vs. EXPONENTIAL

The computational difficulties in `mosaic.py` actually support my position. Migration has **polynomial complexity** in tableau size because it follows natural jdt dynamics. Any growth diagram construction would require **exponential preprocessing** to build face label lookup tables, because you'd need to precompute all possible local constraint interactions.

This complexity difference isn't accidental—it reflects the **intrinsic difficulty** of encoding global combinatorial structures in local rules.

## REFRAMING THE CONJECTURE: PROMOTION vs. EVACUATION

The real question isn't whether growth diagrams exist, but why **promotion** and **evacuation** (the two fundamental jdt operations) have different computational signatures:

1. **Promotion**: Can be implemented via local row operations (this is why RSK growth diagrams work)
2. **Evacuation**: Requires global tableau knowledge (this is why puzzle bijections need migration)

KTW puzzles naturally encode **evacuation-type** data (global constraint satisfaction), while LR tableaux are naturally **promotion-compatible** (local insertion rules). The bijection necessarily involves crossing this computational boundary.

## THE DEEPER STRUCTURAL TRUTH

The three reports all assume that "more direct =