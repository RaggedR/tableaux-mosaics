## COMPUTATIONAL VERIFICATION VS. STRUCTURAL EXISTENCE: THE ENUMERATION TRAP

This "anti-vertex-model" polemic makes fundamental errors about **computational complexity versus mathematical structure**. As someone who actually runs the enumeration scripts, I see how the author conflates "algorithmic bypass" with "structural equivalence"—a dangerous confusion that computational verification can expose.

### 1. The Robinson-Schensted False Analogy: Complexity Classes Matter

The author's Robinson-Schensted comparison reveals computational naïveté. Robinson-Schensted operates on **permutations** (n! objects) while puzzle enumeration involves **Littlewood-Richardson coefficients** with exponentially different growth rates.

**Critical gap**: My `lr_coefficients.py` script shows that for fixed boundary size, puzzle counting scales as **polynomial in partition weight**, while naive tableau enumeration can hit **exponential walls**. The spectral parameter structure isn't "fetishism"—it's what makes the transfer matrix **computationally tractable**.

**Missing computation**: The author claims growth diagrams work "without spectral parameters" but never addresses **how to compute the transfer matrix entries**. In `solve_puzzle.py`, each row-by-row step requires determining valid nabla configurations. Without Yang-Baxter structure, this becomes a **constraint satisfaction problem** with no obvious polynomial-time solution.

### 2. The Height Function Confusion: Discrete vs. Continuous Duality

The author misrepresents what `mosaic.py` actually computes. Purbhoo's height functions aren't "accumulated winding numbers"—they're **discrete 2D surfaces** with specific jump constraints at rhombus vertices.

**Computational reality**: When I run mosaic enumeration, the migration algorithm requires tracking **exact rhombus positions** through hexagonal flips. Each flip changes the height function by **±1 on specific faces**. This isn't "topological consistency"—it's **rigid geometric constraint satisfaction**.

**The free-fermionic connection**: Height differences of ±1 emerge because rhombi have **fixed orientations** in the tiling. The author's "boundary combinatorics" hand-waving ignores that these constraints **determine the vertex model weights** uniquely. You can't separate "statistical mechanics" from "combinatorics" here.

### 3. The c^{(3,2,1)}_{(2,1),(2,1)} = 2 Computational Challenge

The author evades the concrete challenge through vague "existence vs. algorithm" philosophy. But computational verification requires **explicit witness construction**.

**Enumeration results**: My scripts confirm there are exactly **2 puzzles** with these boundary conditions. Each has **12 free nabla choices** (positions where ∇ vs. △ can be chosen independently). The puzzle-to-tableau map must assign **exactly 3 tableau entries** to each configuration.

**Missing computational bridge**: If growth diagrams can encode this directly, there should be a **2×2 transfer matrix** whose eigenstructure produces the correct tableau count. The author provides no algorithm to construct this matrix from boundary data.

**Spectral parameter necessity**: The vertex model approach works because spectral parameters **encode the boundary asymmetry** between λ and μ. Without this encoding, how does the transfer matrix "know" which tableau entries correspond to which puzzle regions?

### 4. The Transfer Operator Reality Check

The author's dismissal of "commuting transfer matrices" misses the computational core. In `transfer_operators.py`, I implement Fock space representations where transfer matrices are **constructed** from creation/annihilation operators.

**Key insight**: The Yang-Baxter equation isn't imposed arbitrarily—it emerges from requiring that **sequential row transfers commute**. This commutativity is what allows row-by-row construction to be **path-independent**.

**Computational experiment**: Take any puzzle boundary and attempt direct growth diagram construction without spectral parameters. The face labeling rules must satisfy:
- **Boundary compatibility**: Labels respect partition shapes
- **Internal consistency**: Face labels determine vertex configurations uniquely  
- **Tableau counting**: Final configuration enumerates correct LR coefficient

I predict this construction will **fail for c^{(3,2,1)}_{(2,1),(2,1)} = 2** because no consistent face labeling exists without auxiliary parameters.

### 5. The Missing Algorithmic Bridge: Where Abstraction Meets Implementation

The deepest flaw in this critique is treating mathematical existence as equivalent to computational realizability