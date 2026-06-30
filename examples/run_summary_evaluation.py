from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from clinical_workflow import load_records
from summary_evaluation import evaluate_summaries, load_expectations


def main() -> None:
    records = load_records(ROOT / "synthetic-data" / "patient-fixtures.json")
    expectations = load_expectations(ROOT / "synthetic-data" / "expected-summary-fixtures.json")
    results = evaluate_summaries(records, expectations)

    print("SUMMARY EVALUATION")
    for result in results:
        status = "PASS" if result["passed"] else "REVIEW"
        print(f"- {result['id']}: {status}")
        if result["missing_required"]:
            print(f"  Missing required phrases: {', '.join(result['missing_required'])}")
        if result["present_forbidden"]:
            print(f"  Forbidden phrases present: {', '.join(result['present_forbidden'])}")


if __name__ == "__main__":
    main()
