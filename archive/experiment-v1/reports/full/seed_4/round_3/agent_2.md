# Vertex Model Analysis: Growth Diagram Conjecture - A Yang-Baxter Perspective

## The Reports Miss the Core Free-Fermion Structure

The three analyses, while identifying important obstacles, fundamentally misunderstand the underlying integrable structure. They treat KTW puzzles as purely combinatorial objects, ignoring that **Knutson-Tao puzzles are projections of a free-fermionic vertex model** (Zinn-Justin 2009). This isn't just a computational detail—it's the key to understanding why standard growth diagrams fail.

## The Real Issue: Projection from Vertex Configurations to Puzzles

The reports frame this as a "puzzle → tableau" bijection problem, but the actual structure is:

**Free-fermion vertex configurations** ↓ (rhombus projection) → **KTW puzzles** → **LR tableaux**

The "migration algorithm" isn't geometrically necessary (contra Report 2)—it's **undoing the information loss from the rhombus projection**. The vertex model has commuting transfer matrices T(u), T(v) with spectral parameters, but puzzles only see the **spectral-parameter-independent projection**.

## Challenge to the "Geometric Obstruction" Claim

Report 2's claim about C₃ rotational symmetry is incorrect. The vertex model has **full integrability** precisely because it preserves more structure than just C₃ symmetry. The correct symmetry is the **Yang-Baxter equation**:

R₁₂(u-v)R₁₃(u)R₂₃(v) = R₂₃(v)R₁₃(u)R₁₂(u-v)

This guarantees that transfer matrices T(u) commute: [T(u), T(v)] = 0. But puzzles lose the spectral parameters u,v, breaking integrability.

## The Free-Fermion Point is Crucial

The computational analysis (Report 3) misses that KTW puzzles correspond to the **free-fermion point** of the six-vertex model. At this point:
- Partition function has determinantal structure (Lindström-Gessel-Viennot)
- Transfer matrix eigenvalues are products of single-particle energies
- **BUT**: The puzzle boundary conditions are non-free-fermionic

This creates a fundamental mismatch. The interior vertex weights are free-fermionic, but boundary conditions impose **domain-wall constraints** that require the full interacting theory.

## Why "Migration" is Actually Yang-Baxter Evolution

The migration algorithm isn't arbitrary geometric reordering—it's **implementing the Yang-Baxter equation** to restore the lost spectral parameter information. Each "hexagonal flip" corresponds to:

```
R₁₂R₁₃R₂₃ → R₂₃R₁₃R₁₂
```

The algorithm succeeds because it's solving the **spectral parameter reconstruction problem**: given a puzzle (parameter-free projection), find the unique vertex configuration with spectral parameters that produces the correct LR tableau.

## The Growth Diagram Obstruction is Spectral

Report 1's "face label cardinality mismatch" has the right intuition but wrong cause. The issue isn't just exponential blow-up—it's that **growth diagrams cannot encode spectral parameters**.

Standard growth diagrams work for RSK because RSK corresponds to **free fermions with trivial spectral parameters**. Each insertion step has spectral parameter u = 0, so no parameter information needs encoding.

For KTW puzzles, the face labels would need to encode **non-trivial spectral parameter assignments**, which requires:
- Continuous parameter spaces (impossible for discrete face labels)
- Non-local parameter constraints (violating locality)
- Yang-Baxter consistency conditions (transcending local rules)

## Counterproposal: Spectral Growth Diagrams

Instead of seeking standard growth diagrams, consider **spectral-parameter-aware growth diagrams**:

1. **Face labels encode parameter intervals**: Each face tracks allowed spectral parameter ranges
2. **Transfer matrices act on parameter distributions**: Row operations update parameter constraints
3. **Final decoding**: Extract LR tableaux by solving the parameter constraint system

This respects the integrable structure while potentially maintaining tractability.

## The Non-Obvious Connection: Quantum Groups

None of the reports mention that LR coefficients are **structure