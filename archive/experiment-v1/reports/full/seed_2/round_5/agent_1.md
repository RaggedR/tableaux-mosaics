# Growth Diagram Specialist Analysis: The Fomin-Krattenthaler Gap Everyone Missed

## CRITICAL CHALLENGE: Your Transfer Matrix Construction Ignores Fundamental Growth Diagram Theory

The computational analysis proposes "explicit transfer matrix construction" but reveals a profound misunderstanding of what growth diagrams actually are. You're not looking for arbitrary transfer matrices—you need **local rules** that satisfy the **Fomin growth diagram axioms**. None of the reports address whether KTW puzzles can satisfy these axioms, which is the actual mathematical question.

## THE FUNDAMENTAL AXIOM VIOLATION: NON-RHOMBIC FACE LABELS

In genuine growth diagrams (Fomin 1994), face labels satisfy the **rhombic constraint**: each 2×2 square of vertices determines a **unique face label** via local rules. But KTW puzzle "choices" violate this fundamentally:

**Critical Observation**: The "12 free nabla choices" mentioned in the problem occur at **rhombus vertices**, not faces. A rhombus with three fixed edge orientations still has **multiple valid nabla assignments** at its center vertex. This creates **label degeneracy** that genuine growth diagrams cannot accommodate.

In matrix terms: if f(a,b,c,d) represents the face label for a 2×2 square with corner values (a,b,c,d), then growth diagrams require **f to be a function**. But KTW puzzles allow multiple nabla orientations for the same rhombus edge configuration, making f **multivalued**.

## CYLINDRIC GROWTH DIAGRAMS: THE WRONG ANALOGY

The computational report hints at "cylindric growth diagram construction" but misapplies it. Cylindric growth diagrams (Krattenthaler-Schlosser) handle **periodic boundary conditions**, not constraint propagation across irregular boundaries.

**Key Distinction**: 
- **Cylindric case**: Regular lattice with periodic left-right identification
- **KTW case**: Triangular lattice with three distinct boundary types (λ, μ, ν edges)

The triangular geometry creates **corner effects** where three different boundary constraint types meet. These corners cannot be handled by cylindric methods, which assume translation-invariant local rules.

## THE MISSING DIRECTED GRAPH STRUCTURE

Your analysis completely ignores that growth diagrams require **directed edge labeling** where the direction encodes information flow. In RSK, this corresponds to **insertion direction** (left-to-right processing).

**Fatal Flaw**: KTW puzzles have **undirected rhombi**. The three edge orientations of a rhombus are **symmetric**—there's no canonical "input" versus "output" direction for information processing. This breaks the directed graph structure that growth diagrams fundamentally require.

Compare to **symmetric functions**: RSK works because words have **temporal order** (processing direction). But puzzle rhombi are **spatial**—they exist simultaneously without processing order.

## FACE LABEL ENCODING: THE RECORDING DATA PROBLEM

The core insight you've all missed: growth diagram face labels don't just count objects—they **encode the actual recording tableau entries**. For KTW puzzles, what would the face labels encode?

**Recording Data Analysis**: In RSK, face labels record **which element was inserted** at each step. For puzzles:
- **Rhombus orientations** are determined by boundary constraints
- **Nabla choices** are the only "free" degrees of freedom
- **LR tableau entries** are complex functions of global puzzle structure

There's no **local rule** that maps (rhombus configuration, nabla choice) to (tableau entry). The tableau construction requires **global migration**, which is fundamentally **non-local**.

## THE BRANCHING STRUCTURE MISCONCEPTION

The problem statement asks whether "KTW puzzle branching choices form a growth diagram"—but this reveals confusion about what **branching** means in growth diagram context.

**True Growth Diagram Branching**: At each step, multiple **paths** can lead to the same **final configuration**, and face labels encode which path was taken.

**KTW "Branching"**: Multiple **nabla assignments** can occur in the same **puzzle configuration**, but they don't represent **different paths to the same outcome**—they represent **different final states**.

This is the difference between:
- **Path degeneracy** (many ways to build the same tableau) → growth diagrams can handle this
- **State degeneracy** (many distinct final configurations) → growth diagrams