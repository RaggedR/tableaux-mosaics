# Initial Analysis: Implementing Purbhoo's Mosaic Migration Bijection

## Problem Overview
I need to specify how to implement the three-step bijection from KTW puzzles to Littlewood-Richardson tableaux:
1. **Puzzle → Mosaic conversion**: Transform triangular puzzle tiling into hexagonal mosaic
2. **Migration algorithm**: Move rhombi through local hexagonal operations  
3. **Mosaic → LR tableau extraction**: Read final tableau from migrated configuration

## Key Technical Challenges

### 1. Coordinate Systems & Representation
The paper uses multiple coordinate systems that need careful implementation:
- **Puzzle coordinates**: Equilateral triangular grid with 60°/120° rhombi pieces
- **Mosaic coordinates**: Hexagonal region with three "nests" (corner regions) containing 150°/30° rhombi
- **Standard diagram coordinates**: Rectangular Young diagram format for final LR tableaux

### 2. Migration Algorithm Specification
The migration process involves:
- **Flock identification**: Find "accessible" rhombi collections that form valid skew diagrams
- **Local hexagonal flips**: Two types of 6-tile local transformations (2-fold and 3-fold rotational)
- **Standard order traversal**: Process rhombi in specific tableau-theoretic order
- **Orientation tracking**: Handle how compass directions rotate during migration

### 3. Data Structure Requirements
Need to represent:
- **Tilings**: Collections of positioned geometric pieces (triangles, squares, rhombi)
- **Orientations**: Vector pairs (E,N) that define "east" and "north" directions locally
- **Flocks**: Triples (shape, orientation, labeling function) representing tableau-like structures on rhombi
- **Boundary data**: The partition/string data that labels puzzle boundaries

## Test Case Analysis
For c^(3,2,1)_{(2,1),(2,1)} = 2, I need to:
- Handle two distinct input puzzles with boundary strings encoding partitions (3,2,1), (2,1), (2,1)
- Verify each produces a different LR tableau of shape (3,2,1)/(2,1) with content (2,1)
- Ensure the migration paths are well-defined and deterministic

## Critical Implementation Gaps
The paper provides theoretical guarantees but lacks algorithmic details for:
- Explicit puzzle-to-mosaic coordinate transformation
- Step-by-step hexagonal flip recognition and execution
- Concrete flock accessibility checking
- Final tableau extraction from rhombi positions

My report must bridge these gaps with concrete data structures and algorithms a coding agent can directly implement.