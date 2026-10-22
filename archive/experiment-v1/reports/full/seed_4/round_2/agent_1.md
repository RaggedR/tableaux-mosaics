# Growth Diagram Analysis: Fundamental Structural Obstacles

The computational and vertex model analyses expose critical issues, but they miss the deeper **structural impossibility** inherent in the growth diagram conjecture. As a specialist in Fomin growth diagrams and local rules, I must challenge the core premise more fundamentally.

## The Local Rule Contradiction

Growth diagrams succeed when **local face labels uniquely determine global structure**. The three analyses reveal why this fails catastrophically for KTW puzzles:

**Critical Observation:** The "12 free nabla choices → 3 tableau entries" compression isn't just a 4:1 ratio—it's evidence that the puzzle-to-tableau correspondence is **inherently non-local**. In standard RSK growth diagrams, each face label encodes exactly one insertion/bumping decision. Here, multiple puzzle regions must coordinate to produce a single tableau entry.

The vertex model analysis correctly identifies Yang-Baxter integrability as necessary, but misses that **KTW puzzle constraints violate the locality assumption** required for Yang-Baxter equations to apply meaningfully.

## Face Label Cardinality Mismatch

The computational analysis hints at this but doesn't push far enough. In a valid growth diagram:
- Face label alphabet size grows polynomially with diagram size
- Local rules have bounded look-ahead
- Path-counting remains tractable

For KTW puzzles, the "transfer matrix" would require face labels encoding:
- Current partial tableau state (exponential in tableau size)
- Pending nabla resolution constraints (exponential in puzzle height)
- Global compatibility conditions (non-local)

This isn't a "dimensionality problem"—it's proof that no local rule system can exist.

## The Migration Algorithm as Obstruction

The second analysis treats migration as an "essential non-local coordination mechanism," but doesn't recognize its deeper significance. Migration isn't just resolving conflicts—it's **implementing jeu de taquin evacuation**, which is fundamentally a **global** algorithm.

**Key Insight:** Jeu de taquin evacuation requires tracking sliding paths that can span the entire tableau. Any growth diagram encoding this must have face labels that "remember" arbitrarily distant past decisions. This violates the Markov property that makes growth diagrams tractable.

## Alternative: Cylindric Growth Diagrams Don't Help

The computational analysis suggests cluster algebra connections, which naturally leads to considering **cylindric growth diagrams** (periodic boundary conditions). However, KTW puzzles don't exhibit the translation invariance required for cylindric constructions to apply.

The boundary conditions in KTW puzzles (fixed partitions λ, μ, ν) break the translation symmetry that makes cylindric growth diagrams work for, e.g., symmetric function identities.

## What Growth Diagrams Can Capture

Rather than abandoning the growth diagram framework entirely, here's what **is** possible:

**Proposition:** Growth diagrams can encode the **puzzle → mosaic** step, with face labels tracking local rhombus orientations. The obstruction appears precisely at the **mosaic → tableau** boundary, where migration begins.

This suggests a **hybrid approach**:
1. Growth diagram: puzzle → mosaic (local rules work here)
2. Global algorithm: mosaic → tableau (migration necessary)

## The Real Research Question

Instead of seeking impossible direct bijections, the productive question is:

**"Can we characterize the precise boundary where local rules fail in the KTW construction?"**

This would involve:
- Identifying which nabla choices can be resolved locally
- Characterizing the "residual non-local constraints"
- Understanding how migration complexity scales with these residual constraints

## Counter-Example Construction

To definitively refute the conjecture, consider the family c^{(n,n-1,...,1)}_{(n-1,n-2,...,1),(1)} for large n. The number of free nabla choices grows exponentially, but the LR coefficient equals 1 (single tableau). Any growth diagram encoding this must have face labels of exponential complexity—contradicting the local rule principle.

## Conclusion

The growth diagram conjecture fails not due to computational limitations or missing Yang-Baxter integrability, but because **KTW puzzle-to-tableau correspondence is fundamentally non-local**. Migration isn't an inefficient detour—it's the only known algorithm that can resolve the global constraint interactions that define this correspondence.

The productive research direction is understanding **hybrid local-global constructions** where growth diagrams handle the locally-resolvable components, while global algorithms manage the