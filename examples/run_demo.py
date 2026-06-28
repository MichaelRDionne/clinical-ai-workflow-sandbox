from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from clinical_workflow import build_follow_up_queue, intake_summary, load_records, longitudinal_snapshot, safety_flags


def main() -> None:
    records = load_records(ROOT / "synthetic-data" / "patient-fixtures.json")

    print("INTAKE SUMMARY")
    print(intake_summary(records[0]))
    print()

    print("LONGITUDINAL SNAPSHOT")
    for line in longitudinal_snapshot(records):
        print(f"- {line}")
    print()

    print("FOLLOW-UP QUEUE")
    for item in build_follow_up_queue(records):
        print(f"- {item['id']} [{item['priority']}]: {item['reason']}")
    print()

    print("SAFETY FLAGS")
    for record in records:
        flags = safety_flags(record)
        if flags:
            print(f"- {record['id']}: {'; '.join(flags)}")


if __name__ == "__main__":
    main()
