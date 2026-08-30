import time
import requests

URL = "https://jsonplaceholder.typicode.com/users"

start = time.perf_counter()

try:
    response = requests.get(URL, timeout=10)
    elapsed = time.perf_counter() - start

    print("API Data Checker")
    print("----------------")
    print("Status code:", response.status_code)
    print(f"Response time: {elapsed:.2f} seconds")

    if response.status_code != 200:
        print("API Status: FAIL")
        raise SystemExit(1)

    users = response.json()

    if not isinstance(users, list):
        print("API Status: FAIL - expected a list")
        raise SystemExit(1)

    required_fields = {"id", "name", "email"}

    for user in users:
        missing = required_fields - user.keys()
        if missing:
            print("API Status: FAIL")
            print("Missing fields:", missing)
            raise SystemExit(1)

    print("Users found:", len(users))
    print("API Status: PASS")

except requests.RequestException as error:
    print("Request failed:", error)
    raise SystemExit(1)
