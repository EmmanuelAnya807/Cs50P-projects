def main():
    """Calls check"""

    # Takes in user input
    greeting = input("Greeting: ")
    check(greeting)

def check(input):
    """Checks the greeting and prints the corresponding price"""

    # Converts the input to lowercase for case-insensitive comparison
    input = input.lower()

    # Removes leading and trailing whitespace
    input = input.strip()

    # Checks if the input starts with "hello", "h", or something else and prints the corresponding price
    if input.startswith('hello'):
        print("$0")

    elif input.startswith('h'):
        print("$20")

    else:
        print("$100")


main()


