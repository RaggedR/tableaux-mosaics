# Vertex Model Analysis: KTW Puzzle Migration Implementation

## Assessment of Growth Diagram Approach

The growth diagram framework provides valuable structure, but we're missing the essential vertex model perspective that explains WHY the migration algorithm works. The local hexagonal transformations aren't arbitrary - they satisfy Yang-Baxter relations that guarantee commutativity of the transfer matrices.

## Vertex Model Foundation for Migration

KTW puzzle migration is fundamentally a free-fermionic vertex model where rhombi carry spectral parameters. The hexagonal rotations are vertex weights in an integrable system:

```cpp
struct VertexWeight {
    // R-matrix entry: encodes allowed local configurations
    array<int, 6> edge_states;  // 0/1 labels on hex edges
    double spectral_parameter;  // Controls rhombus "momentum"
    bool is_allowed;           // Yang-Baxter constraint
};

struct TransferMatrix {
    map<Configuration, Configuration> T;
    double spectral_param;
    
    // Commutativity: [T(u), T(v)] = 0 for all u,v
    bool commutes_with(const TransferMatrix& other) const;
};
```

## Critical Insight: Free-Fermion Constraints

The key constraint is that puzzle configurations correspond to free-fermion ground states. This severely restricts which migration paths are valid:

```cpp
struct FermionicState {
    vector<int> partition_shape;  // Young diagram
    vector<int> filling;          // LR tableau content
    
    // Free-fermion condition: determinantal structure
    bool satisfies_lindstrom_gessel_viennot() const {
        // Non-intersecting path constraint
        return check_path_non_intersection();
    }
};

bool is_valid_migration_step(const HexConfig& before, 
                           const HexConfig& after,
                           int rhombus_content) {
    // Yang-Baxter equation ensures this is well-defined
    VertexWeight w = lookup_vertex_weight(before, after);
    
    // Free-fermion constraint: partition differences ≤ 1
    if (!satisfies_partition_growth_rule(w, rhombus_content)) {
        return false;
    }
    
    return w.is_allowed;
}
```

## Spectral Parameter Implementation

Each rhombus carries a spectral parameter that determines its migration behavior:

```cpp
struct SpectralRhombus {
    int content;                    // Tableau entry
    complex<double> spectral_u;     // Controls integrability
    HexCoord position;
    
    // Migration follows eigenvalue evolution
    complex<double> compute_next_position_eigenvalue() const {
        return spectral_u * exp(I * M_PI / 3);  // 60° rotation
    }
};

class CommutingTransferMatrices {
    vector<TransferMatrix> T_matrices;
    
public:
    // Migration preserves commutativity
    bool migrate_preserves_integrability(const SpectralRhombus& rho) const {
        for (size_t i = 0; i < T_matrices.size(); ++i) {
            for (size_t j = i+1; j < T_matrices.size(); ++j) {
                if (!T_matrices[i].commutes_with(T_matrices[j])) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

## Algorithm: Vertex Model Migration

```cpp
LRTableau vertex_model_migration(const KTWPuzzle& puzzle,
                               int source_nest, int target_nest) {
    // Phase 1: Extract spectral rhombi from puzzle
    vector<SpectralRhombus> rhombi = extract_spectral_rhombi(puzzle);
    
    // Phase 2: Initialize commuting transfer matrices
    CommutingTransferMatrices system;
    system.initialize_from_boundary_data(puzzle.boundary);
    
    // Phase 3: Migrate in spectral order (not geometric order!)
    sort(rhombi.begin(), rhombi.end(), 
         [](const SpectralRhom