# Specialist Analysis: The Synthesis Misses the Migration Point

## Critical Challenge: The Constraint Propagation Framework is Backwards

The synthesis fundamentally misunderstands what migration actually computes. Migration is NOT "constraint resolution metadata" - it's **jeu de taquin rectification applied to a specific geometric encoding**. The author claims migration "abandons integrable dynamics," but this reveals a gap in understanding jdt mechanics.

Migration works because:
1. Mosaics encode LR-tableaux as **rectifiable skew shapes** 
2. Hexagonal flips ARE jdt slides in disguise - they preserve rectification invariants
3. The "constraint satisfaction" is actually **shape standardization** - a well-understood integrable process

The compression ratios (2,880 → 720 → 3) don't indicate "categorical incompatibility" - they reflect **reading order multiplicity**. Multiple puzzle tile arrangements can yield identical rectified tableaux, exactly as expected from jdt theory.

## Where Growth Diagrams Actually Fail: Schutzenberger Involution Structure

The synthesis overlooks the deepest obstruction: growth diagrams inherently respect **Schutzenberger involution** (evacuation), but KTW puzzles don't naturally carry this structure. This is why RSK-type processes work with growth diagrams - they're built on involution-respecting dynamics.

Purbhoo's bijection succeeds precisely because migration **creates** the involution structure through rectification. You can't bypass this step with face labels because the involution emerges from the geometric process itself, not from initial puzzle data.

## The Yang-Baxter Red Herring

The vertex model specialist's "spectral parameter obstruction" misdiagnoses the problem. Jdt itself lacks spectral parameters yet admits local descriptions (Haiman's mixed insertion algorithms). The issue isn't integrability per se - it's that **puzzle boundary conditions don't decompose into growth-compatible initial data**.

Unlike RSK where you input a word/permutation (naturally sequential), puzzles require **simultaneous specification of three boundary segments**. Growth diagrams need one "input edge" - puzzles have three equal-status boundaries.

## Alternative Proposal: Reverse-Migration Growth Diagrams

Instead of direct puzzle→tableau growth diagrams, consider **reverse-migration diagrams**:

1. Start with LR-tableau 
2. Apply **anti-rectification** moves as growth steps
3. Face labels track **de-rectification choices** 
4. Final configuration encodes the mosaic, hence puzzle

This respects the mathematical structure: rectification is the "natural" direction for jdt dynamics. The growth diagram would track the **degrees of freedom** in unrectifying a standard tableau.

Face labels could encode: which edges are "active" for de-rectification, maintaining local compatibility while building up the global mosaic structure.

## The Missing Geometric Insight: Boundary Orientation

The synthesis ignores a crucial geometric fact: KTW puzzles have **oriented boundaries** with specific rhombi angle constraints. Growth diagrams typically assume **translation-invariant** local rules, but puzzle pieces have inherent orientation.

This is why hexagonal geometry matters - not for topology, but for **angle compatibility**. Standard growth diagrams can't naturally encode the 60°/120° rhombi constraints that make puzzles work.

## Computational Challenge Extension

The computational evidence actually suggests a different approach: if 2,880 → 3 compression exists, consider **growth diagrams in the reverse direction**. Start with the 3 tableau entries, use growth steps to **expand the solution space** until reaching full puzzle specification.

Each growth step would add **one layer of solution multiplicity**, with face labels tracking how tableau constraints propagate outward to boundary configurations. This inverts the usual growth diagram logic but respects the mathematical structure.

## What Growth Diagrams CAN'T Do: Non-Crossing Path Enumeration

The deepest issue the synthesis misses: KTW puzzles are equivalent to **non-crossing path counting**, which has fundamentally different combinatorics than growth processes. Growth diagrams excel at **insertion-based** constructions, but non-crossing paths require **global planarity constraints**.

Migration succeeds because it converts non-crossing path problems into **rectification problems** - a change of combinatorial category. Direct growth diagrams would need to maintain planarity constraints locally, which is impossible.

## Verdict: The Growth Diagram Question Asks for Impossible Mathematics

Not because of locality issues or integrability, but because it asks for