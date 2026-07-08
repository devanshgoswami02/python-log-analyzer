import csv
import json


def generate_report(log_count, error_counter):
    """
    Generates a text report.
    """

    with open("report.txt", "w") as file:

        file.write("LOG ANALYSIS REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write("Log Summary\n")
        file.write("-" * 20 + "\n")

        file.write(f"INFO Logs    : {log_count['INFO']}\n")
        file.write(f"WARNING Logs : {log_count['WARNING']}\n")
        file.write(f"ERROR Logs   : {log_count['ERROR']}\n\n")

        file.write("Top Repeated Errors\n")
        file.write("-" * 20 + "\n")

        if error_counter:

            for error, count in error_counter.most_common():
                file.write(f"{error:<25} : {count}\n")

        else:
            file.write("No ERROR logs found.\n")

    print("✅ report.txt generated successfully.")


def generate_csv_report(log_count):
    """
    Generates a CSV report.
    """

    with open("report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Log Level", "Count"])
        writer.writerow(["INFO", log_count["INFO"]])
        writer.writerow(["WARNING", log_count["WARNING"]])
        writer.writerow(["ERROR", log_count["ERROR"]])

        total_logs = (
            log_count["INFO"] +
            log_count["WARNING"] +
            log_count["ERROR"]
        )

        writer.writerow(["TOTAL", total_logs])

    print("✅ report.csv generated successfully.")


def generate_json_report(log_count, error_counter, parsed_logs):
    """
    Generates a JSON report.
    """

    report = {

        "summary": log_count,

        "top_errors": dict(error_counter),

        "parsed_logs": parsed_logs

    }

    with open("report.json", "w") as file:

        json.dump(report, file, indent=4)

    print("✅ report.json generated successfully.")