# Initial Analysis: Purbhoo's Mosaic Migration Bijection

## Problem Overview

I need to specify an algorithmic implementation of Purbhoo's bijection between Knutson-Tao-Woodward (KTW) puzzles and Littlewood-Richardson (LR) tableaux. The bijection has three phases:

1. **Puzzle → Mosaic**: Convert triangular puzzle tiling to hexagonal mosaic tiling
2. **Migration**: Move rhombi through local hexagonal transformations 
3. **Mosaic → Tableau**: Extract LR tableau from final rhombi positions

## Key Mathematical Objects

**KTW Puzzle**: Tiling of equilateral triangle with three piece types (each with 0/1 edge labels):
- Unit triangles 
- Unit rhombi with 30°/150° angles
- Boundary constraint: adjacent pieces must have matching edge labels

**Mosaic**: Tiling of hexagon with:
- Unit triangles
- Unit squares  
- Unit rhombi (30°/150° angles) packed in three corner "nests"

**Migration**: Sequence of local moves that transport rhombi between nests while preserving a tableau structure.

## Test Case Verification
The coefficient c^(3,2,1)_{(2,1),(2,1)} = 2 means there should be exactly 2 puzzles with:
- Boundary strings with 2 ones each
- Total constraint ensuring valid puzzle existence

Each puzzle should yield a distinct LR tableau through migration.

## Critical Implementation Challenges

1. **Coordinate Systems**: Need precise geometric representation of hexagonal regions, rhombi orientations, and nest boundaries
2. **Migration Algorithm**: The "hexagonal flip" operations require careful specification of when/how rhombi move
3. **Tableau Extraction**: Converting final rhombi positions to standard LR tableau format

## Next Steps Needed

The paper provides theoretical framework but lacks algorithmic details. I need to:
- Specify exact data structures for puzzles, mosaics, rhombi
- Detail the geometric transformations for puzzle→mosaic conversion
- Algorithmically describe migration as a sequence of local operations
- Define the final tableau readout process

The coding agent will need concrete procedures, not just the mathematical bijection proof.