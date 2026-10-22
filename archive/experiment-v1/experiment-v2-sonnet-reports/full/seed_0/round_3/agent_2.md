# Report: Implementing KTW Puzzle → LR Tableau Bijection via Vertex Models

## Analysis of Previous Approaches

The previous reports correctly identify Purbhoo's three-phase structure but miss a crucial insight: this bijection can be implemented more directly using **free-fermionic vertex model theory**. Rather than tracking complex geometric transformations, we can exploit the Yang-Baxter structure underlying both KTW puzzles and LR tableaux.

## Vertex Model Foundation

**Key Insight**: Both KTW puzzles and LR tableaux arise as configurations of the same vertex model - they're different boundary conditions of identical transfer matrices. The "migration" is actually a sequence of Yang-Baxter moves that preserve spectral parameters.

### Vertex Weights and R-matrices

The fundamental vertex has 4 edges (north, east, south, west) with states 0 or 1:
```
VertexState {
    north: bool
    east: bool  
    south: bool
    west: bool
}
```

The **free-fermionic condition** means valid vertices satisfy:
- Conservation: north + west = south + east (mod 2)
- Yang-Baxter weight: w(n,e,s,w) ∈ {0,1} depends only on fermion parity

This gives us exactly 6 allowed vertices, which correspond to:
- KTW puzzle pieces (when viewed in triangular coordinates)
- LR tableau local rules (when viewed in rectangular coordinates)

### Transfer Matrix Commutativity

The bijection exists because **transfer matrices commute**:
```
T_horizontal * T_vertical = T_vertical * T_horizontal
```

This commutativity is what guarantees the growth diagram is well-defined.

## Implementation Strategy

### Data Structure: Growth Diagram
```
struct GrowthStep {
    input_partitions: (λ, μ)  // Two Young diagrams
    output_partitions: (λ', μ')
    vertex_config: VertexState  // The 4-edge vertex
}

struct BijectivePath {
    steps: List[GrowthStep]
    weight: int  // Always 1 for LR coefficients
}
```

### Algorithm: Direct Bijection Construction

**Phase 1**: Parse KTW puzzle as vertex configuration
```python
def parse_puzzle_to_vertices(puzzle_pieces):
    vertices = {}
    for position in triangular_grid:
        # Each puzzle piece determines vertex states in local region
        vertex_state = determine_vertex_from_puzzle_pieces(position)
        vertices[position] = vertex_state
    return vertices
```

**Phase 2**: Execute growth diagram
```python
def construct_growth_diagram(vertices, boundary_data):
    # Start with empty partitions
    current_lambda = empty_partition()
    current_mu = empty_partition()
    
    tableau_entries = {}
    
    # Process vertices in "northeast" order
    for position in northeast_order(vertices.keys()):
        vertex = vertices[position]
        
        # Apply local growth rule
        (new_lambda, new_mu, tableau_entry) = apply_growth_rule(
            current_lambda, current_mu, vertex
        )
        
        if tableau_entry is not None:
            tableau_entries[position] = tableau_entry
            
        current_lambda = new_lambda
        current_mu = new_mu
    
    return construct_LR_tableau(tableau_entries)
```

**Phase 3**: Growth rule implementation
```python
def apply_growth_rule(lambda_in, mu_in, vertex_state):
    # The vertex state determines how partitions grow
    if vertex_state == VERTEX_TYPE_A:
        # Add box to λ partition
        lambda_out = lambda_in.add_box_at_northeast()
        mu_out = mu_in
        return (lambda_out, mu_out, lambda_in.height())
        
    elif vertex_state == VERTEX_TYPE_B:
        # Add box to μ partition  
        lambda_out = lambda_in
        mu_out = mu_in.add_box_at_northeast()
        return (lambda_out, mu_out, mu_in.height())
        
    # Handle other vertex types...
```

## Concrete Implementation for Test