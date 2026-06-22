# AI agent benchmark failure patterns

Developed by the LetsCookTech Open Source Team.

- Treating model self-critique as verification.
- Missing indirect prompt injection from tools, web pages, retrieved docs, or MCP responses.
- Missing tool permission boundaries.
- Missing safe stop conditions for autonomous loops.
- Ignoring memory poisoning, privacy, retention, and deletion.
- Ignoring multi-agent deadlocks or conflicting objectives.
- Missing cost fan-out from retries, tools, subagents, and long context.
- Missing observability for decisions, actions, failures, and spend.
