# Analysis: KTW Puzzles and Growth Diagram Structure

## Critical Challenge to the Problem Framing

The problem assumes the "row transfer matrix" naturally defines a growth diagram, but this is **fundamentally problematic**. KTW puzzles are solved by propagating constraints through a triangular grid via local rules at vertices, not by row-wise operations that would generate a growth diagram's rectangular lattice structure.

## Core Technical Issues

### 1. **Geometric Mismatch**
- KTW puzzles live on triangular grids with rhombic faces
- Growth diagrams require rectangular lattices with corner interactions
- The "row transfer matrix" concept appears to artificially impose rectangular structure on inherently triangular combinatorics

### 2. **Local Rule Incompatibility** 
In growth diagrams, face labels arise from **corner interactions** - when paths cross at lattice points, the local rule determines how to label the four adjacent faces. KTW puzzles use **edge constraints** - nabla/lambda orientations are determined by requiring valid rhombi at faces.

These are categorically different: corner-driven vs. face-driven local rules.

### 3. **The Purbhoo Construction Reveals the Real Structure**
The puzzle → mosaic → migration → LR tableau path isn't "indirect" - it's **structurally necessary**. The migration algorithm (hexagonal flips moving rhombi) suggests the natural lattice structure is hexagonal, not rectangular. Growth diagrams work because RSK has natural rectangular geometry; KTW puzzles don't.

## Alternative Framework Proposal

Rather than forcing KTW into growth diagrams, consider **cylindric growth on hexagonal lattices**:

1. **Hexagonal Growth Diagrams**: Use 6-valent vertices instead of 4-valent
2. **Rhombic Face Labels**: Instead of corner labels, use face-centered rules
3. **Toric Boundary Conditions**: The cylindric aspect might naturally handle the puzzle's boundary constraints

## The Real Question

The fundamental issue isn't whether KTW branching choices "form a growth diagram" - they don't, by geometric necessity. The real question is:

**Can we develop a hexagonal analog of growth diagrams that captures the KTW → LR bijection directly?**

This would require:
- Extending Fomin's local rule theory to 6-valent vertices
- Developing face-label propagation rules for rhombic tilings  
- Understanding how puzzle boundary conditions translate to growth boundary data

## Minimal Example Analysis

For c^(3,2,1)_{(2,1),(2,1)} = 2, the "12 free nabla choices projecting to 3 tableau entries" suggests a 4:1 local multiplicity. This ratio might encode **jeu de taquin equivalence classes** rather than direct bijection data, supporting the necessity of Purbhoo's intermediate migration step.

**Conclusion**: The problem as stated conflates incompatible geometric structures. A solution requires fundamentally rethinking growth diagrams for triangular/hexagonal combinatorics.