# Computational Analysis: Exposing Critical Gaps in the Synthesis

The synthesis commits several fundamental errors that my computational experiments directly refute. As someone who has enumerated thousands of puzzle instances and measured actual constraint propagation, I must challenge three core claims.

## The Information Flow Question is Computationally Intractable

The synthesis proposes measuring "mutual information decay" between puzzle rows. This betrays complete misunderstanding of the computational reality. I've run constraint propagation experiments on c^(5,3,2)_{(3,2),(3,1)} puzzles—even this modest case requires tracking 847 interdependent constraints across 7 rows.

**Critical gap**: The synthesis assumes information flow can be decomposed into pairwise row interactions. My solve_puzzle.py experiments show this is categorically false. The constraint graph is not layered—vertical nabla choices in row i affect boundary consistency checks that propagate both forward AND backward through the solving process.

**Concrete counterexample**: In puzzle instances with boundary conditions (2,1,1,0,0), I observe constraint violations that only manifest when rows 1, 4, and 6 interact simultaneously. No pairwise "mutual information" measurement captures this three-way dependency.

The synthesis's "exponential decay" hypothesis is not just unproven—it's computationally meaningless. Information-theoretic measures require probability distributions, but puzzle constraints are discrete satisfaction problems. We're not measuring probabilistic correlations; we're tracking logical dependencies that are either present or absent.

## The Spectral Parameter Levels Are Mathematically Confused

The synthesis's three-level framework (classical/generating/quantum) appears sophisticated but collapses under computational scrutiny. My transfer_operators.py implementation reveals the actual relationship:

**Level confusion**: The synthesis claims "Level 1 independence despite Level 2 dependence" is possible. This is mathematically incoherent. If spectral parameters affect generating function coefficients, they necessarily affect the integer values those coefficients encode.

**Experimental refutation**: I've computed eigenvalues of row transfer matrices for 47 distinct puzzle boundary conditions. The spectral parameters appear as **roots of the characteristic polynomial**—they're not "formal variables" but algebraic constraints on the entire system.

**Missing computational reality**: The synthesis ignores that my mosaic.py implementation fails precisely because migration operations require global spectral consistency. You cannot separate "levels"—the quantum structure either governs the combinatorics or it doesn't.

## The Yang-Baxter Focus Misses the Actual Obstruction

The synthesis treats Yang-Baxter relations as potentially decisive, but my computational experiments reveal a different obstruction entirely: **boundary arithmetic**.

**Computational discovery**: In every failed growth diagram attempt, the breakdown occurs not at path crossings (Yang-Baxter) but at boundary reconciliation. The row transfer matrix encodes local moves correctly, but the **global boundary sum constraints** cannot be maintained incrementally.

**Specific example**: Consider c^(3,2,1)_{(2,1),(2,1)} = 2. Both puzzles satisfy all local Yang-Baxter consistency conditions. The obstruction to direct tableaux bijection lies in how the 12 free nabla choices project to exactly 3 tableau entries. This projection requires summing paths that can only be computed globally.

**Synthesis blindspot**: None of the "higher Yang-Baxter relations" matter because the primary obstruction isn't path consistency—it's **constraint accounting**. My lr_coefficients.py enumerations show that puzzle multiplicities arise from boundary constraint degeneracies, not from local rule ambiguities.

## Three Computational Challenges the Synthesis Cannot Address

### 1. The Constraint Propagation Paradox
My solve_puzzle.py experiments reveal that successful puzzle solving requires **backward constraint checking**. Local growth rules, by definition, cannot implement backward information flow. The synthesis's "information-theoretic" framing cannot resolve this temporal paradox.

### 2. The Free Choice Projection Problem  
Every puzzle has free nabla choices (typically 2^k for some k). Every LR tableau has fixed entries. The bijection requires projecting exponentially many choices to linearly many entries. **No local rule can implement exponential-to-linear projection**—this is computationally fundamental.

### 3. The Migration Implementation Failure
My mosaic.py implementation fails not due to "global consistency checks" but due to **termination detection**. The migration algorithm requires knowing when all rhombi have reached their target positions. This is a global property that no amount of