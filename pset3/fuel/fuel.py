def main():
    # Start the fuel tracking program
    print(fuel_fraction())


def fuel_fraction():
    """Prompt user for a fraction and loop until valid input is given."""
    while True:
        try:
            fraction = input("Fraction: ")

            # If valid, pass to gauge and exit the loop
            return fuel_guage(fraction)

        except (ValueError, ZeroDivisionError):
            # Ignore invalid formatting or division by zero and prompt again
            pass


def fuel_guage(fraction):
    """Convert fraction string to percentage and print fuel level."""
    # Parse numerator and denominator
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    percentage = round((x / y) * 100)

    # Ensure the fraction is mathematically and logically valid
    if x >= 0 and x <= y:
        if percentage <= 1:
            result = "E"

        elif percentage >= 99:
            result = "F"

        else:
            result = f"{percentage}%"

        return result
    else:
        # Force a loop reset if the fraction makes no logical sense
        raise ValueError


main()
