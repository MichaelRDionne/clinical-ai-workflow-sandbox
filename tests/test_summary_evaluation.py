from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from clinical_workflow import load_records
from summary_evaluation import evaluate_summaries, evaluate_summary, load_expectations


class SummaryEvaluationTests(unittest.TestCase):
    def test_fixture_summaries_match_expected_phrases(self) -> None:
        records = load_records(ROOT / "synthetic-data" / "patient-fixtures.json")
        expectations = load_expectations(ROOT / "synthetic-data" / "expected-summary-fixtures.json")

        results = evaluate_summaries(records, expectations)

        self.assertTrue(all(result["passed"] for result in results), results)
        self.assertEqual([result["id"] for result in results], ["SYN-001", "SYN-002", "SYN-003"])

    def test_evaluation_reports_missing_required_phrases(self) -> None:
        record = {
            "id": "SYN-100",
            "visit_type": "intake",
            "presenting_concerns": ["sleep disruption"],
            "current_focus": "Clarify timeline.",
            "medication_context": "Synthetic medication context.",
            "monitoring": {"needs_review": True, "reason": "Synthetic monitoring gap."},
        }
        expectation = {
            "id": "SYN-100",
            "required_phrases": ["missing phrase"],
            "forbidden_phrases": [],
        }

        result = evaluate_summary(record, expectation)

        self.assertFalse(result["passed"])
        self.assertEqual(result["missing_required"], ["missing phrase"])
        self.assertEqual(result["present_forbidden"], [])

    def test_evaluation_reports_forbidden_phrases(self) -> None:
        record = {
            "id": "SYN-101",
            "visit_type": "follow-up",
            "presenting_concerns": ["low mood"],
            "current_focus": "Follow up.",
            "medication_context": "Synthetic medication context.",
            "monitoring": {"needs_review": False, "reason": "No synthetic monitoring gap."},
        }
        expectation = {
            "id": "SYN-101",
            "required_phrases": ["SYN-101 synthetic follow-up summary"],
            "forbidden_phrases": ["synthetic follow-up summary"],
        }

        result = evaluate_summary(record, expectation)

        self.assertFalse(result["passed"])
        self.assertEqual(result["missing_required"], [])
        self.assertEqual(result["present_forbidden"], ["synthetic follow-up summary"])

    def test_evaluate_summaries_requires_expectation_for_each_record(self) -> None:
        records = [{"id": "SYN-404"}]

        with self.assertRaisesRegex(ValueError, "No summary expectation found"):
            evaluate_summaries(records, [])

    def test_load_expectations_rejects_non_list_json(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as handle:
            json.dump({"id": "SYN-001"}, handle)
            handle.flush()

            with self.assertRaisesRegex(ValueError, "Expected a list"):
                load_expectations(handle.name)


if __name__ == "__main__":
    unittest.main()
