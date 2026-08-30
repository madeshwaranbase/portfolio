from collections import Counter
from pathlib import Path

LOG_FILE = Path("sample.log")

if not LOG_FILE.exists():
    LOG_FILE.write_text(
        "INFO Login successful\n"
        "ERROR Database connection failed\n"
        "INFO User logged out\n"
        "ERROR Timeout occurred\n"
        "WARNING Slow response\n"
        "ERROR Database connection failed\n",
        encoding="utf-8"
    )

levels = Counter()
messages = Counter()

with LOG_FILE.open(encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(" ", 1)
        level = parts[0]
        message = parts[1] if len(parts) > 1 else ""

        levels[level] += 1
        if level == "ERROR":
            messages[message] += 1

print("Log Summary")
print("-----------")

for level, count in levels.items():
    print(f"{level:<8}: {count}")

if messages:
    print("\nMost common error:")
    print(messages.most_common(1)[0][0])
