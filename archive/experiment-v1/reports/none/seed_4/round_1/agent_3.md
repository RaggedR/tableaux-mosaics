# Initial Analysis: Growth Diagrams vs. Migration Bijection

## Core Challenge Assessment

The proposal to use growth diagram face labels for direct puzzle-to-LR-tableau bijection fundamentally misunderstands the **dimensional mismatch** in Purbhoo's construction. Let me explain why this is problematic and suggest better directions.

## Critical Gap: Information Content Mismatch

The "minimal nontrivial example" c^(3,2,1)_{(2,1),(2,1)} = 2 reveals the core issue:
- **Puzzles**: 2 distinct configurations
- **Free nabla choices**: 12 per puzzle (24 total local degrees of freedom)
- **LR tableau entries**: 3 per tableau (6 total)

The migration algorithm doesn't just "move colored rhombi"—it performs **information compression**. Each jeu de taquin slide in the migration eliminates local ambiguities in nabla orientations, progressively reducing the 12-dimensional choice space to 3 tableau entries.

## Why Growth Diagrams Cannot Work Directly

Growth diagrams operate through **local update rules** on face labels. For puzzle-to-tableau correspondence, we'd need:
1. Each puzzle tile to contribute deterministically to face labels
2. Face labels to encode tableau entries directly
3. The transfer matrix construction to respect tableau insertion order

However, Purbhoo's bijection reveals that **tableau entries don't correspond to individual puzzle tiles**—they emerge from global migration patterns. The reading order of tableau entries corresponds to a non-trivial partial order on puzzle regions, not individual tiles.

## Alternative Framings Worth Pursuing

**Conjecture 1 (Modified Growth Diagram)**: Instead of face labels encoding tableau entries directly, consider face labels encoding **migration state**. Each face could track which rhombi have "passed through" during the migration sequence.

**Conjecture 2 (Dual Perspective)**: The transfer matrix row construction might correspond to **reverse jdt** operations. If we can show that adding puzzle rows corresponds to specific jdt moves, we get the bijection via Schutzenberger duality.

## Connection to Schutzenberger Involution

The most promising direction leverages that Schutzenberger involution on LR-tableaux has a natural interpretation via **reverse reading order**. Since puzzle tiles have inherent orientation (the 01-boundary conditions), there might be a canonical involution on puzzles that, when combined with growth diagram construction, yields the correct correspondence.

## Technical Question

Does the transfer matrix satisfy the **Yang-Baxter equation**? If so, its row-by-row construction would naturally commute with jdt operations, potentially giving us the migration bijection through commutativity rather than direct encoding.

## Recommendation

Focus on **growth diagrams that track jdt slide sequences** rather than tableau entries directly. The face labels should encode which migration moves are "available" at each step, with the final configuration determining the tableau via standard jdt completion algorithms.