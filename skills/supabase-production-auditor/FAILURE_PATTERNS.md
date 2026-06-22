# Failure patterns

Developed by the LetsCookTech Open Source Team.

- Assuming Supabase Auth automatically protects table data.
- Missing RLS on join tables, audit tables, invitations, or organization membership.
- Using service role in browser or untrusted runtime.
- Public storage buckets containing sensitive files.
- Policies that check `auth.uid()` but ignore tenant membership.
- Realtime subscriptions that leak tenant data or create bandwidth spikes.
- Missing indexes on tenant-scoped queries.
- No backup, migration rollback, or incident recovery plan.
