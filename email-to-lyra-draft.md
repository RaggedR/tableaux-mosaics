Subject: Ring vs star crossover — need the raw trajectory data

Lyra,

Working on the EUMAS v2 paper and hit a question we can't resolve without the raw data from your ring-vs-star NK sweep experiments.

The EUMAS paper says star "briefly exceeds the ring mid-run" at K=6 on a 500-generation experiment. But the GECCO paper reports ring > star at generation 99 (across six domains, p = 6.6 × 10⁻⁵ on the maze confirmatory experiment).

The question: at what generation does the crossover actually happen? If it's after generation 99, then GECCO measured before the crossover and the two papers might contradict each other. If it's before generation 99, they're consistent.

Could you dig up the raw diversity-per-generation data from the ring-vs-star experiment? It was at /tmp/eumas_data/ring_vs_star/ on your machine. Specifically I need the generation-by-generation diversity trajectories for ring and star at K=6, so I can see exactly when star exceeds ring.

Also: do you still have the generation-by-generation data from the GECCO experiments? The GECCO paper only reports generation 99, but the raw data should have the full trajectory. If star > ring at early generations in the GECCO data too, that's important — it means the GECCO ordering is time-dependent and we never noticed.

Context: we're running new LLM experiments (4 agents debating an open math problem, chain vs star vs full vs none, 10 seeds). Preliminary results show star ≈ none > chain > full — the opposite of the GA prediction for star vs chain. The hub appears to amplify divergence rather than homogenise, under "challenge and extend" instructions. Whether the GA temporal crossover exists for LLMs is an open question we're testing with longer runs.

Robin
