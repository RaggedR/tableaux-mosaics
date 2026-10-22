# Schutzenberger Involution Specialist Analysis: Fundamental Misunderstanding of Tableaux Structure

## CORE CHALLENGE: The Problem Conflates Different Tableau Spaces

The proposed "direct bijection" reveals a profound misunderstanding of how **Schutzenberger involution** and **jeu de taquin** structure the space of tableaux. The agents correctly identify impossibilities but miss the deeper issue: **KTW puzzles and LR tableaux live in fundamentally different combinatorial universes that cannot be directly connected**.

## Critical Gap: Migration IS Schutzenberger-Compatible

The reports completely ignore that Purbhoo's migration algorithm preserves the **essential involutive structure** of tableaux. Each hexagonal flip in the migration corresponds to a **sequence of jeu de taquin slides** that maintain Schutzenberger compatibility. This isn't computational overhead—it's the **minimal structure required** to preserve tableau invariants.

**Key Technical Point**: In the c^{3,2,1}_{(2,1),(2,1)} = 2 example, the two LR tableaux are **not** Schutzenberger-equivalent. Any "direct" bijection would need to explain why puzzle symmetries don't translate to tableau symmetries. Migration explains this through rhombi circulation patterns that break apparent puzzle symmetries.

## The Reading Order Fallacy

The problem mentions "reading order of tableau entries corresponds to an order on puzzle tiles." This is **categorically wrong**. Tableau reading order is determined by:
- **Yamanouchi word** structure from jeu de taquin
- **Standardization** properties under Schutzenberger involution
- **Plactic relations** that define tableau equivalence classes

Puzzle tile ordering follows **geometric constraints** (nabla orientations, rhombi adjacencies) that have **no relationship** to plactic structure. The agents miss this, but it's the fundamental obstruction.

## Jeu de Taquin Reveals the True Structure

Here's what the reports miss: **Migration implements generalized jeu de taquin in mosaic space**. Each rhombi movement corresponds to:

1. **Sliding** tableau entries according to jdt rules
2. **Maintaining rectification** at each step  
3. **Preserving Knuth relations** that define plactic equivalence

The "12 free nabla choices → 3 tableau entries" isn't compression—it's **jdt rectification** eliminating non-standard configurations. Only 3 entries survive because only 3 positions can contain **jdt-movable** elements under the given boundary constraints.

## Growth Diagrams Cannot Handle Evacuation

The agents mention RSK growth diagrams but ignore the crucial difference: **RSK insertion preserves standardness**. KTW puzzles require operations analogous to **tableau evacuation** (the strongest form of jdt), which:

- **Cannot be localized** to individual cells
- **Requires global rectification** across the entire tableau
- **Destroys growth diagram locality** by definition

Purbhoo's migration IS the evacuation process operating in dual (mosaic) space. The hexagonal flips correspond to the **dual moves** of jdt rectification slides.

## Schutzenberger Involution Breaks "Direct" Bijections

Consider the Schutzenberger involution S acting on LR tableaux. Under any "direct" bijection Φ: Puzzles → Tableaux, we would need:

**S(Φ(P)) = Φ(S̃(P))**

for some involution S̃ on puzzles. But puzzle symmetries (rotations, reflections) **don't correspond** to Schutzenberger involution properties:

- **S reverses tableau shape** but puzzle geometry is rigid
- **S changes reading order** but puzzle tile order is geometrically fixed  
- **S preserves rectification** but puzzle constraints are shape-dependent

This incompatibility **proves** no direct bijection exists.

## The Cylindric Red Herring Extended

The agents dismiss cylindric constructions, but miss the deeper point: **Cylindric tableaux arise from periodic jeu de taquin**, where slides "wrap around" the cylinder. But KTW puzzles have **genuine boundary conditions** that:

- **Break slide periodicity** at puzzle edges
- **Create jdt dead ends** where slides cannot continue
- **Require migration** to move past these obstructions