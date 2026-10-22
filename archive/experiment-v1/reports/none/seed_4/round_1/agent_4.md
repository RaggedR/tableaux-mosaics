# Computational Analysis: Transfer Matrix vs Growth Diagram Bijection

## Gap Analysis and Alternative Framings

The problem statement contains a critical **conceptual gap**: it conflates the row transfer matrix (a computational tool for enumerating puzzles) with growth diagrams (geometric objects encoding bijective correspondences). These are fundamentally different mathematical structures, and the proposed "direct route" may not exist in the assumed form.

## Computational Challenges with the Proposed Framework

**1. Dimensional Mismatch Problem**
The example c^(3,2,1)_{(2,1),(2,1)} = 2 reveals a structural issue:
- 2 distinct puzzles
- 24 total free nabla choices (12 per puzzle)  
- 6 total LR tableau entries (3 per tableau)

A "direct" face-labeling bijection requires each growth diagram face to encode exactly one tableau entry. But the 4:1 ratio (nabla choices : tableau entries) suggests the relationship is inherently non-bijective at the local level.

**2. Non-Locality of LR Tableau Construction**
LR tableaux satisfy global constraints (increasing rows, weakly increasing columns, lattice word property). The row-by-row transfer matrix construction is inherently local. How can local face labels encode global tableau properties without essentially reconstructing the migration algorithm?

## Alternative Computational Framework

Instead of seeking a direct bijection, I propose investigating a **weighted growth diagram** where:
- Face weights equal the number of compatible nabla configurations
- Vertex labels track partial tableau states
- Edge multiplicities encode constraint propagation

This reframes the question: "Can we construct a growth diagram whose weighted faces give a generating function for LR tableaux?"

## Critical Computational Experiments

**Experiment 1: Transfer Matrix Spectrum Analysis**
For the (3,2,1) case, compute eigenvalues/eigenvectors of the 3×3 row transfer matrices T₁, T₂. If face labels correspond to tableau entries, the spectral data should encode tableau combinatorics.

**Experiment 2: Nabla Configuration Clustering** 
For each puzzle, partition the 12 nabla choices by their induced partial tableau structure. If clustering patterns are consistent across puzzles, this suggests hidden tableau-encoding structure.

**Experiment 3: Growth Path Enumeration**
Enumerate all possible growth paths in a hypothetical 3×3 growth diagram for this case. Count paths compatible with each LR tableau. Non-uniform distributions would indicate the direct bijection fails.

## Connection to Mosaic Migration Algorithm

The migration algorithm's success suggests the puzzle→tableau bijection requires **topological surgery** (hexagonal flips), not just combinatorial relabeling. This indicates the transfer matrix approach may be fundamentally insufficient.

**Conjecture**: Any growth diagram bijection must encode migration-equivalent operations, making it no simpler than Purbhoo's indirect route.

## Computational Verification Strategy

1. **Implement weighted growth diagrams** for small cases
2. **Compare computational complexity** of direct vs. indirect approaches  
3. **Test whether face-labeling preserves puzzle symmetries** (commutativity/associativity)
4. **Verify if local growth rules can enforce global LR constraints**

The core issue: growth diagrams excel at bijections between locally-constrained objects. LR tableaux have global constraints that may require non-local operations, potentially making the "direct" approach computationally intractable.

**Prediction**: The minimal example will reveal that face labels cannot simultaneously encode puzzle configurations and tableau entries without reconstructing the migration algorithm's topological complexity.