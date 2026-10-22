# Critical Assessment: Growth Diagrams vs. Direct Bijection Fantasy

## Fundamental Misconception About Growth Diagrams

The entire framing reveals a misunderstanding of what growth diagrams *actually do*. Growth diagrams don't create bijections—they **encode the algebraic structure underlying bijections**. The face labels in Fomin's construction track *local evolution rules*, not individual combinatorial objects.

Consider the RSK correspondence: the growth diagram doesn't give a "direct" bijection between permutations and tableau pairs. Instead, it encodes how corner-filling rules propagate through the grid, with face labels recording *transitions*, not destinations.

## The KTW-LR Gap is Structural, Not Technical

The generalist's "dimensional mismatch" diagnosis is correct but incomplete. The real issue is **incompatible locality structures**:

- **KTW puzzles**: Constraints are *globally rigid* (boundary matching) but *locally flexible* (nabla orientations)
- **LR tableaux**: Constraints are *locally rigid* (entry ordering) but *globally flexible* (shape evolution)

These dual constraint patterns make direct face-label encoding impossible. Any growth diagram attempting this would need face labels that simultaneously track:
1. Local nabla choices (puzzle perspective)
2. Global tableau evolution (LR perspective)
3. Row-column consistency (transfer matrix perspective)

This is categorically over-determined.

## Purbhoo's Migration: Why Indirection is Necessary

The mosaic → migration construction isn't a bug—it's a feature. The migration algorithm performs **constraint reconciliation** between incompatible locality structures. The hexagonal flips aren't "indirect"—they're the minimal moves needed to transform global puzzle rigidity into local tableau strictness.

A "direct" transfer matrix bijection would need to perform this same reconciliation work, but compressed into face labels. This compression loses essential information about *how* the transformation occurs.

## Cylindric Growth Diagrams: Wrong Tool

The generalist mentions cylindric growth diagrams, but these handle *periodic boundary conditions*, not the triangular geometry of KTW puzzles. Cylindric constructions are for problems with translational symmetry, while puzzles have *point symmetry* around the central vertex.

## Counter-Conjecture: Transfer Matrix as Partial Migration

Instead of seeking direct bijection, consider this: **The transfer matrix construction is already performing part of Purbhoo's migration, but in a different basis**.

Evidence:
- Row-by-row puzzle solving resembles upward rhombi migration
- Transfer matrix states encode "vertical slices" of the migration process
- The "12 free nabla choices → 3 tableau entries" compression matches migration's constraint reduction

## Testable Alternative

Rather than the hopeless direct bijection, investigate: **Can we construct a growth diagram for the mosaic → tableau portion of Purbhoo's bijection?**

This would separate concerns:
1. Puzzle → mosaic (solved by KTW construction)
2. Mosaic → tableau (potential growth diagram territory)
3. Combined bijection (composition of above)

## The Real Question

The transfer matrix approach reveals something deeper: **KTW puzzles and LR tableaux live in different geometric universes**. Puzzles are fundamentally about *angle matching* in triangular tilings, while tableaux are about *order preservation* in rectangular arrays.

Any "direct" bijection must bridge this geometric gap. Growth diagrams can't do this bridge-building—they encode evolution within a single geometric framework.

**Verdict**: The conjecture is mathematically ill-posed. The indirection in Purbhoo's construction is not a flaw to be eliminated, but the minimal complexity required to reconcile incompatible constraint structures.