# Vertex Model Analysis: The Yang-Baxter Structure Demands Reconstruction

## Fundamental Spectral Parameter Problem

The synthesis correctly identifies a **spectral parameter archaeology** phase, but fundamentally misunderstands what this means. The 4:1 redundancy ratio (12 nabla choices → 3 tableau entries) isn't "gauge degrees of freedom"—it's evidence of **spectral parameter degeneracy** that breaks integrability.

In free-fermionic vertex models, the Yang-Baxter equation requires:
```
R₁₂(u-v)R₁₃(u-w)R₂₃(v-w) = R₂₃(v-w)R₁₃(u-w)R₁₂(u-v)
```

KTW puzzles correspond to the **homogeneous limit** where all spectral parameters coincide (u=v=w=0). At this degenerate point, the R-matrix loses invertibility, and commuting transfer matrices collapse to a single eigenvalue sector. The "working" transfer matrix implementation is therefore **not integrable** in the technical sense—it's computing projections onto specific eigenspaces.

## The Triangular Geometry Contradiction

The synthesis proposes "triangular growth diagrams" as a solution, but this reveals a deeper misunderstanding of why vertex models work. The **triangular boundary conditions** of KTW puzzles are topologically incompatible with the Yang-Baxter braid relations, which require **cylindrical topology** (periodic boundary conditions) or careful **boundary Yang-Baxter** constructions.

Free-fermionic models work on triangular domains only when the vertex weights satisfy **domain wall boundary conditions** with specific asymptotic behavior. The KTW vertex weights (0,1,∞) don't satisfy these conditions—they're designed for **finite counting**, not spectral theory.

## Migration Algorithm: Already Broken Integrability

The claim that "migration already is a growth diagram" misses the crucial point: **migration breaks the fermionic statistics**. Purbhoo's local hexagonal flips preserve combinatorial structure but violate the **fermionic exchange relations** that make transfer matrices commute.

In a true integrable formulation, migration moves would correspond to **Bäcklund transformations** that preserve the spectral curve. But KTW puzzles don't have spectral curves—they're discrete objects without the analytic continuation necessary for classical integrability.

## The Real Mathematical Obstruction

The synthesis frames this as reconciling three frameworks, but the actual obstruction is more fundamental: **KTW puzzles exist in a finite combinatorial category that cannot support the analytic structures required for vertex model integrability**.

The correct question is not "Can we build a growth diagram?" but rather "Can we **lift** KTW puzzles to an infinite-dimensional integrable system whose finite truncations reproduce the combinatorics?"

This requires:
1. **Spectral parameter restoration**: Embed puzzles in a family parametrized by spectral variables
2. **Boundary condition deformation**: Modify the triangular boundary to support Yang-Baxter structures  
3. **Thermodynamic limit definition**: Define what happens as puzzle size approaches infinity

## Counter-Proposal: The Affine Extension

Instead of forcing KTW puzzles into growth diagram framework, consider the **dual approach**: 

Construct an **affine KTW system** where:
- Puzzles live on infinite triangular lattices with spectral parameters
- Finite KTW puzzles emerge as **critical point residues** 
- Migration becomes **soliton propagation** in the infinite system
- LR tableaux are **asymptotic data** encoding scattering behavior

The "growth diagram" would then be the **finite truncation** of infinite Yang-Baxter evolutions, with face labels encoding soliton interaction data rather than tableau entries directly.

## Technical Challenge to the Synthesis

The synthesis claims transfer matrices "already exist computationally" and dismisses this as "numerical implementation." This is backwards—the computational existence proves that some integrable structure exists, but we're **misidentifying what it is**.

The real challenge: **Reverse-engineer the spectral parameters and boundary conditions that make the existing transfer matrix construction mathematically rigorous**.

The minimal example c^(3,2,1)_{(2,1),(2,1)} = 2 should be studied not as "two puzzles with migration paths" but as **boundary correlation functions