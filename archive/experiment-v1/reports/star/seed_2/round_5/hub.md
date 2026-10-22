# SYNTHESIS: Exposing the False Dichotomies and Hidden Assumptions

## CHALLENGING THE PREMISE: Growth Diagrams Are Not Universal Bijection Factories

The core question assumes growth diagrams provide a "natural" framework for direct puzzle↔tableau bijection, but this assumption is mathematically naive. Growth diagrams work for RSK because **insertion and recording tableaux have identical geometric constraints**—both grow by adding boxes to Young diagrams under identical rules.

KTW puzzles and LR-tableaux have fundamentally **incompatible constraint geometries**: puzzles satisfy hexagonal rhombus-tiling conditions while tableaux satisfy rectangular word-reading conditions. The specialists' debates over Yang-Baxter relations, spectral parameters, and face-labeling schemes all miss this basic geometric incompatibility.

**CRITICAL INSIGHT**: The question reverses cause and effect. Growth diagrams don't create bijections—they **encode existing bijections with compatible geometric structure**. Asking why no direct growth diagram exists is like asking why there's no direct coordinate transformation between spherical and hyperbolic geometries.

## THE MIGRATION "INDIRECTNESS" IS MATHEMATICALLY NECESSARY

Multiple specialists defend migration's constructivity, but they miss the deeper point: migration's apparent "indirectness" reflects **fundamental geometric necessity**. The puzzle→mosaic→LR-tableau path isn't computational inefficiency—it's the unique geometric transformation that preserves combinatorial structure while changing constraint topology.

The computational specialist's observation that migration has "exponential branching complexity" reveals the true issue: **migration implements geometric rectification**, not simple bijection. Each branch represents a different geometric path through the constraint space. The 4:1 compression ratios emerge because multiple geometric paths project to identical combinatorial outcomes.

**ALTERNATIVE FRAMING**: Instead of seeking direct bijection, we should ask: what geometric transformations preserve Littlewood-Richardson multiplicities while changing constraint topology? Migration answers this question—growth diagrams cannot.

## THE SPECIALISTS' FUNDAMENTAL DISAGREEMENT: Local vs. Global Structure

The reports reveal a deeper tension between **local rule systems** (growth diagrams, vertex models) and **global geometric constraints** (puzzle rhombus tilings, tableau rectification). Each specialist advocates their preferred mathematical framework without addressing this fundamental mismatch.

The growth diagram specialist claims "global structure emerges from purely local operations," but this only works when local rules are **geometrically compatible** with global constraints. KTW puzzles have global constraints (valid rhombus tilings) that cannot be decomposed into local rules preserving tableau-reading structure.

The vertex model specialist recognizes this with "spectral parameter constraints," but misses that these parameters encode precisely the **geometric incompatibility** between puzzle and tableau constraints.

## COMPUTATIONAL REALITY EXPOSES THEORETICAL BLIND SPOTS

The computational specialist provides crucial perspective: theoretical sophistication becomes irrelevant if it cannot predict computational behavior. The 12→3 compression ratio appears "systematic" across examples, suggesting underlying structure, but **none of the specialists can predict these ratios from first principles**.

This computational pattern-recognition succeeds where theoretical frameworks fail. The compression ratios encode genuine mathematical structure that current theoretical approaches cannot capture. This suggests our theoretical frameworks are **fundamentally incomplete**.

**SYNTHESIS INSIGHT**: The growth diagram conjecture fails not because puzzles lack structure, but because our theoretical frameworks cannot handle **multi-scale geometric constraints**. Growth diagrams work for single-scale problems (tableaux-to-tableaux). Puzzles require multi-scale analysis.

## THE BIJECTION EXISTENCE MYSTERY: A False Problem

Several specialists ask "why does any bijection exist at all?" This question reveals conceptual confusion. The bijection exists because **both objects count identical algebraic invariants**—Littlewood-Richardson coefficients in cohomology of Grassmannians.

The mystery isn't bijection existence but bijection **computational complexity**. Both puzzles and tableaux provide combinatorial algorithms for computing the same algebraic numbers. The question is whether one algorithm can be efficiently transformed into the other.

Migration provides such transformation, but with exponential complexity. The growth diagram conjecture asks whether polynomial-time transformation exists. The answer is likely **no**, for fundamental geometric reasons.

## IDENTIFYING THE CORE MATHEMATICAL TENSION

The specialists' disagreements cluster around a central tension: **deterministic vs. probabilistic structure**. Growth diagrams require deterministic local rules. Vertex models allow probabilistic weights. Migration implements deterministic geometry but with exponential branching.

This tension suggests the growth diagram conjecture asks an **ill-posed question**. Instead of seeking deterministic transfer matrices, we