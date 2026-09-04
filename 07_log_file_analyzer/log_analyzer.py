from collections import Counter
from pathlib import Path

LOG_FILE = Path("sample.log")

SAMPLE_LOG = (
    "INFO Login successful\n"
    "ERROR Database connection failed\n"
    "INFO User logged out\n"
    "ERROR Timeout occurred\n"
    "WARNING Slow response\n"
    "ERROR Database connection failed\n"
)


def ensure_sample_log(path=LOG_FILE):
    if not path.exists():
        path.write_text(SAMPLE_LOG, encoding="utf-8")


def parse_log(path=LOG_FILE):
    """Read the log file and return (level_counts, error_message_counts)."""
    levels = Counter()
    messages = Counter()

    with path.open(encoding="utf-8") as file:
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

    return levels, messages


def format_summary(levels, messages):
    """Build the report as a string so it's testable and reusable (print or write to file)."""
    lines = ["Log Summary", "-----------"]
    for level, count in levels.items():
        lines.append(f"{level:<8}: {count}")

    if messages:
        lines.append("")
        lines.append("Most common error:")
        lines.append(messages.most_common(1)[0][0])

    return "\n".join(lines)


def main():
    ensure_sample_log()
    levels, messages = parse_log()
    print(format_summary(levels, messages))


if __name__ == "__main__":
    main()
