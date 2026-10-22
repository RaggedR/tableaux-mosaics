# Synthesis Report: Why the Growth Diagram Conjecture Fails (And What This Reveals)

The four specialist reports, despite their different approaches, converge on a **fundamental incompatibility** between KTW puzzles and growth diagram structures. However, they also reveal deeper tensions about what this incompatibility actually means.

## The Core Convergence: Geometric Obstruction

All four reports identify that **triangular puzzle geometry resists rectangular growth decomposition**. But they disagree on why:

- The **geometrician** sees this as "topological violence" - forcing hexagonal local rules into rectangular lattices
- The **vertex model theorist** frames it as violation of free-fermionic constraints and Yang-Baxter integrability
- The **tableaux specialist** calls it a "red herring" - puzzles simply don't have meaningful row structure
- The **computational analyst** demonstrates it empirically - constraint propagation exceeds local bounds

This convergence suggests the obstruction is **multiply overdetermined** - the conjecture fails for several independent mathematical reasons.

## Critical Tension: What Is Migration Really Doing?

The reports fundamentally disagree about the nature of Purbhoo's migration algorithm:

**Position 1** (Geometry/Vertex): Migration preserves essential **topological/spectral invariants** that direct bijections cannot capture. The indirection is mathematically necessary.

**Position 2** (Tableaux/Computation): Migration implements **jeu de taquin in disguise** or handles **constraint satisfaction complexity**. The indirection is algorithmically convenient but potentially eliminable.

This tension is crucial. If Position 1 is correct, the growth diagram conjecture is **categorically impossible**. If Position 2 is correct, it might be possible but **computationally impractical**.

## The Missing Unification: Scale-Dependent Structure

I propose that both positions capture different aspects of a **scale-dependent phenomenon**. The key insight missing from all reports is that KTW puzzles exhibit **hierarchical constraint structure**:

- **Local scale**: Hexagonal rhombus constraints (manageable by direct methods)  
- **Intermediate scale**: Row-wise constraint propagation (what growth diagrams attempt to capture)
- **Global scale**: Boundary condition compatibility (requires topological/spectral methods)

The computational report shows constraint distance can exceed puzzle height, while the geometric report identifies global topological invariants. These observations are **compatible**: local constraint satisfaction accumulates into global topological obstructions.

## The Deeper Mathematical Question

The reports dance around but don't directly address the fundamental question: **What makes some combinatorial bijections "direct" while others require intermediate constructions?**

The tableaux specialist's jeu de taquin insight is crucial here. JdT is itself an **intermediate algorithmic construction** - we don't have "direct" bijections between skew tableaux of different shapes either. This suggests:

**Conjecture**: Bijections requiring intermediate constructions arise when the source and target combinatorial structures encode the **same mathematical object through different constraint hierarchies**.

Puzzles encode LR coefficients through **boundary constraints**, while tableaux encode them through **sequential filling constraints**. The migration algorithm translates between these constraint languages.

## Technical Gap: The Spectral Parameter Mystery

The vertex model analysis raises a crucial point that others missed: **What happens at non-free-fermionic points?** If we deform away from the integrable point, do growth diagram bijections become possible? This suggests:

**Research Direction**: Study puzzle-tableau bijections for **deformed/quantum versions** where Yang-Baxter integrability is broken. If growth diagrams work there, it proves the classical obstruction is specifically due to integrability constraints.

## Computational Resolution Strategy

Rather than the brute-force approaches suggested, I propose testing the **constraint hierarchy hypothesis**:

1. **Measure constraint locality**: For each puzzle size, compute the maximum distance over which a single nabla choice affects other choices
2. **Compare with growth bounds**: Growth diagrams require constraints to propagate at most one step per row
3. **Test the scaling**: If constraint distance grows faster than puzzle size, growth diagrams are impossible

This would definitively resolve whether the obstruction is **fundamental** (geometric/spectral) or **practical** (computational complexity).

## The Real Mathematical Lesson

The growth diagram conjecture fails, but its failure illuminates something profound about **bijective combinatorics**: Not all bijections can be realized through "natural" algorithmic constructions. Some require seemingly artificial intermediate steps that are actually **mathematically essential**.