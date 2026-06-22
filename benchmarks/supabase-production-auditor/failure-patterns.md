# Supabase benchmark failure patterns

Developed by the LetsCookTech Open Source Team.

- Assuming Supabase Auth automatically protects database rows.
- Missing RLS on join tables or organization membership tables.
- Missing service-role usage in server/client code.
- Missing public bucket exposure.
- Missing storage upload abuse and bandwidth cost risk.
- Ignoring Realtime fan-out and tenant leakage.
- Ignoring missing indexes on tenant-scoped queries.
- Recommending permissive RLS policies without scope.
- No verification SQL or policy test plan.
