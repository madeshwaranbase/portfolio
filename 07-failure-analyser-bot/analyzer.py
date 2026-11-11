from __future__ import annotations
import argparse
import json
import os
import re
from pathlib import Path
import requests

REDACTIONS = [
    (re.compile(r"(?i)(password|token|authorization|api[_-]?key)\s*[:=]\s*[^\s,;]+"), r"\1=[REDACTED]"),
    (re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I), "[EMAIL]"),
]

def sanitize(text: str) -> str:
    for pattern, replacement in REDACTIONS:
        text = pattern.sub(replacement, text)
    return text[:8000]

def failures_from_report(report: dict) -> list[dict]:
    found: list[dict] = []
    def visit(suite: dict, parents: list[str]) -> None:
        title = suite.get("title", "")
        path = parents + ([title] if title else [])
        for spec in suite.get("specs", []):
            for test in spec.get("tests", []):
                for result in test.get("results", []):
                    if result.get("status") not in {"failed", "timedOut", "interrupted"}:
                        continue
                    found.append({
                        "test": " / ".join(path + [spec.get("title", "")]),
                        "status": result.get("status"),
                        "duration_ms": result.get("duration"),
                        "errors": [sanitize(e.get("message", "")) for e in result.get("errors", [])],
                    })
        for child in suite.get("suites", []):
            visit(child, path)
    for suite in report.get("suites", []):
        visit(suite, [])
    return found

def ask_ai(failures: list[dict]) -> str:
    key = os.getenv("AI_API_KEY")
    if not key:
        raise RuntimeError("AI_API_KEY is required for --ai.")
    base = os.getenv("AI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("AI_MODEL", "gpt-4.1-mini")
    prompt = ("Analyze these sanitized Playwright failures. Return evidence, likely causes "
              "and next debugging actions. Label causes as hypotheses and do not claim certainty.\n\n"
              + json.dumps(failures, indent=2))
    response = requests.post(
        f"{base}/chat/completions",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def main() -> None:
    parser = argparse.ArgumentParser(description="Create a sanitized Playwright failure triage report.")
    parser.add_argument("--input", required=True, help="Playwright JSON reporter output")
    parser.add_argument("--output", default="failure-summary.md")
    parser.add_argument("--ai", action="store_true")
    args = parser.parse_args()

    report = json.loads(Path(args.input).read_text(encoding="utf-8"))
    failures = failures_from_report(report)
    lines = ["# Playwright Failure Triage", "", f"Failure count: **{len(failures)}**", ""]
    for number, failure in enumerate(failures, 1):
        lines += [f"## {number}. {failure['test']}", f"- Status: `{failure['status']}`",
                  f"- Duration: `{failure['duration_ms']} ms`"]
        for error in failure["errors"]:
            lines += ["", "```text", error, "```"]
        lines.append("")
    if args.ai and failures:
        lines += ["## AI-assisted diagnostic hypotheses", "", ask_ai(failures), ""]
    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output}; parsed {len(failures)} failed test(s).")

if __name__ == "__main__":
    main()
