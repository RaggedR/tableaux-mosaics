# Growth Diagram Challenge: The Fomin Perspective on KTW Puzzle Structure

## FUNDAMENTAL MISALIGNMENT: Growth Diagrams Require Specific Local Rules

The three reports reveal a **critical conceptual error**: they assume any "row-based construction" can become a growth diagram. This is categorically false. Fomin growth diagrams require **specific local rules** where face labels are determined by **adjacent boundary values alone**, with no global dependencies.

The computational report's finding that "nabla choices are correlated across rows" actually **proves** the conjecture false. In legitimate growth diagrams (RSK, Burge, dual RSK), each face label F(a,b,c,d) depends only on its four boundary values. The moment we need "constraint propagation" or "cascade dependencies," we've violated the fundamental locality principle.

## MISSING PIECE: Face Label Commutativity Requirements

None of the reports address the **commutativity constraints** that Fomin growth diagrams must satisfy. For any 2×2 square of faces with labels F₁, F₂, F₃, F₄, we need:
- **Row commutativity**: F₁ ∘ F₂ = F₃ ∘ F₄ 
- **Column commutativity**: F₁ ∘ F₃ = F₂ ∘ F₄

The jeu de taquin specialist hints at this with "multiple slide sequences produce identical tableaux," but misses that this **violates** growth diagram requirements rather than supporting them. Growth diagrams need **unique** face labels for given boundary conditions.

## CYLINDRIC CONSTRUCTION: THE REAL TEST CASE

The reports completely ignore the **cylindric growth diagram construction**, which is the natural generalization for handling boundary constraints like those in KTW puzzles. In cylindric diagrams:
- **Boundaries wrap around** rather than having fixed endpoints
- **Face labels encode periodic constraints** via wrapping conditions
- **Recording tableaux** are replaced by **cylindric tableaux**

The question becomes: can KTW puzzle rhombus orientations define consistent cylindric face labels? My analysis suggests **no**, because:

1. **Rhombus orientations aren't locally determined** by boundary conditions
2. **Color constraints create non-local dependencies** that violate cylindric locality
3. **The 3-fold rotational symmetry** of puzzle pieces doesn't match the 4-fold symmetry of growth diagram squares

## DEEPER STRUCTURAL OBJECTION: Recording vs. Insertion

The most fundamental issue the reports miss: **KTW puzzles don't naturally separate into insertion/recording phases**. Classical growth diagrams work because:
- **Insertion** follows deterministic local rules (RSK insertion)
- **Recording** captures the non-deterministic choices (which box to insert)

But in KTW puzzles, the "insertion" (rhombus placement) and "recording" (color/orientation choices) are **globally coupled**. You cannot make local rhombus decisions without knowing the global color pattern.

This coupling is precisely why migration works—it **decouples** these phases by:
1. **Mosaics** fix the rhombus placement pattern
2. **Migration** then optimizes color assignments
3. **LR tableaux** record the final decoupled state

## ALTERNATIVE FRAMEWORK: Quasi-Growth Diagrams

Instead of forcing classical growth diagrams, consider **quasi-growth diagrams** where face labels depend on **extended neighborhoods**:
- **Standard growth**: F(a,b,c,d) determined by 4 boundary values
- **Quasi-growth**: F(a,b,c,d;context) determined by boundary values plus **context information**

For KTW puzzles, the context would be:
- **Global color constraints** from boundary conditions  
- **Rhombus orientation constraints** from neighboring faces
- **Puzzle validity constraints** ensuring proper tiling

This framework could potentially work, but would lose the **bijective simplicity** that makes standard growth diagrams powerful.

## TESTABLE PREDICTION: Local Rule Existence

Here's my **specific falsification test**: For the c^(3,2,1)_{(2,1),(2,1)} = 2 case, attempt to construct **explicit local rules** that:
1. Take 4 boundary values from adjacent faces
2. Output a unique face label
3. Satisfy commutativity for all 2×2 