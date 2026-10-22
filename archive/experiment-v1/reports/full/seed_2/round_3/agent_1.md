# Growth Diagram Analysis: Fundamental Structural Impediments

**CORE CHALLENGE: The Reports Miss the Fomin Growth Diagram Requirements**

While the previous analyses correctly identify obstacles, they overlook the **specific structural requirements** for Fomin growth diagrams. These aren't arbitrary local update rules—they require **compatible face labels on directed graphs** where each face encodes bijective transformations between combinatorial objects.

## The Critical Gap: Recording Tableau Structure

**Missing Insight**: In RSK-type growth diagrams, face labels don't just track "local choices"—they encode **recording tableau entries** that satisfy specific compatibility conditions across adjacent faces. For KTW puzzles to admit growth diagrams, the puzzle degrees of freedom must naturally decompose into:

1. **Shape evolution data** (analogous to insertion tableau)  
2. **Recording data** (analogous to recording tableau entries)
3. **Local rules** ensuring these data types are consistent across faces

The computational analysis reveals why this fails: the "12 free nabla choices" cannot be cleanly separated into independent recording and shape components because **puzzle constraints couple these aspects globally**.

## Cylindric Growth Diagram Non-Applicability  

**Technical Obstruction**: The cylindric growth diagram construction (Krattenthaler-Müller) applies when the underlying poset has **cylindric symmetry** and the local rules respect this symmetry. But KTW puzzles live on triangular regions with **boundary-dependent constraints** that break any potential cylindric structure.

The boundary conditions (λ,μ,ν) on puzzle edges create **asymmetric constraint propagation** - the top boundary behaves differently from the left/right boundaries. This asymmetry is essential for Littlewood-Richardson structure but incompatible with cylindric growth methods.

## Local Rules vs. Global Rhombi Interactions

**Key Technical Point**: The jeu de taquin analysis identifies hexagonal flips as "generalized jdt slides," but misses a crucial distinction. In growth diagrams, face labels encode **local bijections between finite sets**, not global rectification procedures.

Each face label f should satisfy: if configurations A,B differ by f, then their associated tableaux differ by a **predictable local operation**. But puzzle rhombi interact through:
- **Non-crossing path constraints** (inherently global)
- **Boundary matching conditions** (non-local)  
- **Rhombi orientation propagation** (depends on distant puzzle regions)

No local face label can capture these global interdependencies while maintaining the required bijective properties.

## The Transfer Matrix Misconception

**Fundamental Error**: The vertex model analysis conflates "transfer matrix" in integrable systems with "transfer matrix" in growth diagram theory. These are **completely different objects**:

- **Integrable transfer matrices**: Operators on infinite-dimensional spaces with Yang-Baxter structure
- **Growth diagram transfers**: Finite bijective maps between labeled configurations on adjacent graph regions

KTW puzzles may have integrable structure (à la vertex models), but this doesn't imply growth diagram transfer matrices exist. The two concepts are mathematically orthogonal.

## Alternative Diagnostic: Face Label Dimension Analysis

**Proposed Test**: For growth diagrams to exist, face labels must have **bounded complexity**—each face encodes a bijection between finite sets of bounded size. But computational analysis suggests:

- Puzzle constraint propagation has **unbounded dependency chains**
- Local rhombi choices affect arbitrarily distant regions
- Face label complexity would grow with puzzle size

This violates the **finite type** requirement for growth diagram local rules.

## The Real Structural Question

Rather than seeking direct puzzle↔tableau growth diagrams, consider: **Do KTW puzzles admit growth diagram structure for any meaningful bijection?**

For instance:
- Puzzle ↔ Puzzle (with different boundary labelings)
- Puzzle ↔ Alternative mosaic structures  
- Puzzle ↔ Gelfand-Tsetlin patterns

If no such growth diagrams exist, this suggests KTW puzzles have **intrinsically non-local combinatorial structure** that resists growth diagram encoding entirely.

## Technical Verdict: Structural Impossibility

The growth diagram framework requires **local compatibility conditions** that are incompatible with:
1. Global boundary constraint propagation in triangular puzzles
2. Non-crossing path requirements coupling distant puzzle regions  
3. Recording data structure that spans the entire puzzle geometry

**Recommendation**: Focus on understanding what **minimal non-local structure** is required for puzzle↔tableau