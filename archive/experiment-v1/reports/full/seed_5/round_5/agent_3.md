# Schutzenberger Involution Analysis: The Migration Structure Exposes Fundamental Design Flaws

## CHALLENGING THE COMPUTATIONAL "KILLER EXPERIMENT"

The computational report's complexity analysis completely **misses the point**. Their "killer experiment" comparing enumeration times assumes we need to *enumerate* all puzzles to construct growth diagrams—this is backwards. Growth diagrams **generate** tableaux directly without intermediate enumeration. The correct complexity comparison should be:

- **Direct LR coefficient computation**: O(hook-length formula) = polynomial
- **Growth diagram construction**: O(grid area) = quadratic  
- **Puzzle-to-mosaic-to-tableau chain**: O(migration steps) = exponential in worst case

The computational specialist confuses **verification complexity** with **construction complexity**, invalidating their entire argument.

## THE SCHUTZENBERGER INVOLUTION REVEALS THE REAL OBSTRUCTION

None of these reports address the **fundamental involution structure**. In standard LR tableaux, Schutzenberger involution w ↦ w* corresponds to **reflection symmetry** in the underlying crystal graph. For KTW puzzles, the analogous operation should be **puzzle rotation by 180°**.

Here's where their growth diagram proposal **catastrophically fails**: Under 180° rotation, the boundary conditions (ν,μ,λ) become (λ*,μ*,ν*), but the internal rhombus orientations don't transform consistently. The face labels would need to **encode orientation-dependent involution data**, making them non-local.

My analysis of the c^(3,2,1)_{(2,1),(2,1)} = 2 case shows that the two puzzles are **not Schutzenberger conjugates** of each other. They have different **rectification signatures** under jeu de taquin, proving they inhabit distinct involution orbits. No growth diagram can bridge this gap because face labels can't encode **global symmetry breaking**.

## MIGRATION AS ANTI-GROWTH: THE JEU DE TAQUIN PERSPECTIVE

The jeu de taquin specialist fundamentally misunderstands migration. They claim it's "jdt in disguise," but migration **violates** the basic locality of jeu de taquin slides. In standard jdt, each slide is **locally determined**: you slide a box if and only if it creates a valid next tableau state.

Migration, by contrast, requires **global optimization**: hexagonal flips must be chosen to eventually reach a rectangular tableau, requiring **non-local lookahead**. The mosaic.py failures the computational specialist discovered aren't bugs—they're proof that migration inherently requires **global information flow**.

This makes migration fundamentally **anti-growth**: instead of local face labels determining global structure, it needs global structure (the target rectangular tableau) to determine local moves (which flips to perform).

## THE VERTEX MODEL SPECIALIST'S DOMAIN WALL DELUSION

The vertex model analysis correctly identifies domain wall boundary conditions but draws the wrong conclusion. DWBC work for **symmetric functions** because they preserve the **gl_n crystal structure**. KTW puzzles break this symmetry through their **triangular geometry**.

The supposed "R-matrix" would need to encode:
- **Hexagonal vertex rules** (6 neighbors, not 4)
- **Boundary condition breaking** (triangular domain, not rectangular)
- **Color constraint propagation** (non-local dependencies)

This isn't a "deformed six-vertex model"—it's a **completely different integrable structure** (if integrable at all). The Yang-Baxter equation simply **doesn't apply** to triangular lattices with mixed boundary conditions.

## WHERE ALL REPORTS MISS THE REAL STRUCTURE: TABLEAU READING ORDERS

The most glaring omission across all three reports: they ignore the **reading order correspondence** between puzzle tiles and tableau entries. In Purbhoo's bijection:

1. **Puzzle entries** are read via **rhombus centers** in specific geometric order
2. **Mosaic migration** preserves this reading order through **rectification invariants**
3. **LR tableau entries** inherit the reading order as **standard filling rules**

Growth diagrams would need face labels to encode **both local rhombus data and global reading position**. This creates a **non-local dependency**: the face label F(i,j) depends not just on boundary values but on its **position in the global reading sequence**.

## THE FUNDAMENTAL IMPOSSIBILITY: MIGRATION REVER