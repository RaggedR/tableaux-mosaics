# Specialist Analysis: The Synthesis Misses the Jeu de Taquin Core

## The Migration-Growth Diagram Disconnect

The synthesis correctly identifies the locality tension but **fundamentally misunderstands migration dynamics**. Migration isn't "jeu de taquin slides" in sequence—it's **simultaneous hexagonal flips** that preserve global mosaic validity. The synthesis conflates two different combinatorial operations:

1. **Migration flips**: Local hexagonal moves that preserve rhombus orientations
2. **Jeu de taquin slides**: Tableau operations that change filling patterns

These aren't equivalent. A migration step can involve multiple simultaneous flips that together preserve the boundary conditions, while jdt slides are inherently sequential and local-to-global propagating.

## The "Stratified Locality" Red Herring

The synthesis's proposed "stratified locality" framework is mathematically vacuous. **Hierarchical data structures don't resolve the fundamental tension**—they just push it up one level. If Level 0 requires global information to determine local choices, then the "locality" is illusory.

More critically, the synthesis ignores that **Purbhoo's bijection already resolves the locality problem**: mosaics ARE the local encoding of global structure. Each rhombus placement is determined by local rules (avoiding monochromatic vertices), but the global boundary conditions emerge from these local constraints.

## Where Growth Diagrams Actually Fail

The synthesis misses the real obstruction. Growth diagrams work for objects with **canonical normal forms** (like Robinson-Schensted correspondence). KTW puzzles don't have this property—multiple distinct puzzles can yield the same LR coefficient, and there's no canonical choice among them.

The computational specialist's "4:1 ratio" isn't about spectral parameters or gauge freedom. It's about **orbit-stabilizer counting**: the 12 nabla choices form orbits under puzzle symmetries, and growth diagrams can't naturally encode orbit structures in face labels.

## The Missing Connection: Rectification as Inverse Limit

Here's what all the specialists (and the synthesis) miss: **migration isn't a process—it's a rectification procedure that finds canonical representatives**. The growth diagram question is backwards. Instead of asking whether puzzles admit growth diagrams, ask: **Do growth diagrams admit puzzle interpretations?**

This inversion reveals the actual mathematical structure:
- Growth diagrams naturally produce **rectified tableaux**
- Puzzles are **unrectified pre-images** under the migration map
- The bijection works because migration is **surjective with structured fibers**

## The Schutzenberger Involution Gap

The synthesis completely ignores the **Schutzenberger involution** ω, which is crucial for understanding why Purbhoo's bijection preserves the ring structure. Under ω:
- Puzzle boundary conditions transform predictably
- Migration paths map to dual migration paths  
- LR tableaux map to transposed evacuation tableaux

Growth diagrams for puzzles would need to respect this involution **at the face label level**, which requires encoding non-local duality information locally. The synthesis's "algebraic constraints" discussion touches this but doesn't recognize the involution as the core obstruction.

## Experimental Counter-Proposal

Instead of the synthesis's vague "falsifiable tests," here's a concrete challenge:

**Conjecture**: Any growth diagram purporting to implement puzzle→tableau bijection must have face labels that are **Schutzenberger-equivariant**.

**Test**: For the minimal case c^(3,2,1)_{(2,1),(2,1)} = 2, construct explicit face labels for both puzzles. Apply Schutzenberger involution to the boundary conditions and verify the face labels transform consistently.

If this fails (which I predict it will), then growth diagrams cannot capture the puzzle bijection without additional non-local structure.

## The Representation Theory Reality

The synthesis asks "where do algebraic properties come from?" The answer is **geometric**: Littlewood-Richardson coefficients count intersection multiplicities in cohomology. The algebraic structure comes from **cup product associativity**, not from combinatorial bijections.

Purbhoo's brilliance was recognizing that **migration preserves intersection geometry**—it's not just a combinatorial trick but a geometric rectification that maintains cohomological meaning. Growth diagrams encode different geometric information (usually related to crystal bases or representation theory), which is why forcing this connection is problematic.

The synthesis's "stratified locality"