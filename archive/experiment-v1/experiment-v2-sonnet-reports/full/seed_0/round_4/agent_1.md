# Report: Growth Diagram Analysis for KTW Puzzle Migration

## Core Problem: KTW Migration vs Standard Growth Diagrams

After analyzing the previous reports and Purbhoo's construction, I must address a fundamental mismatch: **KTW puzzle migration does NOT naturally form a standard growth diagram structure**.

### Why Previous Approaches Miss the Mark

1. **Growth Diagram Misconception**: The reports assume migration can be encoded as face labels with local update rules. However, Purbhoo's migration is inherently **global** - rhombi traverse long paths across the entire mosaic, not local vertex neighborhoods.

2. **Yang-Baxter Fantasy**: The first report invokes "free-fermionic vertex models" and "Yang-Baxter equations" without justification. KTW puzzles don't satisfy Yang-Baxter conditions - they have different local rules than RSK-type correspondences.

3. **JdT Sequence Error**: The second report claims migration equals "sequences of jeu de taquin slides." This is backwards - Purbhoo shows migration CORRESPONDS to JdT in the final tableau, not that migration IS implemented by JdT moves.

## The Real Implementation Challenge

### Purbhoo's Actual Construction

The migration bijection has three distinct phases that resist growth diagram encoding:

**Phase 1: Puzzle → Mosaic** (Geometric transformation)
- Convert triangular puzzle tiling to hexagonal mosaic tiling
- Requires non-local coordinate changes
- Creates "nest" regions where rhombi accumulate

**Phase 2: Migration** (Global path-following)
- Each rhombus follows a deterministic path across the entire mosaic
- Paths determined by "minimal hexagon" detection at each step
- Order matters: process rhombi in "standard order" (lexicographic by tableau values)

**Phase 3: Final Configuration → LR Tableau** (Readout)
- Extract partition shapes from final nest configurations
- Convert rhombi positions to tableau entries

### Why Growth Diagrams Don't Apply

**Missing Local Structure**: Growth diagrams require that face labels update based only on adjacent vertex/edge information. Migration violates this:

```python
# This is NOT how migration works:
def local_face_update(north_face, east_face, south_face, west_face, vertex_input):
    # Migration paths can span the entire mosaic
    # Cannot be computed from local neighborhood
    return updated_face  # IMPOSSIBLE
```

**Non-Commutative Operations**: Growth diagram face updates must commute (order-independence). Migration explicitly violates this - the "standard order" is crucial and changing it breaks the bijection.

## Correct Implementation Strategy

### Data Structures
```python
class HexPosition:
    q: int  # axial coordinates for hexagonal lattice
    r: int

class Rhombus:
    position: HexPosition
    tableau_value: int  # entry in the LR tableau this represents
    orientation: int  # 0, 1, 2 for three possible orientations

class Mosaic:
    triangles: Set[HexPosition]
    squares: Set[HexPosition] 
    nests: Dict[str, List[Rhombus]]  # "A", "B", "C" -> rhombi lists
    
class MinimalHexagon:
    center: HexPosition
    tiling: List[Union[Triangle, Square, Rhombus]]
    symmetry_type: str  # "2-fold" or "3-fold"
```

### Core Migration Algorithm
```python
def migrate_flock(mosaic: Mosaic, source_nest: str, target_nest: str, 
                  flock: List[Rhombus]) -> Mosaic:
    
    # Sort rhombi in standard order (lexicographic by tableau value)
    sorted_rhombi = sort_by_standard_order(flock)
    
    new_mosaic = mosaic.copy()
    
    for rhombus in sorted_rhombi:
        path = []
        current_pos = rhombus.position
        
        # Follow the migration path
        while not in_target_nest(current_pos, target_nest):
            # Find minimal hexagon containing current_pos
            hex_region = find_minimal_hexagon(new_mosaic, current_pos)
            
            # Apply rotation rule