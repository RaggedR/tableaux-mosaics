# Extended Analysis: Local Rules vs. Global Constraints in KTW Puzzle Growth Diagrams

## What I Missed: The Branching Structure is the Key

My initial analysis overlooked the most crucial aspect: **KTW puzzles inherently encode branching processes**. Each nabla piece at an interior vertex represents a 3-way branching decision that must satisfy local compatibility. This isn't just about "degrees of freedom" - it's about **coherent branching data** that could naturally fit into a growth diagram framework.

The "12 free nabla choices projecting to 3 tableau entries" actually suggests something deeper: we have a **many-to-one correspondence** where multiple local configurations yield the same global recording data. This is precisely what face labels in growth diagrams are designed to handle.

## Critical Oversight: RSK-Type Correspondence Structure

I failed to recognize that KTW puzzles might naturally form an **RSK-type correspondence**. The puzzle construction involves:

1. **Input data**: Boundary conditions (like a permutation in RSK)
2. **Local decisions**: Nabla orientations at each interior vertex  
3. **Recording process**: How these decisions accumulate into tableau entries

This structure could support a growth diagram where:
- **Vertices** represent partial puzzle states
- **Edges** represent local nabla choices
- **Face labels** track the cumulative recording information

## The Cylindric Construction Challenge

My suggestion about cylindric growth diagrams was too vague. Here's the specific issue: **KTW puzzles have triangular, not rectangular, domains**. The boundary consists of three sides with different types of constraints:

- **Bottom edge**: Input partition λ
- **Left edge**: Input partition μ  
- **Right edge**: Output partition ν

A cylindric growth diagram typically assumes periodic or at least uniform boundary conditions. The triangular geometry of KTW puzzles breaks this symmetry fundamentally.

## What I Should Explore Next: Local Rules vs. Rhombus Tilings

The connection to **rhombus tilings** is where the growth diagram structure might emerge. Each KTW puzzle corresponds to a tiling of a hexagon with colored rhombi. The key insight I missed:

**Rhombus tilings naturally support growth diagram structures** because:
1. Each rhombus can be viewed as a local rule (2-face)
2. Edges carry orientation/color data
3. Vertices accumulate this data according to local constraints

But here's the technical challenge I didn't address: **KTW puzzles use triangular pieces, not just rhombi**. The nabla and delta pieces break the pure rhombus tiling structure. This suggests we need a **hybrid growth diagram** that can handle multiple types of local rules simultaneously.

## The Purbhoo Construction Reconsidered

I was too quick to dismiss the possibility of bypassing mosaics. The migration algorithm in Purbhoo's construction might actually **encode the face labels** of an implicit growth diagram. Each hexagonal flip corresponds to a local move that preserves certain invariants - these invariants could be exactly the face label data.

The question becomes: **Can we make this implicit growth diagram structure explicit?**

## Proposed Technical Investigation

Instead of my vague "cylindric construction," here's a concrete research program:

1. **Triangular Growth Diagrams**: Develop the theory of growth diagrams on triangular domains with mixed boundary conditions

2. **Hybrid Local Rules**: Extend Fomin's local rules to handle both rhombic and triangular pieces simultaneously

3. **Face Label Polynomials**: Investigate whether the face labels naturally live in the polynomial ring that governs equivariant cohomology (connecting to the Knutson-Tao equivariant puzzle rule)

## The Missing Connection: Equivariant Puzzles

I completely ignored that Knutson-Tao developed puzzles for **equivariant cohomology**, not just ordinary cohomology. The equivariant setting involves polynomial coefficients, which could provide the natural setting for face labels that encode more complex recording data than simple tableau entries.

This suggests the growth diagram structure might be more natural in the equivariant setting, where the face labels are polynomials rather than just combinatorial objects.