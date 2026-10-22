# Mathematical Synthesis: Beyond the Local-Global Dichotomy

The four specialist reports reveal a deeper mathematical tension than initially apparent. While ostensibly about growth diagrams for KTW puzzles, the core dispute concerns **the nature of combinatorial equivalence itself**—when are different computational procedures counting the same mathematical objects?

## The Fundamental Categorical Error

All specialists commit a crucial error: they conflate **procedural locality** with **structural locality**. The growth diagram specialist argues puzzles resist local rules due to "global boundary constraints." The migration specialist counters that hexagonal flips are "purely local." Both miss the key distinction.

**Critical insight**: Locality in growth diagrams isn't about spatial neighborhoods—it's about **information flow**. A rule is local if the face label at position (i,j) depends only on labels at positions (i-1,j), (i,j-1), and the input letter. Whether this corresponds to "local geometric operations" is irrelevant.

The migration specialist's claim that "rhombus flips are local" is geometrically correct but informationally false. Each flip requires knowledge of the **entire rhombus configuration** to determine validity—this is global information, regardless of geometric locality.

## The Spectral Parameter False Dilemma

The vertex model specialist's quantum group framework and the computational specialist's eigenvalue analysis appear contradictory but actually address **different mathematical levels**:

- **Level 1**: Classical enumerative combinatorics (LR coefficients as integers)
- **Level 2**: Generating function algebra (spectral parameters as formal variables) 
- **Level 3**: Quantum integrable systems (parameters as physical observables)

**Resolution**: The growth diagram question lives at Level 1, but its answer may require Level 2 techniques. The computational specialist's numerical experiments test Level 1 independence, while the vertex model specialist's quantum group structure suggests Level 2 dependence. These aren't contradictory—they're testing different mathematical objects.

**Testable prediction**: If spectral parameters affect combinatorics only through **higher-order corrections** (terms that vanish when coefficients are integers), then Level 1 independence holds despite Level 2 dependence.

## The Yang-Baxter Misdirection Reveals Structural Depth

All specialists fixate on Yang-Baxter relations, but from opposite perspectives. The growth diagram specialist dismisses them as irrelevant to local rule existence. The vertex model specialist treats them as fundamental quantum group structure. The migration specialist ignores them entirely.

**Synthetic resolution**: Yang-Baxter relations are neither sufficient nor irrelevant—they're **necessary but not decisive**. Here's why:

1. **Necessity**: Any growth diagram implementation must satisfy Yang-Baxter-like consistency conditions where paths cross
2. **Insufficiency**: As the computational specialist notes, consistency doesn't guarantee correct enumeration
3. **Decidability**: The specific Yang-Baxter equation relevant to KTW puzzles can be computationally verified

**Missing perspective**: None of the specialists consider **higher Yang-Baxter relations**—consistency conditions involving more than two crossing paths. These may be the decisive obstruction.

## The Jeu de Taquin Reductionism Fails

The synthesis attempted to reduce the growth diagram question to jeu de taquin implementability. All specialists reject this reduction, but for different reasons:

- Growth diagram: "Jeu de taquin is irrelevant to face label existence"
- Migration: "Migration isn't jeu de taquin on tableaux"
- Computational: "Jeu de taquin requires global consistency checks"

**Correct framing**: The question isn't whether jeu de taquin can be implemented locally. It's whether the **inverse direction** of Purbhoo's bijection (tableau → mosaic → puzzle) can be implemented as local growth rules. This requires understanding how **tableau entries project to geometric constraints**.

## Three Unified Mathematical Questions

Synthesizing the specialists' perspectives, three precise questions emerge:

### 1. The Information Flow Question (Computational + Growth Diagram)
**Precise formulation**: In row-by-row puzzle construction, does the **mutual information** between row i and rows j > i+k decay exponentially in k?

**Why decisive**: This directly tests whether local rules can capture puzzle structure, using information-theoretic rather than geometric intuition.

**Testable**: The computational specialist's constraint propagation experiments directly measure this.

### 2. The Quantum Classical Correspondence Question (Vertex Model + Migration)
**