# Failure patterns

Developed by the LetsCookTech Open Source Team.

- Treating Next.js as only a frontend framework and ignoring data, auth, runtime, deployment, and cost boundaries.
- Approving Server Actions without authorization, validation, idempotency, and rate-limit checks.
- Adding Client Components unnecessarily and creating hydration or bundle bloat.
- Confusing metadata presence with SEO health.
- Ignoring AI-search extractability, entity clarity, and answerability.
- Using Edge Runtime for dependencies that require Node APIs.
- Depending on stale cache behavior without revalidation strategy.
- Missing Supabase service-role exposure or weak RLS in server-side code.
- Recommending Vercel features without cost and vendor-limit analysis.
