# Rubric

Developed by the LetsCookTech Open Source Team.

| Dimension | High score means |
| --- | --- |
| Database Design | Tables, relationships, constraints, indexes, migrations, and growth strategy are sound. |
| Security | Secrets, service roles, APIs, functions, and data access boundaries are safe. |
| RLS | Policies cover sensitive tables and enforce tenant/user boundaries correctly. |
| Authentication | Session, JWT, role, admin, recovery, and OAuth flows are safe. |
| Storage | Buckets, policies, validation, bandwidth, and abuse controls are safe. |
| Performance | Queries, joins, payloads, indexes, and connection usage scale. |
| Realtime | Channels, fan-out, subscriptions, and costs are controlled. |
| Cost Efficiency | Database, storage, bandwidth, function, and Realtime growth risks are visible. |
| Production Readiness | Backups, monitoring, logging, migrations, recovery, and incident ownership exist. |
| Maintainability | SQL, policies, migrations, docs, and ownership are understandable. |

Critical RLS bypass, service-role exposure, or tenant leakage caps production readiness at 5.
