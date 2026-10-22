# Synthesis Report: The Growth Diagram Question Through Multiple Mathematical Lenses

The four specialist reports reveal fundamental tensions about what constitutes mathematical explanation versus computational verification. Each perspective identifies genuine obstacles, but their disagreements illuminate deeper structural issues about the nature of combinatorial bijections.

## Critical Gap: The Locality vs. Globality Tension

All specialists acknowledge that KTW puzzles have **long-range correlations** that resist local rule decomposition, but they fundamentally disagree on whether this is surmountable:

- The growth diagram specialist declares it "mathematically impossible" due to temporal ordering requirements
- The vertex model specialist suggests it's solvable via "colored vertex models" with spectral parameters
- The migration specialist claims it's merely a technical challenge about encoding hexagonal Robinson-Schensted moves
- The computation specialist treats it as an empirically decidable question

**My synthesis**: This disagreement reveals that the specialists are actually studying **different mathematical objects**. The growth diagram specialist analyzes abstract local rule systems, while others examine concrete algebraic constructions. The question isn't whether puzzles admit growth diagrams—it's whether the **algebraic structures** underlying puzzles can be **faithfully represented** by local combinatorial rules.

## The Spectral Parameter Confusion Demands Clarification

The vertex model specialist emphasizes spectral parameters as fundamental deformation parameters, while the computation specialist dismisses them as "numerical stability parameters." The migration specialist treats them as implementation details. This confusion is mathematically unacceptable.

**Challenge to all perspectives**: The spectral parameter disagreement suggests we lack a unified understanding of what these parameters actually control. If they're fundamental (vertex model view), then computational studies ignoring them are meaningless. If they're artifacts (computational view), then the vertex model analysis is over-complicated. If they're implementation choices (migration view), then neither extreme position is correct.

**My diagnostic**: The specialists are conflating **mathematical parameters** (which encode geometric or representation-theoretic data) with **computational parameters** (which control algorithmic behavior). A proper analysis must distinguish these carefully.

## The Jeu de Taquin Blind Spot

Remarkably, three of the four specialists barely mention jeu de taquin, despite it being the **core algebraic operation** in Purbhoo's construction. Only the migration specialist recognizes its universal algebraic properties. This represents a serious gap in the analysis.

**Fundamental insight**: Jeu de taquin is not just "one way to connect frameworks"—it's the **unique canonical operation** that preserves the relevant combinatorial invariants. The growth diagram question reduces to: **Can jeu de taquin slides be implemented as local growth rules?**

This reframing eliminates much of the ontological confusion. We're not asking about general framework translation—we're asking about the **local implementability** of a specific, well-understood algebraic operation.

## The Experimental Challenge is Mis-Specified

The computation specialist proposes definitive experiments, but these test the wrong mathematical properties. Counting intermediate states or measuring spectral radii doesn't address whether growth diagrams **could exist** in principle—it only tests whether **current algorithms** implement them.

**Better experimental design**: Instead of counting configurations, test whether jeu de taquin operations on mosaics satisfy the **Yang-Baxter equation**. This is both computationally tractable and mathematically decisive. If they do, growth diagrams are possible; if not, the obstruction is fundamental.

## The Category Theory Red Herring

Multiple specialists invoke "derived algebraic geometry" or "categorical frameworks" without concrete mathematical content. This suggests **mathematical hand-waving** when the specialists encounter technical difficulties.

**My verdict**: The categorical language obscures rather than clarifies. The growth diagram question is about **elementary combinatorial algebra**—whether certain local moves satisfy consistency relations. Derived categories don't resolve consistency failures; they merely provide language to describe them.

## Three Testable Mathematical Propositions

The specialist disagreements can be resolved by testing three specific mathematical claims:

1. **Hexagonal Yang-Baxter Conjecture**: Do jeu de taquin slides on hexagonal tilings satisfy modified Yang-Baxter relations? (Migration specialist says yes, growth diagram specialist says no)

2. **Spectral Independence Conjecture**: Do Littlewood-Richardson coefficients computed via puzzles depend on spectral parameter choices? (Vertex model specialist suggests yes, computation specialist suggests no)

3. **Local Evacuation Conjecture**: Can tableau evacuation be implemented via local face operations on growth diagrams? (Migration specialist claims this is the key test,