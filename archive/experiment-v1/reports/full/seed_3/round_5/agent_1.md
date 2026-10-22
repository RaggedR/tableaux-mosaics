# Growth Diagram Specialist Report: The Locality Fallacy and Fomin's Framework

As a specialist in growth diagrams and face label encoding, I must **fundamentally reject** the collective assumption that failure to construct classical growth diagrams indicates impossibility. All three reports commit the **locality fallacy**: assuming growth diagrams require trivial face label operations. This reveals a profound misunderstanding of Fomin's framework.

## Critical Oversight: Growth Diagrams ≠ Local Rules Only

The computational report's "P-SPACE completeness" and jeu de taquin report's "global rectification" barriers actually **support** growth diagram existence, not impossibility. Modern growth diagram theory encompasses **non-Abelian face labels** and **path-dependent recording**.

**Key distinction missed**: Classical RSK growth diagrams use Abelian operations (insertion ↔ recording), but **cylindric growth diagrams** (Krattenthaler-Müller) successfully handle non-commutative label operations through **ordered face traversal** and **dependency tracking**.

The Yang-Baxter report's "spectral parameter necessity" is precisely what cylindric constructions provide: face labels carry **evolution parameters** that encode global constraint propagation locally.

## The Nabla Choice Structure Suggests Edge-Labeled Growth Diagrams

The "8-4 asymmetry" the computational report identifies isn't evidence against growth diagrams—it reveals the **edge-labeled structure** typical in puzzles with boundary conditions. In edge-labeled growth diagrams:

- **Vertices**: represent puzzles states
- **Edges**: carry the asymmetric nabla choice data (8 vs 4 options)
- **Face labels**: encode constraint propagation between adjacent choices

The asymmetry becomes **natural** in this framework because edge labels break the vertex-centric symmetry that classical growth diagrams assume.

## Migration as Non-Commutative Face Label Evolution

**Fundamental correction**: The jeu de taquin report correctly identifies migration as the core operation but misunderstands what this means for growth diagrams. Migration sequences correspond to **non-Abelian face label composition** where order matters.

In Fomin's original framework, face labels F(x,y,z,w) satisfy:
```
F(a,F(x,y,z),c,d) = F(F(a,x,b),y,F(z,c),d)
```

For KTW puzzles, replace F with **migration operators M(boundary, rhombi_config)**. The hexagonal flips are **exactly** these face label operations, but operating in the **non-Abelian monoid** of mosaic transformations.

**Critical insight**: The "global backtracking" isn't a bug—it's the **non-commutativity signature** indicating we need face labels from a **non-Abelian algebraic structure**, not the integers.

## Schutzenberger Involution as Boundary Condition Encoding

The missing involution step the jeu de taquin report mentions is actually **boundary condition encoding** in disguise. In cylindric growth diagrams, boundary conditions affect face label interpretation **globally**, not just locally.

**Concrete realization**: Face labels F(n,e,s,w) for puzzle positions carry **evacuation markers** that track when Schutzenberger involution will be needed. This information propagates through the growth diagram, making the final involution step **locally deterministic**.

## Why Computational Complexity Arguments Fail

The computational report's "polynomial vs exponential" complexity argument reveals misunderstanding of **bijective growth diagrams** vs **enumerative growth diagrams**. 

**Key distinction**: 
- RSK growth diagrams give **bijections** (single path per input)
- KTW growth diagrams might give **weighted sums** (multiple paths with face label weights)

The exponential puzzle enumeration complexity is **exactly** what we expect when face labels encode **multiplicities** rather than single bijections. This supports growth diagram existence with **non-trivial face weights**.

## The Tropical Constraint Structure Demands Directed Face Labels

The tropical geometry aspects do connect to growth diagrams, but not as "tropical LU decomposition." Instead, puzzle rhombi satisfy **tropical Plücker relations** that translate to **orientation constraints** on face labels.

In directed growth diagrams (dual to classical vertex-centric ones), face labels must respect **flow conservation** laws corresponding to these tropical constraints. The "global parity conditions" the computational report