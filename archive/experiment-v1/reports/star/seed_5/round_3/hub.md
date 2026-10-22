# Synthesizing the Growth Diagram Debate: Where Mathematics Meets Reality

The four specialist reports reveal a fascinating tension between mathematical sophistication and practical understanding. Each expert correctly identifies flaws in others' reasoning while committing similar errors themselves. Let me identify the core mathematical tensions and propose a resolution.

## The Central Mathematical Tension: Local Rules vs Global Constraints

All four reports wrestle with the same fundamental question: **Can globally constrained combinatorial objects (puzzles) be constructed through purely local rules (growth diagrams)?** But they approach this from incompatible perspectives:

- **Growth diagram expert**: Claims non-planarity prevents local rule formulation
- **Vertex model expert**: Insists quantum integrability conditions are necessary  
- **Jeu de taquin expert**: Argues migration IS local when viewed geometrically
- **Computational expert**: Shows constraints propagate efficiently, suggesting locality

**The synthesis reveals a category error**: Everyone assumes "locality" means the same thing across their specialisms. It doesn't.

## Three Conflicting Notions of Locality

**Combinatorial locality** (growth diagrams): Face labels determine evolution using only adjacent information. This requires **planar decomposition** of the constraint structure.

**Physical locality** (vertex models): Interactions have finite range in the lattice geometry. This allows **Yang-Baxter factorization** of transfer operators.

**Algorithmic locality** (computation): Constraint propagation has bounded dependency graphs. This enables **dynamic programming** solutions.

These are **mathematically distinct** conditions. The reports conflate them, leading to contradictory conclusions about feasibility.

## The Migration Algorithm as Mathematical Bridge

Here's what every report misses: **Migration doesn't eliminate the locality problem—it changes the question entirely.**

Purbhoo's construction works because:
1. Puzzles→Mosaics: **Pure encoding** (preserves all information)
2. Mosaics→Migration: **Rectification dynamics** (jeu de taquin slides)
3. Migration→Tableaux: **Crystallization** (reading off entries)

The jeu de taquin expert correctly identifies that migration IS local geometrically. But they miss that **geometric locality ≠ growth diagram locality**. Jeu de taquin moves are local in the mosaic plane but create non-local dependencies when projected onto any row-by-row construction order.

## The Dimensional Reduction Red Herring

Multiple reports obsess over "12 free choices → 3 tableau entries" as evidence against direct bijection. This reveals **fundamental misunderstanding of combinatorial bijections**.

**Counter-example**: Robinson-Schensted gives bijection between n! permutations and pairs of tableaux with ~n² entries. The "dimensional reduction" 2^(n log n) → n² is far more dramatic than 12→3, yet growth diagrams work perfectly.

**The real issue**: Not dimension reduction, but **constraint propagation structure**. Can puzzle constraints be resolved incrementally in a way compatible with face label updates? This is a **graph-theoretic question**, not a dimensional one.

## Quantum vs Classical: A False Dichotomy

The vertex model expert's quantum formalism is mathematically correct but **practically irrelevant** to the growth diagram question. Free-fermion conditions ensuring quantum integrability are **sufficient but not necessary** for growth diagram existence.

**Counter-evidence**: Many classical growth diagrams (plane partitions, Gelfand-Tsetlin patterns) have no natural quantum interpretation but possess well-defined face label dynamics.

**The missing link**: We need **discrete integrability** conditions, not continuous ones. This means Yang-Baxter relations for **finite state machines**, not infinite-dimensional quantum systems.

## What Computational Experiments Actually Reveal

The computational expert correctly identifies that constraint propagation is **efficient**, but misinterprets what this means for growth diagrams.

**Key insight**: Efficient constraint propagation implies the existence of **good certificates**—compact data structures that determine feasibility. But growth diagrams require more: certificates must be **composable** through local face operations.

The enumeration results showing "dependency chains where early choices constrain later ones" actually **supports** growth diagram feasibility. This is exactly the incremental constraint resolution that face labels could track.

## The Real Mathematical Challenge: Certificate Composition

Here's the precise formulation everyone misses:

**Definition**: A puzzle certificate is a data structure that determines which LR-tableau entries are compatible with a partially constructed puzzle.

**Question**: Do certificates compose locally? That is, can