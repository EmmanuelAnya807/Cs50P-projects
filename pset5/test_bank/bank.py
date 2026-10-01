def main():
    """Calls check"""

    # Takes in user input
    greeting = str(input("Greeting: "))
    print(f"${value(greeting)}")


def value(greeting):
    """Checks the greeting and prints the corresponding price"""

    # Converts the input to lowercase for case-insensitive comparison
    greeting = greeting.lower()

    # Removes leading and trailing whitespace
    greeting = greeting.strip()

    # Checks if the input starts with "hello", "h", or something else and prints the corresponding price
    if greeting.startswith('hello'):
        return (0)

    elif greeting.startswith('h'):
        return (20)

    else:
        return (100)


if __name__ == "__main__":
    main()
