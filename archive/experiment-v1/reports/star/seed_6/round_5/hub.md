# Synthesis Report: The Growth Diagram Question Reveals Deeper Structural Incompatibilities

## Primary Tension: Locality vs. Global Constraint Architecture

The core disagreement centers on **why** direct growth diagrams fail for KTW puzzles, revealing fundamentally different conceptions of mathematical structure:

- **Growth Diagram Specialist**: Claims over-constraint is backwards—RSK succeeds because of rigid local rules. The real obstruction is face label alphabet mismatch (|Λ|³ shape transitions vs. |Γ| tableau letters).

- **Vertex Model Specialist**: Argues the issue is absence of quantum group symmetry. KTW's geometric angle constraints don't lift to conserved charges in integrable systems.

- **Migration Specialist**: Identifies migration as "jeu de taquin in disguise" but emphasizes that canonicalization requires global path optimization, violating locality.

- **Computational Specialist**: Focuses on complexity classes—growth diagrams are O(n²) while KTW enumeration is #P-complete due to unbounded treewidth.

**My Assessment**: These perspectives are talking past each other. The **locality breakdown occurs at different structural levels**—information-theoretic (face labels), algebraic (symmetry breaking), algorithmic (path planning), and computational (constraint graph width). The question requires unified analysis across these domains.

## Common Thread: Information Flow Architecture

Despite disagreements, all specialists implicitly agree that **information propagation structure** distinguishes growth diagrams from migration. However, they locate the obstruction differently:

1. **Local Determinism**: Growth diagrams require face labels computable from corner data alone
2. **Global Consistency**: Migration requires backtracking and future path feasibility checks
3. **Algebraic Structure**: The compression must respect underlying symmetries (plactic, quantum group, or crystal)
4. **Computational Tractability**: The local rules must yield polynomial-time algorithms

**Critical Gap**: None address whether these requirements are **mathematically equivalent** or represent genuinely distinct obstructions.

## The Hexagonal Coordinate Fallacy

Three specialists (Growth, Migration, Computational) independently reject hexagonal reformulations but for different reasons:
- **Growth**: Hexagonal tilings lack canonical directed flow
- **Migration**: Migration operates on tiling patterns, not coordinate systems  
- **Computational**: Coordinate transformations don't commute with enumeration

**My Challenge**: This convergent rejection suggests a deeper issue. Perhaps the question itself reflects a **category error**—attempting to force KTW puzzles into a framework (growth diagrams) that assumes fundamentally different mathematical architecture.

## Missing Perspective: Reverse Engineering Success Cases

**Critical Omission**: All specialists focus on why direct growth diagrams fail, but none systematically analyze why Purbhoo's indirect bijection succeeds. The puzzle → mosaic → migration → tableau pathway works—what does this reveal about structural compatibility?

**Key Insight**: The Migration Specialist notes that puzzle → mosaic IS local (hence growth-diagram-compatible), while mosaic → migration requires global planning. This suggests:

**Alternative Framing**: Instead of seeking direct puzzle-tableau growth diagrams, ask whether **mosaic-tableau** growth diagrams exist. If mosaics encode the "right" geometric information for local tableau construction, the original question becomes: "Can we bypass migration's global optimization?"

## The Quantum Group vs. Complexity Theory Tension

The Vertex Model Specialist's emphasis on quantum group symmetry directly conflicts with the Computational Specialist's complexity analysis:

- **Vertex Model**: Failure due to broken U_q(gl_n) symmetry in geometric constraints
- **Computational**: Failure due to #P-completeness and unbounded treewidth

**My Synthesis**: These aren't contradictory—they're **different levels of the same obstruction**. Quantum group symmetries typically correspond to tractable constraint satisfaction problems. When geometric constraints break these symmetries, complexity explodes. The mathematical elegance and computational tractability are intrinsically linked.

## Information-Theoretic Redux: What Compression Actually Measures

The Growth Diagram Specialist correctly challenges the "11.5 → 1.6 bit" analysis as naive, but the Computational Specialist's statistical mechanics perspective suggests a deeper interpretation:

**Refined Question**: The bit compression measures **mutual information** between puzzle regions. If this information decays exponentially (like RSK), local encoding works. If it decays polynomially (like KTW), global encoding is required.

This connects to the Migration Specialist's observation about global path feas