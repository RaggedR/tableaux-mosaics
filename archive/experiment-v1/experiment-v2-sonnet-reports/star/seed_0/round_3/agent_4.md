# Computational Implementation Report: Purbhoo Migration Algorithm

## Executive Summary for Coding Agent

The generalist's synthesis misses critical implementation details. I'll provide concrete algorithms, data structures, and worked examples for the full bijection. The core insight: migration is a sequence of **hexagonal rotations** that preserve **standard tableau order**.

## Essential Data Structures

```cpp
struct HexCoord {
    int q, r, s;  // cube coordinates, q+r+s=0
    HexCoord(int q, int r) : q(q), r(r), s(-q-r) {}
};

struct Rhombus {
    HexCoord center;
    int orientation;  // 0=horizontal, 1=+60°, 2=+120°
    int label;        // tableau entry
};

struct Mosaic {
    vector<Rhombus> rhombi_A, rhombi_B, rhombi_C;  // three boundary regions
    set<HexCoord> triangles, squares;               // interior tiles
    int n, d;
};

struct LRTableau {
    vector<vector<int>> shape;  // Young diagram as 2D array
    map<pair<int,int>, int> entries;  // (row,col) -> tableau value
};
```

## Algorithm 1: Puzzle to Mosaic Conversion

**Input**: Three boundary strings π, ρ, σ of length n with d ones each
**Output**: Mosaic with rhombi packed in three nests

```cpp
Mosaic puzzle_to_mosaic(string pi, string rho, string sigma) {
    Mosaic M;
    M.n = pi.length();
    M.d = count(pi.begin(), pi.end(), '1');
    
    // Convert each 01-string to Young diagram via lattice path
    auto lambda = string_to_partition(pi);
    auto mu = string_to_partition(rho);  
    auto nu = string_to_partition(sigma);
    
    // Pack partitions as rhombi in hexagonal nests
    M.rhombi_A = pack_partition_in_nest(lambda, NEST_A);
    M.rhombi_B = pack_partition_in_nest(mu, NEST_B);
    M.rhombi_C = pack_partition_in_nest(nu, NEST_C);
    
    // Fill interior with canonical tiling
    M.triangles = compute_interior_triangles(M);
    M.squares = compute_interior_squares(M);
    
    return M;
}

vector<int> string_to_partition(const string& s) {
    vector<int> partition;
    int current_height = 0;
    
    for (char c : s) {
        if (c == '1') current_height++;
        else if (current_height > 0) {
            partition.push_back(current_height);
            current_height--;
        }
    }
    
    // Pad with zeros to length d
    while (partition.size() < d) partition.push_back(0);
    return partition;
}
```

## Algorithm 2: Migration (Core Bijection)

**Key Insight**: Migration moves rhombi via **local hexagonal flips** while preserving **standard order**.

```cpp
LRTableau migrate_flock_A_to_tableau(Mosaic& M) {
    // Step 1: Compute standard order on rhombi_A
    vector<int> order = compute_standard_order(M.rhombi_A);
    
    // Step 2: Migrate each rhombus in order via hexagonal rotations
    for (int idx : order) {
        migrate_single_rhombus(M, M.rhombi_A[idx], NEST_A, NEST_B);
    }
    
    // Step 3: Read tableau from final positions in nest B
    return read_tableau_from_nest(M.rhombi_B, M.rhombi_A);
}

void migrate_single_rhombus(Mosaic& M, Rhombus& rho, int from_nest, int to_nest) {
    HexCoord pos = rho