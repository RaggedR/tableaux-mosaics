# Mathematical Synthesis: The Growth Diagram Chimera

## The Core Tension: Locality vs. Connectivity

All four specialists converge on a fundamental incompatibility, though they frame it differently. The **central mathematical issue** is that KTW puzzles encode **global connectivity constraints** (monochromatic paths must connect boundary components correctly) while growth diagrams require **strict locality** (face labels depend only on immediate neighbors).

This isn't just a technical obstacle—it's a **categorical mismatch**. Growth diagrams work precisely because RSK insertion has bounded support: inserting element k affects only positions ≤ k. Puzzle resolution has **unbounded support**: resolving a nabla vertex affects path connectivity throughout the entire configuration.

## The Migration Algorithm Misconception

The specialists are unanimous: migration is **not** a growth diagram in any sense. But they miss a deeper point. Migration operates by **homotopy deformation**—it preserves topological invariants while changing local combinatorial structure. Growth diagrams operate by **inductive construction**—they build bijections step-by-step through local rules.

The synthesis attempted to bridge this gap by invoking "dual complexes," but this creates more problems than it solves. There's no natural embedding where migration becomes local, because the **connectivity preservation** requirement is inherently global.

## The 4:1 Arithmetic Pattern: A Diagnostic

The computational specialist's 4:1 ratios reveal something profound that other specialists misinterpret. This isn't "branching multiplicities" or "quantum group signatures"—it's evidence of **exponential growth** in the nabla degree-of-freedom space relative to tableau space.

Consider: 12 free nablas per puzzle, 3 tableau entries per puzzle. If there were a local growth diagram, we'd expect roughly equal degrees of freedom at each level. Instead, we see 4:1 expansion, suggesting the bijection **necessarily involves global coordination** that cannot be encoded locally.

## The Yang-Baxter Red Herring

The Yang-Baxter specialist overcomplicates the spectral parameter issue. The real question isn't whether puzzles are "integrable" in the quantum sense—it's whether they admit **deterministic local evolution rules**. The degree-6 vertex constraint is a red herring; the issue is that puzzle boundary conditions **overdetermine** the internal configuration in ways that prevent local rule-based construction.

However, the specialist correctly identifies that puzzle weights are binary (0/1), which breaks any continuous parameter structure. This suggests we should look for **discrete analogues** of integrability, not classical Yang-Baxter equations.

## The Schutzenberger Constraint: Misunderstood Severity

The tableau specialist underestimates how severely Schutzenberger equivariance constrains growth diagram construction. Evacuation is a **global operation** that depends on the entire tableau structure. Any local encoding of Schutzenberger-equivariant data would require face labels to implicitly track **arbitrarily distant** tableau information.

But there's a deeper issue: puzzle configurations have **three-fold rotational symmetry** while LR tableaux have inherent **left-right asymmetry** (through the insertion process). This symmetry breaking cannot be achieved through local rules—it requires global knowledge of which boundary should be treated as "input" versus "output."

## The Missing Framework: Stratified Bijections

All specialists miss that the real mathematical structure might be **stratified bijections**—different local rules in different regions of the puzzle space. This isn't the "exponential blowup" the synthesis feared, but rather a **finite stratification** where puzzle types require different growth diagram architectures.

The computational obstructions might signal **stratum boundaries**—places where one local rule system must hand off to another. This would explain both the migration failures and the arithmetic patterns without requiring global non-locality.

## The Correct Research Direction

Instead of forcing KTW puzzles into the growth diagram framework, we should ask: **What is the natural categorical framework for puzzle-tableau bijections?**

The evidence points toward **graph homomorphisms between structured posets**:
- Puzzle space: directed graph with connectivity constraints
- Tableau space: distributive lattice with insertion order
- Bijection: structure-preserving graph homomorphism

This explains why migration works (it preserves graph structure through local moves) while growth diagrams fail (they assume lattice structure that puzzles don't possess).

## Synthesis: The Fundamental Category Error

The growth diagram conjecture commits a **fundamental category error**: it assumes that because