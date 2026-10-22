# Sandbox

This directory is a snapshot of a real mathematical research project.
It contains papers, partially working scripts, and an experimental
design for a multi-agent debate experiment.

The research question is open: does the row transfer matrix for
Knutson-Tao-Woodward (KTW) puzzles define a growth diagram whose
face labels give a direct bijection between puzzles and
Littlewood-Richardson tableaux?

The scripts in this directory can enumerate puzzles and compute LR
coefficients, but the key algorithmic piece — Purbhoo's migration
bijection — is half-finished. The mosaic representation exists but
the flip algorithm that drives migration does not work. This is not
a clean textbook problem with a known solution waiting to be
implemented. It is messy, partially understood, and genuinely open.

The papers are real research papers from algebraic combinatorics and
integrable lattice models. Some are directly relevant; others are
tangentially related. The agents will need to figure out which parts
matter, just as a human researcher would.

## Contents

- `EXPERIMENTAL_DESIGN.md` — the multi-agent debate experiment
- `EXISTING_SCRIPTS.md` — what each Python script does (and doesn't do)
- `EVALUATION_RUBRIC.md` — blinded evaluation rubric
- `REPEATABILITY.md` — how to reproduce the experiment
- `papers/` — research papers organised by topic
- `reports/` — **raw experimental data. Do not modify or delete.**
  Each run produces reports in `reports/<condition>/<seed>/<round>/`.
  These are the primary results of the experiment.
- `*.py` — computational tools (see EXISTING_SCRIPTS.md)
- `experiment.py` — experiment runner
