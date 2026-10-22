# Synthesis Report: The Growth Diagram Question as a Fundamental Category Error

## The Core Mathematical Tension

The four specialists reveal a fascinating disagreement about **what kind of mathematical object** a growth diagram actually is. The growth diagram specialist treats them as "constraint resolution systems," the vertex model specialist views them as "quantum evolution operators," the tableaux specialist sees them as "rectification processes," and the computational specialist frames them as "information encoding mechanisms." 

**This isn't just terminology—it's a fundamental categorical confusion that exposes why this problem is hard.**

Each perspective is partially correct but incomplete. Growth diagrams ARE constraint resolution systems, but only for constraints that form **commutative algebraic structures** (as the vertex model specialist correctly notes about symmetric functions). They ARE information encoding mechanisms, but only when the encoding respects certain **locality principles** that the computational analysis shows KTW puzzles violate.

## The Information-Theoretic Core Insight

The computational specialist's 11.5 → 1.6 bit compression analysis is the most penetrating insight, but needs mathematical sharpening. The issue isn't raw information compression—RSK also has massive compression (n! permutations → two tableaux of size n). The issue is **how the information is structured**.

In RSK, the information loss occurs through **order statistics**—many permutations have the same increasing/decreasing subsequence structure. This admits local recording because order relationships are **transitive**: if a < b and b < c locally, then a < c globally.

KTW puzzles lose information through **geometric constraint satisfaction**, where constraints interact through **non-transitive angle relationships**. The 60°/120° rhombi constraints create global interdependencies that cannot be factored into local transitivity relations.

**Key insight**: Growth diagrams work precisely for combinatorial structures where global invariants factor into transitive local relations. KTW puzzles violate this factorization property.

## The Yang-Baxter Red Herring vs. Real Obstruction

The vertex model specialist's emphasis on spectral parameters misses the point, but their particle conservation insight is crucial. However, I challenge their conclusion: the obstruction isn't missing quantum symmetry—it's **excessive geometric rigidity**.

RSK succeeds because tableaux have **flexible growth rules**—multiple valid ways to extend a partial tableau. This flexibility allows local decision-making. KTW puzzles are **over-constrained**—the rhombi angles force unique completions once you specify enough boundary data.

This over-constraint is precisely what makes migration work: the geometric rigidity guides the hexagonal flips unambiguously. But it's also what makes growth diagrams impossible: there's no "choice" for face labels to encode.

## The Migration Algorithm as Proto-Growth Diagram

The tableaux specialist's insight about reverse-migration growth diagrams points to the real solution, but backwards. Instead of asking whether row-by-row growth can simulate migration, ask: **Can migration be reformulated as a growth process?**

Here's the key observation all specialists missed: Migration IS already a local process—but in **hexagonal coordinates**, not square coordinates. Each hexagonal flip is a local rule operating on a constant-radius neighborhood.

**Proposal**: The growth diagram exists, but not on the puzzle domain. It exists on the **dual hexagonal lattice** where migration operates. Face labels would encode rhombi orientations, and transitions would encode flip rules.

The challenge: translating this hexagonal growth diagram back to square coordinates for tableau readout. This is possible but requires the **coordinate transformation** that current approaches avoid.

## Extending the Computational Obstruction

The computational specialist's quantum growth diagram proposal is intriguing but problematic. Quantum superposition doesn't resolve the information bottleneck—it just delays the measurement. The exponential blowup occurs when you measure the quantum state, recovering the classical constraint satisfaction problem.

However, their observation about transfer operators having "quantum mechanical structure" deserves investigation. Not because quantum mechanics helps, but because it suggests the **wrong algebraic structure**. Transfer matrices assume **linear evolution**, but constraint satisfaction is fundamentally **Boolean**.

**Alternative framework**: Instead of quantum growth diagrams, consider **tropical growth diagrams** where face labels live in the tropical semiring (min,+). Boolean constraint satisfaction naturally lifts to tropical polynomial evaluation, potentially resolving the algebraic structure mismatch.

## The Deepest Gap: Boundary Condition Topology

All four specialists miss the most fundamental issue: **boundary condition topology**. Standard growth diagrams have **two-boundary** input (row and column), while KTW puzzles have **three-boundary**