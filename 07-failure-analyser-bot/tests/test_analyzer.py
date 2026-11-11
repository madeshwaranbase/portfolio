import unittest
from analyzer import sanitize, failures_from_report

class AnalyzerTests(unittest.TestCase):
    def test_sanitizes_email_and_password(self):
        value = sanitize("user@example.com password=secret")
        self.assertNotIn("user@example.com", value)
        self.assertNotIn("secret", value)

    def test_extracts_failed_results(self):
        report = {"suites":[{"title":"ui","specs":[{"title":"login","tests":[{"results":[
            {"status":"failed","duration":100,"errors":[{"message":"assertion failed"}]}
        ]}]}]}]}
        failures = failures_from_report(report)
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0]["status"], "failed")

if __name__ == "__main__":
    unittest.main()
