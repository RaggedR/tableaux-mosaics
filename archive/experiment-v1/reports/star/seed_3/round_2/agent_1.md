# SPECIALIST ANALYSIS: The Growth Diagram Coherence Problem

## CHALLENGING THE "MIRAGE" FRAMING

The synthesis makes a critical error by accepting the specialists' implicit assumption that growth diagrams require **temporal locality**. This conflates Fomin's original construction with its subsequent generalizations. Modern growth diagram theory, particularly after Krattenthaler's work on cylindric diagrams, explicitly handles **non-local face labels** where labels depend on boundary data propagated through the diagram.

The "mirage" characterization fundamentally misunderstands what makes a growth diagram work: it's not local rules but **coherent face labeling** where labels satisfy consistency across all adjacent faces. KTW puzzles might perfectly support this structure.

## THE MISSING BIJECTION IS HIDING IN PLAIN SIGHT

The synthesis overlooks the most obvious interpretation of the computational evidence. The 12→3 "compression" isn't mysterious—it's exactly what we expect from **recording tableaux in RSK-type correspondences**. Each of the 12 nabla choices corresponds to a local branching decision in a growth process, and the 3 tableau entries are the **accumulated recording data**.

Consider: if KTW puzzles encode boundary conditions for a growth process, then the nabla choices are precisely the **face labels** we need. The "compression" is the standard phenomenon where multiple local labelings produce the same global recording tableau.

## CATEGORICAL ERROR: CONFLATING OBJECTS WITH THEIR ENCODINGS

The synthesis commits a basic categorical mistake by treating puzzles as "geometric objects" distinct from tableaux as "combinatorial objects." This is wrong. **Both are combinatorial encodings of the same algebraic structure**—Littlewood-Richardson coefficients.

In growth diagram theory, we routinely have bijections between seemingly disparate objects:
- Gelfand-Tsetlin patterns ↔ semistandard tableaux  
- Rhombic tilings ↔ alternating sign matrices
- Puzzle pieces ↔ Littelmann paths

The apparent "categorical incompatibility" dissolves when we recognize that all these objects are **different coordinate systems** for the same underlying algebraic variety.

## THE BOUNDARY CONDITION REFRAMING IS BACKWARDS

The alternative synthesis proposes viewing puzzles as boundary conditions rather than input data. This gets the mathematics exactly backwards. In Fomin growth diagrams, **boundary conditions ARE input data**. The innovation isn't separating these concepts but recognizing their identity.

More critically, the reframing ignores the **directed nature** of growth diagrams. We don't propagate "boundary constraints inward"—we propagate **growth decisions outward** from initial data. The KTW transfer matrix naturally fits this pattern: each row represents one step in an outward growth process.

## SPECTRAL THEORY IS THE KEY, NOT THE DISTRACTION

The synthesis dismisses the vertex model specialist's focus on spectral properties, but this reveals a profound gap in understanding. Growth diagrams work precisely because their transfer matrices have **compatible spectral decompositions**. When the vertex model specialist mentions "spectral curves," they're identifying the algebraic structure that makes face labeling coherent.

The RTT relations aren't abstract algebra—they're the **consistency conditions** that ensure face labels propagate correctly through the diagram. If KTW puzzles satisfy analogous relations (which the transfer matrix structure suggests), then the growth diagram construction is automatic.

## THE COMPUTATIONAL PREDICTIONS ARE INSUFFICIENT

The synthesis over-privileges computational falsifiability, but this reflects mathematical naivety. The computational specialist's predictions about "sparse matrices over F₂" miss the point entirely. Growth diagrams aren't about computational efficiency—they're about **bijective proof**.

The real question isn't whether we can compute faster, but whether the face labeling gives **canonical bijections** that respect all algebraic structure. This requires proving that labels satisfy exchange relations, which computational enumeration cannot verify.

## WHAT THE SYNTHESIS MISSED: CYLINDRIC EXTENSIONS

Most critically, the synthesis ignores the **cylindric growth diagram construction**. This is precisely designed for problems where standard growth diagrams fail due to boundary constraints. KTW puzzles, with their hexagonal boundary conditions, are exactly the setting where cylindric methods should apply.

The cylindric construction handles the "global constraint" problem by **wrapping the diagram** so that boundary information flows continuously through the growth process. This potentially resolves all the specialists' objections while preserving the local rule structure.

## PROPOSED RESEARCH DIRECTION

Rather than accepting the "mirage" diagnosis, I propose investigating whether:

1. KT