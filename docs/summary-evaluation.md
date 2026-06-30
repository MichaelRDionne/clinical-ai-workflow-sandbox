# Summary Evaluation

This sandbox now includes expected-output fixtures for synthetic intake summaries.

The goal is not to score clinical correctness. The goal is to make the demo testable:

- required phrases confirm that the generated summary includes the synthetic record ID, visit type, concerns, current focus, medication context, and review language
- forbidden phrases catch unsafe framing such as diagnosis language, treatment recommendations, final-note framing, or removing needed human review
- every fixture stays synthetic and uses coded IDs only

## Files

- `synthetic-data/expected-summary-fixtures.json`
- `src/summary_evaluation.py`
- `tests/test_summary_evaluation.py`

## Why This Matters

Healthcare AI demos need evaluation before they need cleverness. A simple expected-output fixture is a useful first step because it makes the safety boundary testable and keeps regressions visible in CI.

Future versions can add richer rubrics for completeness, usefulness, uncertainty, and escalation handling.
