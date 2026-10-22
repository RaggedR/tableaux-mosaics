# Growth Diagram Specialist Analysis: The Synthesis Misses the Local Rule Crisis

## CRITICAL CHALLENGE: The Synthesis Conflates Geometry with Combinatorics

The synthesis makes a fundamental error by treating "triangular geometry" as the primary obstruction. This misunderstands what growth diagrams actually encode. Growth diagrams are **not about geometric shapes** - they're about **local consistency of combinatorial moves**. The Fomin construction works perfectly fine on triangular regions when proper local rules exist.

Consider the standard RSK correspondence: we have a growth diagram on a rectangular grid, but each face encodes **local insertion/deletion operations** that depend only on the four adjacent edge labels. The geometry is irrelevant - what matters is that we can define consistent local rules.

## THE REAL PROBLEM: Face Label Semantics Are Fundamentally Wrong

The synthesis completely ignores the core issue: **what would face labels even mean in a KTW growth diagram?**

In RSK growth diagrams:
- Edge labels = partial tableaux shapes  
- Face labels = letters being inserted
- Local rule = RSK insertion algorithm

For KTW puzzles, the proposed correspondence would need:
- Edge labels = ??? (partial puzzle configurations?)
- Face labels = ??? (nabla orientations? rhombus colorings?)
- Local rule = ??? (hexagonal constraint satisfaction?)

**FUNDAMENTAL GAP**: The synthesis assumes face labels could encode "LR tableau entries directly," but this reveals a deep misunderstanding. Face labels in growth diagrams encode **the combinatorial data being processed**, not the final output. They're the input letters in RSK, not the tableau entries.

## MIGRATION IS NOT JEU DE TAQUIN - IT'S CONSTRAINT PROPAGATION

The tableaux specialist's jeu de taquin analogy is seductive but wrong. Jeu de taquin preserves **shape invariants** while changing **content locally**. Purbhoo's migration does something entirely different: it propagates **global boundary constraints** through local hexagonal moves.

The key insight the synthesis misses: migration doesn't just translate between "constraint languages" - it **resolves constraint conflicts** that arise from the fundamental incompatibility between:
1. **Boundary encoding** (puzzles specify global boundary conditions)
2. **Sequential construction** (tableaux built by successive insertions)

Growth diagrams require these to be **locally compatible**. They're not.

## COUNTER-PROPOSAL: The Issue is Temporal vs. Spatial Encoding

The real obstruction isn't geometric or spectral - it's **temporal vs. spatial information encoding**:

**Tableaux**: Encode information **temporally** (reading order determines construction sequence)
**Puzzles**: Encode information **spatially** (boundary conditions determine global constraints)

Growth diagrams work when temporal and spatial encodings are **locally equivalent** - when you can recover the temporal sequence from spatial neighborhoods. This fails for KTW because:

- Puzzle boundary conditions create **action-at-a-distance** effects
- A single nabla choice near one boundary can force specific choices near opposite boundaries  
- No local rule can capture this global dependency

## EXPERIMENTAL REFUTATION OF THE SYNTHESIS

The synthesis proposes testing "constraint hierarchy hypothesis" by measuring constraint propagation distance. This fundamentally misunderstands the problem. 

**Counter-experiment**: Take the minimal case c^(2,1)_{(1),(2)} = 1. This has exactly one puzzle with 3 nabla choices. The synthesis predicts these should form a growth diagram since constraint distance is minimal.

**Reality check**: Even here, the nabla orientations don't decompose into independent local moves. The constraint that forces consistent rhombus colorings is **inherently global** - it's not about distance, it's about the fact that puzzle consistency requires solving a global matching problem.

## THE SPECTRAL PARAMETER IS A RED HERRING

The synthesis fixates on the vertex model theorist's "non-free-fermionic points" speculation. This misses the point entirely. The Yang-Baxter equation ensures **star-triangle relations** hold consistently. But KTW puzzles don't satisfy star-triangle relations in the first place - they satisfy **hexagonal matching constraints**.

These are categorically different types of local rules. Deforming the spectral parameter won't magically transform hexagonal matching into star-triangle moves.

## WHAT THE SYNTHESIS GETS RIGHT (ACCIDENTALLY)

The synthesis correctly identifies that some bijections require "intermediate constructions," but for the wrong reason. It's not