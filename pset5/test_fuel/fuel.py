def main():
    # Start the fuel tracking program
    """Prompt user for a fraction and loop until valid input is given."""
    while True:
        try:
            fraction = input("Fraction: ")

            # If valid, pass to gauge and exit the loop
            percentage = convert(fraction)
            break

        except (ValueError, ZeroDivisionError):
            # Ignore invalid formatting or division by zero and prompt again
            pass

    print(gauge(percentage))


def convert(fraction):
    """Convert fraction string to percentage and print fuel level."""
    # Parse numerator and denominator
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)

    if x > y or x < 0:
        raise ValueError

    elif y == 0:
        raise ZeroDivisionError

    elif x >= 0 and x <= y and y > 0:
        percentage = round((x / y) * 100)

    return percentage


def gauge(percentage):

    if percentage <= 1:
        return ("E")

    elif percentage >= 99:
        return ("F")

    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()
