from __future__ import annotations
import argparse, json, os
from pathlib import Path
import requests

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "options", "head"}

def operations_from_spec(spec: dict) -> list[dict]:
    operations = []
    for path, item in (spec.get("paths") or {}).items():
        for method, operation in item.items():
            if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            operations.append({
                "path": path, "method": method.upper(),
                "operation_id": operation.get("operationId", ""),
                "summary": operation.get("summary", ""),
                "description": operation.get("description", ""),
                "parameters": operation.get("parameters", []),
                "request_body": operation.get("requestBody"),
                "responses": operation.get("responses", {}),
                "security": operation.get("security", spec.get("security", [])),
            })
    return operations

def ai_ideas(operations: list[dict]) -> str:
    key = os.getenv("AI_API_KEY")
    if not key:
        raise RuntimeError("AI_API_KEY is required for --ai.")
    base = os.getenv("AI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("AI_MODEL", "gpt-4.1-mini")
    prompt = ("Suggest positive, negative, boundary, authorization and schema test ideas "
              "for these OpenAPI operations. Do not invent required fields or business rules; "
              "mark missing information as questions.\n\n" + json.dumps(operations, indent=2)[:30000])
    response = requests.post(
        f"{base}/chat/completions",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"model": model, "messages": [{"role":"user","content":prompt}], "temperature":0.2},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--output", default="proposed-test-cases.md")
    parser.add_argument("--ai", action="store_true")
    args = parser.parse_args()
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    if not (spec.get("openapi") or spec.get("swagger")):
        raise ValueError("The input is not an OpenAPI/Swagger JSON document.")
    operations = operations_from_spec(spec)
    lines = ["# Proposed EventHub API Test Design", "",
             f"- API: {spec.get('info', {}).get('title', 'Untitled')}",
             f"- Version: {spec.get('info', {}).get('version', 'unknown')}",
             f"- Operations discovered: {len(operations)}", "",
             "> Draft generated from the contract. Review with the API owner before implementing.", ""]
    for op in operations:
        lines += [f"## {op['method']} `{op['path']}`",
                  f"- Operation ID: `{op['operation_id'] or 'not specified'}`",
                  f"- Summary: {op['summary'] or 'not documented'}",
                  f"- Request body: {'documented' if op['request_body'] else 'not documented'}",
                  f"- Responses: {', '.join(op['responses'].keys()) or 'not documented'}",
                  "- Candidate checks: documented success response; documented error responses; parameter boundaries; required-field validation where schema specifies it; authorization where security is declared; response content type and schema.",
                  ""]
    if args.ai and operations:
        lines += ["## AI-assisted scenario suggestions", "", ai_ideas(operations), ""]
    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated draft for {len(operations)} operations: {args.output}")

if __name__ == "__main__":
    main()
