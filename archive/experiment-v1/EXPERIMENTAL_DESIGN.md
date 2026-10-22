# Experimental Design

## The Problem

An open question in algebraic combinatorics: does the row transfer
matrix for Knutson-Tao-Woodward (KTW) puzzles define a growth diagram
whose face labels give a direct bijection between puzzles and
Littlewood-Richardson tableaux?

Four specialist Claude Opus agents debate this question under three
communication structures.

## Agents

| Agent | Specialism | Papers |
|-------|-----------|--------|
| Growth Diagram | Fomin growth diagrams, local rules, face labels | Purbhoo, Knutson-Tao (2003) |
| Yang-Baxter | Yang-Baxter equation, vertex models, transfer matrices | Purbhoo, Zinn-Justin (2009 tilings, 2009 survey, 2024) |
| Bijection | Purbhoo's migration bijection, jeu de taquin, mosaics | Purbhoo, Knutson-Tao (2003) |
| Computational | Enumeration, verification, numerical experiments | Purbhoo, lr_coefficients.py, solve_puzzle.py, transfer_operators.py |

All agents use negative coupling ("challenge and extend").

## Communication Structures

At the end of each round, every agent writes a **report**. The
communication structure determines which reports each agent reads at
the start of the next round.

### None (baseline)

Each agent reads only its own previous report. No cross-pollination.

```
Round 1:  A writes report    B writes report    C writes report    D writes report
Round 2:  A reads A_r1       B reads B_r1       C reads C_r1       D reads D_r1
          A writes report    B writes report    C writes report    D writes report
...
```

4 agents, 0 arcs. Each agent iterates on its own ideas independently.
This measures the natural diversity of four specialists working alone
on the same problem.

### Chain (labelled "ring" in GA literature)

Agents execute sequentially. Each reads its left neighbour's most
recent report.

```
Round 1:  A (no input) -> B (reads A_r1) -> C (reads B_r1) -> D (reads C_r1)
Round 2:  A (reads D_r1) -> B (reads A_r2) -> C (reads B_r2) -> D (reads C_r2)
Round 3:  A (reads D_r2) -> B (reads A_r3) -> ...
```

4 agents, 4 arcs (directed cycle). Round 1 is a chain (A starts
cold). The cycle closes from round 2 onward, but information is
always staggered by one round — the topology is a spiral, not a
closed cycle.

### Star (orchestrated parallel)

Two layers per round. First the hub reads all specialists' reports
and writes a synthesis. Then all specialists read the hub's synthesis
and write their reports in parallel.

```
Round 1:
  Layer 1:  Hub (no input) writes synthesis
  Layer 2:  A (reads Hub_r1)    B (reads Hub_r1)    C (reads Hub_r1)    D (reads Hub_r1)
            all write reports in parallel

Round 2:
  Layer 1:  Hub reads A_r1, B_r1, C_r1, D_r1, writes synthesis
  Layer 2:  A (reads Hub_r2)    B (reads Hub_r2)    C (reads Hub_r2)    D (reads Hub_r2)
            all write reports in parallel
```

5 agents (4 specialists + 1 generalist hub), 8 arcs (4 in to hub +
4 out from hub). Specialists never see each other directly. All
cross-pollination passes through the hub.

## Known Confounds

The three conditions differ in multiple ways simultaneously:

| Property | None | Chain | Star |
|----------|------|-------|------|
| Arcs | 0 | 4 | 8 |
| Agents | 4 | 4 | 5 |
| Execution | Parallel | Sequential | Hub sequential, specialists parallel |
| Feedback round | N/A | Round 2 | Round 2 |
| Information filtering | None | None (raw predecessor) | Hub synthesises |

We cannot attribute diversity differences to any single factor. In
particular, the star condition includes a fifth agent (the hub) that
synthesises all specialists' reports before broadcasting. Star
agents receive curated, processed input; chain agents receive one
raw predecessor's output. Higher star diversity may reflect the
synthesis step rather than the topology. The experiment tests these
communication structures as practitioners would use them, not
isolated topological properties.

## Parameters

| Parameter | Value |
|-----------|-------|
| Model | Claude Opus |
| Rounds | 5 |
| Seeds | 10 per condition |
| Coupling | Negative ("challenge and extend") |
| Max tokens per report | 800 |
| Conditions | 3 (none, chain, star) |
| Total runs | 30 |
| Estimated cost | ~$15-20 |

## Evaluation

Diversity is measured as **mean pairwise cosine distance** on
sentence embeddings of agent reports within each round.

Embedding model: **all-MiniLM-L6-v2** (384-dimensional, L2-normalised).
For each round, all specialist reports are embedded (the hub's report
is excluded from the star condition to keep agent count consistent
at 4). Cosine distance = 1 - dot product of normalised embeddings.
The mean across all 6 pairs (4 choose 2) gives a single diversity
score per round.

This metric is deterministic, free to compute, and matches the
metric used in the coding-task experiment. Its limitation: it
measures vocabulary diversity, not necessarily idea diversity. Two
agents could describe the same mathematical idea in different
notation and appear "diverse," or describe genuinely different ideas
in similar language and appear "similar."

### Measurements

- **Diversity score**: mean pairwise cosine distance per round
- **Diversity fingerprint**: the trajectory of diversity scores over
  5 rounds
- **Temporal crossover**: does star start higher and chain overtake?
- **Baseline comparison**: how does none's diversity compare to chain
  and star at each round?

### Cost

- Agent calls: ~850 × ~$0.003 (Sonnet) = ~$2.50
- Evaluation: free (local computation)
- Total: ~$5-8 (context grows with rounds)

## Conjecture

**Star higher early, chain higher later.** The star's hub broadcasts
a synthesis to all specialists simultaneously, producing higher
early diversity through wider bandwidth. But the hub is an
information compressor: it turns four perspectives into one framing,
and all specialists respond to that one framing. Over rounds, this
homogenises. The chain has no such bottleneck — each specialist
hears a different predecessor, so local threads develop independently
and diversity is preserved longer.

The "none" baseline tells us whether the chain is *preserving*
diversity or the star is *destroying* it.

This conjecture is consistent with GA experiments (ring > star for
diversity at later generations) and with a single-run LLM pilot that
showed the same temporal crossover. But both previous results are
confounded, and the LLM coding-task experiment (which had no feedback
cycles) showed that GA predictions do not straightforwardly transfer
to LLM agents.
