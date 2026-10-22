# Migration Algorithm Specialist Report

## Critical Assessment: The Generalist Missed the Core Mechanism

The generalist's attempt reveals **fundamental misunderstanding** of migration. As a specialist in Purbhoo's bijection, I must correct several critical errors and provide the precise algorithmic details.

## Major Corrections Required

### Error 1: Migration is NOT "transport of individual rhombi"
**Correction**: Migration is a **sequence of jeu de taquin slides**. The rhombi don't "move" - they represent tableau entries that slide through the ambient tiling structure.

### Error 2: Wrong data structure approach
**Correction**: We need **growth diagram faces**, not geometric coordinates. The bijection works because each migration step corresponds to a single jdt slide.

## Correct Implementation Framework

### Core Data Structures
```cpp
struct TableauEntry {
    int value;
    int row, col;  // position in skew shape
};

struct FlockData {
    vector<TableauEntry> entries;
    SkewShape shape;  // λ/μ for some partitions λ,μ
    Orientation orient;  // (E,N) vectors
};

struct MosaicState {
    FlockData nests[3];  // A, B, C positions
    int n, d;
};
```

### The True Migration Algorithm

Migration is **NOT** moving rhombi through hexagons. It's applying the **reading order bijection** between:
1. Flock entries in nest A (puzzle rhombi)  
2. Standard tableau entries (LR tableau)

```cpp
LRTableau migrate_puzzle_to_tableau(const PuzzleBoundary& boundary) {
    // Step 1: Extract nest A rhombi as flock
    FlockData flock_A = extract_flock_from_boundary(boundary.alpha, 
                                                   Orientation(-E_A, -N_A));
    
    // Step 2: The bijection IS the jdt slide sequence
    LRTableau result;
    result.shape = complement_shape(boundary.gamma);  // λ = γ^∨
    result.inner_shape = boundary.beta;               // μ = β
    
    // Step 3: Apply jdt slides in tableau reading order
    for (const auto& entry : flock_A.entries) {
        jdt_slide_to_position(result, entry.value, entry.target_position);
    }
    
    return result;
}
```

## Algorithmic Details for jdt_slide_to_position

This is where the "migration" actually happens:

```cpp
void jdt_slide_to_position(LRTableau& tab, int value, Position target) {
    Position current = find_empty_corner(tab.shape, tab.inner_shape);
    
    while (current != target) {
        // Find the "minimal hexagon" - this is the jdt sliding rule
        Direction slide_dir = determine_slide_direction(tab, current, target);
        
        if (slide_dir == EAST) {
            // Slide east: swap with entry to the right
            swap_entries_horizontally(tab, current);
            current.col++;
        } else if (slide_dir == NORTH) {
            // Slide north: swap with entry above
            swap_entries_vertically(tab, current);
            current.row++;
        }
        
        // Verify LR property maintained
        assert(satisfies_LR_rule(tab));
    }
    
    tab.set_entry(target, value);
}
```

## Test Case Implementation: c^(3,2,1)_{(2,1),(2,1)} = 2

**Boundary data for the two puzzles**:
- n=6, d=3 (since |π|=|ρ|=|σ|=6, each has 3 ones)
- Puzzle 1: (π₁, ρ₁, σ₁) 
- Puzzle 2: (π₂, ρ₂, σ₂)

```cpp
void test_case_implementation() {
    // The two puzzles with boundary:
    // α corresponds to content (3,2,1)
    // β corresponds to inner shape (2,1)