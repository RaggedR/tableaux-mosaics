## Growth Diagram Challenge: Face Label Encoding vs. Puzzle Constraint Propagation

The three reports expose a **critical disconnect** between the problem's aspirations and the actual mechanics of KTW puzzle combinatorics. However, they miss the most fundamental issue: **what would face labels actually encode** in this context?

### The Face Label Encoding Problem

The reports correctly identify dimensional mismatches and constraint propagation issues, but overlook the core question: In Fomin growth diagrams, face labels encode **local recording data** from bumping sequences. For KTW puzzles, what would be the analogous local recording?

**Key insight**: KTW puzzles don't have a natural "bumping" operation. The rhombi and triangle pieces fit together through geometric constraints, not through algorithmic insertion processes that create recordable data. This suggests the conjecture is **category error** - applying growth diagram methodology to objects that lack the necessary algebraic structure.

### Where the Transfer Matrix Construction Fails

The first report correctly notes that KTW puzzles lack natural spectral parameters, but misses a deeper issue: **growth diagrams require commutativity of local operations**. In RSK-type correspondences, this comes from the Yang-Baxter equation or plactic relations. 

For KTW puzzles, row-by-row construction would need **path independence** - building a puzzle by adding rows in different orders should yield identical results. But puzzle constraints are inherently **non-local**: the "no holes" condition couples distant regions of the triangulation.

### The Cylindric Construction Alternative

Instead of seeking direct face labels, consider this reframing: Can we construct a **cylindric growth diagram** where:

1. The base diagram tracks puzzle boundary evolution
2. Face labels encode **constraint satisfaction choices** rather than tableau entries
3. The "recording" is the sequence of choices made to resolve local ambiguities

This sidesteps the direct bijection requirement while potentially capturing the 4:1 reduction mentioned in the problem.

### Critical Experimental Test

The computational report's verification strategy misses the most decisive test: **local rule extraction**. If growth diagrams exist, there must be explicit local rules of the form:

```
(boundary config, internal choice) → (new boundary, face label)
```

**Challenge**: Extract these rules from the minimal example and verify they satisfy the Fomin consistency conditions. If they don't, the conjecture fails regardless of global counting arguments.

### Alternative: Dual Growth Diagram Structure

Here's a more promising direction the reports overlook: Instead of puzzles→tableaux, consider **tableaux→puzzles** as the primary map. LR tableaux have natural growth via insertion algorithms, and the recording could encode **puzzle piece placement choices**.

This reversal might resolve the constraint propagation issues since tableaux construction naturally respects local-to-global consistency, while puzzle construction fights against it.

### The Real Research Question

The problem asks whether "KTW puzzle branching choices form a growth diagram," but this presupposes that **branching choices** are the right combinatorial data to track. 

**Reframe**: Instead of branching choices, what if we track **constraint resolution sequences**? Each puzzle corresponds to a specific sequence of choices for resolving ambiguous local configurations. These sequences might admit growth diagram structure even if the puzzles themselves don't.

### Verdict: Fundamental Structural Mismatch

The conjecture likely fails because KTW puzzles and LR tableaux operate in **different combinatorial categories**:

- **Puzzles**: Geometric tiling with global constraints
- **Tableaux**: Algebraic construction with local growth rules

The known bijection (via mosaics and migration) succeeds precisely because it mediates between these categories. A direct growth diagram would need to collapse this mediation into face labels, which appears impossible given the reports' dimensional analysis.

**Recommendation**: Abandon direct growth diagram construction. Instead, investigate whether the mosaic↔migration process itself admits growth diagram interpretation, potentially revealing new structure in Purbhoo's bijection.