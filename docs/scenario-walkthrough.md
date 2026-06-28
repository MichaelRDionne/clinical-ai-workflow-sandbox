# Scenario Walkthrough

This walkthrough shows the kind of synthetic workflow this sandbox is modeling.

## Scenario

A follow-up patient record enters the queue with:

- persistent insomnia
- worsening concentration
- a missed monitoring task
- language that suggests possible risk review is needed

## What The Demo Should Do

1. Generate a short intake summary from the structured synthetic fields.
2. Place the record into the follow-up queue with visible priority.
3. Flag the monitoring gap.
4. Route risk language to clinician review before any operational closeout.

## What The Demo Should Not Do

- diagnose
- recommend treatment
- close the task automatically
- present the generated text as a final clinical note

## Why This Matters

The value is not fancy summarization by itself. The value is reducing chart-prep friction while keeping the failure modes visible:

- missing monitoring should stay visible
- risk language should interrupt automation
- a human reviewer should still own the final action

## Good Interview Framing

This is the kind of workflow I would prototype first before discussing any live EHR integration. I want to know whether the summary is useful, whether the queue logic matches real follow-up work, and whether the review gates are strong enough before touching production systems.
