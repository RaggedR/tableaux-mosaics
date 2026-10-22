## Refined Analysis of Purbhoo's Mosaic Migration Implementation

The previous researcher made significant progress but contains critical errors that would lead to incorrect implementation. Let me provide the correct analysis based on careful reading of Purbhoo's paper.

### Critical Corrections

#### 1. **Puzzle-to-Mosaic Conversion: The Correct Physical Process**

The previous report's rhombus orientation mapping is incorrect. Purbhoo describes a specific physical transformation:

**Correct Algorithm**:
1. Remove all rhombi from the puzzle (keep triangles fixed)
2. Convert squares to flexible rhombi with hinges at corners
3. Pull corners A', B', C' outward until boundary straightens
4. During this process:
   - Edges rotate either clockwise (→ label 0) or counterclockwise (→ label 1)
   - Squares become 30°/150° rhombi in the mosaic
   - The hexagon naturally forms with 150° angles at A, B, C

**Key insight**: This isn't about mapping individual puzzle pieces to mosaic pieces based on labels. It's about tracking which edges rotate which direction during the straightening process.

#### 2. **Flock Formation and Labeling**

The previous report has the orientation backwards. From the paper:

**For the canonical flock on α with orientation (-E_A, -N_A)**:
- The flock represents the identity element
- Labels increase moving northwest (in the -E_A direction) and northeast (in the -N_A direction)

**Correct labeling algorithm**:
```
1. Order rhombi by their position in the transformed diagram α
2. In orientation (-E_A, -N_A), this means:
   - Primary sort: northeast to southwest (increasing in -N_A direction)
   - Secondary sort: northwest to southeast (increasing in -E_A direction)
3. Assign label k to the k-th rhombus in this order
```

This creates a flock where labels strictly increase northward and weakly increase eastward in the (-E_A, -N_A) orientation.

#### 3. **Migration Algorithm: The Key Details**

The previous report misunderstands hexagon finding. From Purbhoo:

**Finding the minimal hexagon**:
1. For rhombus ρ, look "to the right" (in migration direction)
2. Find the minimal hexagon that is "entirely weakly right of the leftmost point on ρ"
3. This hexagon may appear above or below ρ, not just directly right

**Type determination**:
- Type A: 2-fold rotational symmetry → rotate 180°
- Type B: 3-fold rotational symmetry → rotate 120°
  - Choose rotation so "some edge of the rhombus ends up exactly horizontal, or exactly vertical"
  - In the mosaic coordinate system, this means parallel to one of the three tile directions

#### 4. **Standard Order and Wake Preservation**

The paper defines standard order precisely:

**Standard order <_f on a flock**:
- X <_f Y if f(X) < f(Y), OR
- X <_f Y if f(X) = f(Y) and X is west/northwest of Y

**Wake mechanics**:
```
When rhombus ρ migrates:
1. Create wake = path of displaced tiles
2. wake_upper = tiles above ρ's midline
3. wake_lower = tiles below ρ's midline

For later rhombus σ:
- If σ starts above ρ's midline AND wake_upper[ρ] intact:
  → σ cannot cross below midline during its journey
  → Preserves relative vertical positions
```

#### 5. **Reading the LR-Tableau**

After migration from A to B:

**The resulting configuration**:
1. Rhombi at B form a skew shape in the (E_B, N_B) orientation
2. The function f' on migrated rhombi preserves values: f'(ρ') = f(ρ)
3. This directly gives an LR-tableau because:
   - Rows increase (migration preserves east-west order)
   - Columns strictly increase (wake lemma preserves north-south order)
   - LR-word property holds (by the specific migration order)

### Implementation Data