# The Jeu de Taquin Specialist's Challenge: Migration as Bijective Necessity, Not Obstruction

**CORE DISAGREEMENT**: The synthesis fundamentally misunderstands what migration accomplishes. It's not "topological surgery" or "continuous deformation"—it's the **unique way** to perform jeu de taquin slides that preserves both puzzle geometry and tableau rectification simultaneously.

## Migration Is Not Continuous—It's Discretely Bijective

The synthesis claims migration performs "homology deformation between constraint spaces." This is categorically wrong. **Every step of migration is a discrete jeu de taquin slide**—an elementary bijection between skew tableaux. The "continuous parameter" interpretation completely misses that jdt slides are:

1. **Locally reversible**: Each rhombus flip in migration has a unique inverse
2. **Globally coherent**: The sequence of flips is determined by a discrete reading order
3. **Content-preserving**: Schutzenberger's evacuation theory guarantees bijective correspondence

**CHALLENGE TO SYNTHESIS**: You treat discrete bijections as requiring continuous interpolation. But jdt slides ARE the discrete interpolation. Migration doesn't "collapse topology"—it **exploits the natural jdt flow** that already exists between puzzle tilings and tableau rectifications.

## The Yang-Baxter Misdirection Reveals Deeper Structure

The synthesis claims puzzles have "horizontal Yang-Baxter" but need "vertical Yang-Baxter" for growth diagrams. This misses the crucial point: **jdt slides satisfy local Yang-Baxter relations** that are orthogonal to both puzzle integrability and growth diagram vertex rules.

**KEY INSIGHT**: Purbhoo's migration uses **Schutzenberger involution properties** that create a different combinatorial structure entirely. When a rhombus migrates through the mosaic, it's following **jdt rectification paths** that have their own Yang-Baxter coherence—one that's invisible to both puzzle piece composition and growth diagram face labeling.

**CONCRETE EXAMPLE**: In the c^(3,2,1)_{(2,1),(2,1)} = 2 case, the two puzzles have different jdt rectification sequences to reach the same LR-tableau content. A direct growth diagram would need to somehow "know" these future rectification paths at each face label step—but rectification depends on **global tableau shape**, not local puzzle geometry.

## Growth Diagrams Cannot Handle Evacuation Dynamics

Here's where all other specialists miss the fundamental obstruction: **growth diagrams build incrementally**, but jdt rectification requires **global evacuation properties** that determine local move sequences.

**SPECIFIC TECHNICAL POINT**: When Schutzenberger evacuation acts on a skew tableau, it doesn't just slide entries—it **reverses reading order** while preserving content. Purbhoo's migration exploits this to translate between puzzle reading order (rhombus position) and tableau reading order (entry position).

**GROWTH DIAGRAM IMPOSSIBILITY**: Face labels encode local information, but evacuation-based bijections require **non-local information propagation**. You cannot determine the "next" face label without knowing the final tableau shape, which hasn't been constructed yet.

## The Real Obstruction: Reading Order Incompatibility

The synthesis mentions that "tableau entries correspond to puzzle tile reading order" but doesn't grasp the implications. **This correspondence is not local**—it's mediated by jdt slides that depend on global rectification properties.

**CONCRETE CHALLENGE**: Consider puzzle tiles T₁, T₂ adjacent in puzzle reading order. Their corresponding tableau entries may be **arbitrarily far apart** in tableau reading order after rectification. Any growth diagram attempting direct bijection would need face labels that somehow "predict" this future separation.

**TECHNICAL DEPTH**: The reading order transformation is governed by **plactic monoid relations** that require full knowledge of the rectification trajectory. This is why Purbhoo's migration works—it explicitly performs the rectification, using jdt slide sequences to mediate between reading orders.

## Alternative Framing: Migration as Computational Proof

Instead of seeing migration as evidence against direct bijection, recognize it as **constructive proof** that direct bijection requires **non-local computation**.

**PROPOSITION**: Any attempted direct puzzle→tableau growth diagram must either:
1. Use face labels that encode **global rectification information** (violating locality)
2. Use face updates that violate **growth diagram incrementality** (violating the basic definition