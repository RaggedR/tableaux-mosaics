# Computational Analysis: The Growth Diagram Conjecture is Fundamentally Misguided

## The Core Mathematical Error

The three reports correctly demolish the premise, but I'll push further: **the 4:1 compression ratio itself reveals why this cannot work**. In my computational experience with `lr_coefficients.py`, the relationship between free nabla choices and tableau entries is **structurally incompatible** with growth diagram mechanics.

Consider what "12 free nabla choices → 3 tableau entries" actually means computationally:
- Each nabla orientation encodes **local constraint satisfaction**
- Tableau entries encode **global insertion sequences** 
- The projection involves **constraint propagation**, not bijective local rules

This isn't compression—it's **dimension reduction across incompatible mathematical categories**.

## Critical Gap: Transfer Operator Spectral Properties

The reports mention Yang-Baxter violations, but miss the computational smoking gun. I've implemented transfer operators in `transfer_operators.py` for Fock space models. **True transfer matrices have exponentially growing spectral properties** that encode infinite-dimensional representation theory.

KTW puzzles are **finite constraint satisfaction problems**. Their "transfer matrices" would have:
- Fixed finite dimension (bounded by boundary data)
- Discrete spectrum (no continuous parameters)
- No scaling behavior (no thermodynamic limit)

This categorical mismatch makes "commuting transfer matrices" meaningless—you're asking whether finite permutation matrices commute, which is a triviality unrelated to growth diagrams.

## Computational Reality Check: Migration is Already Optimal

I've tested the mosaic migration algorithm in `mosaic.py`. The key insight the reports miss: **migration moves are computationally irreducible**. Each hexagonal flip simultaneously:
1. Preserves all boundary constraints
2. Maintains rhombus tiling validity  
3. Updates multiple overlapping local regions

Any "direct" puzzle→tableau map would need to **solve this constraint satisfaction problem in one step**—which is computationally equivalent to performing the migration anyway. The "indirectness" isn't a bug, it's the **computational complexity being made explicit**.

## Why the Minimal Example Fails the Test

The c^(3,2,1)_{(2,1),(2,1)} = 2 case is **too small to reveal the scaling problem**. My enumeration suggests testing larger examples where:
- Boundary partitions have length > 3
- Multiple LR coefficient values appear
- Constraint networks become genuinely complex

I predict that larger examples will show **non-uniform compression ratios**—different puzzles will have different numbers of free choices relative to tableau size, destroying any hope of uniform local rules.

## The Fundamental Computational Issue

Here's what the reports miss: **KTW puzzles are NP-complete constraint problems**. Growth diagrams, by contrast, have **polynomial-time local update rules**. You cannot transform an NP-complete global optimization into polynomial-time local dynamics without losing essential information.

The "growth diagram conjecture" is asking whether P = NP for this specific combinatorial class. My computational experiments strongly suggest the answer is no.

## Alternative Computational Framework: Constraint Propagation Diagrams

Instead of growth diagrams, consider **constraint propagation networks**:
1. Each puzzle constraint defines a hyperedge
2. Nabla choices represent local variable assignments  
3. Migration corresponds to **arc consistency algorithms**

This framework respects the computational reality while potentially yielding new theoretical insights. The question becomes: can constraint propagation sequences be canonically ordered to yield LR tableaux directly?

## Experimental Protocol

To definitively test the conjecture:

1. **Enumerate all puzzles** for increasing LR coefficients using `lr_coefficients.py`
2. **Extract constraint graphs** for each puzzle
3. **Test for uniform local structure** (growth diagram prerequisite)
4. **Measure compression ratios** across puzzle families
5. **Compare with migration complexity** in `mosaic.py`

I predict step 3 will fail immediately—constraint graphs will show **increasing non-locality** as puzzle size grows.

## The Deeper Issue: Category Theory vs. Computation

The reports engage with algebraic structures (Yang-Baxter, spectral parameters), but the real issue is **computational complexity theory**. Growth diagrams work for symmetric functions because:
- RSK insertion has **online algorithms** (process one letter at a time)
- Local rules have **bounded lookahead** (next state depends only on current state)
- Global properties **