# Critical Analysis: Spectral Parameters and the Degeneracy Problem

## What I Missed: The Fundamental Mismatch

My previous analysis focused on free-fermionic constraints but **missed the core issue**: I assumed KTW puzzles naturally fit into Yang-Baxter integrability, when they actually represent a **discrete optimization problem** masquerading as a vertex model.

The "12 free nabla choices → 3 tableau entries" isn't gauge freedom—it's **overcounting**. Each puzzle configuration has internal degrees of freedom that don't affect the boundary data, creating artificial degeneracy that has nothing to do with transfer matrix eigenspaces.

## The Spectral Parameter Trap

I incorrectly suggested that spectral parameters u,v are missing. But KTW puzzles are **combinatorial**, not quantum mechanical. The commutativity [T(u), T(v)] = 0 comes from **inhomogeneous** vertex models where each column has different spectral weights. 

For growth diagrams, we need **homogeneous** transfer matrices where all vertices in a row have identical weights. The spectral parameter becomes a **generating function variable**, not a physical parameter enabling integrability.

## What Should Be Explored Next: The Bijection Bottleneck

The real question isn't whether transfer matrices work, but whether the **bijection is constructive**. Purbhoo's migration uses:

1. **Hexagonal flips** (local moves on mosaics)
2. **Global consistency** (ensuring moves don't conflict)
3. **Termination** (reaching canonical tableau form)

This is fundamentally different from transfer matrix eigenvalue problems. The migration algorithm is more like **chip-firing** or **sandpile models**—discrete dynamical systems, not quantum integrable ones.

## The Missing Link: Boundary Conditions

I overlooked that growth diagrams require **specific boundary conditions** that encode the initial partition data. For KTW puzzles:
- Boundary edges fix the outer partitions λ, μ, ν
- Interior face labels should track tableau entries
- Transfer matrix should preserve partition constraints

But KTW boundary conditions are **triangular**, not rectangular. Standard transfer matrices act on **rectangular domains** with periodic or domain-wall boundaries.

## Alternative Hypothesis: Non-Commutative Structure

Perhaps the obstruction is deeper: KTW puzzles might correspond to **non-commutative** transfer matrices where [T₁, T₂] ≠ 0. This would explain why direct growth diagrams fail—the row-by-row construction isn't consistent.

The Purbhoo bijection works precisely because it **bypasses** this non-commutativity through the mosaic intermediate step, which restores some form of local consistency.

## Next Investigation: R-Matrix Deformation

The crucial test: Can we find an R-matrix R(λ,μ,ν) that:
1. Reduces to KTW weights at special values
2. Satisfies Yang-Baxter equation R₁₂R₁₃R₂₃ = R₂₃R₁₃R₁₂
3. Generates commuting transfer matrices

If yes, then growth diagrams exist but require **deformation** away from the combinatorial KTW point. If no, then the problem is fundamentally ill-posed, and Purbhoo's indirect route is the only viable bijection.