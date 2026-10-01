import sys
from tabulate import tabulate
import csv


def main():
    # Execute the program pipeline step-by-step
    file = command_line_arg()
    file_to_read = check_python_file(file)
    print(tabulate_csv(file_to_read))


def command_line_arg():
    """Validate command-line arguments and return the target file path."""

    # Check if exactly one argument (the filename) is passed alongside the script execution
    if len(sys.argv) == 2:
        file = sys.argv[1]
        return file

    # Handle error state where the filename argument is missing entirely
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")

    # Handle error state where extra parameters are provided in the terminal instruction
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")


def check_python_file(file):
    """Verify that the provided file has a valid .py extension."""

    # Isolate the file extension from the right side
    extension = file.rsplit('.', 1)

    # Fail validation if no dot element exists in the filename structure
    if len(extension) != 2:
        sys.exit("Not a CSV file.")

    # Fail validation if the string segment after the dot is not the required extension keyword
    elif extension[1] != 'csv':
        sys.exit("Not a CSV file.")

    # Return verified filename string if all conditions pass successfully
    else:
        return file


def tabulate_csv(file_to_read):
    """Read a CSV file and return its data formatted as a grid table."""
    try:
        # Open the specified CSV file safely for reading
        with open(file_to_read) as f:

            # Parse the CSV rows into dictionaries using the first row as keys
            reader = csv.DictReader(f)

            # Generate and return a structured grid string using column headers
            return tabulate(reader, headers='keys', tablefmt='grid')

    except FileNotFoundError:
        # Terminate execution if the specified file pathway is missing
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
