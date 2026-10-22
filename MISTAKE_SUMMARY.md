# Mistake Summary

## What happened

We ran 3 seeds of a 4-condition multi-agent debate experiment (none,
chain, star, full) with 5 rounds each. Four specialist Claude Sonnet
agents debated an open problem in algebraic combinatorics under
"challenge and extend" coupling.

## What we found

All four conditions converged to the same diversity level (~0.47
cosine distance) by round 5. Early differences (star highest, full
lowest) collapsed. Qualitatively, all agents across all conditions
converged on the same argument: "growth diagrams require locality,
puzzles are global, therefore the bijection can't work."

Nobody proposed a construction. Nobody explored alternative
approaches. Every agent in every condition spent 5 rounds explaining
why the problem is impossible.

## The question I asked

> "Does the row transfer matrix for KTW puzzles define a growth
> diagram whose face labels give a direct bijection between puzzles
> and Littlewood-Richardson tableaux?"

This is a yes/no question. Combined with "challenge and extend"
coupling, it invited criticism, not construction. The agents found
their objection ("locality vs global constraints") in round 1 and
spent four more rounds elaborating on why it can't work.

## The question I should have asked

> "Implement Purbhoo's migration bijection: given a KTW puzzle,
> convert it to a mosaic, run the migration algorithm (hexagonal
> flips), and produce the corresponding LR tableau. The mosaic.py
> script has the mosaic representation but the flip detection is
> broken — migration finds zero available flips. Fix it. Test on
> c^(3,2,1)_{(2,1),(2,1)} = 2."

This is a concrete coding task with a broken starting point and
testable output. Different specialists would approach the bug from
different angles: Growth Diagram would look at face label
structure, Yang-Baxter at vertex weight constraints, Bijection at
the jdt slide mechanics, Computational at the actual code. The
diversity that matters is diversity of *debugging approaches*, not
diversity of *objections*.

## What the data is still good for

1. It shows that "challenge and extend" on a yes/no question
   produces convergent criticism regardless of communication
   structure. The coupling instruction dominated the topology.

2. The early-round pattern (star highest, full lowest) is
   reproducible across 3 seeds, even if it fades by round 5.

3. The cost was ~$1. The lesson was cheap.

## What to do next

Rerun with the constructive problem statement. Keep everything
else the same: 4 conditions, 10 seeds, 5 rounds, cosine diversity,
same agents and papers. Change only the problem statement and
possibly the coupling instruction ("propose and test" rather than
"challenge and extend").
