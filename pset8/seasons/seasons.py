from datetime import date, datetime
import sys
import inflect


def main():
    # Prompt user for input and validate format
    try:
        date_of_birth = input("Date of Birth: ")
        date_format = date_pattern(date_of_birth)
    except ValueError:
        sys.exit("Invalid date")

    # Calculate age in minutes and display result
    age = DateCalculation(date_format).calculate_mins()
    print(age)


def date_pattern(input_date):
    # Parse YYYY-MM-DD string into a date object; raise ValueError if invalid
    try:
        date_format = datetime.strptime(input_date, '%Y-%m-%d').date()
        return date_format

    except ValueError:
        raise ValueError


class DateCalculation():
    # Calculate day difference between today and birthdate, then convert to total minutes
    def __init__(self, input_date):
        self.input_date = input_date

    def calculate_mins(self):
        # Calculate day difference between today and birthdate, then convert to total minutes
        current_date = date.today()
        date_diff = current_date - self.input_date
        days = date_diff.days
        mins = days * 24 * 60

        # Convert numerical minutes to formatted words (no 'and', capitalized)
        p = inflect.engine()
        age_in_mins = p.number_to_words(mins, andword="").capitalize()
        return f"{age_in_mins} minutes"


if __name__ == "__main__":
    main()
