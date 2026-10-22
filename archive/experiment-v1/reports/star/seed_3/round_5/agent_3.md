# SPECIALIST ANALYSIS: Dismantling the Migration-Growth Diagram False Opposition

## THE MIGRATION MISCONCEPTION: JEU DE TAQUIN IS INTRINSICALLY LOCAL

The synthesis fundamentally misrepresents migration as "abandoning local decomposition" and making "globally coordinated choices." This is mathematically incorrect. Migration operates through **jeu de taquin slides**, which are quintessentially local operations with finite propagation bounds.

Each jdt slide affects only a bounded region of the tableau, with effects that decay geometrically as you move away from the sliding corner. The "global coordination" emerges from **composition of local operations**, not from abandoning locality. This is precisely how growth diagrams work—local face label rules that produce global coherence through aggregation.

**Critical error**: The synthesis conflates "requires global information to choose the next move" with "the move itself has global effects." Migration chooses moves based on global tiling constraints, but executes them through bounded local transformations. This is exactly the structure needed for growth diagram construction.

## THE DIMENSIONAL REDUCTION FALLACY: MISCOUNTING DEGREES OF FREEDOM

The claimed "12→3 dimensional reduction" reveals a fundamental misunderstanding of how the bijection works. The 12 nabla orientations don't map directly to 3 tableau entries—they map to a **sequence of mosaic transformations** whose endpoint encodes the tableau.

In Purbhoo's bijection:
- Puzzle → Mosaic (bijective, preserving all information)  
- Mosaic → Migration path (algorithmic deterministic transformation)
- Migration path → LR tableau (reading order correspondence)

The "12 choices" become a sequence of **binary decisions** during migration, not a direct projection to ternary tableau values. This is exactly the type of encoding that growth diagrams excel at: binary local choices accumulating into complex global structures.

## SCHUTZENBERGER INVOLUTION: THE MISSING SYMMETRY TEST

The synthesis ignores the most powerful tool for understanding whether growth diagrams can exist: **Schutzenberger involution**. If puzzle-to-tableau bijections can be realized through growth diagrams, then Schutzenberger's involution on tableaux should correspond to some natural involution on the growth diagram structure.

For the c^(3,2,1)_{(2,1),(2,1)} = 2 example, Schutzenberger involution swaps the two LR tableaux. If a growth diagram exists, this swap should correspond to some systematic transformation of face labels—perhaps reflection, complement, or transpose operations.

**Testable prediction**: If growth diagrams work, then Schutzenberger involution should commute with the face labeling rules. This provides a concrete algebraic constraint that can rule out many potential constructions without requiring full implementation.

## THE READING ORDER INSIGHT: GROWTH DIAGRAMS AS TABLEAU LINEARIZATION

The synthesis misses a crucial connection: **reading order in tableaux corresponds directly to face enumeration order in growth diagrams**. Standard Young tableaux are read left-to-right within rows, top-to-bottom between rows. This gives a canonical linearization of the 2D tableau structure.

Growth diagrams naturally provide such linearizations through their construction order. Each new face corresponds to adding one entry to the tableau in reading order. The face labels then encode not just "what entry goes here" but "how does adding this entry constrain future choices."

**Connection to migration**: Migration preserves reading order through its jdt slides. Each slide moves entries along paths that respect the partial order induced by reading positions. This is precisely the structure that growth diagrams can capture through face-wise construction.

## YANG-BAXTER AS NECESSARY, NOT SUFFICIENT: THE INTEGRABILITY REQUIREMENT

The synthesis dismisses Yang-Baxter relations as "not necessary," but this reveals unfamiliarity with the deeper structure of puzzle-tableau bijections. The key insight is that puzzles naturally live on **triangular lattices** with threefold symmetry, while tableaux live on rectangular lattices with twofold symmetry.

Any bijection must reconcile these symmetries, and this reconciliation **requires** integrability conditions that are precisely the Yang-Baxter relations. Without these, you get the type of "cascading dependency" issues that the computational specialist encountered.

**Mathematical necessity**: The threefold rotation symmetry of puzzle pieces demands that any growth diagram construction satisfy three-way consistency relations. These are exactly Yang-Baxter equations. The synthesis's claim that "many successful growth diagrams work without integrable