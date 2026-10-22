# SPECTRAL THEORY EXPOSES THE FUNDAMENTAL FLAW

The response demonstrates sophisticated understanding of growth diagram theory but commits a **critical algebraic error** that undermines its entire argument. The Yang-Baxter framework, while mathematically elegant, cannot rescue what is fundamentally a **spectral dimension mismatch**.

## THE CATASTROPHIC DIMENSION PROBLEM

**Fatal Error**: The response treats nullspace dimension 1 as evidence of "single integrability constraint." This is backwards. In vertex models with Yang-Baxter structure, **transfer matrices must have maximal rank** for the commutation relations T(u)T(v) = T(v)T(u) to generate meaningful spectral families.

**Spectral Reality Check**: For c^(3,2,1)_{(2,1),(2,1)} = 2, we need transfer matrices whose eigenvalues encode **both puzzle multiplicities**. A rank-deficient matrix with 1-dimensional nullspace cannot distinguish between the two distinct puzzles—it projects both to the **same spectral state**.

**Why the Yang-Baxter argument fails**: R-matrices satisfying the Yang-Baxter equation generate **invertible transfer matrices**. The observed rank deficiency indicates we're not looking at proper R-matrix evolution, but rather at **degenerate constraint propagation** that loses essential information.

## CONSTRAINT PROPAGATION VS. BIJECTIVE ENCODING

The response conflates two distinct mathematical structures. **Constraint propagation** (what migration actually does) operates in a different algebraic framework than **bijective face label encoding** (what growth diagrams require).

**Crucial Distinction**: In RSK-type growth diagrams, face labels encode **full bijective information**—every step of the correspondence is reversible through the face label sequence. Migration, however, uses **irreversible local moves** that lose global positioning information.

**The 4:1 ratio problem**: The response suggests nabla choices are "local constraint decisions" while tableau entries are "global constraint resolutions." But this **breaks reversibility**—you cannot reconstruct which of the 4 nabla configurations generated a given tableau entry from the face labels alone.

## YANG-BAXTER EQUATIONS: NECESSARY BUT NOT SUFFICIENT

**Conceding the Point**: The response is correct that Yang-Baxter consistency is necessary for growth diagram structure. However, it's **not sufficient** when the underlying combinatorial objects have incompatible enumeration structures.

**The Spectral Parameter Problem**: In free-fermionic vertex models, spectral parameters encode **continuous deformation families**. KTW puzzles are discrete objects with **no natural spectral parameter structure**. The "integrability" comes from geometric intersection theory, not Yang-Baxter algebraic relations.

**Missing Connection**: Even if local moves satisfy Yang-Baxter consistency, the **global enumeration constraints** (Littlewood-Richardson multiplicities) impose additional restrictions that vertex model weights cannot naturally encode.

## THE MIGRATION-AS-DUAL-GROWTH FALLACY

**Critical Gap**: The response claims migration "IS the direct transfer, but in the dual coordinate system." This requires proving that **rhombus position coordinates** can be consistently mapped to **face label coordinates** while preserving the bijective structure.

**Computational Challenge**: The hexagonal flip rules in migration depend on **global mosaic structure**, not just local rhombus configurations. Face labels in growth diagrams must be **locally determined**. This creates an **unavoidable conflict** between the two encoding schemes.

**The reversibility test**: If migration were truly dual growth diagram evolution, then **every hexagonal flip sequence** should correspond to a unique face label trajectory. But migration allows multiple paths between the same initial and final mosaics—this **violates growth diagram uniqueness**.

## THE CYLINDRIC CONSTRUCTION REVEALS THE DEEPER ISSUE

The cylindric construction actually **exposes why the growth diagram fails**. In vertex models, periodic boundary conditions create **monodromy matrices** whose eigenvalues encode the physical spectrum. For KTW puzzles, cylindric constructions would need to satisfy **geometric consistency conditions** from toric variety intersection theory.

**The Fundamental Incompatibility**: Vertex model monodromy encodes **quantum group representations**, while puzzle monodromy must encode **Schubert calculus relations**. These are **different categorical structures** that cannot be unified through face label evolution.

## EXPERIMENTAL PROTOCOLS THAT WOULD DEFINITIVELY RESOLVE THIS

**Experiment 1**: Implement face label tracking during row construction, but **test reversibility explicitly**. Can