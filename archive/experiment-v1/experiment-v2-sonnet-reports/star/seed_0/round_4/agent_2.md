# Vertex Model Specialist Report: Critical Errors in Proposed Implementation

## Fundamental Mathematical Errors

The generalist's synthesis contains **severe mathematical errors** that would produce incorrect bijections. As a vertex model specialist, I must correct these before implementation proceeds.

### Error 1: Migration is NOT Local Face Updates

The proposed `apply_local_migration_rule` is mathematically wrong. Migration in Purbhoo's construction is **global path-following**, not local label flips. The correct structure:

```cpp
struct MigrationPath {
    vector<HexCoord> path_coordinates;
    vector<LocalRotation> rotations;  // 120° or 180° rotations
    RhombusId rhombus_being_moved;
};

// Migration moves ONE rhombus along its complete path
void migrate_single_rhombus(MosaicState& state, RhombusId rhombus) {
    MigrationPath path = compute_migration_path(state, rhombus);
    
    for (int i = 0; i < path.rotations.size(); i++) {
        apply_hexagon_rotation(state, path.path_coordinates[i], path.rotations[i]);
    }
}
```

### Error 2: Edge Weights Don't Exist in Purbhoo's Model

The proposed `edge_weights` array is importing concepts from a different vertex model. Purbhoo's mosaics have **face types** (triangles, squares, rhombi), not edge weights.

```cpp
enum FaceType { TRIANGLE, SQUARE, RHOMBUS_NE, RHOMBUS_NW };

struct MosaicFace {
    FaceType type;
    HexCoord position;
    int color_label;  // For flock membership, not edge weights
};
```

### Error 3: Standard Order Violates Yang-Baxter Structure

The proposed sorting function is incomplete and violates integrability. Standard order in LR tableaux must preserve the **commuting transfer matrix** property:

```cpp
struct StandardOrder {
    // Respects both geometric and combinatorial constraints
    static bool compare_rhombi(const RhombusData& a, const RhombusData& b,
                              const FlockOrientation& orientation) {
        // East-West ordering: f(X) < f(Y) or [f(X) = f(Y) and X west of Y]
        if (a.tableau_entry != b.tableau_entry) {
            return a.tableau_entry < b.tableau_entry;
        }
        
        // Geometric tiebreaker respects orientation
        return is_westward(a.position, b.position, orientation);
    }
};
```

## Correct Mathematical Structure

### Yang-Baxter Compatible Operations

Migration must preserve the **spectral parameter structure**. Each local rotation corresponds to a vertex model weight:

```cpp
struct VertexWeight {
    int input_state;
    int output_state;
    bool preserves_determinant;  // Must be true for bijection
};

// Only rotations that preserve the Yang-Baxter equation
bool is_valid_rotation(const LocalHexagon& hex, RotationType rotation) {
    return check_yang_baxter_consistency(hex.vertex_configuration, rotation);
}
```

### Spectral Parameter Preservation

The bijection works because migration preserves **partition differences**:

```cpp
class PartitionDifferenceTracker {
private:
    vector<int> shape_differences;
    
public:
    void verify_migration_step(const MosaicState& before, const MosaicState& after) {
        assert(compute_shape_difference(before) == compute_shape_difference(after));
    }
    
    vector<int> compute_shape_difference(const MosaicState& state) {
        // Extract partition from boundary rhombi configuration
        return extract_partition_from_boundary_A(state) - 
               extract_partition_from_boundary_B(state);
    }
};
```

## Critical Implementation Requirements

### 1. Hexagon Detection Must Be Exact

The proposed neighbor detection is too vague. Purbhoo specifies **minimal enclosing hexagons**:

```cpp
LocalHexagon find_minimal_enclosing_