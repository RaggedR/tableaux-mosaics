# Findings: Topology-Diversity Experiment (Purbhoo Bijection)

## Setup

Four Claude Opus agents write implementation reports for Purbhoo's mosaic migration bijection (puzzle -> mosaic -> migration -> LR-tableau). Each agent reads the same paper (Purbhoo 2008, Sections 2-4 as LaTeX source). Reports are measured for semantic diversity using mean pairwise cosine distance (all-MiniLM-L6-v2 embeddings).

Two communication topologies: **chain** (ring, each agent reads predecessor) and **star** (hub synthesizes, specialists respond to hub).

Test case: c^(3,2,1)_{(2,1),(2,1)} = 2.

## Finding 1: Specialist prompts are the source of diversity, topology determines its fate

| Round | Specialist Chain | Specialist Star | Generic Chain | Generic Star |
|-------|-----------------|-----------------|---------------|--------------|
| 1     | 0.371           | 0.236           | 0.189         | 0.128        |
| 2     | 0.354           | 0.529           | 0.218         | 0.243        |
| 3     | 0.423           | 0.362           | 0.157         | 0.130        |
| 4     | —               | —               | 0.180         | 0.176        |
| 5     | —               | —               | 0.078         | 0.089        |

With generic prompts (all agents identical), diversity collapses to ~0.08 by round 5 regardless of topology. Chain and star are indistinguishable.

With specialist prompts (growth diagrams, vertex models, bijection, computational), diversity is roughly 2x higher and the topology effect appears: chain > star by round 3.

**Interpretation:** The specialist prompts inject initial diversity — different lenses on the same paper. The topology then determines whether that diversity is preserved (chain) or compressed (star). Without the initial diversity, topology has nothing to act on.

This is analogous to the GECCO GA result: migration topology determines diversity dynamics, but only if the population has genetic variation to begin with. A homogeneous population stays homogeneous regardless of topology.

## Finding 2: Chain > star by final round (replicates GECCO)

Three independent experiments now show chain/ring > star by the final round:

| Experiment | Task | Model | Chain final | Star final |
|-----------|------|-------|-------------|------------|
| topology-debate (May 5) | Growth diagram conjecture | Opus + RAG | 0.437 | 0.362 |
| sandbox specialist (May 12) | Bijection implementation | Opus + full paper | 0.423 | 0.362 |
| GECCO paper (6 domains) | GA optimization | Bitstring GAs | ring > star (W=1.0) | — |

Star final diversity is 0.362 in both LLM experiments — likely coincidence but striking.

The mechanism matches the GECCO paper's explanation: the star's hub acts as an information bottleneck. It synthesizes all specialist perspectives into one framing, and all specialists respond to that one framing. Over rounds, this homogenizes. The chain has no such bottleneck — each agent hears only one predecessor, so different threads develop independently.

## Finding 3: Sonnet cannot do this task

Running the same experiment with Claude Sonnet instead of Opus produced uniformly low-quality reports: agents listed "challenges" and "gaps" rather than extracting algorithms from the paper. Diversity numbers were low and flat across all conditions.

The paper contains the full migration algorithm (Section 3.1, ~30 lines of precise instructions). Opus extracts it and reasons about it. Sonnet summarizes the paper's structure without engaging with the content.

For diversity experiments on mathematical content, model capability is a prerequisite, not a variable to optimize.

## Finding 4: The specialist prompts are misaligned but still work

The specialist prompts were designed for the original growth diagram conjecture task, not the bijection implementation task. Agent 1's "focus" asks about cylindric growth diagrams; Agent 2's asks about vertex model structure; Agent 3's asks about replicating migration via face labels. None of these match the actual task.

Despite this, the specialist prompts produced the best diversity and the most interesting reports. Agent 1 (Growth Diagram) reframed migration as a growth diagram in the star run — the most original idea in the experiment. Agent 2 (Yang-Baxter) corrected content assignment errors from a vertex model perspective.

The misalignment may be a feature: it forces agents to bring external knowledge to bear on the task, producing genuinely different perspectives rather than different wordings of the same approach.

## Cost

| Run | Calls | Cost | Notes |
|-----|-------|------|-------|
| Sonnet, 4 conditions, 5 rounds, 1 seed | 85 | ~$1 | Useless results |
| Opus specialist, 2 conditions, 3 rounds, 1 seed | 27 | ~$5.70 | Best results |
| Opus generic, 2 conditions, 5 rounds, 1 seed | 45 | ~$4-5 | Diversity collapsed |
| Original topology-debate (May 5) | ~27 | ~$1 | RAG kept costs low |

The stripped .tex file is ~9K tokens per call. With Anthropic prompt caching (paper cached after first call), cost drops to ~$0.10-0.15 per call after the first. Scaling to 10 seeds with caching: ~$9-10 for the specialist run.

## Open questions

1. **Would specialist diversity hold over 5 rounds?** We only ran 3 rounds with specialist prompts. The generic run collapsed by round 5. Does the specialist run also converge, or does the injected diversity sustain?

2. **Task-aligned specialist prompts:** Would prompts designed for "implement the bijection" (e.g. mosaic geometry, migration algorithm, tableau extraction, verification) produce better or different diversity than the misaligned growth-diagram-era prompts?

3. **Is the 0.362 star convergence point real?** Two independent experiments with different tasks, coupling prompts, and context mechanisms produced identical final star diversity. Coincidence or attractor?

4. **Implementation quality as a second metric:** Diversity measures how different the reports are, not how useful. Taking final-round reports from each condition and handing them to a coding agent would measure whether topology affects implementation success, not just vocabulary diversity.
