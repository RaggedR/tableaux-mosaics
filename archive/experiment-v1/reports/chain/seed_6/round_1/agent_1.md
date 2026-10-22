## Initial Analysis: KTW Puzzles and Growth Diagram Structure

**CHALLENGE TO THE FRAMING:**

The problem's premise that KTW puzzle branching choices "naturally" form a growth diagram requires serious scrutiny. Growth diagrams fundamentally depend on **local rules** that preserve essential invariants across adjacent cells, but puzzle branching choices are inherently **global constraints** - each nabla orientation must respect the puzzle's rhombus tiling structure across the entire hexagonal region.

**CRITICAL GAP: Locality vs. Globality**

In RSK-type growth diagrams, face labels encode local recording decisions where each 2×2 square can be resolved independently using bumping/insertion rules. However, KTW puzzles exhibit **constraint propagation** - a single nabla choice can force cascading orientation decisions across multiple rhombi. This suggests the "free choices" aren't actually local degrees of freedom but rather manifestations of global consistency requirements.

**ALTERNATIVE INTERPRETATION:**

Rather than viewing the 12 free nabla choices → 3 tableau entries as a growth diagram encoding, consider this as evidence that puzzle solutions live in a **fiber bundle** over LR tableaux. The 2^4 = 16 apparent degrees of freedom reduced to 2 actual puzzles suggests the constraint variety has codimension much higher than a typical growth diagram would permit.

**DEEPER STRUCTURAL QUESTION:**

The Purbhoo construction (puzzle → mosaic → migration → tableau) succeeds because mosaics naturally support **jeu de taquin**-like operations. But jeu de taquin fundamentally relies on **rectification algorithms** that don't obviously correspond to growth diagram face label updates.

**TECHNICAL OBJECTION:**

Growth diagrams typically require that face labels form a **distributive lattice** structure where covering relations correspond to elementary moves. KTW puzzle pieces (rhombi with fixed orientations) don't obviously admit such ordering - they're geometric objects, not combinatorial ones with natural partial orders.

**ALTERNATIVE RESEARCH DIRECTION:**

Instead of forcing puzzle branching into a growth diagram framework, investigate whether the **cylindric growth diagram** construction applies to the **dual problem**: given an LR tableau, can we use growth diagram local rules to enumerate all corresponding puzzles? This reverses the encoding direction but might reveal clearer local structure.

The fundamental issue remains: puzzle constraints are **topologically rigid** while growth diagrams require **combinatorially flexible** local rules.