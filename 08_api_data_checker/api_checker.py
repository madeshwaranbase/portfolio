import sys
import time

import requests

URL = "https://jsonplaceholder.typicode.com/users"
REQUIRED_FIELDS = {"id", "name", "email"}


def fetch_users(url=URL, timeout=10):
    """Make the request and return (status_code, elapsed_seconds, users_or_none, error_or_none)."""
    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException as error:
        return None, time.perf_counter() - start, None, str(error)

    elapsed = time.perf_counter() - start

    if response.status_code != 200:
        return response.status_code, elapsed, None, f"non-200 status: {response.status_code}"

    try:
        users = response.json()
    except ValueError as error:
        return response.status_code, elapsed, None, f"invalid JSON: {error}"

    return response.status_code, elapsed, users, None


def validate_users(users, required_fields=REQUIRED_FIELDS):
    """Return (is_valid, error_message_or_None)."""
    if not isinstance(users, list):
        return False, "expected a list of users"

    for user in users:
        missing = required_fields - user.keys()
        if missing:
            return False, f"missing fields: {missing}"

    return True, None


def check_api(url=URL, timeout=10):
    """Run the full check and return a result dict — no printing, no sys.exit."""
    status_code, elapsed, users, fetch_error = fetch_users(url, timeout)

    result = {
        "status_code": status_code,
        "elapsed": elapsed,
        "passed": False,
        "users_count": None,
        "error": fetch_error,
    }

    if fetch_error:
        return result

    is_valid, validation_error = validate_users(users)
    if not is_valid:
        result["error"] = validation_error
        return result

    result["passed"] = True
    result["users_count"] = len(users)
    return result


def print_report(result):
    print("API Data Checker")
    print("----------------")
    if result["status_code"] is not None:
        print("Status code:", result["status_code"])
    print(f"Response time: {result['elapsed']:.2f} seconds")

    if result["passed"]:
        print("Users found:", result["users_count"])
        print("API Status: PASS")
    else:
        print("API Status: FAIL")
        print("Reason:", result["error"])


def main():
    result = check_api()
    print_report(result)
    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
