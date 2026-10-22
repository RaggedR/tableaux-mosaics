# Yang-Baxter Specialist Report: Mathematical Foundations and Implementation Requirements

## Core Mathematical Structure

The generalist's synthesis misunderstands the fundamental mathematical nature of this system. This is NOT merely "geometric movement of rhombi" but a **vertex model with spectral parameters** where migration preserves Yang-Baxter integrability.

### Correcting the Mathematical Framework

**Key Error in Synthesis**: The generalist treats migration as ad-hoc geometric operations. In reality, Purbhoo's construction is a **free-fermion vertex model** where:

1. Each hexagonal vertex has an R-matrix weight
2. Migration preserves the **total weight** (guaranteeing bijection)  
3. The "local hexagonal flips" are **Yang-Baxter moves** with specific spectral parameters

## Required Mathematical Data Structures

```cpp
// Correct vertex model structure
struct VertexWeight {
    array<array<int, 2>, 3> edge_config;  // 3 edges, each 0 or 1
    double spectral_weight;                 // R-matrix entry
    int vertex_type;                       // Determines allowed transitions
};

struct SpectralParameters {
    complex<double> u, v, w;  // Spectral parameters for three boundary regions
    // Migration preserves: u*v*w = constant (free-fermion condition)
};
```

**Why This Matters**: Without tracking spectral weights, you cannot guarantee the migration produces valid LR tableaux. The bijection relies on weight preservation.

## Critical Implementation Requirements

### 1. Vertex Classification System
Each vertex in the hexagonal tiling has one of **exactly 10 types** based on edge configurations. The generalist's "edge_labels" approach cannot distinguish between vertices that require different migration rules.

```cpp
enum VertexType {
    TRIANGLE_000, TRIANGLE_111,           // Triangle tiles
    SQUARE_0011, SQUARE_0110, SQUARE_1001, SQUARE_1100,  // Square orientations  
    RHOMBUS_010, RHOMBUS_101,            // Rhombus in nests
    BOUNDARY_01, BOUNDARY_10             // Boundary vertices
};
```

### 2. R-Matrix Migration Rules
The "local hexagonal flips" must follow **strict R-matrix constraints**:

```cpp
bool is_valid_migration_step(const VertexWeight& before, const VertexWeight& after) {
    // Check Yang-Baxter equation: R12*R13*R23 = R23*R13*R12
    return yang_baxter_check(before.spectral_weight, after.spectral_weight) &&
           partition_difference_constraint(before.edge_config, after.edge_config);
}
```

**The generalist's "deterministic paths" claim is wrong**: Migration paths depend on **spectral parameter matching** at each vertex.

### 3. Free-Fermion Weight Computation
```cpp
double compute_vertex_weight(const VertexWeight& vertex, 
                           const SpectralParameters& params) {
    // Free-fermion weights have specific form
    if (vertex.vertex_type == RHOMBUS_010) {
        return (params.u - params.v) / (params.u + params.v);
    }
    // ... other vertex types have different weight formulas
}
```

## Correcting the Migration Algorithm

### Standard Order is Spectral, Not Geometric
```cpp
vector<HexCoord> compute_spectral_order(const MosaicState& state) {
    vector<pair<complex<double>, HexCoord>> weighted_rhombi;
    
    for (const auto& [pos, rhombus] : state.rhombi) {
        if (state.nest_A.count(pos)) {
            complex<double> spectral_value = 
                compute_eigenvalue(state, pos);  // From transfer matrix
            weighted_rhombi.push_back({spectral_value, pos});
        }
    }
    
    // Sort by SPECTRAL eigenvalue, not tableau entry
    sort(weighted_rhombi.begin(), weighted_rhombi.end(),
         [](const auto& a, const auto& b) {
             return real(a.first) > real(b.first