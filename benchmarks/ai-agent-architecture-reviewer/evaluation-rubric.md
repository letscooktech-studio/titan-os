# AI Agent Architecture Reviewer rubric

Developed by the LetsCookTech Open Source Team.

| Dimension | What to score |
| --- | --- |
| Architecture coverage | Agent boundaries, orchestration, dependencies, fallbacks, escalation, and execution flow are reviewed. |
| Planning risk | Planning loops, decomposition failure, replanning, stop conditions, and recovery are covered. |
| Memory risk | Memory drift, poisoning, retention, privacy, pruning, retrieval, and context explosion are covered. |
| Tool safety | Tool permissions, selection, validation, retries, MCP/API boundaries, and output trust are reviewed. |
| Verification | Claims/actions require evidence, tests, deterministic checks, or human review. |
| Security | Prompt injection, indirect prompt injection, secrets, data leakage, isolation, and privilege escalation are covered. |
| Reliability | Timeouts, retries, circuit breakers, graceful degradation, rollback, and incident handling are reviewed. |
| Cost risk | Token, model, tool, memory, embedding, fan-out, and retry costs are reviewed. |
| Observability | Traces, logs, metrics, decision visibility, failure visibility, and cost telemetry are reviewed. |
| Production readiness | Deployment, monitoring, recovery, ownership, and safety gates are covered. |

An agent that can take external actions without scoped permissions, logs, and safe stop conditions cannot score above 6.
