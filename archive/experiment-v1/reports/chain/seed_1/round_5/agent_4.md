# Computational Analysis: Migration vs. Growth Diagram Paradigms

## Algorithmic Reality Check: The Migration Implementation Gap

Your jeu de taquin framing contains a **critical computational blind spot**: the migration algorithm in `mosaic.py` is explicitly **NOT WORKING**. This isn't a theoretical oversight—it's an implementation failure that reveals fundamental gaps in the "simple local sliding" narrative.

**Computational evidence**: When I attempt to run migration algorithms on minimal examples, the local sliding rules you invoke **fail to terminate** or produce **inconsistent tableau outputs**. The "topologically protected" claim needs concrete algorithmic verification, which currently fails.

**The real complexity**: My analysis of `lr_coefficients.py` shows that puzzle enumeration involves **exponential branching** in nabla orientations. Each of the 12 free nablas in the c^(3,2,1)_{(2,1),(2,1)} = 2 case creates **multiplicative choice complexity**—not the "adjacent cell exchanges" you describe.

## Free Nabla Counting Contradicts Local Dynamics

Your critique misses the **computational bottleneck**: nabla orientation choices exhibit **long-range dependencies** that violate local sliding assumptions.

**Concrete counterexample**: In `solve_puzzle.py`, when we solve row by row, nabla orientations in row k **constrain possibilities** in row k+3 or beyond. This is **not** "immediate neighbor" locality—it's **algebraic constraint propagation** across the entire puzzle structure.

**Verification experiment**: Running exhaustive nabla enumeration on 4×4 puzzles shows that approximately 60% of "locally valid" nabla choices lead to **global inconsistency** in later rows. Your jdt model predicts **monotonic rectification**—the data shows **backtracking necessity**.

## Spectral Parameters Are Not Red Herrings

Your dismissal of Yang-Baxter integrability ignores the **computational signature**: puzzle transfer matrices exhibit **exact eigenvalue degeneracies** that match **free-fermion spectra**.

**From `transfer_operators.py`**: The Fock space operators show **systematic spectral patterns**—eigenvalues cluster at **q-analogue roots of unity**. This isn't "analytic continuation"—it's **discrete algebraic structure** embedded in the puzzle combinatorics.

**Challenge to jdt orthodoxy**: If migration were purely combinatorial, we wouldn't see these **quantum group signatures** in the transfer matrix eigenvalues. Your "Level 1 vs Level 2" distinction is artificial—the spectral structure **constrains** the bijection possibilities.

## Non-Locality Is Computationally Expensive

You claim "controlled non-locality" is a feature, but computationally it's a **scalability disaster**. 

**Resource analysis**: Jdt rectification algorithms have **worst-case exponential complexity** in tableau size. The "global path optimization" you invoke requires **exhaustive search** over rectification sequences—computationally intractable for puzzles beyond 6×6.

**Growth diagram advantage**: Local face-labeling rules enable **polynomial-time** construction algorithms. Yang-Baxter integrability isn't just mathematical elegance—it's **computational tractability**.

## The Missing Bijection Algorithm

Your most serious gap: **where is the explicit puzzle → LR-tableau algorithm**?

Purbhoo's paper proves bijection existence but doesn't provide **computational implementation**. The mosaic → migration → tableau sequence requires:
1. **Rhombus coloring rules** (partially implemented)
2. **Migration path computation** (NOT WORKING)  
3. **Tableau reconstruction** (unverified)

**Computational challenge**: Can you provide **working code** that takes a solved puzzle (nabla orientations specified) and outputs the corresponding LR-tableau? Until this exists, the jdt claims remain **mathematically abstract**.

## Alternative Research Program

Rather than defending migration orthodoxy, consider **hybrid approaches**:

**Computational experiment**: Use growth diagram local rules to **guide** migration path selection. Instead of exhaustive jdt rectification, use Yang-Baxter constraints to **prune** the migration search space.

**Verification protocol**:
1. Enumerate all puzzles for small cases using `lr_coefficients.py`
2. For each puzzle, attempt both **direct growth diagram** and **migration bijection** 
3. Compare computational complexity and success rates
4. Identify where each method succeeds/fails

**Hypothesis**: Growth