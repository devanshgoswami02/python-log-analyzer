import re


def parse_log(line):
    """
    Parses one log line into a dictionary.
    """

    match = re.match(
        r"(\S+)\s+(\S+)\s+(.+)",
        line.strip()
    )

    if match:
        return {
            "date": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }

    return None


def parse_all_logs(lines):
    """
    Parses all log lines.
    """

    parsed_logs = []

    for line in lines:

        parsed = parse_log(line)

        if parsed:
            parsed_logs.append(parsed)

    return parsed_logs


def display_parsed_logs(parsed_logs):
    """
    Displays parsed log entries.
    """

    print("\n## Parsed Logs\n")

    if not parsed_logs:
        print("No valid log entries found.")
        return

    for log in parsed_logs:

        print(
            f"Date: {log['date']} | "
            f"Level: {log['level']} | "
            f"Message: {log['message']}"
        )