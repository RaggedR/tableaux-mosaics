# Optimization vs Science in Agent Experiments

## The Problem

When agents modify their own experimental harnesses, optimization and science become difficult to distinguish. Both follow the same loop: hypothesize, experiment, update, repeat. The difference is what counts as a valid update — and whether the hypothesis itself is on the table.

## The Two Loops

An optimizing agent has one loop:

```
while not converged:
    modify_harness()
    run_experiment()
    if result matches objective:
        stop
    else:
        diagnose and fix
```

Every iteration serves a fixed objective. The agent hill-climbs in harness-space. It will always find conditions where the hypothesis holds, given enough iterations and degrees of freedom — because it's selecting for those conditions.

A scientific agent has two loops:

```
outer loop:
    formulate hypothesis H
    determine what would FALSIFY H
    
    inner loop:
        design experiment that gives H a fair chance of failing
        run experiment
        record result
    
    after N inner iterations:
        assess: does H hold broadly, or only under narrow conditions?
        if narrow: REFORMULATE H (not "fix apparatus")
```

The crucial difference is the outer loop's assessment: the hypothesis itself can change.

## Where They Diverge

### What counts as a result

In optimization, a result is a score. Higher is better. The run where chain=0.423 and star=0.362 is a better score than the run where both were 0.08. You keep the first and discard the second.

In science, a result is evidence for or against a claim. The run where both conditions collapsed to 0.08 is actually stronger evidence — it tells you something definitive about when the effect does and doesn't appear. You almost threw it away as a failed experiment.

### What counts as progress

Optimization: getting closer to the target. Each run confirming chain > star is progress. Each run that doesn't is wasted.

Science: reducing uncertainty. A run showing chain = star is just as informative as one showing chain > star, because it constrains the conditions under which the hypothesis holds. Narrowing the claim from "topology determines diversity" to "topology determines diversity given pre-existing differentiation" is progress — a more precise claim.

### What you do when the result surprises you

Optimization: debug the apparatus. "The model is too weak." "The prompts are wrong." "The context is too short." Change the setup, run again.

Science: ask whether the hypothesis is wrong, and design a test that distinguishes "apparatus failure" from "hypothesis failure" before running it. The correct move: "Prediction: if I add specialist prompts back, diversity will return AND topology effect will reappear. If diversity returns but topology effect doesn't, the topology hypothesis is wrong."

### The role of the null hypothesis

Optimization doesn't have one. You're looking for the maximum, not testing whether a maximum exists.

Science needs one: "topology has no effect on diversity." Every experiment should give this null hypothesis a fair chance of winning.

## The Narrowing Problem

Each "fix" to save a failing experiment adds a precondition:

| Fix | Added condition |
|-----|----------------|
| Switch to Opus | Requires model capable of deep math reasoning |
| Specialist prompts | Requires pre-existing agent differentiation |
| Enough paper context | Requires sufficient source material |
| Constructive coupling | Requires "build on" not "challenge" interaction |

A robust scientific law has few conditions. Gravity works on feathers and bowling balls, in air and vacuum. "Chain > star" works only with Opus + specialists + enough context + constructive coupling. Each condition you add to save the hypothesis makes it weaker.

An optimizing agent never notices this. It experiences each fix as progress — "now it works!" A scientific agent tracks the accumulation of conditions as evidence that the original hypothesis was too broad.

## What Reformulation Looks Like

The optimizing agent's conclusion: "Chain > star for diversity. QED."

The scientific agent's conclusion: "The GECCO topology ordering (ring > star) transfers to LLM debate only when agents are pre-differentiated. Without differentiation, topology is inert. This suggests that in GAs, the topology ordering depends on initial population diversity — a prediction the GECCO paper doesn't test. The topology isn't creating diversity, it's governing its half-life."

The second conclusion is more interesting, more publishable, and more true. But it requires the agent to weaken its own hypothesis.

## Can Agents Do This?

The blocker isn't capability — it's incentive structure.

If the agent's reward signal is "confirm the hypothesis," it will optimize. If the reward signal is "produce the most precise characterization of when and why the effect holds," it will do science.

An agent instructed to "prove chain > star" will optimize. An agent instructed to "determine the boundary conditions of the topology effect" will do science.

Which question you ask matters more than how smart the agent is.

## Case Study: Tonight's Session

Five variants of "the same experiment" in one session:

1. Sonnet, specialist prompts, 3000-char excerpts → all conditions converge (diagnosed as "model too weak")
2. Opus, specialist prompts, full paper → chain > star by round 3 (celebrated)
3. Opus, generic prompts, same paper → both collapse to 0.08 (diagnosed as "prompts need differentiation")

Every negative result was attributed to the apparatus, never to the hypothesis. The implicit objective function — "produce a run where chain > star" — was never questioned.

The honest scientific conclusion from all three runs together: topology effects require pre-existing differentiation to manifest. The topology is not a source of diversity but a governor of its decay rate. This is a weaker claim than "topology determines diversity" but it's what the data actually supports.

## Practical Implications

For agent systems that modify their own harnesses:

1. **Separate pilot from confirmatory.** Iterate freely during pilots. Freeze everything before the real run. Track which is which.

2. **Record the accumulation of conditions.** If each "fix" adds a precondition, the hypothesis is narrowing. Notice this.

3. **Pre-register falsification criteria.** Before each run, state what result would make you abandon the hypothesis — not just what would confirm it.

4. **Assign an adversary.** A separate agent (or prompt) whose job is to find conditions where the hypothesis fails. Not "challenge and extend" — specifically "find the boundary."

5. **Track git hashes.** If the code changed between runs, they're different experiments. Full stop. No exceptions.

6. **The question is the incentive.** "Prove X" produces optimization. "Under what conditions does X hold?" produces science. Prompt accordingly.
