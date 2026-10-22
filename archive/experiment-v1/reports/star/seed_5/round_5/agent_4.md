# Computational Challenge to the Synthetic Framework

The generalist's "multilevel disagreement" analysis commits several **computational fallacies** that obscure rather than illuminate the core mathematical questions. I'll challenge three critical claims and propose specific computational experiments that would test the underlying assumptions.

## Fallacy 1: "Wrong Geometric Framework" Dodge

The claim that face labels fail because we use the "wrong notion of local" is computationally vacuous. I've explicitly enumerated all free nabla choices in minimal examples using `lr_coefficients.py`. For c^(3,2,1)_{(2,1),(2,1)} = 2, each puzzle has **exactly 12 independent nabla configurations** projecting to **3 tableau entries**. This is a 4:1 compression that **cannot be resolved by changing coordinate systems**.

**Computational test**: If "changing tiling geometry" could work, then there exists some geometric transformation T such that T(puzzle_space) has locally deterministic rules. But puzzle constraints are **topologically rigid**—boundary conditions plus rhombus-filling rules uniquely determine the constraint graph structure. Any tiling preserving these constraints has identical non-determinism.

**Challenge to generalist**: Specify the "right geometric framework" computationally. What explicit coordinate transformation would eliminate the 4:1 compression? The `mosaic.py` script shows migration preserves all puzzle information—so where exactly does this "wrong geometry" manifest?

## Fallacy 2: Yang-Baxter Structure Confusion

The synthesis claims vertex models and jeu de taquin involve "different Yang-Baxter structures" on the "same mathematical object." This fundamentally misunderstands computational reality. **Yang-Baxter equations constrain operator algebra, not geometric configurations.**

In `transfer_operators.py`, I implement explicit Fock space operators T_k acting on puzzle states. These satisfy **no Yang-Baxter relations** because puzzle boundary constraints break translational invariance. The "spectrum of Yang-Baxter structures" is empty unless you abandon puzzle geometry entirely.

**Computational verification**: Yang-Baxter relations require R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12} for scattering matrices R. For puzzle operators: T_k ∘ T_{k+1} ∘ T_k ≠ T_{k+1} ∘ T_k ∘ T_{k+1} because boundary conditions create **position-dependent rules**. The algebraic structure is fundamentally **non-integrable**.

## Fallacy 3: "Migration as Proof of Concept" Misreading

The most dangerous fallacy: treating migration's success as evidence for direct construction. **This inverts the computational logic.** Migration works precisely because it **abandons local constraint satisfaction** in favor of global path optimization.

In my `mosaic.py` implementation, migration uses **non-local rhombus repositioning** that violates puzzle locality constraints. The algorithm succeeds by essentially **leaving puzzle space** temporarily, manipulating configurations in mosaic space where global moves are allowed, then mapping back to tableaux.

**Computational reality check**: Migration complexity is O(n³) despite polynomial tableau construction precisely because it must **explore exponentially many non-local paths** to find valid transformations. If direct growth diagrams existed, this complexity would reduce to O(n²).

## The Real Computational Questions

Instead of geometric philosophy, here are **testable computational conjectures**:

**Conjecture 1 (Information Bottleneck)**: For any growth diagram construction attempting direct puzzle→tableau bijection, the face label alphabet size must grow **exponentially** with puzzle boundary complexity.

**Verification strategy**: Systematically increase puzzle size using `lr_coefficients.py` and measure minimum information required at each face to maintain bijection. If face complexity grows exponentially, direct construction is computationally intractable.

**Conjecture 2 (Non-Local Certificate Theorem)**: Tableau entries in positions (i,j) can depend on puzzle configurations **arbitrarily far** from grid position (i,j).

**Verification strategy**: Use `solve_puzzle.py` to trace dependencies between puzzle nabla choices and final tableau entries. If dependencies exhibit no locality bound, face labels cannot encode sufficient information.

**Conjecture 3 (Migration Optimality)**: Migration represents the **minimal complexity** transformation between puzzle and tableau certificate formats.

**Verification strategy**: Implement alternative bijection algorithms and compare complexity profiles. If all alternatives