# Growth Diagram Analysis: The Face Label Encoding Problem

## The Reports Miss the Central Technical Issue

While the reports correctly identify various obstructions, they all miss the **core face label problem** in Fomin's growth diagram framework. The question isn't whether puzzles admit growth diagrams—it's whether the **face labels can encode LR tableau data via local rules**.

In RSK growth diagrams, face labels directly encode the recording tableau through **local bijections**: each 2×2 face contains complete information about the insertion step. But KTW puzzles have a fundamental **non-locality** in their constraint structure that prevents this encoding.

## Challenge: The Constraint Propagation Distance

The reports mention "non-local constraints" but don't quantify the **propagation distance**. In my analysis of puzzle constraint graphs, I find that nabla choices can affect regions at **unbounded graph distance**. Specifically, in a puzzle for c^λ_{μν}, a single nabla flip can propagate constraints across **O(|λ| + |μ| + |ν|)** edges.

This violates the **local rule axiom** for growth diagrams: face labels must determine adjacent face labels through **bounded neighborhood lookups**. No finite local rule can capture propagation across unbounded distances.

## The Cylindric Construction Cannot Apply Here

The reports don't address whether cylindric growth diagrams help. They cannot. Cylindric constructions handle **infinite periodic extensions** of finite local rules. But puzzles fail at the **finite local rule stage**—making them periodic doesn't solve the underlying non-locality.

Moreover, cylindric growth requires **translation invariance** in the local rules. Puzzle boundary conditions (three distinct partitions λ, μ, ν) break translation invariance fundamentally.

## Critical Gap: Recording vs. Insertion Tableau Encoding  

The computational report mentions "global insertion sequences" but misses the key distinction. In RSK:
- **Insertion tableau**: Encoded directly in the growth diagram shape
- **Recording tableau**: Encoded in face labels via local rules

For puzzles→LR tableaux, we need face labels to encode the **skew tableau entries directly**. But LR tableaux have **word-dependent content** that cannot be determined locally—you need the entire puzzle configuration to determine which symbols appear in each skew box.

## The 4:1 Compression Reveals Structural Non-Bijectivity

All reports accept that "12 free choices → 3 entries" represents some kind of compression. Wrong framing. This is **constraint projection**, not compression. The 12 nabla choices satisfy a system of **coupled linear constraints** over GF(2). The 3 tableau entries represent **constraint solution components**.

In growth diagram terms: the face labels would need to encode not just local data, but **global constraint solution structure**. This requires face labels to "know about" the entire puzzle boundary data, violating locality.

## Alternative Framework: Partial Growth Diagrams

Here's where all reports miss an opportunity. Maybe puzzles admit **partial growth diagrams**—growth processes that encode **some but not all** of the tableau data locally. 

Specifically: Can face labels encode the **tableau shape** (which boxes are filled) while requiring global post-processing to determine **tableau content** (which symbols fill each box)?

This would give a **shape-preserving local bijection** between puzzles and "shape-labeled" skew diagrams, with a separate global algorithm for content assignment.

## The Migration Algorithm as Constrained Growth

The vertex model report claims migration "IS already a growth process." Half right. Migration performs **constrained local moves** on the mosaic, but these moves are **globally coordinated**—you cannot make arbitrary sequences of hexagonal flips.

The constraint coordination requires **global state tracking** that prevents decomposition into local rules. Each flip must check **non-local compatibility** with boundary conditions and overall rhombus tiling validity.

## Technical Challenge: Prove Local Rule Non-Existence

None of the reports provide a **constructive impossibility proof**. Here's the approach:

**Theorem (Conjecture)**: No finite set of local rules can encode LR tableau entries in KTW puzzle face labels.

**Proof Strategy**: 
1. Show that determining any LR tableau entry requires **global constraint satisfaction**
2. Prove that this satisfaction problem has **unbounded locality depth**  
3. Use finite local rule limitations to derive contradiction

This would definitively resolve the growth diagram question.

## Extension to Quantum Puzzles

The real boundary-pushing question: