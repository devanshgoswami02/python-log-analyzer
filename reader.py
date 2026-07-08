import os


def read_logs(filename):
    """
    Reads all log lines from a single log file.
    """

    try:
        with open(filename, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"ERROR: {filename} was not found.")
        return []

    except PermissionError:
        print(f"ERROR: Permission denied while reading {filename}.")
        return []

    except Exception as error:
        print(f"Unexpected Error: {error}")
        return []

    finally:
        print("Log reading process completed.\n")


def read_multiple_logs(folder):
    """
    Reads all .log and .txt files from a folder.
    """

    all_lines = []

    for filename in os.listdir(folder):

        if filename.endswith(".log") or filename.endswith(".txt"):

            path = os.path.join(folder, filename)

            try:
                with open(path, "r") as file:
                    all_lines.extend(file.readlines())

            except Exception as error:
                print(f"Could not read {filename}: {error}")

    return all_lines