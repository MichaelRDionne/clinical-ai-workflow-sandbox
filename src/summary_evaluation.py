from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from clinical_workflow import intake_summary


def load_expectations(path: str | Path) -> list[dict[str, Any]]:
    with Path(path).open("r", encoding="utf-8") as handle:
        expectations = json.load(handle)
    if not isinstance(expectations, list):
        raise ValueError("Expected a list of summary expectations")
    return expectations


def evaluate_summary(record: dict[str, Any], expectation: dict[str, Any]) -> dict[str, Any]:
    summary = intake_summary(record)
    lower_summary = summary.lower()
    required = expectation.get("required_phrases", [])
    forbidden = expectation.get("forbidden_phrases", [])

    missing_required = [phrase for phrase in required if phrase.lower() not in lower_summary]
    present_forbidden = [phrase for phrase in forbidden if phrase.lower() in lower_summary]

    return {
        "id": record["id"],
        "summary": summary,
        "passed": not missing_required and not present_forbidden,
        "missing_required": missing_required,
        "present_forbidden": present_forbidden,
    }


def evaluate_summaries(
    records: list[dict[str, Any]], expectations: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    expectations_by_id = {expectation["id"]: expectation for expectation in expectations}
    results = []
    for record in records:
        if record["id"] not in expectations_by_id:
            raise ValueError(f"No summary expectation found for {record['id']}")
        results.append(evaluate_summary(record, expectations_by_id[record["id"]]))
    return results
