def main():
    """
    Prompt the user for a valid time input and
    display the corresponding meal time.
    """

    # Keep asking until a valid time is entered
    while True:

        time = input("What time is it? ")
        hour = convert(time)

        if hour:
            break

    meal = meal_time(hour)

    if meal:
        print(meal)


def convert(time):
    """
    Convert a time string in HH:MM format
    into a floating-point hour value.

    Returns:
        float: Decimal representation of time.
    """

    try:

        # Remove leading and trailing spaces from input
        time = time.strip()

        # Split the time into hour and minute components
        hours, minutes = time.split(':')

        # Convert hours and minutes into numeric values
        if ':' in time and hours.isdigit() and minutes.isdigit():

            minutes = int(minutes)
            hours = int(hours)

        # Convert minutes into a fractional hour
        if minutes >= 0 and minutes < 60:
            converted_hr = hours + (minutes / 60)

        return converted_hr

    except (ValueError):
        print("Re-enter time in this format ##:##")


def meal_time(hour):
    """
    Determine which meal corresponds to a given hour.

    Args:
        hour (float): Time represented as a decimal hour.

    Returns:
        str: Meal name if within a meal period.
    """

    if hour >= 7.00 and hour <= 8.00:
        return "breakfast time"

    elif hour >= 12.00 and hour <= 13.00:
        return "lunch time"

    elif hour >= 18.00 and hour <= 19.00:
        return "dinner time"


if __name__ == '__main__':
    main()
