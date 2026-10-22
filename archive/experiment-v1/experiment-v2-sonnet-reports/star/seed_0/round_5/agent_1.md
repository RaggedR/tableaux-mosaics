# Specialist Report: Fomin Growth Diagrams and KTW Puzzle Structure

## Assessment of Mathematical Synthesis

The generalist's synthesis contains several critical errors that will prevent correct implementation. As a specialist in growth diagrams and face labelings, I must correct the fundamental misunderstanding about the mathematical structure.

## Critical Error Analysis

**Major Problem**: The synthesis completely misses that KTW puzzles ARE growth diagrams with specific local rules. The "migration" is not arbitrary geometric movement—it's the canonical growth diagram construction applied to puzzle pieces.

**The synthesis treats migration as ad-hoc geometric movement when it's actually deterministic face relabeling following Fomin's local rules.**

## Correct Mathematical Framework

### KTW Puzzles as Growth Diagrams

A KTW puzzle of size n naturally embeds in a directed graph where:
- Vertices are intersection points of the triangular lattice
- Edges carry binary labels {0,1} from the puzzle pieces
- Faces are the individual puzzle pieces with their internal structure

**Key Insight**: Each puzzle piece encodes a local rule. The "migration" process is exactly the growth diagram construction moving recording tableaux through the network.

### Correct Data Structure

```cpp
struct GrowthDiagram {
    // Directed graph structure
    map<Vertex, set<Edge>> adjacency;
    map<Edge, int> edge_labels;  // {0,1}
    map<Face, LocalRule> face_rules;
    
    // Recording tableaux at vertices
    map<Vertex, PartialTableau> recording_data;
    
    // Boundary conditions
    Partition lambda, mu, nu;  // Shape constraints
};

struct LocalRule {
    // Input edge labels determine output transformation
    array<int, 3> input_labels;   // Three edges into face
    array<int, 3> output_labels;  // Three edges out of face
    
    // Tableau transformation encoded in face
    function<PartialTableau(PartialTableau)> transform;
};
```

## Why the Synthesis Fails

1. **No Local Rules**: The synthesis has no mechanism to enforce the constraint structure that makes KTW puzzles work. Migration becomes arbitrary movement rather than constraint-preserving transformations.

2. **Missing Recording Data**: KTW migration fundamentally tracks how tableau entries move through the network. The synthesis conflates the geometric rhombi with the abstract tableau data they carry.

3. **Wrong Order**: The "standard order" in the synthesis is geometrically motivated but mathematically wrong. Growth diagrams have a canonical processing order determined by the directed graph structure.

## Correct Migration Algorithm

### Phase 1: Construct Growth Diagram
```cpp
GrowthDiagram puzzle_to_growth_diagram(const KTWPuzzle& puzzle) {
    GrowthDiagram G;
    
    // Each puzzle piece becomes a face with local rule
    for (const PuzzlePiece& piece : puzzle.pieces) {
        Face f = piece.position;
        G.face_rules[f] = extract_local_rule(piece);
    }
    
    // Boundary conditions from puzzle boundary
    set_boundary_tableaux(G, puzzle.boundary_data);
    
    return G;
}
```

### Phase 2: Apply Growth Diagram Rules
```cpp
LRTableau migrate_via_growth_diagram(GrowthDiagram& G) {
    // Topological sort to get processing order
    vector<Face> processing_order = topological_sort(G);
    
    // Apply local rules in order
    for (const Face& f : processing_order) {
        apply_local_rule(G, f);
    }
    
    // Extract final tableau from target boundary
    return extract_boundary_tableau(G, TARGET_NEST);
}
```

### Phase 3: Local Rule Application
```cpp
void apply_local_rule(GrowthDiagram& G, Face f) {
    LocalRule rule = G.face_rules[f];
    
    // Gather input recording data from incident vertices
    vector<PartialTableau> inputs;
    for (Vertex v : incident_vertices(f)) {
        inputs.push_back(G.recording_data[v]);
    }
    
    // Apply the face transformation
    auto outputs = rule.transform(inputs);
    
    