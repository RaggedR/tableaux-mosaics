# Report: Implementing Purbhoo's Mosaic Migration for KTW Puzzles

## Core Analysis

The previous researcher correctly identifies key gaps but overcomplicates several aspects. Their focus on discrete coordinates and complex symmetry detection misses the geometric essence of Purbhoo's construction. More critically, they don't address how to handle the specific test case c^(3,2,1)_{(2,1),(2,1)} = 2.

## Corrected Data Structures

```rust
// Simplified but complete representation
struct KTWPuzzle {
    pieces: Vec<PuzzlePiece>,
    boundary: (String, String, String)  // (π, ρ, σ) as 01-strings
}

struct PuzzlePiece {
    piece_type: PieceType,
    edges: [u8; 3],  // 0 or 1 labels
    coords: HexCoord  // Triangular lattice coordinates
}

enum PieceType { Triangle0, Triangle1, Rhombus01, Rhombus10 }

// Mosaic uses same coordinate system but adds nest structure
struct Mosaic {
    tiles: HashMap<HexCoord, Tile>,
    nests: [Nest; 3],
    rhombi_assignments: HashMap<RhombusId, NestId>
}

struct Nest {
    corner: NestCorner,  // A, B, or C
    orientation: (Vector2, Vector2),  // (E, N) basis vectors
    rhombi: Vec<RhombusId>
}
```

## Key Algorithm: Migration Implementation

The previous report's hexagon detection is correct but incomplete. Here's the full migration process:

```rust
fn migrate_flock(mosaic: &mut Mosaic, flock: &Flock, target_nest: NestId) {
    let rhombi_order = compute_standard_order(&flock.rhombi, &flock.tableau_function);
    
    for rhombus in rhombi_order {
        migrate_single_rhombus(mosaic, rhombus, target_nest);
    }
}

fn migrate_single_rhombus(mosaic: &mut Mosaic, rhombus: RhombusId, target: NestId) {
    while !rhombus_in_nest(mosaic, rhombus, target) {
        let hex = find_minimal_containing_hexagon(mosaic, rhombus);
        apply_hexagonal_transformation(mosaic, hex);
    }
}

fn find_minimal_containing_hexagon(mosaic: &Mosaic, rhombus: RhombusId) -> HexRegion {
    let pos = mosaic.get_rhombus_position(rhombus);
    
    // Critical: "weakly right" means in migration direction
    // For the standard case, this is eastward from leftmost point
    let candidates = get_unit_hexagons_containing(pos);
    
    candidates.into_iter()
        .filter(|h| h.is_weakly_in_migration_direction(pos))
        .min_by_key(|h| h.size())
        .expect("No valid hexagon found")
}

fn apply_hexagonal_transformation(mosaic: &mut Mosaic, hex: HexRegion) {
    let tiles = hex.get_tiles(mosaic);
    
    match analyze_symmetry(tiles) {
        SymmetryType::TwoFold => rotate_180_degrees(mosaic, hex),
        SymmetryType::ThreeFold => {
            // The "horizontal/vertical constraint" determines rotation direction
            let direction = if forces_horizontal_or_vertical_edge(tiles) {
                RotationDirection::TowardsTarget
            } else {
                RotationDirection::AwayFromTarget  
            };
            rotate_120_degrees(mosaic, hex, direction);
        }
    }
}
```

## Standard Order Correction

The previous researcher's implementation has the right idea but wrong comparison logic:

```rust
fn compute_standard_order(rhombi: &[RhombusId], tableau: &TableauFunction) -> Vec<RhombusId> {