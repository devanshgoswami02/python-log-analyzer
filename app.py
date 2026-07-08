import argparse
import os

from reader import read_logs, read_multiple_logs

from analyzer import (
    count_logs,
    display_result,
    top_errors,
    display_top_errors
)

from parser import (
    parse_all_logs,
    display_parsed_logs
)

from reports import (
    generate_report,
    generate_csv_report,
    generate_json_report
)


def main():

    parser = argparse.ArgumentParser(
        description="Python Log Analyzer CLI Tool"
    )

    parser.add_argument(
        "filename",
        help="Path of the log file or folder"
    )

    args = parser.parse_args()

    # Read single file or multiple files
    if os.path.isdir(args.filename):

        print(f"\nAnalyzing all log files inside: {args.filename}\n")

        lines = read_multiple_logs(args.filename)

    else:

        lines = read_logs(args.filename)

    if not lines:
        print("No logs available for analysis.")
        return

    # Analyze logs
    log_count = count_logs(lines)
    display_result(log_count)

    error_counter = top_errors(lines)
    display_top_errors(error_counter)

    parsed_logs = parse_all_logs(lines)

    # Generate reports
    generate_report(log_count, error_counter)
    generate_csv_report(log_count)
    generate_json_report(
        log_count,
        error_counter,
        parsed_logs
    )

    # Display parsed logs
    display_parsed_logs(parsed_logs)


if __name__ == "__main__":
    main()