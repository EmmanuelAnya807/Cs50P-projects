# List of valid month names for text-based date validation
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    # Start the date-reformatting program
    outdated(month_list)


def outdated(month_list):
    """Loop indefinitely to prompt the user for a date until a valid format is parsed."""
    while True:
        try:
            date = input("Date: ")
            # Process format; if successful, it breaks the loop via return
            return date_format(date, month_list)

        except ValueError:
            # Silently catch validation errors and prompt the user again
            pass


def date_format(date, month_list):
    """Validate numeric or text date string and print in YYYY-MM-DD format."""
    # Handle numeric format (e.g., MM/DD/YYYY)
    if '/' in date:
        x, y, z = date.split("/")
        month = int(x)
        day = int(y)
        year = int(z)

        # Validate calendar boundaries
        if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):
            print(f"{year}-{month:02d}-{day:02d}")

        else:
            raise ValueError

    # Handle text format (e.g., September 8, 1636)
    elif ',' in date:
        date = date.replace(',', '')
        x, y, z = date.split()
        # Normalize text to match month_list casing
        x = x.capitalize()

        if x in month_list:
            month = month_list.index(x) + 1
            month = int(month)
            day = int(y)
            year = int(z)

            # Validate calendar boundaries
            if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):
                print(f"{year}-{month:02d}-{day:02d}")

            else:
                raise ValueError

        else:
            raise ValueError

    # Reject unsupported string formats
    else:
        raise ValueError


main()
