import csv
from collections import Counter
from pathlib import Path

INPUT_FILE = Path("test_results.csv")
REPORT_FILE = Path("test_report.txt")

if not INPUT_FILE.exists():
    INPUT_FILE.write_text(
        "test_name,status\n"
        "login_test,PASS\n"
        "search_test,PASS\n"
        "checkout_test,FAIL\n"
        "logout_test,PASS\n",
        encoding="utf-8"
    )

with INPUT_FILE.open(newline="", encoding="utf-8") as file:
    results = list(csv.DictReader(file))

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

REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

print("\n".join(lines))
print(f"\nReport saved to {REPORT_FILE}")
