# FOMIN GROWTH DIAGRAM ANALYSIS: Missing the Forest for the Trees

The three reports demonstrate sophisticated domain knowledge but **fundamentally misframe the growth diagram question** by conflating different algebraic structures. As a specialist in Fomin growth diagrams and local rules, I must challenge their core assumptions and redirect toward the actual mathematical content.

## Critical Misunderstanding: What Are We Actually Testing?

All three reports treat this as a question about **existence** of growth diagrams, but the real question is about **canonical form**. Growth diagrams don't require Yang-Baxter equations, spectral parameters, or even commutativity—they require **local consistency of face labels under rectangular moves**.

The computational report's "P-SPACE completeness" objection reveals deep confusion. Migration complexity is irrelevant because **growth diagrams encode bijection witnesses, not construction algorithms**. Fomin's theory handles arbitrarily complex global bijections through local face operations—this is the entire point.

## The Face Label Encoding Error

Most critically, all reports misunderstand what face labels should encode. They assume labels must contain "tableau data" or "migration choices," but this violates Fomin's framework. **Face labels encode edge weights in the growth process**, not combinatorial objects themselves.

For KTW puzzles, the correct face labels should encode:
- **Boundary data evolution**: how λ, μ, ν change as we add rows
- **Internal constraint satisfaction**: local consistency conditions for puzzle pieces
- **Bijection tracking**: correspondence with LR tableau construction steps

The "12 nabla choices → 3 tableau entries" dimensional analysis is completely wrong-headed. Face labels track **growth process states**, not final object components.

## Where Cylindric Construction Actually Applies

The computational critique about "2:1 asymmetry" actually **supports** rather than contradicts growth diagram existence. Fomin's cylindric growth diagrams specifically handle cases where different paths through the growth process have different multiplicities. The asymmetric nabla distribution is exactly what we'd expect if face labels properly encode the branching structure.

**Key insight**: The asymmetry indicates that puzzle construction exhibits **path-dependent multiplicities**, which is precisely when cylindric growth diagrams become necessary rather than impossible.

## Local Rules vs. Global Migration: False Dichotomy

The migration specialist correctly identifies that migration IS a sequence of local jdt slides, but then incorrectly concludes this supports growth diagram existence. This conflates **algorithmic locality** with **face rule locality**.

Migration performs **globally determined** local moves—each jdt slide depends on the entire current configuration. Growth diagram face rules perform **locally determined** operations that happen to produce globally consistent results. These are opposite architectural principles.

**The real question**: Can we replace globally-determined migration with locally-determined face rules that produce the same bijection? This is highly non-trivial and cannot be assumed.

## Testing Framework Completely Wrong

The computational verification strategy misses the correct test entirely. We don't enumerate puzzles and extract face rules—we start with **hypothetical face rules** and test whether they:

1. **Satisfy rectangular consistency**: Face operations commute under rectangular moves
2. **Preserve boundary evolution**: Row additions produce correct λ → λ' transitions  
3. **Generate correct multiplicities**: Final weights match LR coefficients

The reports' approaches test bijection correctness, not growth diagram structure. These are orthogonal questions.

## Alternative Conjecture: Growth Diagrams Don't Exist, But...

Based on proper understanding of Fomin's framework, here's my assessment: **Direct growth diagrams for KTW puzzles likely don't exist** because puzzle constraint propagation is inherently non-local. However, there may exist **modified growth diagrams** with auxiliary vertex decorations that capture the necessary global information.

**Specific proposal**: Augmented growth diagrams where vertices carry "constraint state" labels that encode global puzzle validity. Face rules then operate on (edge weight, constraint state) pairs rather than pure edge weights.

## The Schutzenberger Connection Is a Red Herring

The migration report emphasizes Schutzenberger involution, but this is irrelevant to growth diagram structure. Schutzenberger acts on **final tableaux**, not construction processes. Growth diagrams encode forward construction, not involution symmetries.

This confusion stems from conflating **bijection properties** with **construction properties**. The bijection may respect Schutzenberger involution while the construction process violates local consistency.

## What Would Actual Proof Look Like?

A genuine resolution requires:

1. **