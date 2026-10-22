# Challenging the Non-Locality Assumption: A Vertex Model Analysis

**THE YANG-BAXTER PERSPECTIVE REVEALS HIDDEN STRUCTURE**

Your assertion that puzzle-to-tableau correspondence requires "global coordination" fundamentally misunderstands the nature of integrable systems. The Yang-Baxter equation precisely governs how **local interactions propagate to create global consistency**. The fact that Purbhoo's migration uses "global hexagonal flips" doesn't prove non-locality—it may simply reflect an inefficient algorithmic choice.

Consider the free-fermionic vertex models underlying Schur function identities. These exhibit **perfect locality**: each vertex weight depends only on adjacent edge configurations, yet the partition function encodes global topological data. The key insight from Zinn-Justin's work is that **spectral parameters** provide the mechanism for local rules to track global information.

Your dismissal of this approach ignores that KTW puzzles are themselves a **restriction of the six-vertex model**. The rhombus tilings correspond to specific vertex configurations, and the boundary conditions encode the partition data. If the underlying six-vertex structure is integrable, then local growth diagram rules should exist—we simply haven't found the right parameterization.

**THE TRANSFER MATRIX COMMUTATIVITY IS THE KEY TEST**

You correctly identify commutativity as crucial, but then dismiss it without proper investigation. Here's the specific technical challenge your analysis avoids: **do puzzle row operators satisfy [T_i(u), T_j(v)] = 0 for spectral parameters u,v?**

In integrable systems, this commutativity isn't just a mathematical nicety—it's the **fundamental reason why growth diagrams work**. Commuting transfer matrices guarantee that different row orderings produce the same partition function, which translates directly to growth diagram consistency conditions.

The failure to find direct puzzle→tableau bijections may reflect our **failure to identify the correct spectral parameter space**, not the absence of commutativity itself. Your computational approach should test whether puzzle constraints can be embedded in a larger parameter family where commutativity emerges.

**THE BOUNDARY ENCODING IS OVER-CONSTRAINED**

Your "boundary data encoding problem" actually reveals why existing approaches fail. You assume face labels must **simultaneously encode multiple pieces of information**, but this over-constrains the system. In successful vertex model constructions, the **spectral parameter carries the global information** while face labels handle only local constraints.

For KTW puzzles, this suggests seeking a parameterization where:
- Face labels encode only rhombus placement (local)
- Spectral parameters track partition evolution (global)  
- Transfer matrix commutativity ensures consistency

Your computational framework tests neither spectral parameters nor their associated commutation relations. Without this, you're essentially trying to solve an integrable system while ignoring its most fundamental property.

**THE MIGRATION ALGORITHM REVEALS FREE-FERMIONIC STRUCTURE**

Purbhoo's hexagonal flips aren't evidence of non-locality—they're evidence of **fermion braiding relations**. Each flip corresponds to moving a fermion past another, and the migration paths trace fermion worldlines through the lattice.

This is precisely the structure underlying free-fermionic vertex models. The colored rhombi represent fermion occupation states, and migration corresponds to **fermion evolution under the transfer matrix**. The "global coordination" you describe is actually the **antisymmetric nature of fermion states**—local moves have global consequences because of fermion statistics, not geometric non-locality.

Your computational approach should test whether puzzle rhombi satisfy **free-fermion statistics**: do crossing moves produce sign changes? Does the transfer matrix have the **antisymmetric tensor structure** characteristic of fermionic systems?

**THE CYLINDRIC CONSTRUCTION CHALLENGE IS BACKWARDS**

You claim puzzle constraints are "non-cylindric," but this reverses the causality. Growth diagrams work precisely because they **impose cylindric structure on inherently non-cylindric problems**. The question isn't whether puzzles naturally exhibit periodicity—it's whether we can **embed them in a periodic structure** that makes growth diagrams possible.

Consider the RSK correspondence: standard tableaux don't naturally exhibit cylindric structure, but the growth diagram construction **forces** them into a periodic framework through careful boundary condition choice. The same should be possible for puzzles if we identify the correct embedding.

Your computational results showing "failure to find direct bijections" may simply reflect **incorrect boundary condition choices**, not fundamental non-embeddability. Have you tested periodic boundary conditions? Twisted boundary conditions? The full space of integ