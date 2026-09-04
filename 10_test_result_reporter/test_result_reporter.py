import csv
from collections import Counter
from pathlib import Path

INPUT_FILE = Path("test_results.csv")
REPORT_FILE = Path("test_report.txt")

SAMPLE_RESULTS = (
    "test_name,status\n"
    "login_test,PASS\n"
    "search_test,PASS\n"
    "checkout_test,FAIL\n"
    "logout_test,PASS\n"
)


def ensure_sample_input(path=INPUT_FILE):
    if not path.exists():
        path.write_text(SAMPLE_RESULTS, encoding="utf-8")


def load_results(path=INPUT_FILE):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def build_report(results):
    """Compute summary + failed-test list and return the report as a string."""
    counts = Counter(row["status"].upper() for row in results)
    total = len(results)
    passed = counts["PASS"]
    failed = counts["FAIL"]
    pass_rate = (passed / total * 100) if total else 0

    lines = [
        "Automation Test Summary",
        "=======================",
        f"Total Tests : {total}",
        f"Passed      : {passed}",
        f"Failed      : {failed}",
        f"Pass Rate   : {pass_rate:.1f}%",
        "",
        "Failed Tests",
        "------------",
    ]

    failed_tests = [row["test_name"] for row in results if row["status"].upper() == "FAIL"]
    lines.extend(failed_tests or ["None"])

    return "\n".join(lines)


def save_report(report, path=REPORT_FILE):
    path.write_text(report, encoding="utf-8")


def main():
    ensure_sample_input()
    results = load_results()
    report = build_report(results)
    save_report(report)
    print(report)
    print(f"\nReport saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()
