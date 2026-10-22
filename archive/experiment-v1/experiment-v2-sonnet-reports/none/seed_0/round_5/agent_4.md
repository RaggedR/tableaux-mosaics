## Wake Crossing Mechanics: The Missing Algorithm Core

You're absolutely right - I completely missed the **algorithmic heart** of migration. Let me dissect what the Wake Crossing Lemma actually means for implementation:

### The Wake Tracking System is Everything

The paper's Figure 7 (wake diagram) reveals the true migration algorithm:

```
CRITICAL_INSIGHT: Migration isn't "move rhombus right" - it's:
1. Rhombus creates 2-tile-wide displacement path (wake)
2. Wake persists as constraint for ALL subsequent rhombi  
3. Later rhombi can't cross intact wakes
4. This creates a DEPENDENCY GRAPH, not just ordering
```

**Implementation Reality**: We need a **wake collision detection system**:

```cpp
struct WakeSegment {
    Point start, end;
    bool is_upper;  // upper vs lower wake
    Rhombus* owner;
    set<Tile*> displaced_tiles;
};

class WakeTracker {
    vector<WakeSegment> active_wakes;
    
    bool can_cross_midline(Rhombus* r, Point current_pos) {
        for (auto& wake : active_wakes) {
            if (wake.intersects(current_pos) && wake.is_intact()) {
                return false;  // Wake Crossing Lemma violation
            }
        }
        return true;
    }
};
```

### The Canonical Flock Mystery - My Biggest Miss

From Lemma 2.7: "there is a unique function f which makes F = (α, (E,N), f) a flock"

**What I completely missed**: This isn't just assigning numbers - it's reconstructing the **tableau filling order** from geometric position!

The key insight: In orientation (E,N), the "standard order" on rhombi corresponds to **reverse reading order** of the tableau. The canonical flock algorithm must be:

```cpp
LR_Tableau compute_canonical_flock(vector<Rhombus> rhombi, Orientation orient) {
    // Step 1: Sort rhombi by standard order in given orientation
    sort(rhombi, standard_order_comparator(orient));
    
    // Step 2: This is the MISSING ALGORITHM
    // Somehow map geometric positions → tableau entries
    // Such that LR conditions (i,ii,iii) are satisfied
    
    // The paper says this is "straightforward" but HOW?
}
```

### What I Must Explore Next

**Priority 1: Reverse-engineer the canonical flock algorithm**

The paper gives examples (Figure 5) but no algorithm. I need to:
- Study how rhombi positions in French notation map to tableau entries
- Figure out how the orientation (E,N) determines the filling pattern
- Work out the "standard order" comparison function geometrically

**Priority 2: Wake path computation**

From the Wake Crossing Lemma proof: wakes are determined by the sequence of hexagon rotations. I need:
- Algorithm to compute wake boundaries from hexagon flip sequence
- Midline tracking as rhombi move
- Wake intersection detection

**Priority 3: The missing test case verification**

For c^(3,2,1)_{(2,1),(2,1)} = 2, I need to:
- Build both KTW puzzles explicitly 
- Show their mosaic conversions differ in rhombi placement
- Trace through migration to get different LR tableaux
- Verify the tableaux have correct boundary data

### The Hardest Missing Piece

**Question**: In Figure 5 (canonical flock example), the rhombi arrangement produces flock content (4,4,2,1,1). But **what's the actual function f: rhombi → ℕ**?

The paper shows the content but not which rhombus gets which number. This mapping is the **bijection's foundation** - without it, I can't implement anything.

**My hypothesis**: The canonical flock uses **hook-length formula** or similar Young tableau filling, but applied to the transformed (non-orthogonal) diagram coordinates. This would explain why it's "straightforward" - it's standard tableau theory in skewed coordinates.

**Next exploration target**: Extract the rhombus→entry mapping from the geometric constraints.