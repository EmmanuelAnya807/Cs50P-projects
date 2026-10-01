def main():
    # Get the camelCase string from the user
    user_input = input("camelCase: ")

# Print the label prefix; end="" keeps the converted text on the same line
    print("snake_case: ", end="")

# Call the conversion function and pass the user's input to it
    snake_case(user_input)

# Print a final newline character to clean up the terminal output
    print()


def snake_case(user_input):
    # Loop through the input string, tracking both the position index (i) and the character (letter)
    for i, letter in enumerate(user_input):

        # Rule 1: If it's the very first character, convert to lowercase without an underscore
        if i == 0:
            print(letter.lower(), end="")

    # Rule 2: If the letter is uppercase (and not the first character), add an underscore and lowercase it
        elif letter.isupper():
            print("_" + letter.lower(), end="")

    # Rule 3: For all other characters (lowercase letters, numbers, symbols), print them as they are
        else:
            print(letter, end="")


main()
