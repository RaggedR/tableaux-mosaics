# Growth Diagram Analysis: Fundamental Structural Misalignment

The synthesis reveals a sophisticated understanding but misses the **most critical point**: the specialists are debating symptoms while ignoring the underlying **face label incompatibility theorem**. Let me provide the definitive analysis.

## The Core Error: Misunderstanding What Growth Diagrams Actually Are

The synthesis treats growth diagrams as "information flow architecture" - this is **categorically wrong**. Growth diagrams are **combinatorial encoding machines** where face labels must satisfy the **compatibility diamond condition**:

For any 2×2 grid with corner shapes (λ, μ, ν, σ), the face labels must determine σ uniquely from (λ, μ, ν). This isn't about "information flow" - it's about **local inversion**.

**Critical Gap**: None of the specialists addressed whether KTW puzzle constraints even permit such diamonds to exist. The synthesis assumes they do and asks why they "fail to work" - but the real question is whether they're **mathematically possible**.

## Why the Migration Bypass Fails: The Fomin-Kirillov Obstruction

The synthesis proposes studying mosaic→tableau growth diagrams to "bypass migration's global optimization." This reveals fundamental misunderstanding of **why** Fomin growth diagrams work for RSK:

1. **RSK case**: Bumping paths have **unique endpoints** determined by local insertion rules
2. **Mosaic case**: Rhombi movements have **multiple valid destinations** requiring global path planning

The local diamond condition **cannot exist** for mosaics because the same local configuration can lead to different global outcomes. This isn't a computational complexity issue - it's a **mathematical impossibility**.

## The Hexagonal Coordinate Insight Nobody Saw

The synthesis notes three specialists rejecting hexagonal reformulations but misses the **deeper geometric reason**: KTW puzzles live in **affine coordinate systems** while growth diagrams require **projective coordinates**.

Here's the key: Fomin's original construction works because Young tableaux naturally embed in the **integer lattice Z²**. But KTW puzzles encode **Grassmannian cohomology**, which has **projective geometry** at its core. The angle constraints aren't just "geometric" - they're **projective invariants**.

**New Conjecture**: Growth diagrams can only exist for combinatorial objects that embed naturally in **affine torus actions**. KTW puzzles require **projective torus actions**, hence the structural incompatibility.

## The Quantum Group Red Herring

The vertex model specialist's U_q(gl_n) analysis is **mathematically precise but irrelevant**. Quantum group symmetries are **sufficient** for integrability but not **necessary** for growth diagrams. The RSK correspondence predates quantum groups by decades and has a purely combinatorial construction.

The real obstruction is **algebraic**: growth diagrams require **plactic monoid actions** on face labels. KTW puzzles encode multiplication in **cohomology rings**, which are **commutative** but not **plactic**. You can't force cohomological multiplication through plactic compression.

## What the Bit Analysis Actually Reveals

The computational specialist's "11.5 → 1.6 bit" calculation is profound but misinterpreted. This isn't measuring "mutual information decay" - it's measuring **local rule complexity**.

**Key Insight**: In RSK, each face label encodes **one bit** (bump/no-bump). In KTW, each local choice requires **log₂(3) ≈ 1.6 bits** (three rhombi orientations). But the **constraint propagation** requires tracking **multiple future possibilities**, exploding the face label alphabet.

The growth diagram framework **fundamentally requires** that face labels form a **finite alphabet**. KTW's constraint propagation demands **exponentially growing alphabets**, violating the basic growth diagram axioms.

## The Missing Cylindric Construction

Here's what **everyone missed**: Fomin's later work on **cylindric growth diagrams** specifically addresses cases where traditional growth diagrams fail. The cylindric construction allows **non-local** information propagation through **boundary conditions**.

**New Research Direction**: Instead of asking whether KTW puzzles have growth diagrams, ask whether they have **cylindric growth diagrams**. This requires studying how puzzle boundary conditions propagate through the tiling.

The Grassmannian's **cylindric coordinates** (via Plücker relations) might naturally correspond to cylindic growth diagram structure. This could provide