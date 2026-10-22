**MIGRATION MECHANICS VS. GROWTH DIAGRAM MYTHOLOGY: A JEU DE TAQUIN PERSPECTIVE**

The vertex modelist's technical objections reveal deep confusion about what migration actually accomplishes and how growth diagrams relate to tableau dynamics. Their Yang-Baxter fixation misses the central point: we're not trying to build a vertex model—we're asking whether existing growth diagram technology can capture Purbhoo's bijection more directly.

## Migration is Already Local (When Properly Understood)

**Fundamental mischaracterization**: The claim that "hexagonal flips affect rhombi arbitrarily far away" betrays unfamiliarity with how migration actually works. Each hexagonal flip in Purbhoo's algorithm corresponds to a *single jeu de taquin slide* in the target tableau. JdT slides are rigorously local operations—they move one box along a uniquely determined path until reaching a corner.

**The locality is in tableau space, not puzzle space**: Migration doesn't "rearrange global configurations"—it implements a sequence of elementary JdT moves. Each hexagonal flip moves exactly one colored rhombus to an adjacent position, following the same constraint-satisfaction logic as sliding a tableau entry to fill an adjacent hole.

**Reading order correspondence**: The vertexalist completely ignores that puzzle rhombi have a canonical reading order (induced by the triangular lattice orientation) that corresponds directly to the standard reading order for LR-tableaux. This isn't coincidental—it's the core insight that makes Purbhoo's bijection work.

## Growth Diagrams Don't Need Yang-Baxter

**Categorical error**: The insistence on Yang-Baxter equations reveals fundamental confusion about growth diagrams versus integrable lattice models. Growth diagrams for RSK work precisely because they DON'T require integrability—they exploit the local path-counting structure of Young tableaux, not quantum R-matrices.

**Fomin's original insight**: Growth diagrams succeed when face labels encode "how many ways to extend a partial configuration." For puzzles → tableaux, the relevant question is: given partial puzzle boundary data, how many valid completions exist? This is a purely combinatorial counting problem, not a spectral parameter optimization.

**Free-fermionic red herring**: The demand for explicit fermion occupation patterns misses that puzzle tiles already encode occupation data—each rhombus color corresponds to which "strand" occupies that position in the triangular lattice. The constraint satisfaction IS the exclusion principle.

## The Auxiliary Space Dimension Non-Problem

**Exponential vs. tractable**: Yes, the full configuration space is exponential, but growth diagrams don't track full configurations—they track *incremental extensions*. For RSK, auxiliary states are Young diagrams (exponentially many), but face rules only need to distinguish "box added" vs. "box not added" locally.

**Puzzle auxiliary states**: The analogous auxiliary space for puzzles would track *partial boundary completions*—how many valid ways to extend the current puzzle boundary by one edge. This is potentially tractable because puzzle constraints are highly structured (they encode Grassmannian intersection theory).

**Migration sequence encoding**: Here's the crucial insight the vertexalist misses: if we can show that the sequence of hexagonal flips in migration corresponds to a sequence of face rule applications in some growth diagram, then the face labels would directly encode the JdT slide sequence, giving the LR-tableau immediately.

## The Real Challenge: Constraint Propagation Structure

**Where the difficulty lies**: The genuine obstacle isn't Yang-Baxter relations or fermion exclusion—it's whether puzzle constraint satisfaction can be decomposed into local face rules. KTW puzzles have global consistency requirements (the boundary conditions must be simultaneously satisfiable), while growth diagrams work by building consistent configurations incrementally.

**Testable reformulation**: The right question is whether puzzle boundary data can be extended edge-by-edge in a manner where each extension choice corresponds to exactly one JdT slide in the target tableau. If so, face labels counting these extensions would give the bijection directly.

**Connection to crystal operators**: The vertexalist dismisses crystal bases, but this is precisely relevant. Crystal operators on LR-tableaux correspond to adding/removing boxes according to specific rules. If puzzle edge extensions correspond to crystal operations, then growth diagram faces encode crystal operator applications—exactly what we need.

## Minimal Example Analysis: Beyond c^{(3,2,1)}_{(2,1),(2,1)}

**Why this example is misleading**: The 2-puzzle case is too small to see the pattern.