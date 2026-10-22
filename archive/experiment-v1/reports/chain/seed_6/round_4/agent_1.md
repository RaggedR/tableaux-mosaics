# The Critical Gap Between Growth Diagrams and Brute-Force Enumeration

**THE COMPUTATIONAL APPROACH MISSES THE FUNDAMENTAL STRUCTURAL QUESTION**

Your computational verification entirely sidesteps the core theoretical issue. The question isn't whether we can enumerate all puzzles for small cases—of course we can. The question is whether the **row transfer matrix construction** naturally gives rise to a Fomin-type growth diagram where face labels encode LR tableau data directly.

You've implemented `solve_puzzle.py` with "greedy constraint satisfaction," but this completely misses the point. The growth diagram framework asks: can we define **local rules** on a directed graph such that face labels propagate according to simple update rules, and the final configuration encodes the LR tableau? Your brute-force enumeration doesn't address whether such local rules exist.

Consider the minimal case c^(3,2,1)_{(2,1),(2,1)} = 2. You correctly note there are two puzzles, but the crucial question is: **can we construct a growth diagram where the 12 nabla choices at each position follow local update rules that directly track tableau entries?** Your computational approach doesn't even attempt this construction.

**THE MIGRATION ALGORITHM REVEALS WHY DIRECT BIJECTION FAILS**

Purbhoo's migration algorithm is precisely what's missing from your analysis. The fact that it requires **global hexagonal flips** through the entire mosaic demonstrates why a local growth diagram approach may be impossible.

In classical RSK growth diagrams, face labels update via purely local rules—each face depends only on its immediate neighbors. But puzzle-to-tableau correspondence requires **global coordination** through the migration process. Your observation about "cascade failures" and "global topology constraints" actually supports this: the inherent non-locality suggests growth diagram methods may be fundamentally inadequate.

**THE SPECTRAL PERSPECTIVE REVEALS DEEPER STRUCTURE**

Your dismissal of spectral analysis misses a crucial point about **transfer matrix eigenvalues in integrable systems**. The question isn't about random matrix spectra—it's about whether the puzzle transfer matrices exhibit the **integrability signatures** found in other RSK-related growth diagrams.

Fomin growth diagrams work precisely because the underlying algebraic structures (like Robinson-Schensted) have **commuting transfer matrices** with special spectral properties. If KTW puzzles lack this structure, it explains why no direct growth diagram bijection has been found despite 20+ years of research.

Your `transfer_operators.py` code computes eigenvalues, but do you test for **commutativity relations** between transfer matrices at different rows? Do the eigenspaces have the **nested structure** characteristic of integrable systems? These are the relevant spectral questions, not generic spectral gap analysis.

**THE BOUNDARY DATA ENCODING PROBLEM**

Here's the specific technical challenge your computational approach doesn't address: in Fomin growth diagrams, face labels must simultaneously encode **multiple pieces of information**—both the local constraint satisfaction and the global recording data.

For KTW puzzles, each face choice affects:
1. Local rhombus placement constraints
2. Global boundary condition satisfaction  
3. Tableau entry recording

Classical growth diagrams handle this through **carefully designed face label alphabets** where local rules automatically maintain global consistency. Your computational enumeration doesn't reveal whether such an alphabet exists for puzzles.

**THE NON-OBVIOUSNESS OF CYLINDRIC CONSTRUCTION**

The most intriguing aspect of your computational results is what they **don't** show. If puzzle branching naturally formed a growth diagram, we'd expect to see **cylindric periodicity** in the constraint structure—the ability to "wrap around" the puzzle boundary with consistent local rules.

Your implementation treats each puzzle row independently, but growth diagrams require **coherent global structure**. The failure to find direct bijections may reflect that puzzle constraints are genuinely **non-cylindric**—they can't be embedded in the periodic structure that makes growth diagrams work.

**THE REAL QUESTION: LOCAL VS GLOBAL ENCODING**

The fundamental issue isn't computational complexity—it's **information encoding locality**. Migration algorithms work by moving colored rhombi through global paths. This suggests the tableau information is **globally distributed** across the puzzle, not locally encodable in face labels.

If true, this explains why Purbhoo's bijection requires the intermediate mosaic construction: the global-to-local information transfer happens during migration, not during initial puzzle construction. Your computational approach, focused on constraint satisfaction, doesn't probe this **encoding locality question**.

**THE PATH FORWARD: CONSTRUCTIVE