# Fomin Growth Diagram Specialist Report: Critical Structural Deficiencies

## Major Gap: The Synthesis Misses Fundamental Graph-Theoretic Constraints

The synthesis contains a **category error** about growth diagrams that undermines its entire framework. Growth diagrams are not merely "algorithms with face labels"—they are **directed graph structures** where vertex labelings satisfy strict compatibility conditions under edge-reversal operations. The KTW puzzle domain violates these structural prerequisites in ways the synthesis completely ignores.

### Face Label Consistency Requires Planar Duality

The synthesis discusses "three-way compatibility" for triangular boundaries as if this were merely a generalization of pairwise constraints. This misses the critical point: **growth diagrams require planar dual graph structures** where each face corresponds to a unique vertex in the dual. KTW puzzles live on triangulated hexagonal regions whose planar duals have **degree-6 vertices**, not the degree-4 vertices that make Robinson-Schensted growth diagrams work.

The local rule structure isn't about "spectral parameters" or "fermionic statistics"—it's about **graph homomorphisms** between the puzzle graph and the tableau poset graph. Without degree compatibility, no such homomorphism can exist.

### The Transfer Matrix Red Herring

The synthesis conflates "transfer matrix existence" with "growth diagram existence," but these are **orthogonal concepts**. Transfer matrices are linear operators on vector spaces; growth diagrams are combinatorial bijections encoded by graph labelings. The fact that transfer matrices for KTW puzzles have been computed proves nothing about whether the underlying combinatorial objects admit growth diagram structure.

Consider the minimal example: the 4:1 ratio (12 nabla choices → 3 tableau entries) isn't "spectral gauge freedom"—it's evidence that **the puzzle graph has too many degrees of freedom** to biject directly with tableau data via local rules. Each face would need to encode multiple tableau configurations simultaneously, violating the fundamental principle that face labels should parametrize unique local updates.

## The Migration Algorithm is NOT a Growth Diagram

The synthesis accepts the representation theorist's claim that "migration already is a growth diagram," but this reveals profound confusion about what growth diagrams actually are.

### Missing Commutability Structure

Growth diagrams satisfy **strong commutability conditions**: the order of applying local rules must be irrelevant to the final outcome. Purbhoo's migration algorithm explicitly depends on the **order of hexagonal flips**—different flip sequences through the same mosaic can yield different intermediate states, even if they reach the same final tableau.

This isn't a "reordering" problem that can be solved by aligning with transfer matrix structure. It's evidence that migration fundamentally **lacks the commutative monoid structure** that makes growth diagrams work.

### Jeu de Taquin is Not a Local Rule

The synthesis treats jeu de taquin slides as potential "face label operations," but this misunderstands their mathematical nature. Jeu de taquin operations are **global rectification procedures** that can affect arbitrarily distant parts of a tableau. They cannot be decomposed into local rules that depend only on adjacent face labels.

Any growth diagram for LR tableaux would need local rules that somehow "know about" distant tableau structure. This requires **non-local face label dependencies** that violate the defining properties of growth diagrams.

## Alternative Framework: Directed Path Models

Instead of forcing KTW puzzles into growth diagram frameworks, consider **directed path models** on the puzzle graph. Each puzzle configuration corresponds to a **non-intersecting path family** from source vertices to sink vertices, with edge weights encoding local rhombus types.

### Path Weight Generating Functions

The bijection with LR tableaux emerges from **path weight generating functions** rather than face labels. Each path contributes a monomial whose exponents encode tableau entries, and the sum over all valid path configurations gives the LR coefficient.

This approach sidesteps the growth diagram structural problems because:
1. **No face labeling required**: The bijection emerges from path enumeration
2. **Natural triangular boundary handling**: Source/sink arrangements match puzzle geometry  
3. **Spectral parameters naturally included**: Edge weights can carry spectral data without affecting combinatorial structure

### Lindström-Gessel-Viennot Connection

The path model connects KTW puzzles to **Lindström-Gessel-Viennot determinantal formulas** for non-intersecting paths. This explains why transfer matrices work: they're computing determinants of path adjacency matrices, not implementing growth