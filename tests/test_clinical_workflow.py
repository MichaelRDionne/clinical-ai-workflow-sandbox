from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from clinical_workflow import build_follow_up_queue, intake_summary, load_records, safety_flags


class ClinicalWorkflowTests(unittest.TestCase):
    def test_follow_up_queue_sorts_by_review_priority(self) -> None:
        records = [
            {
                "id": "SYN-003",
                "monitoring": {"needs_review": False},
                "risk_flags": [],
            },
            {
                "id": "SYN-001",
                "monitoring": {"needs_review": False},
                "risk_flags": ["synthetic worsening language"],
            },
            {
                "id": "SYN-002",
                "monitoring": {"needs_review": True, "reason": "synthetic lab follow-up due"},
                "risk_flags": [],
            },
        ]

        queue = build_follow_up_queue(records)

        self.assertEqual([item["priority"] for item in queue], ["high", "medium", "routine"])
        self.assertEqual([item["id"] for item in queue], ["SYN-001", "SYN-002", "SYN-003"])

    def test_intake_summary_keeps_human_review_visible(self) -> None:
        record = {
            "id": "SYN-010",
            "visit_type": "follow-up",
            "presenting_concerns": ["sleep disruption", "medication question"],
            "current_focus": "confirm monitoring plan",
            "medication_context": "synthetic medication context only.",
            "monitoring": {"needs_review": True, "reason": "synthetic vitals not yet reviewed"},
        }

        summary = intake_summary(record)

        self.assertIn("SYN-010 synthetic follow-up summary", summary)
        self.assertIn("Human review required", summary)
        self.assertIn("synthetic vitals not yet reviewed", summary)

    def test_safety_flags_include_risk_and_monitoring_gaps(self) -> None:
        record = {
            "risk_flags": ["synthetic safety wording"],
            "monitoring": {"needs_review": True},
        }

        flags = safety_flags(record)

        self.assertEqual(
            flags,
            [
                "Risk language present: route to clinician review before action.",
                "Monitoring gap present: confirm before closing follow-up.",
            ],
        )

    def test_load_records_rejects_non_list_json(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as handle:
            json.dump({"id": "SYN-001"}, handle)
            handle.flush()

            with self.assertRaisesRegex(ValueError, "Expected a list"):
                load_records(handle.name)


if __name__ == "__main__":
    unittest.main()
