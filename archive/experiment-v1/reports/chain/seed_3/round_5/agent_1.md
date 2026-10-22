# Growth Diagram Spectral Analysis: Why Transfer Operators Miss the Geometric Heart

## The Computational Hubris Problem

The computational researcher's demand for "explicit enumeration" reveals a **fundamental misunderstanding** of what makes growth diagrams work. Growth diagrams aren't just about counting—they encode **geometric correspondences** through local face labels that satisfy **edge consistency conditions**. The researcher's `lr_coefficients.py` can enumerate puzzles, but enumeration ≠ growth diagram construction.

**Critical Gap**: Fomin growth diagrams require **local rules** where each face label depends only on its three neighbors. The researcher's transfer operator approach T = T_k ∘ ... ∘ T_1 is inherently **global**—operator composition cannot generate local face labels unless the operators themselves factorize locally. This is exactly what **fails** for KTW puzzles.

**Missing Geometric Insight**: The researcher treats "constraint satisfaction graphs" as abstract combinatorial objects, but KTW constraints arise from **hexagonal tiling geometry**. When a nabla choice at position (i,j) constrains choices at positions (i±1, j±1), you get **crossing dependencies** that cannot be resolved by planar growth diagram rules. This isn't "assertion without verification"—it's **geometric necessity**.

## Transfer Operators vs. Local Growth: A Category Error

The researcher's spectral approach fundamentally mischaracterizes the problem. Growth diagrams work because they implement **local bijections** through face label arithmetic. The face labels aren't "matrix elements" of some global operator—they're **local data** that determines how paths through the diagram correspond to tableaux.

**Why Eigenspaces Don't Help**: Even if the transfer matrix T has nice eigenspaces, the eigenvectors are **global objects**. Growth diagrams need local face labels f(a,b,c,d) where knowing three neighboring labels determines the fourth. The researcher's Jordan decomposition approach cannot produce these local rules because **global spectral structure doesn't constrain local geometry**.

**Fomin's Construction Requirements**: In RSK-type growth diagrams, we need:
1. Local face labels that depend only on edge data
2. Unique path correspondence between input/output
3. Deterministic local rules for face computation

KTW puzzles violate (3) because nabla choices create **branching** that cannot be resolved locally.

## The Mosaic Migration Decomposition Delusion

The researcher's claim that "cluster moves might be decomposable into sequences of local moves" shows deep confusion about **what migration actually does**. Purbhoo's migration moves entire rhombus clusters because the **combinatorial structure requires it**. This isn't a limitation of current algorithms—it's the **mathematical reality** of the bijection.

**Why Local Decomposition Fails**: Migration preserves the **global mosaic connectivity**. When you move a rhombus cluster, you must simultaneously update:
- All adjacent rhombi orientations
- The background triangular regions
- The boundary edge labelings

These updates are **geometrically coordinated**—decomposing them into "local moves" would break the mosaic structure. The researcher's computational experiment proposal misses this entirely.

**Category Theory Perspective**: Migration operates in the category of **decorated triangulations**, where morphisms preserve triangulation structure. Local moves would correspond to generating morphisms, but migration morphisms don't factor through local generators because they involve **non-contractible topology changes**.

## The Multiplicity Structure Reveals Non-Locality

The researcher correctly identifies the core counting: 12 nabla choices → 3 tableau entries, but their factorization hypothesis (12 = 2×6) is **geometrically impossible**. Here's why:

**KTW Constraint Analysis**: The 4 vs 8 nabla multiplicity arises from different **hexagonal neighborhoods** in the two puzzles. In Puzzle 1, certain nabla positions have forced values due to boundary constraints. In Puzzle 2, the same positions are free because of different puzzle boundary data. This creates **position-dependent degrees of freedom** that cannot factor cleanly.

**Growth Diagram Requirements**: For growth diagrams to work, the degrees of freedom must be **locally separable**. Each row's choices should depend only on adjacent row data. But KTW nabla constraints can span **multiple rows simultaneously** when hexagonal regions cross row boundaries.

## The Cylindric Construction Alternative

Rather than forcing KTW into classical growth diagrams, consider **cylindric growth diagrams** (Fomin-Stanton