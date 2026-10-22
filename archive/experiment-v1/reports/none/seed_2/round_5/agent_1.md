# Fundamental Challenge: The Migration Path Illusion

## Your Coordinate Transformation Hypothesis is Wrong

You claim the migration algorithm "implements" a growth diagram in different coordinates, but this reveals a profound misunderstanding of what migration actually does. **Migration doesn't preserve the algebraic structure that growth diagrams require**.

### The Critical Issue: Non-Reversible Operations

Migration involves **rhombi annihilation**—colored pieces disappear entirely when they reach boundaries. This is fundamentally different from face label updates, which must maintain **conservation laws**. In RSK-type growth diagrams, information flows through faces but is never destroyed.

Consider what happens in migration:
- Rhombi move through hexagonal lattice
- When rhombus reaches tableau boundary, it vanishes
- The vanishing encodes a tableau entry

**But**: This violates the bijective property that growth diagrams must satisfy. Face labels represent **reversible local transitions**—given boundary data, you must be able to reconstruct the entire interior configuration.

## Where the Transfer Matrix Framework Actually Fails

Your "row-by-row construction" fundamentally misunderstands puzzle geometry. KTW puzzles aren't naturally stratified by rows—they're **triangular domains** with boundary conditions on all three sides simultaneously.

### The Boundary Coupling Problem

Growth diagrams require **separable boundary conditions**: you can specify top/left boundaries independently and compute right/bottom boundaries. But puzzles have:
- Coupled boundary constraints across all three triangle edges
- **Cohomological consistency** requirements that span the entire domain
- Global orientation constraints that can't be factored

This isn't about "different lattice orientations"—it's about **topological incompatibility**.

## The Cylindric Construction Red Herring

Your "4-fold symmetry" hypothesis shows you're grasping at patterns that don't exist. The 12→3 ratio isn't periodic structure—it's **overcounting due to gauge redundancy**.

KTW puzzles have **internal symmetries** (nabla rotations) that don't correspond to any natural group action on LR tableaux. This breaks the fundamental growth diagram requirement that **face labels encode bijective transitions**.

### What You're Missing: Gauge Theory Structure

Puzzles are closer to **gauge field configurations** than combinatorial growth processes:
- Multiple nabla configurations give same "physical" content
- Gauge fixing (choosing canonical orientations) breaks locality
- The migration procedure is essentially **gauge reduction**, not growth

## The Real Question: Why Does RSK Work But KTW Doesn't?

RSK correspondence works as growth diagram because:
- **Insertion process is inherently local** (each letter affects bounded tableau region)
- **Recording captures only local changes** (bumping paths have finite support)
- **Boundary data factorizes cleanly** (word × vacant tableau → filled tableau × recording word)

KTW puzzles fail because:
- **Rhombus constraints are globally coupled** (changing one piece affects constraint satisfaction everywhere)
- **LR tableau entries depend on global puzzle topology**
- **No natural factorization** of boundary data

## Your Proposed "Investigation" is Backwards

You ask whether "nabla orientations can be encoded as edge labels." This gets it exactly wrong. The question isn't whether orientations can be **encoded**—it's whether the **dynamics of orientation constraints** can be localized.

The constraint propagation I mentioned isn't about "non-local constraints" as algebraic objects—it's about **constraint satisfaction being a global optimization problem**, not a local growth process.

## What This Reveals About the Deeper Structure

The puzzle→mosaic→migration→tableau path isn't "avoiding" growth diagrams—it's following the **natural information flow** in this system:

1. **Puzzle**: Global constraint satisfaction
2. **Mosaic**: Gauge-fixed representation  
3. **Migration**: Irreversible reduction process
4. **Tableau**: Canonical output

This is fundamentally **different** from growth diagrams, which preserve information at every step.

## The Challenge You Must Address

Stop trying to force KTW into the growth diagram framework. Instead, explain:

**Why does your coordinate transformation hypothesis survive the migration information loss problem?**

If rhombi vanish during migration, what growth diagram "face labels" could possibly encode this vanishing while maintaining bijectivity?

The burden is on you to show how **irreversible gauge reduction** can be reformulated as **reversible local growth**. 

What's your answer to this fundamental incompatibility?