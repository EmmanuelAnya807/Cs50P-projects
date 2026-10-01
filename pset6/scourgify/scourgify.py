import sys
import csv


def main():
    # Execute the program pipeline step-by-step
    file_to_read, file_to_write = command_line_arg()
    clean_csv(file_to_read, file_to_write)


def command_line_arg():
    """Validate command-line arguments and return the target file path."""

    # Check if exactly one argument (the filename) is passed alongside the script execution
    if len(sys.argv) == 3:
        file_read = sys.argv[1]
        file_write = sys.argv[2]
        return file_read, file_write

    # Handle error state where the filename argument is missing entirely
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")

    # Handle error state where extra parameters are provided in the terminal instruction
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")


def clean_csv(file_to_read, file_to_write):
    """Read a CSV file and return its data formatted as a grid table."""
    try:
        # Open the specified CSV file safely for reading
        with open(file_to_read) as f1, open(file_to_write, 'w') as f2:

            # Parse the CSV rows into dictionaries using the first row as keys
            reader = csv.DictReader(f1)
            writer = csv.DictWriter(f2, (["first", "last", "house"]))
            writer.writeheader()
            for row in reader:
                name = row['name']
                last, first = name.split(',')
                first = first.strip()

                writer.writerow({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        # Terminate execution if the specified file pathway is missing
        sys.exit(f"Could not read {file_to_read}")


if __name__ == "__main__":
    main()
