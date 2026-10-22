# Computational Mathematics Analysis: Exposing the Critical Gaps

## CHALLENGING THE COMPUTATIONAL EVIDENCE: Insufficient Testing Depth

The reports fundamentally misunderstand what constitutes rigorous computational verification. The claim that "nabla choices are correlated across rows" is based on **minimal test cases** (essentially just c^(3,2,1)_{(2,1),(2,1)} = 2). This is computationally inadequate for several reasons:

1. **Sample bias**: Testing only the smallest nontrivial case cannot distinguish between fundamental impossibility and implementation artifacts
2. **Missing systematic enumeration**: No report demonstrates exhaustive testing across parameter ranges
3. **Algorithmic confusion**: The "non-commuting transfer operators" could result from incorrect transfer matrix construction rather than fundamental impossibility

## CRITICAL GAP: The Enumeration-Verification Loop is Broken

From my computational perspective, the most glaring issue is that **none of the reports implement the basic verification pipeline**. Using the available scripts:

- `lr_coefficients.py` should enumerate ALL puzzles for systematic parameter ranges
- `solve_puzzle.py` should construct candidate transfer matrices for each enumerated case  
- The growth diagram hypothesis requires testing **commutativity patterns** across hundreds of cases, not cherry-picking failures

The reports substitute **theoretical speculation** for **systematic computation**. This is methodologically backwards.

## EXPOSING THE LOCALITY ASSUMPTION: False Dichotomy

The Fomin specialist's emphasis on "face labels determined by adjacent boundary values alone" creates a **false constraint**. Modern growth diagrams (particularly in crystal base theory) routinely use **extended neighborhoods** without losing bijective properties. Consider:

- **Affine crystal operators** depend on entire boundary sequences
- **Cylindric RSK** uses wraparound information  
- **Quantum crystal graphs** have non-local mutation rules

The question isn't whether KTW puzzles satisfy classical locality, but whether they admit **consistent extended-local rules**. This requires computational verification of specific **quasi-local** patterns, not theoretical impossibility arguments.

## VERTEX MODEL ANALYSIS: Missing the Computational Framework

The vertex model specialist correctly identifies Yang-Baxter structure but completely misses the **computational implementation challenge**. The RTT relations they cite:
```
R_{12}(u/v) T_1(u) T_2(v) = T_2(v) T_1(u) R_{12}(u/v)
```

This requires **systematic computation** of R-matrices from puzzle data, then **numerical verification** of RTT commutation. None of the reports attempt this. The computational scripts could be extended to:

1. Extract local R-matrix weights from puzzle configurations
2. Construct transfer operators from these weights
3. Test Yang-Baxter equations numerically across parameter families

## JDT PERSPECTIVE: Computational Complexity Red Herring

The jeu de taquin specialist claims migration has "polynomial complexity" while growth diagrams would require "exponential preprocessing." This is **computationally false**:

- **Migration complexity** is actually O(n³) in tableau size due to global constraint propagation
- **Growth diagram lookup tables** can be computed incrementally with O(n²) space
- **Modern dynamic programming** makes face label construction tractable

The complexity argument confuses **algorithmic implementation** with **mathematical structure**. A proper computational analysis would benchmark actual runtimes across systematic test cases.

## THE MISSING EXPERIMENT: Systematic Bijection Testing

Here's the crucial computational experiment **none of the reports propose**:

**Experiment Design**: For each Littlewood-Richardson coefficient c^λ_{μν} ≤ 10:
1. Enumerate all valid puzzles using `lr_coefficients.py`
2. For each puzzle, extract all free nabla choice patterns  
3. Construct candidate transfer matrices from these patterns
4. Test growth diagram properties: commutativity, Yang-Baxter, face label consistency
5. Compare with LR tableau enumeration from `solve_puzzle.py`

**Success Criterion**: Consistent face label assignment that reproduces LR multiplicities.

**Failure Analysis**: If face labels fail, determine whether failure is:
- **Systematic** (proving conjecture false)
- **Parameter-dependent** (suggesting modified conjecture)  
- **Implementation-dependent** (requiring algorithm refinement)

## DEEPER STRUCTURAL CHALLENGE: The Free Parameter Problem

All reports ignore the **fundamental counting question**: KTW puzzles with fixed boundary have **expon