## Critical Implementation Gaps I Still Have

Looking deeper, I'm realizing the **coordinate system and discrete representations** are the fundamental blockers for implementation. The paper uses continuous geometric language, but a coding agent needs discrete data structures.

### 1. **The Rhombic Tiling Coordinate System**
The paper never explicitly states how to represent the hexagonal mosaic discretely. I need:
- **Discrete coordinates for the hexagon vertices** A', A, B', B, C', C
- **How rhombi positions are encoded** in this coordinate system
- **Adjacency rules** for the hexagonal flip operations

From the figures, it looks like we're working in a **triangular lattice**, but with rhombi that have specific orientations. The three nest orientations suggest we need coordinates that naturally handle 60° rotations.

### 2. **Puzzle Piece → Mosaic Tile Mapping**
This conversion is described as "physical intuition" but I need the discrete algorithm:

**From Puzzle (with labeled edges 0/1):**
- Each puzzle rhombus has three edges labeled 0 or 1
- Under the "straightening" transformation, some become squares, some triangles

**Critical Question:** How do I algorithmically determine which puzzle pieces become which mosaic tiles? The paper mentions "some line segments rotate clockwise (0s) vs counterclockwise (1s)" but doesn't give the discrete rule.

### 3. **Standard Order Implementation**
This is algorithmic nightmare territory. The standard order depends on:
- Current tableau values f(rhombus) 
- Lexicographic position when values equal
- But positions change during migration!

I think the key insight I'm missing: **standard order is defined on the ORIGINAL configuration and determines migration sequence**. The rhombi move in this predetermined order, not in an order that changes dynamically.

### 4. **Flock Construction Algorithm**
Lemma 3.1 says there's a unique canonical tableau, but doesn't give the construction. Looking at Figure 7 (canonical flock), it appears to be:
- **Entries increase left-to-right within rows**  
- **Entries increase bottom-to-top within columns**
- **Values assigned greedily to satisfy LR tableau conditions**

But I need the precise algorithm for irregular shapes.

## New Strategy: Focus on the Test Case

For c^(3,2,1)_{(2,1),(2,1)} = 2, let me try to reverse-engineer the missing pieces:

### The Two Input Puzzles
With boundary data ((2,1), (2,1), (3,2,1)), these are puzzles on equilateral triangles of side n=4 with d=3 ones on each side.

**Key insight:** The complement relationship means the boundary strings have specific structure. If α corresponds to (2,1) partition, the boundary string should be 0110.

### Expected LR Tableaux Output
The two distinct LR tableaux should have:
- **Shape:** (3,2,1)/(2,1) = 3 boxes arranged in specific skew pattern
- **Content:** (2,1) = 2 ones and 1 two
- **Different arrangements** of these entries satisfying LR conditions

## What I Need to Explore Immediately

### 1. **Concrete Hexagonal Coordinate System**
I should specify:
```
Hexagon vertices in integer coordinates:
A' = (0, 0), A = (d, 0), B' = ?, B = ?, C' = ?, C = ?

Rhombi positions as (x, y, orientation) where orientation ∈ {0, 1, 2}
```

### 2. **The Two Hexagonal Flip Rules**
For each rhombus position, determine:
- What constitutes the "minimal hexagon containing it"
- How to detect 2-fold vs 3-fold symmetry case
- Explicit coordinate transformation rules

### 3. **Partition ↔ String ↔ Rhombi Correspondence**
Work out the exact bijection:
```
Partition (2,1) ↔ String 0110 ↔ Rhombi arrangement in nest
```

### 4. **LR Tableau Reading Algorithm**
Given final migrated flock, how exactly do I:
- Identify the "accessible" subset ζ of rhombi