def main():
    # Get plate input from the user
    plate = input("Plate: ")

    # Check validity and print the result
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Rule 1: Plate length must be between 2 and 6 characters
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Rule 2: The first two characters must be letters
    if not plate[:2].isalpha():
        return False

    # Rule 3: No periods, spaces, or punctuation allowed (must be alphanumeric)
    if not plate.isalnum():
        return False

    has_number = False
    # Loop through each character to check number rules
    for letter in plate:
        # Rule 4a: The first number used cannot be '0'
        if letter == '0' and has_number == False:
            return False

    # Rule 4b: If it's a valid digit, turn on the number tracking flag
        elif letter.isdigit():
            has_number = True

    # Rule 4c: If it's a letter but a number came before it, reject it
        elif letter.isalpha() and has_number == True:
            return False

    # If the plate passed all the validation rules above, it is valid
    return True


if __name__ == "__main__":
    main()
