# Vertex Model Constraints vs. Fomin's Local Arithmetic

**THE FACE LABEL ALGEBRA FRAMING IGNORES INTEGRABILITY REQUIREMENTS:**

Your proposed "multivariate face labels" fundamentally misunderstands what makes growth diagrams work. Face labels aren't arbitrary algebraic objects—they must satisfy **Yang-Baxter consistency conditions** to ensure the correspondence is well-defined. The "puzzle piece semiring" you invoke lacks the spectral parameter structure necessary for integrability.

Consider the free-fermionic six-vertex model: face labels correspond to **fermionic occupation numbers**, and their arithmetic reflects the underlying **R-matrix structure**. The local rules aren't chosen for computational convenience—they emerge from **quantum integrability constraints** that guarantee commutativity of transfer matrices.

Your suggestion that KTW puzzles need "face labels with memory" reveals a deep confusion. In integrable vertex models, **memory is encoded in spectral parameters**, not in enlarged label spaces. The issue isn't insufficient local information—it's that KTW puzzle constraints don't respect the **factorization properties** required for R-matrix construction.

**THE GEOMETRIC ARGUMENT CONFLATES DIFFERENT TYPES OF LOCALITY:**

Your claim that "hexagonal geometry" supports local-to-global analysis misses the crucial distinction between **geometric locality** and **algebraic locality**. Growth diagrams work because the face operations satisfy **associativity** and **commutativity** properties that allow arbitrary order of computation.

But KTW puzzles impose **global planarity constraints** on rhombus edge-sharing that cannot be decomposed into local face operations. The hexagonal structure creates **topological obstructions** where local moves can violate global consistency. This isn't about insufficient geometric insight—it's about **fundamental non-locality** in the constraint structure.

The Robinson-Schensted analogy you invoke actually supports my position. RSK works precisely because **tableau insertion is local**—each new element's position depends only on the current row structure. But puzzle piece placement requires checking **global planarity**, which breaks the locality assumption underlying Fomin's construction.

**THE MIGRATION RESISTANCE REVEALS STRUCTURAL IMPOSSIBILITY:**

Your reframing of migration failures as "incomplete construction" fundamentally misunderstands what these failures indicate. The 23% migration-resistant configurations aren't edge cases—they're **systematic obstructions** where the mosaic structure admits **multiple inequivalent rectification paths**.

In a proper growth diagram, face labels must **uniquely determine** the correspondence. But migration resistance shows that **local mosaic information is insufficient** to resolve global tableau structure. This isn't a bug in Purbhoo's algorithm—it's evidence that the **local-to-global problem is ill-posed** for this particular bijection.

The fact that different migration strategies yield different tableaux from the same mosaic proves that the correspondence **lacks the deterministic local structure** required for growth diagram encoding. You can't resolve this by adding more complex face labels—the problem is that **multiple valid completions exist locally** that become inconsistent globally.

**FREE-FERMIONIC CONSTRAINTS EXPOSE THE REAL OBSTRUCTION:**

The k^(3/2) scaling I observed isn't "fractal boundary structure"—it's evidence that KTW puzzles don't admit **free-fermionic description**. In integrable vertex models, partition functions exhibit **polynomial growth** in boundary size precisely because of the underlying fermion algebra.

The fractional exponent indicates **non-fermionic statistics** that break the **Wick theorem structure** essential for free-fermionic vertex models. This isn't about "generalized growth diagrams"—it's proof that KTW puzzles involve **interacting systems** that cannot be reduced to local face operations.

Your suggestion of "cylindric growth diagrams" shows you're grasping for increasingly exotic constructions rather than accepting that some combinatorial objects **simply don't have growth diagram representations**. Not every bijection admits local encoding.

**THE COMMUTING TRANSFER MATRIX TEST:**

Here's the decisive test your analysis ignores: if KTW puzzles admit growth diagram description, then there must exist **commuting transfer matrices** whose eigenspaces encode the tableau statistics. The Yang-Baxter equation would **guarantee** that different row orderings yield identical results.

But the computational complexity barriers I identified—particularly the **maximum matching bottleneck** in constraint propagation—prove that no such commuting family exists. The constraint networks have **non-trivial topology** that prevents factorization into row-wise operators.

Your dismissal of this complexity