## Implementation Report: Purbhoo's Mosaic Migration for KTW Puzzles

I'll build on the previous researcher's work, correcting critical errors and providing concrete implementation details.

### Key Corrections

1. **Puzzle-to-Mosaic Mapping**: The previous report is vague about the actual transformation. The physical process described by Purbhoo involves removing rhombi, flexing squares into rhombi, and pulling vertices outward to straighten edges.

2. **Flock Orientation**: The report correctly identifies orientation (-E_A, -N_A) but misunderstands the standard order. Since E is reversed, positions increase westward, not decrease.

3. **Migration Details**: The hexagon rotation rules need clarification for deterministic implementation.

### Complete Implementation

#### Data Structures

```
Puzzle:
  - pieces: List of (position, type, edge_labels)
  - position: barycentric (i,j,k) with i+j+k=n
  - edge_labels: {NE: 0/1, E: 0/1, SE: 0/1} (clockwise from top)

Mosaic:
  - tiles: Dict[(x,y) -> Tile]
  - Tile: {type: 'triangle'|'square'|'rhombus', 
           orientation: angle,
           edges: edge labels if rhombus}
  - rhombi_sets: {A: Set[Rhombus], B: Set[Rhombus], C: Set[Rhombus]}

Rhombus:
  - position: (x,y) in mosaic coordinates
  - edges: {dir -> 0/1} for the two edges
  - value: integer assigned by flock
```

#### Step 1: Puzzle to Mosaic

The bijection maps the equilateral triangle to hexagon A'AB'BC'C:

```
1. Map puzzle vertices to hexagon:
   - (0,0,n) -> A'
   - (n,0,0) -> B'  
   - (0,n,0) -> C'
   - Vertices at distance d from edges map to A, B, C

2. For each puzzle piece at (i,j,k):
   a. Compute mosaic position via affine map
   b. If unit rhombus with edges e1=0, e2=0:
      - If e1,e2 point toward A',B': assign to nest A
      - If e1,e2 point toward B',C': assign to nest B  
      - If e1,e2 point toward C',A': assign to nest C
   c. Else: place triangle/square at mapped position

3. Fill gaps with triangles to complete hexagon tiling
```

#### Step 2: Create Canonical Flock

For rhombi α in nest A with orientation (-E_A, -N_A):

```
1. Define comparison for standard order:
   rhombus p < q iff:
     - p.y < q.y (strictly north), OR
     - p.y = q.y AND p.x > q.x (west when tied)
   
2. Sort α by this order

3. Assign values maintaining LR conditions:
   current_row = 1
   for i, rhombus in enumerate(sorted_α):
     rhombus.value = current_row
     if i+1 < len(α) and α[i+1].y > α[i].y:
       current_row += 1
```

#### Step 3: Migration Algorithm

Migration south from A to B:

```
for rhombus ρ in standard order:
  while ρ not in nest B:
    1. Find minimal hexagon containing ρ:
       - Scan southeast from ρ's rightmost vertex
       - Find first complete hexagon of 6 tiles
       
    2. Apply rotation:
       if hexagon has opposite edges parallel (type a):
         rotate_tiles_180°(hexagon)
       else: # type b with 3-fold symmetry
         if ρ.top_edge is 30° from horizontal:
           rotate_tiles_120°_clockwise(hexagon)
         else:
           rotate_tiles_120°_counterclockwise(hexagon)
           
    