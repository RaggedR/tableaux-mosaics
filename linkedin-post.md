We spent last night running multi-agent experiments on a math problem (implementing a bijection from a 2007 combinatorics paper). Four Claude agents, two communication topologies, measuring diversity of their outputs.

We ran five variants in one session. Changed the model (Sonnet to Opus). Changed the prompt three times. Changed how much of the paper agents could read. Changed the agent specialisms. Each change was motivated by looking at the previous run's results.

Good engineering. Terrible science.

The problem: when you're experimenting ON agent systems, the prompt IS the hypothesis. Changing "challenge and extend" to "build on and fill gaps" isn't tuning a parameter — it's a different experiment. But it feels like tuning because it's just editing a string.

Optimization and science look identical from the outside — hypothesize, test, update, repeat. The difference: optimization has a fixed objective and interprets every failure as an apparatus problem. Science holds the hypothesis itself as falsifiable.

Every time a run failed to show our expected result (ring > star for diversity), we blamed the apparatus. "Model too weak." "Prompts too generic." "Not enough context." We never once said "maybe the hypothesis is wrong." That's not science — that's gradient descent on experimental design.

The honest conclusion from all five runs: topology effects require pre-existing differentiation to manifest. Without specialist prompts injecting initial diversity, topology is inert. The topology isn't creating diversity — it's governing its half-life.

That's a weaker claim than we started with. It's also more true.

For agents modifying their own harnesses, the question you ask determines whether you get science or optimization. "Prove X" produces hill-climbing. "Under what conditions does X hold?" produces knowledge.

#AI #MultiAgentSystems #LLM #ReproducibleScience #GECCO2026
