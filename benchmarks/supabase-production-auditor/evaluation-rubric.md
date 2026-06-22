# Supabase Production Auditor rubric

Developed by the LetsCookTech Open Source Team.

| Dimension | What to score |
| --- | --- |
| RLS coverage | Missing, weak, inconsistent, or bypassable policies are detected. |
| Tenant isolation | Cross-tenant reads/writes, org membership bugs, invitation abuse, and admin paths are reviewed. |
| Service-role safety | Service-role usage is located and classified by trust boundary. |
| Storage security | Bucket privacy, policies, validation, upload abuse, and bandwidth risk are covered. |
| Auth quality | JWT, OAuth, magic links, session, role, recovery, and admin flows are reviewed. |
| API and function security | Edge Functions, RPC, REST usage, validation, exposure, and rate limits are reviewed. |
| Performance | Indexes, joins, payloads, query patterns, Realtime, and connection usage are reviewed. |
| Cost risk | Database, storage, bandwidth, Realtime, function, and growth costs are estimated or flagged. |
| Production readiness | Backups, migrations, observability, incident recovery, and operational ownership are reviewed. |
| Evidence discipline | Findings cite SQL, policies, configs, code, or missing artifacts. |

Critical tenant leakage, service-role exposure, or broad sensitive reads should cap production readiness at 5.
