# Benchmark lab

The benchmark lab exists to prove or disprove AI Engineering Arsenal's value. It is not a marketing page.

Developed by the LetsCookTech Open Source Team.

## Required artifact set

Every benchmarked skill should have:

```text
benchmarks/<skill>/
  evaluation-rubric.md
  failure-patterns.md
  baseline-output.md
  framework-output.md
  comparison-report.md
  coverage-report.md
  risk-detection-report.md
  accuracy-report.md
  actionability-report.md
  time-savings-report.md
```

For early skills, `evaluation-rubric.md` and `failure-patterns.md` are the minimum acceptable proof-pack seed. Do not claim performance improvement until the output reports exist.

## Benchmark protocol

1. Freeze input artifacts and task prompt.
2. Run default AI without AI Engineering Arsenal.
3. Run the same model with AI Engineering Arsenal.
4. Keep model, temperature, tools, context, and time budget comparable.
5. Score both outputs with the AI Engineering Arsenal Evaluation Standard.
6. Publish the raw outputs unless safety or privacy requires redaction.
7. Publish limitations, evaluator notes, and known failure modes.

## Comparison report format

| Dimension | Default AI | AI Engineering Arsenal | Winner | Notes |
| --- | ---: | ---: | --- | --- |
| Accuracy |  |  |  |  |
| Evidence |  |  |  |  |
| Verification |  |  |  |  |
| Actionability |  |  |  |  |
| Security |  |  |  |  |
| Scalability |  |  |  |  |
| Maintainability |  |  |  |  |
| Completeness |  |  |  |  |
| Risk awareness |  |  |  |  |
| Business impact |  |  |  |  |
| User value |  |  |  |  |

## Claim rules

- "AI Engineering Arsenal improved the result" requires a scored comparison.
- "AI Engineering Arsenal found more risks" requires a coverage report.
- "AI Engineering Arsenal saved time" requires either measured execution time or a clearly labeled estimate.
- "Production-grade" requires verification, rollback, ownership, and failure handling.
