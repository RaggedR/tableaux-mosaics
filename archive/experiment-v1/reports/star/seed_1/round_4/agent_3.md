# Specialist Report: Migration Theory and the Fundamental Misdiagnosis

As a specialist in Purbhoo's bijection, migration algorithms, and jeu de taquin, I must **fundamentally challenge** this synthesis. The generalist has committed a category error that undermines their entire analysis.

## The Core Misdiagnosis: Migration ≠ Jeu de Taquin Implementation

The synthesis claims that "the growth diagram question reduces to: Can jeu de taquin slides be implemented as local growth rules?" This is **mathematically incorrect**. 

**Critical distinction**: In Purbhoo's bijection, migration is **not** a sequence of jeu de taquin slides on tableaux. Migration operates on **mosaic rhombi** through hexagonal flips, creating a correspondence that **projects** to jeu de taquin behavior on the resulting LR-tableaux. The synthesis conflates the **geometric operation** (hexagonal flips) with its **combinatorial shadow** (jdt slides).

This misunderstanding invalidates the proposed "Hexagonal Yang-Baxter Conjecture." Yang-Baxter relations govern **how operations compose**, not whether geometric flips project correctly to tableau operations.

## The Locality Claim Reverses the Actual Mathematical Structure

The generalist asserts that puzzles have "long-range correlations that resist local rule decomposition." This is backwards. **Puzzles are built from local constraints** - each hexagonal tile type enforces local boundary matching rules. The apparent "non-locality" emerges from **global consistency requirements**, not intrinsic long-range interactions.

**Concrete example**: In a c^{(3,2,1)}_{(2,1),(2,1)} puzzle, the 12 free nabla choices appear non-local only because we're viewing them through the **wrong coordinate system**. In mosaic coordinates, each rhombus flip is purely local - it only affects its immediate hexagonal neighborhood.

The growth diagram specialist's impossibility claim assumes puzzles must be encoded in **row-reading order**. But migration naturally suggests **rhombus-deletion order**, which could preserve locality.

## The Spectral Parameter Red Herring Conceals the Real Issue

The synthesis obsesses over spectral parameters, but in migration theory these are **artifacts of algorithmic implementation**, not mathematical content. The vertex model specialist's emphasis on spectral deformation misses that in Purbhoo's construction, the bijection is **combinatorially canonical** - there are no continuous parameters to vary.

**The real parameter space**: Migration paths can branch at certain rhombus configurations. These discrete choices (not continuous deformations) determine which of the multiple valid LR-tableaux gets selected. This is purely combinatorial and has nothing to do with Yang-Baxter integrability.

## The Experimental Framework Targets the Wrong Mathematical Objects

The proposed "Local Evacuation Conjecture" tests whether tableau evacuation can be implemented via face operations. But **evacuation is not the relevant operation** for the puzzle-tableau bijection! 

**What should be tested**: Whether the **inverse migration** algorithm (LR-tableau → puzzle) can be implemented as local growth rules. This is the direction that would prove/disprove the growth diagram possibility, since we need to construct puzzles row-by-row from tableau data.

**Concrete algorithmic challenge**: Given an LR-tableau of shape λ/μ, can we determine the puzzle's row i+1 from knowledge of only rows 1,...,i? The migration bijection suggests this might be possible through **rhombus insertion rules**, but proving locality requires understanding how tableau entries project to hexagonal constraints.

## The Category Theory Dismissal Misses Deep Structural Insights

The synthesis dismisses categorical frameworks as "hand-waving," but there's a profound connection the generalist missed. **The migration algorithm naturally lives in the derived category of perverse sheaves** on the Grassmannian, where puzzles correspond to intersection cohomology complexes.

This isn't abstract nonsense - it explains why migration preserves the **correct algebraic structures**. The hexagonal flips correspond to **derived equivalences** that preserve intersection multiplicities. Understanding this categorical structure is essential for determining whether growth diagram implementations exist.

## Three Alternative Testable Propositions

The synthesis's three conjectures test the wrong properties. Here are the actual mathematical questions:

1. **Rhombus Insertion Locality**: Given an LR-tableau, can we determine its puzzle's next row using only bounded local information? This is decidable via explicit algorithm analysis.