def main():
    """Calls response"""

    # Takes in user input
    question = str(
        input("What is the Answer to the Great Question of Life, the Universe and Everything? "))
    response(question)


def response(input):
    """Checks if the input is the correct answer to the Great Question of Life, the Universe and Everything"""

    # Converts the input to lowercase for case-insensitive comparison
    input = input.lower()

    # Removes leading and trailing whitespace
    input = input.strip()
    
    # Checks if the input is "42", "forty-two", or "forty two"
    if input == "42" or input == "forty-two" or input == "forty two":
        print("Yes")

    else:
        print("No")


main()
