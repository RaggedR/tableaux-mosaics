# Specialist Analysis: The Growth Diagram Fallacy and Categorical Errors

## The Migration Algorithm IS NOT a Growth Diagram

The synthesis contains a **fundamental error** that undermines its entire argument. The claim that "Purbhoo's migration algorithm IS a growth diagram—just not in the plane" reveals a complete misunderstanding of what growth diagrams are.

**Growth diagrams are characterized by**:
1. **Local face label update rules** that depend only on neighboring edge labels
2. **Deterministic propagation** from boundary data
3. **Rectangle insertion/recording factorization** where face labels encode bijection data directly

**Migration algorithms are characterized by**:
1. **Global hexagonal flips** that preserve monochromatic vertex constraints
2. **Non-deterministic path choices** requiring backtracking when obstructions arise  
3. **Homology class preservation** in the mosaic torus, not local face updates

The synthesis conflates these by invoking a mysterious "dual complex" without any mathematical definition. This is **category error**, not insight.

## The Fomin Construction Cannot Apply Here

Fomin growth diagrams work because **RSK insertion has bounded local support**: inserting element k affects only positions ≤k in the tableau. This creates the crucial **locality property** where face labels depend only on immediate neighbors.

**KTW puzzle resolution fundamentally lacks this property**. When a nabla vertex resolves to create three outgoing rhombi, this choice affects the **global connectivity** of the puzzle solution. The "stratified locality" proposal in the synthesis would require face labels to encode exponentially complex non-local data, destroying the growth diagram structure entirely.

## The Spectral Parameter Issue is Deeper Than Claimed

The synthesis dismisses Yang-Baxter integrability as "importing massive machinery," but this misses the crucial point: **degree-6 vertices cannot satisfy the Yang-Baxter equation with rational R-matrices**. The A₂ affine systems don't "explain" the 4:1 ratios—they **preclude** them for topological reasons.

If puzzle transfer matrices were Yang-Baxter integrable, the **braid relations** would force specific spectral parameter relationships that contradict the observed arithmetic patterns. The computational evidence of non-integrability isn't a side effect—it's **mathematically necessary**.

## The Recording Data Problem

Here's the issue no one addresses directly: **what exactly would the face labels record?** In RSK growth diagrams, face labels encode the recording tableau entries because insertion has clear **left-right asymmetry**. 

KTW puzzles have **three-fold rotational symmetry**. There's no canonical way to distinguish which boundary data should be "recorded" versus "inserted." The synthesis's appeal to "dual complexes" and "branching multiplicities" doesn't resolve this—it just pushes the problem to an undefined mathematical object.

## Schutzenberger Equivariance Kills the Construction

The synthesis correctly identifies this constraint but underestimates its power. Schutzenberger involution acts on LR tableaux by **transpose + evacuation**. For a growth diagram to be Schutzenberger-equivariant, the face labels must transform **locally** under a rule that implements this **global** operation.

This is impossible. Evacuation requires **complete tableau structure**, not local face information. Any growth diagram that attempts to encode Schutzenberger-equivariant data will necessarily have face labels depending on **arbitrarily distant** boundary conditions, violating locality.

## The Real Mathematical Structure

The computational evidence points toward the correct framework: **KTW puzzles naturally form a directed graph** where vertices are puzzle configurations and edges are nabla resolutions. The "transfer matrix" is simply the **adjacency structure** of this graph, not a growth diagram generator.

The bijection to LR tableaux operates by **graph homomorphism** to the tableau poset, not through local face label rules. This explains both the computational complexity patterns and the topological migration obstructions—we're trying to embed a high-genus graph structure into the plane.

## Conclusion: Category Theory Redux

The synthesis claims to identify "category errors" while committing the largest one: **assuming different mathematical constructions should be equivalent simply because they involve similar combinatorial objects**. Growth diagrams, puzzle bijections, and migration algorithms operate in **genuinely different categories** that don't naturally compose.

The growth diagram conjecture isn't "difficult"—it's **categorically ill-posed**. The question should be: what is the **correct