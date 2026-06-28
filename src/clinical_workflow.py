from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_records(path: str | Path) -> list[dict[str, Any]]:
    """Load synthetic records from JSON."""
    with Path(path).open("r", encoding="utf-8") as handle:
        records = json.load(handle)
    if not isinstance(records, list):
        raise ValueError("Expected a list of synthetic records")
    return records


def intake_summary(record: dict[str, Any]) -> str:
    concerns = ", ".join(record.get("presenting_concerns", [])) or "not specified"
    monitoring = record.get("monitoring", {})
    review_line = "Human review required" if monitoring.get("needs_review") else "No monitoring gap flagged"
    monitoring_reason = str(monitoring.get("reason", "no reason provided")).rstrip(".")
    return (
        f"{record['id']} synthetic {record['visit_type']} summary: "
        f"main concerns are {concerns}. Current focus: {record['current_focus']} "
        f"Medication context: {record['medication_context']} "
        f"{review_line}: {monitoring_reason}."
    )


def longitudinal_snapshot(records: list[dict[str, Any]]) -> list[str]:
    snapshots: list[str] = []
    for record in records:
        snapshots.append(
            f"{record['id']}: {record['visit_type']} | focus={record['current_focus']} | "
            f"next={record['next_step']}"
        )
    return snapshots


def build_follow_up_queue(records: list[dict[str, Any]]) -> list[dict[str, str]]:
    queue: list[dict[str, str]] = []
    for record in records:
        monitoring = record.get("monitoring", {})
        risk_flags = record.get("risk_flags", [])
        if risk_flags:
            priority = "high"
            reason = "risk language requires clinician review"
        elif monitoring.get("needs_review"):
            priority = "medium"
            reason = monitoring.get("reason", "monitoring review needed")
        else:
            priority = "routine"
            reason = "no synthetic escalation flag"
        queue.append({"id": record["id"], "priority": priority, "reason": reason})
    return sorted(queue, key=lambda item: {"high": 0, "medium": 1, "routine": 2}[item["priority"]])


def safety_flags(record: dict[str, Any]) -> list[str]:
    flags: list[str] = []
    if record.get("risk_flags"):
        flags.append("Risk language present: route to clinician review before action.")
    if record.get("monitoring", {}).get("needs_review"):
        flags.append("Monitoring gap present: confirm before closing follow-up.")
    if "Synthetic" not in "Synthetic data only":
        flags.append("Unexpected data provenance issue.")
    return flags
