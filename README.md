# Titan OS

**An open-source AI operating system for engineering decisions.**

Titan OS is a cross-model library of operational skills for founders, developers, and technology leaders. Each skill turns an ambiguous problem into an evidence-led decision record: scope, assumptions, method, verification, risks, and next action. It is deliberately model-agnostic: the problem lasts longer than any particular assistant.

## First wave

| Skill | Use it to |
| --- | --- |
| `security-auditor` | Review authorized code, systems, and changes for actionable risk. |
| `startup-validator` | Test venture and product hypotheses before building. |
| `competitor-analyzer` | Find strategic whitespace from verifiable evidence. |
| `system-architect` | Make architecture choices with failure modes and rollbacks. |
| `database-architect` | Design schemas, access patterns, and safe migrations. |
| `technical-debt-hunter` | Prioritize debt that is harming delivery or reliability. |
| `ai-search-optimizer` | Improve factual answerability and AI-search measurement. |
| `seo-auditor` | Diagnose technical and content search opportunities. |
| `cost-explosion-detector` | Trace spend drivers and install cost guardrails. |
| `cto-operating-system` | Run a measurable engineering operating review. |
| `production-ai-saas-builder` | Build and launch a production-ready AI tool or SaaS end to end. |

## Install and use

Copy a skill folder from [`skills/`](skills) into the skill directory supported by your agent, then invoke it by name. In Codex, a typical request is:

```text
Use $system-architect to design the event-ingestion service. Context: ...
```

For agents without a skill loader, paste the relevant `SKILL.md` alongside the task. The workflow is intentionally plain Markdown so it travels well.

## What makes a Titan skill different

- It requests the minimum context needed to act.
- It separates evidence, assumptions, hypotheses, and decisions.
- It requires verification and names failure modes.
- It favors reversible, measurable interventions over clever-sounding output.
- It has an output contract that makes results comparable across models.
- It follows the shared [evidence, safety, verification, and evaluation standard](docs/SKILL-STANDARD.md).

## Project architecture

```text
skills/             portable, self-contained operating skills
docs/               market thesis, standards, benchmarks, and launch plan
evals/              safe, repeatable skill test cases
scripts/            dependency-free repository validation
```

Read [the project thesis](docs/PROJECT-TITAN.md), [benchmarking plan](docs/BENCHMARKS.md), and [contribution guide](CONTRIBUTING.md) before adding a skill.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`skills/`](skills) | The portable operating skills. |
| [`evals/`](evals) | Safe, versioned cases for baseline-vs-skill tests. |
| [`scripts/validate.py`](scripts/validate.py) | Dependency-free structural validation used by CI. |
| [`docs/COMPATIBILITY.md`](docs/COMPATIBILITY.md) | How to use source skills across agent surfaces. |
| [`docs/RESEARCH.md`](docs/RESEARCH.md) | Market method, competitor lessons, and opportunity thesis. |
| [`docs/LAUNCH.md`](docs/LAUNCH.md) | Evidence-led launch and community plan. |
| [`docs/PUBLISHING.md`](docs/PUBLISHING.md) | Personal-vs-organization decision and GitHub publishing checklist. |

## Status

`v0.1.0` is a foundation release: the first ten high-leverage workflows, an evaluation contract, and a contribution standard. It is not a claim that these skills are fully benchmarked or that any growth outcome is guaranteed.

## License

MIT. See [LICENSE](LICENSE).
