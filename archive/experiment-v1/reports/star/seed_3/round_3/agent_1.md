# The Growth Diagram Specialist's Challenge: Exposing the Categorical Confusion

## THE FUNDAMENTAL MISREADING OF GROWTH DIAGRAMS

The generalist's analysis commits a severe categorical error by treating growth diagrams as merely "bijective combinatorics." This reveals a profound misunderstanding of what growth diagrams actually accomplish.

Growth diagrams are **not** bijection-generating mechanisms—they are **bijection-revealing structures**. The distinction is crucial. A growth diagram doesn't create correspondences; it exposes the **local rule structure** that underlies existing bijections. The Fomin construction succeeds precisely because RSK already exists as a global bijection, and growth diagrams reveal its **local coherence**.

For KTW puzzles, the question isn't whether we can construct a growth diagram to create a bijection with LR tableaux (that bijection already exists via Purbhoo's mosaic route). The question is whether the **branching structure** of puzzle construction admits local rules that respect this existing bijection.

## WHERE THE SYNTHESIS FAILS: IGNORING FACE LABEL CONSTRAINTS

The generalist's "functorial analysis" completely ignores the **combinatorial constraints** that make growth diagrams work. Face labels aren't arbitrary—they must satisfy **local consistency conditions** that propagate globally. Not every bijection admits a growth diagram presentation.

**Critical oversight**: The synthesis treats "coordinate transformations" as if they're automatically localizable. But growth diagrams require that global bijections decompose into **compatible local moves**. This is a severe restriction that the algebraic approaches cannot guarantee.

The Purbhoo migration algorithm works precisely because it violates this locality requirement—it uses **global hexagonal flips** that cannot be encoded in local face labels. This suggests the puzzle-to-tableau bijection may be **fundamentally non-local**.

## THE SPECTRAL THEORY RED HERRING EXAMINED

The generalist praises the vertex model perspective as "revealing structural truth," but this misses how Yang-Baxter equations actually constrain combinatorial constructions. 

Yang-Baxter compatibility doesn't guarantee growth diagram existence—it guarantees **integrability** of associated transfer matrices. These are different mathematical properties. A system can be Yang-Baxter integrable yet have transfer matrices whose **eigenspace structure** doesn't correspond to growth diagram face labels.

**Specific challenge**: Show that the KTW puzzle transfer matrix eigenspaces naturally encode LR tableau data. The vertex model specialist assumes this without proof, and the generalist accepts it uncritically.

## THE MISSING DIMENSION: DIRECTED GRAPH STRUCTURE

Both the synthesis and all specialists miss the most fundamental constraint: growth diagrams require **directed graph structures** where face labels encode **recording information** via local rules.

KTW puzzles have natural **triangular lattice structure**, but their row-by-row transfer process creates **branching trees**, not rectangular grids. The face label interpretation becomes:
- Faces = branching choices at nabla positions
- Labels = partial tableau construction data
- Local rules = consistency of tableau growth

**Unaddressed question**: Can partial LR tableau data be encoded consistently in face labels of a triangular branching structure? This is a **graph-theoretic question**, not an algebraic one.

## THE CYLINDRIC CONSTRUCTION CHALLENGE

The generalist ignores the most promising technical direction: **cylindric growth diagrams**. These generalize standard growth diagrams to handle **non-rectangular boundaries** and **branching structures**.

For KTW puzzles, the natural approach is:
1. Embed triangular puzzle boundary in cylindric coordinates
2. Define face labels as **puzzle piece choices** at each branching point
3. Show local rules exist that make face labels **LR-tableau compatible**

This construction would resolve the direct bijection question, but requires proving that puzzle branching choices admit **consistent local rules**—a highly non-trivial constraint.

## WHERE THE CATEGORICAL APPROACH LEADS ASTRAY

The synthesis's "functorial analysis" fundamentally misunderstands the relationship between different mathematical presentations. The fact that multiple methods compute identical LR coefficients doesn't imply their computational processes are **naturally equivalent**.

**Category theory cannot resolve algorithmic locality questions.** Whether a global bijection admits local rule decomposition is a **computational complexity question** in disguise. It asks whether certain **information flow constraints** can be satisfied simultaneously.

## THE GENUINE RESEARCH TRAJECTORY

Instead of the generalist's abstract functorial approach, the concrete research should focus on:

**Primary technical question**: Do the face labels arising from KTW puzzle row construction satisfy