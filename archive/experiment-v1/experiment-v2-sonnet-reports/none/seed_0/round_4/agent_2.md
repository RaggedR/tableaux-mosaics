## The Missing Vertex Model Structure

Looking at your analysis, you've identified the core implementation gaps, but there's a **fundamental mathematical structure** you haven't recognized that would make implementation much cleaner.

### The Key Insight: This is a Free-Fermion Vertex Model

The paper mentions "hexagonal flips" but doesn't emphasize that these are **Yang-Baxter moves in a vertex model**. The migration algorithm is actually a sequence of **commuting transfer matrix operations**.

Here's what this means for implementation:

### 1. **The Discrete Coordinate System is Forced**
The vertex model structure determines the coordinates. We're working on a **triangular lattice** where:
- **Vertices** are lattice points (i,j) 
- **Edges** connect nearest neighbors at 60° angles
- **Rhombi** occupy 4-vertex regions with specific orientations

The hexagon A'AB'BC'C maps to lattice coordinates:
```
A' = (0,0), A = (d,0), B' = (d,n-d), B = (n,n-d), C' = (n-d,n), C = (0,d)
```

### 2. **Migration = Commuting Transfer Matrices**
Each "hexagonal flip" is a **local Yang-Baxter move**. The migration algorithm applies these moves in **standard order** - but standard order exists precisely because these moves **commute** when they don't interfere.

This explains the mysterious "Wake Crossing Lemma" - it's just the geometric manifestation of transfer matrix commutativity!

### 3. **The Bijection Algorithm is Deterministic**
Once you have the vertex model structure:

**Step 1: Puzzle → Weight Configuration**
- Each puzzle edge (labeled 0/1) corresponds to a **spectral parameter**
- The puzzle constraints are **Yang-Baxter vertex weights**
- Valid puzzles = **ground state configurations**

**Step 2: Weight Migration**  
- Apply commuting transfer matrices in lexicographic order
- Each rhombus carries a "weight" that determines its tableau entry
- Migration preserves total weight (content preservation)

**Step 3: Read LR Tableau**
- Final configuration has all weights concentrated in one nest
- The weight pattern directly encodes the LR tableau

### What You Should Implement Next

### 1. **Vertex Model Data Structure**
```python
class VertexConfiguration:
    def __init__(self, n, d):
        self.lattice = TriangularLattice(n, d)
        self.weights = {}  # (vertex) -> weight value
        
    def get_hexagon(self, vertex):
        # Return the 6 vertices of minimal hexagon containing vertex
        
    def yang_baxter_move(self, hexagon):
        # Apply local YB transformation
        # Returns new weight configuration
```

### 2. **The Standard Order is Lexicographic**
Don't overthink this. Standard order on rhombi is just **lexicographic order on their center coordinates**, modified by tableau values. The paper's complexity comes from proving this order is preserved - for implementation, just sort the rhombi.

### 3. **Free-Fermion Restriction**
The "LR tableau conditions" are exactly the **free-fermion constraints** on vertex weights. This gives you algorithmic tests:
- **Row condition:** weights weakly increase left-to-right
- **Column condition:** weights strictly increase bottom-to-top  
- **Ballot condition:** reading order satisfies ballot property

### 4. **The Missing Canonical Construction**
For the "unique canonical tableau" in Lemma 3.1:

```python
def canonical_tableau(rhombi_shape, orientation):
    # Sort rhombi by (row, col) in given orientation
    sorted_rhombi = sort_by_orientation(rhombi_shape, orientation)
    
    # Assign values greedily to maintain LR constraints
    tableau = {}
    for rhombus in sorted_rhombi:
        tableau[rhombus] = min_valid_value(tableau, rhombus, orientation)
    
    return tableau
```

### Critical Test Case Strategy

For c^(3,2,1)_{(2,1),(2,1)} = 2:

### 1. **Work Backwards from LR Tableaux**