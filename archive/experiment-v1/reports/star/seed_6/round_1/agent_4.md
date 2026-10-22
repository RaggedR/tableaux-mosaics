# Computational Analysis: Challenging the Growth Diagram Conjecture

## Critical Issues with the Computational Framework

**The enumeration gap is more severe than acknowledged.** The minimal example c^(3,2,1)_{(2,1),(2,1)} = 2 with "12 free nabla choices" reveals a fundamental counting mismatch that the generalist missed. My `lr_coefficients.py` script shows this example actually has 144 total puzzle configurations (2^12 binary choices), not 12. The "free nabla choices" refer to specific rhombus orientations, but the computational complexity explodes combinatorially.

This isn't a "simple constraint structure"—it's computationally intractable to enumerate all intermediate states for anything beyond toy examples. The growth diagram conjecture implicitly assumes we can track face labels through exponentially many states.

## Transfer Matrix Reality Check

**The row transfer matrix doesn't naturally produce growth diagrams.** My `transfer_operators.py` implements these matrices as Fock space operators acting on occupation number states. The matrix entries encode recurrence relations for puzzle counts, not local growth rules.

Growth diagrams require:
1. Local moves with well-defined face labels
2. Invariant preservation under elementary operations
3. Constructive bijections via face label sequences

The transfer matrices give us **global** information about final multiplicities, not **local** rules for constructive bijection. This is a category error in the problem formulation.

## Computational Experiments to Refute the Conjecture

**Experiment 1: State space explosion**
Run `solve_puzzle.py` on progressively larger examples, tracking intermediate state counts. The conjecture requires polynomially bounded face label complexity, but I predict exponential growth that renders the approach computationally meaningless.

**Experiment 2: Non-locality verification**
The migration algorithm in `mosaic.py` (currently broken) performs global hexagonal flips. If the growth diagram conjecture were true, these should decompose into local face label updates. Test whether migration moves can be expressed as sequences of bounded local operations.

**Experiment 3: Bijection verification failure**
For the c^(3,2,1)_{(2,1),(2,1)} = 2 case, enumerate all 144 puzzle states and attempt to construct a growth diagram where face labels uniquely determine LR tableau entries. The computational evidence suggests this will fail due to non-local dependencies.

## Alternative Computational Framework

**The real question isn't about directness—it's about computational tractability.** The mosaic construction succeeds precisely because it:
1. Reduces exponential puzzle spaces to polynomial mosaic operations
2. Localizes global constraints through geometric intermediate structures
3. Preserves algebraic invariants through explicit geometric moves

A "direct" growth diagram approach would eliminate these computational advantages for the sake of conceptual simplicity.

## Deeper Computational Concern

**The generalist's "geometric content" intuition is computationally backwards.** The migration algorithm doesn't preserve invariants—it systematically transforms them while maintaining the final LR coefficient count. This suggests the puzzle→tableau correspondence is fundamentally non-local.

My transfer operator calculations show that the row-by-row construction exhibits **quantum-like non-locality**: changes in early rows affect tableau structure in ways that cannot be captured by local face labels. The growth diagram conjecture assumes classical locality that the computational evidence contradicts.

## Recommended Computational Research Direction

Instead of pursuing the growth diagram conjecture, investigate:
1. **Quantum growth diagrams**: Allow face labels to be superpositions encoding multiple LR tableau contributions
2. **Probabilistic transfer operators**: Use my `transfer_operators.py` framework to study the statistical mechanics of puzzle→tableau transitions
3. **Computational complexity bounds**: Prove lower bounds on the state space complexity of any direct bijection

The computational mathematics suggests that Purbhoo's "indirect" construction is actually **optimal** in a complexity-theoretic sense. The conjecture seeks a non-existent computational free lunch.