from collections import Counter


def count_logs(lines):
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in lines:

        if "INFO" in line:
            log_count["INFO"] += 1

        elif "WARNING" in line:
            log_count["WARNING"] += 1

        elif "ERROR" in line:
            log_count["ERROR"] += 1

    return log_count


def display_result(log_count):

    print("## Log Summary\n")

    print("INFO Logs    :", log_count["INFO"])
    print("WARNING Logs :", log_count["WARNING"])
    print("ERROR Logs   :", log_count["ERROR"])


def top_errors(lines):

    error_messages = []

    for line in lines:

        if "ERROR" in line:

            parts = line.split()

            message = " ".join(parts[2:])

            error_messages.append(message)

    return Counter(error_messages)


def display_top_errors(counter):

    print("\n## Top Repeated Errors\n")

    if not counter:
        print("No ERROR logs found.")
        return

    for error, count in counter.most_common():
        print(f"{error:<25} : {count}")