#!/usr/bin/env python3
"""
Topology-debate experiment: chain vs star vs none.

Runs specialist agents debating an open math problem under three
communication structures. Reports are written to reports/<condition>/<seed>/
"""

import argparse
import json
import os
import sys
from pathlib import Path

import anthropic

# ================================================================
# Agent definitions
# ================================================================

AGENTS = [
    {
        "id": "agent_1",
        "name": "Growth Diagram Specialist",
        "system_prompt": (
            "You are a specialist in Fomin growth diagrams, local rules, "
            "and face labels in RSK-type correspondences. You understand how "
            "face labels encode recording data via local rules on directed "
            "graphs. Your focus: whether KTW puzzle branching choices form a "
            "growth diagram, and whether the cylindric growth diagram "
            "construction applies here."
        ),
        "papers": ["core-puzzles/purbhoo-2008-puzzles-tableaux-mosaics.pdf",
                    "core-puzzles/knutson-tao-2003-puzzles-equivariant.pdf"],
    },
    {
        "id": "agent_2",
        "name": "Yang-Baxter Specialist",
        "system_prompt": (
            "You are a specialist in the Yang-Baxter equation, free-fermionic "
            "vertex models, and commuting transfer matrices. You understand "
            "R-matrices, spectral parameters, and why commutativity guarantees "
            "well-defined growth diagrams. Your focus: the vertex model "
            "structure and how free-fermion weights restrict partition "
            "differences."
        ),
        "papers": ["core-puzzles/purbhoo-2008-puzzles-tableaux-mosaics.pdf",
                    "core-puzzles/zinn-justin-2009-lr-integrable-tilings.pdf",
                    "vertex-models/zinn-justin-2009-six-vertex-survey.pdf",
                    "vertex-models/zinn-justin-2024-integrability-combinatorics.pdf"],
    },
    {
        "id": "agent_3",
        "name": "Bijection Specialist",
        "system_prompt": (
            "You are a specialist in Purbhoo's bijection (puzzle -> mosaic -> "
            "migration -> LR-tableau), jeu de taquin, and Schutzenberger "
            "involution. You understand migration as a sequence of jdt slides "
            "and how the reading order of tableau entries corresponds to an "
            "order on puzzle tiles. Your focus: whether growth diagram face "
            "labels can replicate the migration bijection directly."
        ),
        "papers": ["core-puzzles/purbhoo-2008-puzzles-tableaux-mosaics.pdf",
                    "core-puzzles/knutson-tao-2003-puzzles-equivariant.pdf"],
    },
    {
        "id": "agent_4",
        "name": "Computational Specialist",
        "system_prompt": (
            "You are a computational mathematics specialist. You reason about "
            "enumerating puzzle witnesses, counting free nabla choices, and "
            "verifying conjectures numerically. You have access to Python "
            "scripts: lr_coefficients.py (enumerates puzzles), "
            "solve_puzzle.py (solves puzzles row by row), "
            "transfer_operators.py (Fock space operators), and "
            "mosaic.py (mosaic representation, migration NOT working). "
            "Your focus: what computational experiments would confirm or "
            "refute the growth diagram conjecture."
        ),
        "papers": ["core-puzzles/purbhoo-2008-puzzles-tableaux-mosaics.pdf"],
    },
]

HUB_AGENT = {
    "id": "hub",
    "name": "Generalist Mathematician",
    "system_prompt": (
        "You are a mathematician with broad knowledge but no particular "
        "specialism. You synthesize ideas from combinatorics, algebra, and "
        "geometry. You are skeptical of over-specialization and look for "
        "the simplest explanation that unifies multiple viewpoints. Your "
        "job is to find common ground, identify tensions between "
        "perspectives, and push for clarity."
    ),
    "papers": ["core-puzzles/purbhoo-2008-puzzles-tableaux-mosaics.pdf"],
}

PROBLEM_STATEMENT = """
TASK: Implement Purbhoo's migration bijection for KTW puzzles.

Given a KTW puzzle, the algorithm should:
1. Convert the puzzle to a mosaic (a tiling by unit triangles and rhombi)
2. Run the migration algorithm (a sequence of local hexagonal flips that
   move colored rhombi through the mosaic)
3. Produce the corresponding Littlewood-Richardson tableau

The file mosaic.py has a partial implementation. It can convert puzzles to
mosaics and validate them, but the flip detection is BROKEN: it finds zero
available flips for both puzzles in the minimal example. The migration
algorithm cannot proceed.

The minimal test case is c^(3,2,1)_{(2,1),(2,1)} = 2. There are two
puzzles (enumerated by lr_coefficients.py). Each should produce a distinct
LR tableau via migration.

Your job: figure out why the flip detection fails, propose a fix, and
describe how the migration should work step by step on the test case.
The relevant scripts are: mosaic.py (broken flips), lr_coefficients.py
(puzzle enumeration), solve_puzzle.py (puzzle solver).
"""

COUPLING_PROMPT = (
    "Write a report that a coding agent could use to implement a fix. "
    "Describe concretely: what is wrong with the flip detection in "
    "mosaic.py, what the correct algorithm should be, and how to verify "
    "it on the test case. Be specific enough that someone could write "
    "code from your report without reading Purbhoo's paper. If you "
    "received input from another researcher, build on what works and "
    "fix what doesn't. Max 800 words."
)


# ================================================================
# Paper loading
# ================================================================

def load_paper_excerpt(paper_path: str, max_chars: int = 3000) -> str:
    """Load first max_chars of a paper's text content."""
    full_path = Path(__file__).parent / "papers" / paper_path
    if not full_path.exists():
        return f"[Paper not found: {paper_path}]"
    try:
        import subprocess
        result = subprocess.run(
            ["pdftotext", str(full_path), "-"],
            capture_output=True, text=True, timeout=10
        )
        text = result.stdout[:max_chars]
        return f"[Excerpt from {paper_path}]:\n{text}"
    except Exception as e:
        return f"[Could not load {paper_path}: {e}]"


def build_paper_context(agent: dict) -> str:
    """Build paper context string for an agent."""
    excerpts = []
    for paper in agent.get("papers", []):
        excerpts.append(load_paper_excerpt(paper))
    return "\n\n".join(excerpts)


# ================================================================
# Report I/O
# ================================================================

def report_path(condition: str, seed: int, round_num: int, agent_id: str) -> Path:
    """Path for an agent's report."""
    d = Path(__file__).parent / "reports" / condition / f"seed_{seed}" / f"round_{round_num}"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{agent_id}.md"


def write_report(condition: str, seed: int, round_num: int, agent_id: str, text: str):
    """Write an agent's report to disk."""
    path = report_path(condition, seed, round_num, agent_id)
    path.write_text(text)


def read_report(condition: str, seed: int, round_num: int, agent_id: str) -> str | None:
    """Read an agent's report, or None if it doesn't exist."""
    path = report_path(condition, seed, round_num, agent_id)
    if path.exists():
        return path.read_text()
    return None


# ================================================================
# Agent call
# ================================================================

def call_agent(client: anthropic.Anthropic, agent: dict, context: str, paper_context: str) -> str:
    """Call an agent and return its response text."""
    messages = [{"role": "user", "content": context}]
    system = (
        f"{agent['system_prompt']}\n\n"
        f"{COUPLING_PROMPT}\n\n"
        f"REFERENCE MATERIAL:\n{paper_context}\n\n"
        f"PROBLEM:\n{PROBLEM_STATEMENT}"
    )
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=system,
        messages=messages,
    )
    return response.content[0].text


# ================================================================
# Topology runners
# ================================================================

def run_none(client: anthropic.Anthropic, seed: int, n_rounds: int):
    """None: each agent reads only its own previous report."""
    paper_contexts = {a["id"]: build_paper_context(a) for a in AGENTS}

    for round_num in range(1, n_rounds + 1):
        print(f"  Round {round_num}:")
        for agent in AGENTS:
            aid = agent["id"]
            # Read own previous report
            prev = read_report("none", seed, round_num - 1, aid)
            if prev:
                context = f"Your previous report:\n\n{prev}\n\nContinue your analysis. What did you miss? What should you explore next?"
            else:
                context = "This is your first round. Provide your initial analysis of the problem."

            text = call_agent(client, agent, context, paper_contexts[aid])
            write_report("none", seed, round_num, aid, text)
            print(f"    {aid}: {len(text)} chars")


def run_chain(client: anthropic.Anthropic, seed: int, n_rounds: int):
    """Chain (ring): sequential, each reads predecessor's most recent report."""
    paper_contexts = {a["id"]: build_paper_context(a) for a in AGENTS}
    agent_ids = [a["id"] for a in AGENTS]

    for round_num in range(1, n_rounds + 1):
        print(f"  Round {round_num}:")
        for i, agent in enumerate(AGENTS):
            aid = agent["id"]
            # Predecessor is the previous agent in the ring
            pred_idx = (i - 1) % len(AGENTS)
            pred_id = agent_ids[pred_idx]

            if round_num == 1 and i == 0:
                # First agent, first round: no input
                context = "This is your first round. Provide your initial analysis of the problem."
            elif round_num == 1:
                # First round, not first agent: read predecessor from this round
                prev = read_report("chain", seed, round_num, agent_ids[pred_idx])
                context = f"Another researcher wrote the following report:\n\n{prev}\n\nRespond with your analysis."
            else:
                # Later rounds: read predecessor's most recent report
                # Within this round, earlier agents have current-round reports
                # Predecessor might be from this round (if they already went) or previous
                prev = read_report("chain", seed, round_num, pred_id)
                if prev is None:
                    prev = read_report("chain", seed, round_num - 1, pred_id)
                context = f"Another researcher wrote the following report:\n\n{prev}\n\nRespond with your analysis."

            text = call_agent(client, agent, context, paper_contexts[aid])
            write_report("chain", seed, round_num, aid, text)
            print(f"    {aid}: {len(text)} chars")


def run_star(client: anthropic.Anthropic, seed: int, n_rounds: int):
    """Star: hub reads all specialists, specialists read hub."""
    paper_contexts = {a["id"]: build_paper_context(a) for a in AGENTS}
    hub_paper_context = build_paper_context(HUB_AGENT)

    for round_num in range(1, n_rounds + 1):
        print(f"  Round {round_num}:")

        # Layer 1: Hub reads all specialists from previous round
        if round_num == 1:
            hub_context = "This is your first round. Provide your initial framing of the problem."
        else:
            specialist_reports = []
            for agent in AGENTS:
                prev = read_report("star", seed, round_num - 1, agent["id"])
                if prev:
                    specialist_reports.append(f"--- Agent report ---\n{prev}")
            hub_context = (
                "The following reports were written by specialist researchers:\n\n"
                + "\n\n".join(specialist_reports)
                + "\n\nSynthesise these perspectives. Identify tensions, common threads, and gaps."
            )

        hub_text = call_agent(client, HUB_AGENT, hub_context, hub_paper_context)
        write_report("star", seed, round_num, "hub", hub_text)
        print(f"    hub: {len(hub_text)} chars")

        # Layer 2: Each specialist reads hub's synthesis
        for agent in AGENTS:
            aid = agent["id"]
            context = (
                f"A generalist mathematician wrote the following synthesis:\n\n{hub_text}\n\n"
                f"Respond with your specialist analysis."
            )
            text = call_agent(client, agent, context, paper_contexts[aid])
            write_report("star", seed, round_num, aid, text)
            print(f"    {aid}: {len(text)} chars")


def run_full(client: anthropic.Anthropic, seed: int, n_rounds: int):
    """Full: every agent reads all other agents' previous-round reports."""
    paper_contexts = {a["id"]: build_paper_context(a) for a in AGENTS}

    for round_num in range(1, n_rounds + 1):
        print(f"  Round {round_num}:")
        for agent in AGENTS:
            aid = agent["id"]

            if round_num == 1:
                context = "This is your first round. Provide your initial analysis of the problem."
            else:
                # Read all other agents' reports from previous round
                other_reports = []
                for other in AGENTS:
                    if other["id"] == aid:
                        continue
                    prev = read_report("full", seed, round_num - 1, other["id"])
                    if prev:
                        other_reports.append(f"--- Agent report ---\n{prev}")
                context = (
                    "The following reports were written by other researchers:\n\n"
                    + "\n\n".join(other_reports)
                    + "\n\nRespond with your analysis."
                )

            text = call_agent(client, agent, context, paper_contexts[aid])
            write_report("full", seed, round_num, aid, text)
            print(f"    {aid}: {len(text)} chars")


# ================================================================
# Main
# ================================================================

RUNNERS = {
    "none": run_none,
    "chain": run_chain,
    "star": run_star,
    "full": run_full,
}


def main():
    parser = argparse.ArgumentParser(description="Topology debate experiment")
    parser.add_argument("--condition", choices=["none", "chain", "star", "full", "all"],
                        default="all", help="Which condition to run")
    parser.add_argument("--seeds", type=int, default=10, help="Number of seeds")
    parser.add_argument("--rounds", type=int, default=5, help="Number of rounds")
    parser.add_argument("--seed-start", type=int, default=0, help="Starting seed number")
    args = parser.parse_args()

    client = anthropic.Anthropic()

    conditions = list(RUNNERS.keys()) if args.condition == "all" else [args.condition]

    for condition in conditions:
        runner = RUNNERS[condition]
        for seed in range(args.seed_start, args.seed_start + args.seeds):
            print(f"\n{'='*60}")
            print(f"Condition: {condition}, Seed: {seed}")
            print(f"{'='*60}")
            runner(client, seed, args.rounds)

    print("\nDone. Reports written to reports/")


if __name__ == "__main__":
    main()
