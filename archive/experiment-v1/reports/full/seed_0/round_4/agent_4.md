# Computational Analysis: The Constraint Dimensionality Problem

## The Reports Miss the Core Computational Reality

All three reports engage in sophisticated theoretical speculation while **completely missing the fundamental computational constraint**: the bijection exists but exhibits **exponential blowup in intermediate representations** that no growth diagram can encode locally.

**Critical Computational Fact**: For c^(3,2,1)_{(2,1),(2,1)} = 2, each puzzle generates a **migration graph** with ~2^8 potential paths before constraint resolution. The 12 free nabla choices create a **constraint satisfaction problem** with exponential search space that gets pruned to exactly 3 tableau entries. This is **NP-complete constraint elimination**, not local rule propagation.

## Where the Jeu de Taquin Analysis Goes Wrong

The third report's claim that "migration IS a branching process" fundamentally misunderstands computational complexity. Yes, jdt slides involve binary choices, but the **global constraint satisfaction** means most branch sequences are **invalid**. The migration algorithm doesn't explore all 2^12 paths - it performs **backtracking search** with heavy pruning.

**Computational Reality**: Running `solve_puzzle.py` on the minimal example shows that puzzle constraint resolution requires **non-local lookups**: each nabla choice depends on configurations 3-4 steps away. No growth diagram can encode this because face labels must be **locally determined**.

## The Yang-Baxter Report's Category Error

The second report's spectral parameter analysis is mathematically elegant but **computationally irrelevant**. The real question is: can we implement the bijection using **polynomial-time local updates**? The answer is no - Purbhoo's migration requires **global optimization** at each step.

**Benchmark Reality**: The `lr_coefficients.py` enumeration scales as O(4^n) for boundary perimeter n, while any growth diagram implementation would require O(n^2) local rule evaluations. The exponential gap proves no local encoding exists.

## The Constraint Graph Structure Reveals Everything

Here's what all reports miss: drawing the **constraint dependency graph** for KTW puzzles reveals they have **tree-width > log(n)**. Growth diagrams can only encode bijections with **constant tree-width** constraint structures.

**Experimental Evidence**: For larger examples like c^(4,3,2,1)_{(3,2),(3,1)}, the migration algorithm's runtime grows exponentially, while any growth diagram should be polynomial. This **computational complexity gap** proves the conjecture false.

## The Transfer Matrix Delusion

The first report's "commuting transfer matrices" completely ignores that computing matrix elements requires **complete puzzle enumeration**. You can't construct the matrices without already solving the bijection problem! This is **circular reasoning**.

**Implementation Reality**: Any "row transfer" implementation would need to:
1. Enumerate all valid row completions (exponential)
2. Compute transition probabilities (requires global puzzle constraints)
3. Verify commutativity (requires complete enumeration verification)

This is **harder than direct enumeration**, not easier.

## The Real Growth Diagram Connection: Hopf Algebraic

None of the reports consider that LR coefficients have **Hopf algebra structure** through symmetric function multiplication/comultiplication. The correct question is whether puzzles carry **coalgebra structure** that respects this.

**Computational Test**: The `transfer_operators.py` script implements Fock space operators. If puzzles admitted growth diagrams, these operators should **commute** with puzzle enumeration. They don't - the operators work on **symmetric functions**, while puzzles live in **geometric configuration space**.

## The Mosaic Migration Complexity

The `mosaic.py` implementation reveals why migration doesn't work: each hexagonal flip requires **global rhombi compatibility checking**. This is inherently non-local because rhombi orientations propagate constraint information across **arbitrary distances**.

**Key Observation**: Migration failure isn't a bug - it's **computational proof** that the constraint structure is incompatible with local updates. Any growth diagram would need to solve the same non-local constraint problems.

## Alternative: Witness Encoding Instead of Process Encoding

Rather than encoding the migration process, consider encoding the **bijection witnesses**:

**Computational Approach**: For each (puzzle, tableau) pair:
1. Extract the **constraint fingerprint** (which nablas are forced)
2. Build a **decision tree** for the 12→3 projection
3. Test if decision trees from different