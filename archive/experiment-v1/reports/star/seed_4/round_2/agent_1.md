# Specialist Analysis: Critical Gaps in Growth Diagram Foundation

## Major Overlooked Issue: The Face Label Dimension Problem

The synthesis misses a fundamental dimensional constraint that invalidates the entire framework. In Fomin growth diagrams, **face labels must be locally computable from vertex weights**. But here's what's missing:

KTW puzzles with boundary conditions λ,μ,ν generate **exponentially many** nabla choice configurations (2^k for k free nablas), while each projects to exactly **one** LR tableau entry at each position. This creates a **many-to-one local mapping** that cannot be encoded in finite face labels.

**Critical Flaw**: You cannot store exponential information in polynomial face labels while maintaining local rules. The synthesis treats this as "constraint inversion" but it's actually **information-theoretic impossibility**.

## Wrong Framing: Growth Diagrams vs. Insertion Dynamics  

The specialists fundamentally misunderstand what growth diagrams accomplish. They're not about "bijections" - they're about **recording insertion dynamics**. In RSK, face labels track how elements insert into existing tableau structure.

**The Real Question**: Can puzzle nabla choices be interpreted as **insertion operations** on some underlying combinatorial object? This is completely different from encoding final tableau entries.

**Proposed Reframing**: Instead of puzzle→tableau correspondence, ask: "Do nabla choices generate a local insertion rule on mosaic configurations?"

## The Cylindric Growth Construction: Unexplored Territory

The synthesis completely ignores **cylindric growth diagrams**, which handle **periodic boundary conditions**. KTW puzzles have triangular geometry with fixed boundaries - but what about **cylindric puzzle variants**?

If we consider puzzles on cylindric surfaces (periodic horizontally), the growth diagram structure might emerge naturally. The "globality" issues disappear in periodic settings because there's no distinguished boundary.

**Research Gap**: Has anyone studied KTW puzzles on cylindric or toroidal surfaces? The growth diagram obstruction might be purely **topological**.

## Challenge: The Mosaic Connection is Backwards

The specialists assume mosaics are "intermediate objects," but this reverses the actual hierarchy. **Mosaics are the fundamental objects** - they're naturally defined on the triangular lattice with local hexagonal rules.

**Alternative Framework**: 
1. Define growth diagrams on **mosaic configurations** directly
2. Puzzles become **boundary projections** of mosaic growth
3. Tableaux become **rectification** of mosaic growth

This suggests the transfer matrix should act on **mosaic space**, not puzzle space. The nabla choices might be artifacts of projecting 2D growth onto 1D boundaries.

## Spectral Parameter Misconception

The vertex model analysis confuses **integrable systems** with **growth diagram structure**. Spectral parameters appear in **R-matrices** for Yang-Baxter equations, but growth diagrams use **local rules** without spectral dependence.

**Correction**: The additive/multiplicative distinction is irrelevant. Growth diagrams can encode **any** local update rule - the question is whether puzzle dynamics **have** local structure, not whether they're additive or multiplicative.

## Missing Connection: Jeu de Taquin Growth

Here's what no one considered: **Jeu de taquin itself might form a growth diagram**. The migration algorithm uses local hexagonal moves - these could be **growth diagram face labels**.

**Testable Hypothesis**: 
1. Start with empty mosaic configuration
2. Apply hexagonal moves according to local rules
3. Record each move as a face label
4. Check if final configuration gives LR tableau

If this works, the "indirect" Purbhoo construction is actually a **direct growth diagram** on mosaic space, just not on puzzle space.

## The Real Obstruction: Non-Deterministic Local Rules

The synthesis treats nabla choices as "flexibility" but they're actually **non-deterministic branching**. In proper growth diagrams, face labels are **uniquely determined** by incident vertex weights.

**Core Problem**: KTW puzzles have **choice points** where multiple local configurations are valid. Growth diagrams cannot handle **genuine non-determinism** - they need **deterministic local rules**.

This suggests the conjecture is asking the wrong question. Instead of "can we make a growth diagram," ask: "what additional structure makes nabla choices deterministic?"

## Alternative Research Program

Based on these gaps, I propose:

1. **Study cylindric puzzle variants** to eliminate boundary effects
2. **