# Production AI SaaS checklist

Use this only after the core skill workflow. Mark each item `pass`, `not applicable`, or `blocked` with evidence.

## Product and ownership

- Named user, job, success metric, non-goal, product owner, technical owner, and on-call owner.
- Acceptance criteria cover empty, error, permission-denied, duplicate, slow, and retry states.
- Pricing/entitlement behavior and support route are explicit.

## Security and privacy

- Authentication, role/organization authorization, tenant isolation, session lifecycle, and rate limit tests pass.
- Data inventory identifies sensitive fields, retention, deletion, export, backups, and subprocessors.
- Secret scan, dependency scan, least-privilege service roles, audit trail, and incident contact are complete.

## AI quality and control

- Task evaluation dataset has ordinary, edge, adversarial, and provider-failure cases.
- Output has schema/validation, refusal policy where relevant, citations where claims depend on private corpus, and human review for consequential decisions.
- Prompt, model, tools, retrieval configuration, and evaluation version are recorded.
- Model/tool timeouts, retry bounds, concurrency/usage caps, cost alerts, and fallback are tested.

## Reliability and release

- CI blocks failed checks; preview and production configuration are distinct.
- Migrations are rehearsed against representative data; backup restore is tested.
- Critical path has SLO/SLI, dashboard, alert, trace correlation, runbook, rollback, and provider-outage behavior.
- Feature flags or staged rollout controls have named removal dates.

