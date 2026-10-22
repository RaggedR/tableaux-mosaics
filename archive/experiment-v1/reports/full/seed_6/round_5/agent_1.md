# Fomin Growth Diagram Analysis: Exposing Fundamental Structural Incompatibilities

## The Local Rule Impossibility Theorem

The computational verification framework reveals a critical oversight across all reports: **KTW puzzles fundamentally cannot support Fomin-style local rules**. Here's why this is deeper than Yang-Baxter violations or computational complexity.

In Fomin growth diagrams, face labels encode **local insertion data** - each face transition depends only on adjacent edge labels. But puzzle constraints exhibit **global constraint propagation**: a single nabla orientation choice can force determinate configurations arbitrarily far away through rhombus tiling constraints.

**Challenge**: The "transfer matrix spectrum analysis" misidentifies the eigenstructure. Those "degenerate eigenspectra" aren't encoding bijection data - they're reflecting **constraint singularities**. When eigenvalues cluster at 0/1, you're seeing constraint satisfaction failure modes, not spectral projection structure.

## The Recording Tableau Problem: Why Face Labels Cannot Encode LR-Data

All reports miss the fundamental recording vs. insertion distinction. In RSK growth diagrams, face labels record **bumping sequences** during Robinson-Schensted insertion. But LR-tableaux arise from **skew tableaux standardization**, not bumping.

The compression "12 nablas → 3 tableau entries" isn't information compression - it's **constraint resolution**. Each LR-tableau entry encodes the **resolution state** of multiple overlapping constraints. Face labels in growth diagrams record **local decisions**, but LR-entries encode **global constraint solutions**.

**Structural Impossibility**: Face labels are by definition **local** (depending only on incident edges), but LR-tableau entries are **globally determined** by the entire puzzle boundary. No local rule system can bridge this locality gap.

## Migration Algorithm as Evidence AGAINST Growth Diagrams

The computational report's "migration bug" actually proves my point. The algorithm fails precisely when it encounters configurations requiring **non-local constraint resolution**. This isn't a bug - it's **mathematical necessity**.

Purbhoo's migration works because it **abandons locality** entirely. Each hexagonal flip requires checking **global constraint satisfaction** across the entire mosaic. This is antithetical to growth diagram construction, where each step depends only on local data.

**Counter-Challenge**: The claim that "some puzzles require virtual genus-1 structures" during migration reveals deeper issues. If the bijection requires topological deformation, then any proposed growth diagram must encode **genus data** in face labels - but face labels in triangular lattices are inherently **genus-0 objects**.

## Cylindric Growth Diagrams: The Wrong Generalization

The question mentions "whether the cylindric growth diagram construction applies here." This reveals a fundamental misunderstanding. Cylindric growth diagrams handle **periodic boundary conditions**, but puzzle boundaries are **fixed Dirichlet conditions**.

Cylindric constructions work for **translation-invariant** local rules, but puzzle constraints are **boundary-dominated**. The rhombus orientations near ∂λ, ∂μ, ∂ν are completely different from interior orientations - there's no translation symmetry to cylindrically extend.

## The Branching Structure Exposes Non-Commutativity

Here's what none of the reports addressed: **KTW puzzle branching choices don't form a growth diagram because they don't satisfy the commutativity condition**.

In growth diagrams, different orderings of local rule applications yield identical results. But puzzle constraint propagation is **order-dependent**. Resolve constraints row-by-row vs. column-by-column and you get different intermediate states (though the same final puzzle).

**Verification Challenge**: The proposed "row-by-row puzzle solving with face label recording" will fail not due to computational complexity, but because **face labels depend on constraint resolution order**. Different traversal orders will yield different "face label sequences" for identical puzzles.

## Alternative Framework: Constraint Satisfaction Networks, Not Growth Diagrams

Instead of forcing puzzle bijections into the growth diagram framework, consider **constraint satisfaction network dynamics**. Each nabla position is a **variable node**, each rhombus constraint is a **factor node**.

The puzzle→tableau bijection emerges from the **message passing dynamics** on this network. The LR-tableau entries record the **marginal distributions** after message passing convergence, not local rule applications.

This framework explains:
- Why migration algorithms work (message passing naturally finds global solutions)
- Why growth diagrams fail (constraint networks are inherently non-local)
- Why