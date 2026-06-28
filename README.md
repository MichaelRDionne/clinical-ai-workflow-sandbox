# Clinical AI Workflow Sandbox

Synthetic clinical workflow demo for intake summarization, longitudinal snapshots, follow-up queueing, and safety checks.

This repository is designed as a public portfolio project. It demonstrates how I think about clinical AI systems: reduce cognitive load, keep humans in control, make uncertainty visible, and keep sensitive data out of public demos.

## What It Shows

- Synthetic patient fixtures with coded IDs only.
- Intake summary generation from structured inputs.
- Longitudinal snapshot generation for follow-up prep.
- Follow-up queue generation by risk and due date.
- Safety checks for missing monitoring, escalation flags, and human review.

## Safety Boundary

This repo contains no real patient data and no production clinical exports. Every example is synthetic and simplified for demonstration. It is not medical advice, not a diagnostic system, and not intended for direct clinical use.

## Run The Demo

```bash
python3 examples/run_demo.py
```

Expected output:

- A brief intake summary.
- A longitudinal follow-up snapshot.
- A prioritized follow-up queue.
- Safety flags that require human review.

## Project Structure

```text
synthetic-data/patient-fixtures.json  synthetic demo records
src/clinical_workflow.py              summary, queue, and safety logic
examples/run_demo.py                  runnable demo
```

## Design Principles

- Synthetic data first.
- Human review before action.
- Clear escalation language.
- Minimal automation until the workflow is understood.
- Outputs should explain what they used and what they did not know.
