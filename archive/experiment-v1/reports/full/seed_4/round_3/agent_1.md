# Growth Diagram Specialist Analysis: Fundamental Local Rule Obstruction

## Core Challenge to All Previous Reports

The four reports fundamentally misunderstand what makes growth diagrams work. They focus on geometry, integrability, and computation while **missing the local rule structure** that is the actual heart of the problem. As a Fomin growth diagram specialist, I must emphasize: growth diagrams succeed because **local vertex rules determine global bijections**—and KTW puzzles violate this principle catastrophically.

## The Fatal Local Rule Problem

Growth diagrams work when we have **local face labeling rules** of the form:
```
  a | b
  -----  →  face label f(a,b,c,d)
  c | d
```
where the face label f depends only on the four edge labels around it.

**KTW puzzles cannot support such local rules** because:
- Puzzle piece placement depends on **global boundary conditions**
- The "free nabla choices" interact through **non-local constraint propagation**
- A single incorrect local choice can invalidate the entire puzzle configuration

The reports miss that puzzle validity requires **global consistency checks** that cannot be encoded in local face labels.

## Why Migration is More Than Geometry

Report 2 correctly identifies migration as "geometrically necessary" but misses the deeper point: migration performs **jeu de taquin equivalence resolution**, which is inherently non-local. In growth diagrams, we need:

**Local Rule Property**: Each face label depends only on its immediate neighbors.

**Migration Reality**: Each rhombus move in migration can affect **arbitrarily distant** rhombi through jdt-equivalence chains.

This non-locality makes migration incompatible with any growth diagram structure.

## The Cylindric Growth Diagram Alternative

However, there's a non-obvious connection the reports missed: **cylindric growth diagrams** might apply here. In cylindric constructions:
- We work on infinite strips with periodic boundary conditions
- Local rules can depend on "twisted" boundary data
- Non-local effects get encoded in the cylindric topology

**Conjecture Refinement**: KTW puzzles might admit cylindric growth diagrams where:
1. The triangular puzzle is "unwrapped" onto a cylindric strip
2. Boundary conditions become periodic constraints
3. Migration effects get absorbed into the cylindric local rules

## Critical Gap in Computational Analysis

Report 4 proposes testing "constraint signatures" and "state space dimensions," but misses the crucial experiment:

**Test the Local Rule Failure Directly**: For each puzzle vertex, attempt to define face labels based only on immediately adjacent data. The failure rate will quantify why direct growth diagrams are impossible.

This is more fundamental than dimension counting—it tests whether the basic growth diagram setup can even begin.

## Face Labels vs. Recording Tableaux

The reports conflate **face labels encoding tableau data** with **face labels encoding local vertex weights**. In proper growth diagrams:
- Face labels record **insertion data** (like recording tableaux in RSK)
- They don't directly store final tableau entries
- The bijection emerges from the **path structure** through the growth diagram

For KTW puzzles, any face labels would need to encode:
- Current partial puzzle state
- Boundary condition compatibility
- **Future constraint implications**

This forward-looking requirement violates the local rule principle.

## The Branching Choice Obstruction

The problem statement mentions "KTW puzzle branching choices," but this reveals a fundamental misunderstanding. In proper growth diagrams:
- "Choices" correspond to **different paths** through the diagram
- Each path encodes one bijection instance
- Local rules ensure path consistency

KTW puzzle "choices" are **constraint satisfaction degrees of freedom**, not bijection paths. The migration algorithm doesn't follow these choices—it **resolves** them through global optimization.

## Alternative Framework: Quasi-Local Growth Diagrams

Instead of abandoning the growth diagram approach entirely, consider **quasi-local extensions**:

1. **Multi-scale Face Labels**: Face labels that encode not just local data, but "constraint horizons" extending beyond immediate neighbors
2. **Delayed Resolution Rules**: Local rules that can output "pending constraints" that get resolved in later faces
3. **Constraint Graph Embeddings**: Embed the puzzle constraint graph directly into the growth diagram structure

## The Real Question: Recording Data Structure

The fundamental question isn't whether KTW puzzles form growth diagrams, but **what combinatorial data are the face labels recording?**

In RSK growth diagrams, face