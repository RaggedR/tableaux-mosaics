# SPECIALIST ANALYSIS: The Synthesis Misses the Jeu de Taquin Heart

## The Migration-Growth Diagram Connection is Backwards

The synthesis fundamentally misunderstands what migration **is**. Migration isn't a "hidden growth diagram"—it's a **sequence of jeu de taquin slides** applied to hexagonal tilings. Each migration step corresponds to a specific jdt rectification of a skew shape, and the "hexagonal flips" are precisely the local moves that preserve rectification equivalence classes.

The synthesis claims face labels should encode "braided migration instructions," but this gets the causality wrong. **Migration instructions emerge from tableau rectification requirements**, not from arbitrary face label choices. The 4:1 redundancy (12 nabla → 3 entries) isn't "gauge freedom"—it's the **Schutzenberger equivalence** acting on tableau reading orders.

## Challenging the "Spectral Parameter" Red Herring

The synthesis obsesses over missing spectral parameters, but this reveals a profound misunderstanding of how Purbhoo's bijection works. The bijection puzzle → mosaic → migration → LR-tableau **deliberately avoids** spectral methods precisely because it operates through **pure jdt combinatorics**.

Here's what the synthesis misses: **The puzzle boundary conditions already encode all necessary spectral information** through the geometric constraints of rhombus tilings. Adding explicit spectral parameters would be redundant, not necessary. The "Yang-Baxter relations" mentioned aren't missing—they're built into the **hexagonal tiling constraints** themselves.

## The Real Technical Obstruction

The synthesis correctly identifies triangular vs. rectangular geometry as crucial, but draws the wrong conclusion. Growth diagrams for **rectangular arrays** naturally accommodate jdt slides because rows correspond to **horizontal slide sequences**. But KTW puzzles have **three boundary components** that must be processed simultaneously.

Here's the deeper issue the synthesis avoids: **Growth diagram face labels encode local adjacency constraints, but jdt slides are inherently non-local**. When you slide a tableau entry, it can propagate arbitrarily far through rectification. This **non-locality** cannot be captured by face labels that depend only on adjacent vertices.

## Exposing the "Migration Reordering" Fantasy

Phase 3 of the proposed research program is mathematically impossible. Migration sequences are **canonically ordered by mosaic geometry**—you can't arbitrarily reorder them without breaking the rectification invariants. The synthesis suggests migration could be "reordered to align with transfer matrix rows," but this would destroy the **jdt slide compatibility** that makes migration work in the first place.

The synthesis fundamentally misunderstands that **reading order determines rectification structure**, not vice versa. You can't choose an arbitrary reading order and then force it to work with jdt—the rectification requirements constrain which orders are valid.

## What the Synthesis Gets Right (and Why It Matters)

The synthesis correctly identifies that the existing transfer matrices might "already work but in disguised form." But the disguise isn't spectral parameters—it's **reading order translation**. 

Here's a concrete alternative framework the synthesis overlooks: What if growth diagram face labels don't encode tableau entries directly, but instead encode **jdt slide directions**? Each face could specify which of the possible rectification moves to apply at that position. This would preserve the **local rule structure** while respecting the **global rectification constraints**.

## A Counter-Proposal: Jdt Growth Diagrams

Instead of the synthesis's three-phase program, I propose investigating **jdt-native growth diagrams**:

1. **Face labels as slide instructions**: Each label specifies a rectification move type
2. **Compatibility conditions from tableau constraints**: Adjacent labels must produce valid skew shapes
3. **Boundary conditions from puzzle geometry**: Triangle edges constrain possible slide sequences

This respects both the **local nature of growth diagrams** and the **global constraints of jdt rectification** without invoking unnecessary spectral machinery.

## The Fundamental Challenge the Synthesis Avoids

The real question isn't whether face labels can encode tableau data—it's whether **row-by-row construction can respect jdt slide dependencies**. In Purbhoo's bijection, migration steps depend on the **entire current mosaic configuration**, not just local adjacency data.

This creates an **information flow problem**: growth diagram rows are constructed independently, but jdt slides require **global state awareness**. The synthesis's proposal to use spectral parameters or braided instructions doesn't resolve this fundamental mismatch.

**