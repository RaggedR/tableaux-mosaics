# Vertex Model Analysis: Yang-Baxter Structure and Free-Fermion Constraints

## CRITICAL CHALLENGE: The Problem Misses the Integrable Structure

The proposed "row transfer matrix" for KTW puzzles fundamentally misunderstands the role of transfer matrices in integrable systems. **True transfer matrices arise from R-matrices satisfying the Yang-Baxter equation** - they don't emerge from arbitrary row-by-row constructions on combinatorial objects.

## The Free-Fermion Connection That's Being Ignored

Zinn-Justin's work reveals the crucial insight: **Littlewood-Richardson coefficients emerge from interacting fermion models, not free fermions**. The puzzle structure corresponds to a vertex model where:

- Each puzzle piece encodes specific vertex weights
- The spectral parameters encode the boundary partition data  
- Commutativity of transfer matrices guarantees well-defined enumeration

The "12 free nabla choices → 3 tableau entries" compression isn't a computational inefficiency - it's the **signature of non-trivial fermion interactions** that distinguish LR coefficients from simpler free-fermion enumerations.

## Yang-Baxter Obstruction to Direct Growth Diagrams

**Key Technical Point**: Growth diagrams work for RSK-type constructions because they correspond to **free-fermion vertex models** where the R-matrix is trivial (up to spectral parameters). But KTW puzzles encode interacting fermions with non-trivial R-matrix structure.

The hexagonal flip operations in Purbhoo's migration aren't arbitrary local moves - they correspond to **Yang-Baxter transformations** that preserve the underlying fermion correlation structure. Any "direct" bijection would need to encode these R-matrix relations, but growth diagram face labels cannot capture this complexity.

## Spectral Parameter Analysis Missing

The reports completely ignore how spectral parameters would work in the proposed transfer matrix. In integrable tiling models:

- Boundary conditions set spectral parameter ratios
- Transfer matrix eigenvalues generate partition functions
- **Commutativity requires specific vertex weight relationships**

For the c^(3,2,1)_{(2,1),(2,1)} example, the spectral parameters would encode (3,2,1), (2,1), (2,1) as boundary data. The "row transfer matrix" construction gives no mechanism for how these parameters propagate through the puzzle interior.

## Alternative Framework: Cylindric Vertex Models

Instead of seeking impossible growth diagrams, consider: **Can KTW puzzles be realized as partition functions of vertex models on cylindric geometries?**

This connects to the six-vertex model with domain wall boundary conditions, where:
- Puzzle boundary data becomes domain wall configuration
- Interior puzzle constraints become vertex weights  
- Migration corresponds to transfer matrix time evolution
- LR tableaux emerge from fermion correlation functions

## The Real Obstruction: Non-Additive Structure

The fundamental issue is that **LR coefficients are multiplicative, not additive** in their combinatorial realization. Growth diagrams work for additive structures (like RSK insertion lengths), but puzzle piece constraints interact multiplicatively through the Yang-Baxter relations.

The 24→3 compression ratio signals that puzzle degrees of freedom are **highly constrained by integrability conditions** - most of the 24 apparent choices are actually forbidden by Yang-Baxter consistency requirements.

## Technical Verdict

The conjecture fails because it seeks to replace an **integrable vertex model** (encoded in Purbhoo's migration) with a **non-integrable growth process**. The transfer matrix commutativity that makes LR coefficients well-defined cannot be maintained in the proposed framework.

**Recommendation**: Focus on understanding how Purbhoo's migration encodes R-matrix transformations, rather than seeking to eliminate this essential integrable structure.