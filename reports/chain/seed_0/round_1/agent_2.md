Building on the previous analysis, I'll provide concrete implementation details for Purbhoo's mosaic migration bijection.

## Data Structures

**Coordinate System**: Use axial coordinates (q,r) for hexagonal grid:
- q-axis: 60° from horizontal (northeast)  
- r-axis: 120° from horizontal (northwest)
- Each tile occupies multiple cells in this grid

**Tile Representation**:
```
Triangle: {type: 'triangle', center: (q,r), orientation: 0-5}
Square: {type: 'square', center: (q,r), orientation: 0-2}  
Rhombus: {type: 'rhombus', center: (q,r), orientation: 0-5, label: 0/1}
```

**Mosaic Structure**:
- Hexagon vertices: A'=(0,n-d), A=(0,0), B'=(n-d,n-d), B=(n,n-d), C'=(n,n), C=(d,n)
- Store tiles in spatial index for efficient neighbor queries
- Track nest membership for each rhombus

## Step 1: Puzzle to Mosaic

**Algorithm**:
1. Map puzzle's triangular grid to mosaic's hexagonal grid:
   - Puzzle position (i,j) → Mosaic position (q,r) = (j, n-i-j)
   - This places the puzzle in the upper-right portion of the hexagon

2. For each puzzle piece at (i,j):
   - If triangle with all edges labeled 0: place triangle
   - If rhombus with internal edge labeled k: place rhombus with label k
   - Otherwise: place square (will have mixed 0/1 labels)

3. Fill remaining hexagon area with triangles to complete tiling

## Step 2: Migration Algorithm

**Flock Formation**:
- Collect all rhombi in nest A (those with center q ≤ d)
- Assign labels f(ρ) = content value based on position
- For orientation (-E_A, -N_A) = (southwest, southeast), assign labels by reading rows bottom-to-top

**Standard Order**: 
For rhombi ρ₁, ρ₂ with labels f(ρ₁), f(ρ₂):
- If f(ρ₁) > f(ρ₂), then ρ₁ comes first
- If f(ρ₁) = f(ρ₂) and ρ₁ is southwest of ρ₂, then ρ₁ comes first

**Migration Loop**:
```
Sort rhombi by standard order (largest first)
For each rhombus ρ:
  While ρ not in nest B:
    H = findSmallestHexagon(ρ, direction='east')
    rotateHexagon(H, ρ)
    updatePosition(ρ)
```

**Finding Smallest Hexagon**:
1. Start from rhombus center
2. Scan eastward in layers until finding 6 tiles forming a hexagon
3. Check hexagon types:
   - Type A: 3 triangles + 3 squares → 180° rotation
   - Type B: 6 triangles → 120° rotation (choose rotation that makes rhombus edge axis-aligned)

**Wake Tracking**: 
- Store path of displaced tiles as rhombus moves
- Upper wake: tiles displaced above rhombus trajectory
- Lower wake: tiles displaced below
- Use for collision detection and order preservation

## Step 3: Mosaic to LR Tableau

After migration to nest B:
1. Sort rhombi by position (northwest to southeast)
2. Create tableau shape from rhombus positions
3. Fill entries with rhombus labels in order

## Test Case Walkthrough

For c^(3,2,1)_{(2,1),(2,1)}:
- Puzzle 1: Specific internal structure → Mosaic 1
- Initial flock has 3 rhombi with labels (2,1,1) or (1,2,1)
- Migration produces distinct orderings based on internal connections
- Result: Two different LR tableaux of shape (3,2,1