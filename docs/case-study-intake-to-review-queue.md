# Case Study: Synthetic Intake To Review Queue

This case study explains the main workflow this sandbox is modeling: a structured synthetic intake record becomes a useful summary, queue item, and safety-review signal.

## Starting Point

A clinical team has several follow-up records to review. The pain is not only writing a summary. The real work is deciding what needs attention today, what can be handled operationally, and what should never be closed without clinician review.

The synthetic input includes:

- visit type
- presenting concerns
- current focus
- medication context
- monitoring status
- risk flags
- next step

## Automation Boundary

The demo can:

- summarize structured synthetic fields
- create a longitudinal snapshot
- sort follow-up items by priority
- surface monitoring gaps
- flag risk language for clinician review

The demo should not:

- diagnose
- recommend treatment
- create a final clinical note
- close a follow-up without review
- use real patient records or production exports

## Review Logic

The queue logic is deliberately simple:

- `high`: risk language is present, so a clinician needs to review before action
- `medium`: monitoring needs review, but no risk language is present
- `routine`: no synthetic escalation or monitoring gap is flagged

That simplicity is part of the point. In early healthcare AI prototyping, the first version should make the safety boundary legible before the system becomes clever.

## Output Example

The demo produces:

- an intake summary
- a longitudinal snapshot
- a priority queue
- safety flags

See `examples/demo-output.txt` for the captured run.

## What I Would Improve Next

- Add expected-summary fixtures and compare generated summaries against them.
- Add a lightweight queue view that makes high-priority items visually obvious.
- Add a confidence or uncertainty field for cases where the structured data is incomplete.
- Add a review rubric that separates usefulness, completeness, and safety.

## Why It Matters

The useful product question is not "Can AI summarize a chart?" The better question is "Can this workflow reduce preparation burden while making missing information and escalation needs easier to see?"

That is the clinical AI consulting angle this repo is meant to show.
