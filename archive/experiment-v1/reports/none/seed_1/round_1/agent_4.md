## Computational Analysis: Growth Diagram Conjecture for KTW Puzzles

**CRITICAL GAPS AND CHALLENGES**

The conjecture assumes a direct bijection exists via growth diagrams, but this bypasses fundamental structural differences between puzzles and LR tableaux that make such directness questionable.

### 1. **Dimensional Mismatch Problem**

The example c^(3,2,1)_{(2,1),(2,1)} = 2 reveals a critical scaling issue:
- 2 puzzles × 12 free nabla choices = 24 total puzzle configurations
- But only 3 LR tableau entries per puzzle = 6 tableau data points

This 4:1 ratio suggests the transfer matrix encodes far more information than needed for direct tableau reconstruction. The conjecture needs to address how this excess information gets "compressed" in a growth diagram setting.

### 2. **Transfer Matrix Structure vs. Growth Dynamics**

Standard growth diagrams (RSK-type) have local increment rules where each face represents a single combinatorial operation. However, puzzle transfer matrices encode:
- Global boundary conditions (λ, μ, ν shapes)  
- Non-local rhombi connectivity constraints
- Color consistency across multiple rows

**Computational Test**: Run `lr_coefficients.py` and `solve_puzzle.py` on the (3,2,1) example to extract the explicit transfer matrix entries. Check if these matrices exhibit the locality properties required for growth diagram interpretation.

### 3. **Alternative Computational Framing**

Rather than seeking direct bijection, consider **spectral analysis**:
- The transfer matrix eigenvalues/eigenvectors might encode LR tableau statistics
- Fock space operators in `transfer_operators.py` could reveal hidden symmetries
- The "migration NOT working" in `mosaic.py` suggests algorithmic bottlenecks that growth diagrams might circumvent

### 4. **Verification Strategy**

The conjecture requires three-level validation:

**Level 1**: Verify transfer matrix entries match known LR coefficients
```python
# Extract all c^λ_{μν} for small cases
# Compare row-sums with LR numbers
```

**Level 2**: Check growth diagram axioms
- Face labels must satisfy local consistency
- Boundary conditions must encode (λ,μ,ν)
- Growth paths should enumerate tableaux

**Level 3**: Bijection verification
- Each puzzle→face-label-sequence should be injective
- Reconstruction algorithm from faces→LR tableau should be explicit

### 5. **Computational Experiments**

1. **Eigenvalue Analysis**: Compute transfer matrix spectra for small puzzles. Growth diagrams typically have simple eigenvalue patterns.

2. **Path Enumeration**: For each puzzle, trace its row-by-row solution and record intermediate "growth states." Check if these states have natural tableau interpretations.

3. **Local Rule Discovery**: If growth diagrams exist, local rules should emerge. Use pattern matching on solved puzzles to identify candidate rules.

### 6. **Fundamental Objection**

The Purbhoo construction (puzzle→mosaic→migration→LR tableau) succeeds precisely because it respects the **geometric nature** of the bijection. Puzzles live in tiling space; LR tableaux live in Young diagram combinatorics. The migration algorithm performs necessary geometric-to-combinatorial translation.

Growth diagrams, being inherently combinatorial, might lack the geometric flexibility needed for direct translation. The conjecture may be asking for a "coordinate-free" map between objects that fundamentally require coordinate transformations.

**VERDICT**: The conjecture appears unlikely without additional structure. The dimensional mismatch and geometric-combinatorial divide suggest that Purbhoo's indirect route via mosaics/migration is not just convenient but **necessary**. 

**Next Step**: Compute explicit examples to quantify these structural obstructions.