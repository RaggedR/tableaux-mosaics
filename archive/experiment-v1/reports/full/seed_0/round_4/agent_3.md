# The Local Rule Crisis: Why All Three Reports Miss the Fundamental Architectural Problem

## The Fomin Framework Misunderstanding Goes Deeper

The first report correctly identifies the **Fomin local rule architecture** as missing, but then proposes "cylindric growth diagrams" that sidestep the core issue. The problem isn't finding the right geometric construction—it's that **puzzle constraints violate the locality principle entirely**.

Consider the fundamental growth diagram requirement: face labels must be computable from **immediate neighbors only**. But in KTW puzzles, a single nabla orientation choice at position (i,j) can **invalidate rhombi configurations** arbitrarily far away through the tiling constraint network. This isn't just "non-local optimization"—it's **constraint entanglement** that makes local face computation impossible.

**Critical Gap in Cylindric Proposal**: Even cylindric growth diagrams require that face labels depend only on **adjacent edges and faces**. The mosaic-migration process involves pathfinding that depends on the **entire global state**, not just local neighborhoods.

## Yang-Baxter Analysis Reveals the Wrong Algebraic Structure

The second report's Yang-Baxter obstruction is real but misdiagnosed. The issue isn't that KTW puzzles lack spectral parameter families—it's that **puzzle piece interactions don't form a braid group representation**.

**Fundamental Error**: Claiming migration implements "jeu de taquin rectification" with braid group actions. This is wrong. Standard jeu de taquin has **local exchange rules** between adjacent tableau entries. Migration involves **hexagonal flip cascades** that can propagate across the entire mosaic—these are **global geometric moves**, not local braid relations.

The "boundary R-matrix" proposal misses that puzzle boundaries aren't just inhomogeneities—they create **topological constraints** (genus-zero tiling) that fundamentally alter the algebraic structure. You can't just modify Yang-Baxter equations and preserve integrability.

## The Computational Report Exposes the Real Obstruction

The third report's constraint satisfaction analysis is closest to the truth but still misses the deeper issue. The problem isn't computational complexity—it's **categorical incompatibility** between growth diagram local rules and puzzle global constraints.

**Key Insight Missing**: The "12 → 3 projection" isn't about constraint elimination—it's about **different combinatorial species**. Puzzle nabla orientations live in the **tiling category** (geometric adjacency constraints), while LR tableau entries live in the **filling category** (algebraic ordering constraints). These categories have **no natural local functors** between them.

## The Migration Algorithm is Actually a Category Bridge

Here's what all three reports fundamentally miss: Purbhoo's migration algorithm isn't just "geometric mediation"—it's a **category equivalence construction** between:

1. **Tiling Category**: Objects are rhombi mosaics, morphisms are hexagonal flips
2. **Filling Category**: Objects are skew tableaux, morphisms are jdt slides

The migration process constructs an **explicit isomorphism** between these categories for the special case of LR-compatible boundary data. This is why it's necessarily global—**category equivalences cannot be localized**.

## Why Growth Diagrams Cannot Encode Category Bridges

Growth diagrams work within a **single combinatorial category**—typically the category of labeled paths or tableaux with local modification morphisms. Face labels count objects within this category.

But puzzle-to-tableau bijection requires **crossing categories**:
- Puzzle geometry → Mosaic topology (geometric category)  
- Mosaic dynamics → Migration paths (dynamical category)
- Migration endpoints → Tableau fillings (algebraic category)

Each transition involves **global invariant preservation** that cannot be captured by local face rules.

## The Transfer Matrix Construction is Category-Confused

The "row transfer matrix" approach assumes puzzle enumeration can be embedded in a **single linear algebra framework**. But this ignores that puzzles involve **multiple mathematical structures**:

- **Discrete geometry**: Rhombi tiling constraints
- **Combinatorial dynamics**: Flip move sequences  
- **Representation theory**: LR coefficient interpretation

Standard transfer matrices work because they operate within **homogeneous algebraic structures** (like quantum spin chains). Puzzles are **heterogeneous mathematical objects** that resist linear algebraic treatment.

## A Precise Impossibility Statement

**Theorem** (Informal): No growth diagram can directly implement the puzzle→LR tableau bijection because:

1. **