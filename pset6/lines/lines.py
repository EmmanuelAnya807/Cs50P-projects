import sys


def main():
    # Execute the program pipeline step-by-step
    file = command_line_arg()
    file_to_read = check_python_file(file)
    print(count_lines(file_to_read))


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
        sys.exit("Not a python file.")

    # Fail validation if the string segment after the dot is not the required extension keyword
    elif extension[1] != 'py':
        sys.exit("Not a python file.")

    # Return verified filename string if all conditions pass successfully
    else:
        return file


def count_lines(file_to_read):
    """Count and return lines of code, excluding comments and blank lines."""
    try:

        # Safely open the specified file for inspection and close it automatically when finished
        with open(file_to_read) as f:
            reader = f.readlines()
            new_list = []

            # Evaluate every individual line extracted from the document
            for line in reader:

                # Remove leading whitespace to correctly evaluate indentation level
                line = line.lstrip(" ")

                # Ignore lines that are comments or blank newlines
                if line.startswith('#'):
                    pass
                elif line.isspace():
                    pass

                # Accumulate actual code strings that contain data into the tracking array
                else:
                    new_list.append(line)

            # Return the aggregated total count of matching code rows found
            return (len(new_list))

    # Catch file opening anomalies if the system cannot locate the specified pathway
    except FileNotFoundError:
        sys.exit("File does not exist.")


if __name__ == "__main__":
    main()
