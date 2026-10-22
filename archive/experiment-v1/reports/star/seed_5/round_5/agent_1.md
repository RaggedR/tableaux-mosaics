# SPECIALIST ANALYSIS: Categorical Confusion and Geometric Misframing

The generalist's synthesis contains several **fundamental errors** about growth diagrams that demand correction. While attempting sophisticated categorical language, they miss basic structural facts about local rules and face label semantics.

## The "Wrong Geometric Framework" Fallacy

The generalist claims we need to "change the tiling geometry" rather than fix labeling schemes. This reveals **deep misunderstanding** of growth diagram universality. Fomin growth diagrams work precisely because face labels encode **transition data**, not geometric structure. The rhombic tiling in KTW puzzles is not arbitrary—it reflects the combinatorial structure of Grassmannian Schubert calculus.

**Counter-example**: Consider the standard RSK growth diagram. The face labels (Schur functions) work in ANY regular tiling that preserves the partial order structure. The geometric realization is secondary to the **order-theoretic skeleton**. Changing tiling geometry without understanding the underlying poset structure is mathematically meaningless.

**The real issue**: Nabla vertices in puzzles create **branching in the underlying directed graph**, not "non-deterministic local rules." This is a categorical difference—RSK works on trees, puzzles work on DAGs. Face labels that encode single tableau entries cannot handle the **exponential blow-up** inherent in DAG structure.

## Yang-Baxter Analysis Reveals the Core Problem

The generalist dismisses the Yang-Baxter discussion as "red herring," but this is precisely where the mathematical obstruction lives. Let me be explicit:

**RSK growth diagrams satisfy integrability** because the local rules preserve a conserved quantity (the shape evolution). Each face encodes a **unique transition** between compatible shapes. The Yang-Baxter equation ensures these transitions compose consistently.

**KTW puzzles break integrability** because nabla vertices create **non-unique transitions** between identical boundary configurations. Two puzzles with identical λ,μ,ν can have completely different internal structure. No face labeling scheme can distinguish these while remaining local, because the distinction requires **global path information**.

**Mathematical precision**: The generalist's "spectrum of Yang-Baxter structures" is meaningless. Yang-Baxter equations are **uniquely determined** by the vertex weights in integrable models. If KTW had Yang-Baxter structure supporting growth diagrams, it would already be known—these equations are **computationally checkable**.

## Migration Encodes Non-Local Information

The generalist's claim that "migration might be proof of concept for direct growth diagrams" inverts the mathematical reality. Migration works precisely because it **abandons locality**. The hexagonal flips depend on **global mosaic structure**—you cannot determine flip validity from local neighborhoods alone.

**Concrete obstruction**: In Purbhoo's construction, the migration path for a colored rhombus depends on the **entire evacuation order** of other rhombi. This is inherently non-local. Face labels in growth diagrams must be **locally computable** from boundary data.

**Challenge to the generalist**: Show me **one example** where migration decisions can be made from purely local information. The mathematical literature contains detailed proofs that this is impossible for non-trivial cases.

## The Categorical Framework is Already Known

The generalist seeks "categorical equivalence" between puzzles and tableaux, but this **already exists**—it's called the **derived category of coherent sheaves** on flag varieties. The connection goes:

- Puzzles ↔ Intersection multiplicities in Schubert calculus  
- Tableaux ↔ Standard monomials in coordinate rings
- Migration ↔ Derived equivalences via tilting bundles

The categorical framework is **well-established**. The missing piece isn't categorical understanding—it's whether this categorical equivalence admits **local computational realization**.

## Dual Tilings Cannot Resolve the Fundamental Issue

The generalist's "concrete proposal" about dual tilings misses the point entirely. The obstruction to direct bijection isn't geometric—it's **information-theoretic**. 

**Precise statement**: Let G be the growth diagram graph for KTW puzzles. Each face must encode enough information to distinguish between **all valid puzzle completions** consistent with the local boundary data. For non-trivial cases, this requires **exponential information**, contradicting the polynomial face label constraint in growth diagrams.

**Mathematical fact**: Dual tilings preserve the **same combinatorial complexity**. No geometric reframing can compress exponential information into polynomial labels while