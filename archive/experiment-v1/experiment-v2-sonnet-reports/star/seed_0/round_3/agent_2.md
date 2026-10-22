# VERTEX MODEL SPECIALIST REPORT: Critical Implementation Gaps

The generalist's synthesis contains fundamental errors about the mathematical structures underlying Purbhoo's bijection. As a vertex model specialist, I must clarify the correct framework before implementation can proceed.

## Core Mathematical Error in Synthesis

The synthesis conflates three distinct mathematical objects:
1. **Static mosaic configurations** (what the puzzle-to-mosaic conversion produces)
2. **Dynamic vertex model evolution** (what migration actually computes)
3. **Algebraic tableau operations** (how we interpret the result)

This confusion leads to incorrect data structures and algorithm design.

## Correct Mathematical Framework

### 1. Mosaic as Vertex Configuration

A mosaic is NOT a collection of moving rhombi. It's a fixed vertex model configuration:

```cpp
struct VertexWeight {
    int type;  // 6 possible vertex types in free-fermion model
    complex<double> spectral_param;
    bool fermion_parity[3];  // incoming/outgoing fermion states
};

struct MosaicVertex {
    HexCoord position;
    VertexWeight weight;
    int face_labels[6];  // surrounding face values
};

struct Mosaic {
    vector<vector<MosaicVertex>> hex_lattice;
    BoundaryConditions boundary;
    int n, d;  // lattice dimensions
};
```

### 2. Migration as Commuting Transfer Matrix Evolution

Migration is NOT moving individual rhombi. It's evolution under commuting transfer matrices T₁, T₂, T₃ that preserve the Yang-Baxter integrability:

```cpp
class MigrationOperator {
private:
    Matrix transfer_matrix_A_to_B;
    Matrix transfer_matrix_B_to_C;  
    Matrix transfer_matrix_C_to_A;
    
public:
    // Key: operators commute by Yang-Baxter equation
    Mosaic migrate_flock(const Mosaic& initial, int source_nest, int target_nest) {
        // Apply appropriate transfer matrix
        Matrix T = get_transfer_matrix(source_nest, target_nest);
        
        // Evolution preserves fermion number (content partition)
        Mosaic result = apply_transfer_operator(initial, T);
        
        // Verify commutation relations hold
        assert(verify_yang_baxter_consistency(result));
        return result;
    }
};
```

### 3. Why Standard Order is Insufficient

The synthesis treats "standard order" as a simple tableau sorting, missing the crucial vertex model constraint:

**CRITICAL**: Standard order must respect the **free-fermion constraint**. Two rhombi can only be ordered if their spectral parameters satisfy the R-matrix commutation relation:

```cpp
bool can_order_rhombi(const Rhombus& r1, const Rhombus& r2) {
    // Check R-matrix constraint R₁₂(u₁-u₂) ≠ 0
    complex<double> spec_diff = r1.spectral_param - r2.spectral_param;
    return abs(R_matrix_element(spec_diff)) > EPSILON;
}

vector<int> compute_valid_standard_order(const vector<Rhombus>& rhombi) {
    // Not just tableau order - must satisfy vertex model constraints
    vector<int> order;
    for (int i = 0; i < rhombi.size(); i++) {
        int insert_pos = find_insertion_position_with_R_matrix_constraint(
            order, rhombi, i);
        order.insert(order.begin() + insert_pos, i);
    }
    return order;
}
```

## Corrected Implementation Algorithm

### Phase 1: Puzzle to Vertex Configuration

```cpp
Mosaic puzzle_to_vertex_configuration(const PuzzleBoundary& boundary) {
    // Initialize hex lattice with proper vertex weights
    Mosaic mosaic(boundary.n, boundary.d);
    
    // Set boundary vertex weights from 01-strings
    set_boundary_vertices_from_lattice_paths(mosaic, boundary);
    
    // Fill interior using free-fermion vertex weights
    // Key: Each vertex type has specific R-matrix eigenvalue
    