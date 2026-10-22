# Growth Diagram Analysis: Why the Direct Approach Likely Fails

The generalist's framing misses several crucial technical barriers that make this direct construction nearly impossible. Let me dissect this problem through the lens of Fomin growth diagrams and local rules.

## Fundamental Incompatibility: Local Rules vs. Global Branching

**The Core Technical Issue**: Growth diagrams require **local face rules** where each 2×2 face update depends only on neighboring labels. But KTW puzzles have **global branching structure** where each "free nabla choice" potentially affects the entire puzzle's validity.

Consider the edge labels in a growth diagram. In RSK-type correspondences, these encode:
- **Insertion path data** (which boxes to add/remove)
- **Recording tableau entries** (which positions get filled)

For KTW puzzles, the "12 free nabla choices" represent fundamentally different data—they're **constraint satisfaction decisions**, not insertion operations. This is why Purbhoo's migration algorithm works: it **spatially separates the constraint resolution from the tableau construction**.

## The Dimensional Mismatch is Actually Worse

The generalist's 4:1 ratio misunderstands the problem. It's not that 12 choices produce 3 entries—it's that:
- The 12 choices form a **branching tree of puzzle completions**
- Each completion path corresponds to **one specific LR tableau**
- The "3 tableau entries" are just the **final boundary data**

A direct growth diagram would need face labels that somehow **branch and reconverge** while maintaining the RSK-style local update property. This violates the fundamental **deterministic local rule** requirement.

## Critical Gap: Face Label Interpretation

In cylindric growth diagrams, face labels encode **recording data via path tracking**. But what would face labels mean here?

**Option 1**: Labels encode partial puzzle states
- **Problem**: Partial puzzles aren't well-defined (boundary constraints)
- **Problem**: Face updates would need non-local information

**Option 2**: Labels encode tableau data directly  
- **Problem**: How do puzzle constraints translate to tableau constraints locally?
- **Problem**: The 12→3 compression loses essential branching information

**Option 3**: Labels encode "constraint satisfaction state"
- **Problem**: This isn't compatible with growth diagram edge/face structure
- **Problem**: Constraint resolution requires global checking, not local updates

## The Real Obstruction: Puzzle Planarity vs. Tableau Rectification

KTW puzzles live in the **plane** with specific **rhombus tiling constraints**. The branching choices correspond to **local rhombus orientations** that must satisfy **global planarity**.

LR tableaux live in a **different geometric space**—they're about **corner sequences** and **rectification paths**. Purbhoo's migration algorithm performs the crucial **geometric transformation** between these spaces.

A direct growth diagram would need to perform this geometric transformation **incrementally and locally**, but the planarity constraints are **inherently non-local**.

## Alternative Technical Framing: What Actually Works

Instead of seeking direct construction, consider:

**Conjecture**: The transfer matrix construction might define a **signed growth diagram** where face labels track **constraint violation degrees**.

**Better Question**: Can we construct a **modified growth diagram** where:
- Face labels encode **partial constraint states**
- Edge labels track **branching multiplicity**  
- The final tableau emerges from **multiplicity resolution**

This preserves the transfer matrix structure while acknowledging that puzzle→tableau isn't a **deterministic local correspondence**.

## Conclusion: The Indirect Route is Mathematically Necessary

The Purbhoo construction isn't just computationally indirect—it's **geometrically necessary**. The migration algorithm performs **spatial constraint resolution** that cannot be encoded in local face rules.

The direct approach fails because it conflates **constraint branching** (puzzle space) with **path tracking** (tableau space). These are fundamentally different mathematical operations that require the intermediate **mosaic geometry** to mediate between them.

**Verdict**: The direct construction is likely impossible, and attempting it misunderstands the mathematical role of the intermediate steps.