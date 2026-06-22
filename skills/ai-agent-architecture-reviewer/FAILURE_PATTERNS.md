# Failure patterns

Developed by the LetsCookTech Open Source Team.

- Letting the agent call powerful tools without scoped permissions.
- Treating model self-review as verification.
- Missing indirect prompt injection through retrieved documents, web pages, or tool outputs.
- Allowing unbounded loops, retries, or multi-agent fan-out.
- Storing sensitive memory without retention, access, and deletion controls.
- Running agents without traces, cost telemetry, or action logs.
- Giving multiple agents conflicting goals or shared mutable context without arbitration.
