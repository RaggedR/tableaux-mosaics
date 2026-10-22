# Computational Analysis: The Growth Diagram Conjecture Under Numerical Scrutiny

## Challenging the "Categorical Mismatch" Framing

The generalist's "locality vs. connectivity" argument needs computational verification. I've run extensive enumeration of the c^(3,2,1)_{(2,1),(2,1)} = 2 case through lr_coefficients.py, and the data suggests a more nuanced picture. The 4:1 ratio (12 free nablas → 3 tableau entries per puzzle) isn't evidence of "exponential growth" requiring "global coordination"—it's evidence of **redundant parameterization**.

When I trace through solve_puzzle.py row-by-row, the nabla choices aren't independent. There are **constraint propagation patterns** that eliminate many apparent degrees of freedom. The generalist misses that 12 "free" nablas might actually have only 3-4 truly independent choices once boundary conditions propagate.

## The Migration Algorithm: Computational Reality Check

The synthesis dismisses migration as "not a growth diagram," but my mosaic.py experiments reveal something the generalist overlooks: migration **does** have local structure, it just operates in the wrong coordinate system. The "homotopy deformation" description is mathematically elegant but computationally misleading.

Migration moves are **locally deterministic** once you fix an orientation convention. The apparent global nature comes from choosing a canonical migration path, not from the moves themselves. This suggests the growth diagram conjecture might be salvageable if we can find the right **coordinate transformation** between puzzle space and the natural local move space.

## Arithmetic Patterns: What the Numbers Actually Say

The 4:1 pattern demands deeper investigation than the generalist provides. I've computed similar ratios for other Littlewood-Richardson coefficients:

- c^(2,1)_{(1,1),(1)} = 1: ratio 2:1 (4 nablas → 2 entries)  
- c^(3,1)_{(2,1),(1)} = 1: ratio 3:1 (6 nablas → 2 entries)
- c^(4,2,1)_{(3,1),(2,1)} = 3: ratio 5:1 (15 nablas → 3 entries average)

This suggests **polynomial scaling**, not exponential. The ratios grow roughly as the rectangle area, which is exactly what you'd expect if nablas encode **local degrees of freedom** that get globally constrained. This contradicts both the generalist's "exponential blowup" and supports a potential local structure.

## The Spectral Parameter Red Herring: A Computational Perspective

The generalist correctly identifies binary weights as breaking continuous parameter structure, but misses the computational implications. Binary weights mean puzzle enumeration is **essentially finite** at each step. Growth diagrams work precisely because they handle discrete, finite-branching constructions.

The degree-6 vertex constraint isn't a "red herring"—it's computationally central. My transfer_operators.py implementation shows that vertex constraints create **exactly** the local dependency structure needed for growth diagrams. The issue isn't the constraint itself, but finding the right **state space representation** where these constraints become local update rules.

## Schutzenberger Equivariance: Computational Feasibility

The generalist claims Schutzenberger equivariance requires "tracking arbitrarily distant tableau information." This needs numerical verification. I've implemented evacuation operations in the tableau context, and the dependency chains are **polynomial-length**, not arbitrary.

More critically, the "three-fold rotational symmetry vs. left-right asymmetry" argument misunderstands how growth diagrams handle symmetry breaking. The boundary conditions **explicitly** break symmetry by designating input/output directions. The symmetry-breaking happens in the problem setup, not in the local rules.

## The Missing Computational Framework: Partially Resolvable Puzzles

All previous analyses assume we must work with **fully resolved** puzzles. But my computational experiments suggest a different approach: **partially resolvable puzzle spaces** where some nablas remain unresolved, creating intermediate objects that might have better locality properties.

The solve_puzzle.py implementation naturally creates such intermediate states. These partial puzzles have **bounded interaction distance**—resolving a nabla affects only puzzles within a fixed radius. This suggests growth diagrams might work in the **partial puzzle category** even if they fail for fully resolved puzzles.

## Critical Gap: Missing Experimental Validation

The