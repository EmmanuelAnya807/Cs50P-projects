def main():
    # Get text input from the user
    word = input("Input: ")
    print("Output: ", end="")

    # Process the text to remove vowels
    print(shorten(word))


def shorten(word):
    # Define the vowels to filter out
    vowels = "aeiou"
    letters = []
    for letter in word:
        # If it's a letter, check if it's a consonant
        if letter.isalpha():

            # If its lowercase version isn't a vowel, print it
            if letter.lower() not in vowels:
                letters.append(letter)

        # If it's a symbol, number, or space, print it exactly as it is
        else:
            letters.append(letter)

    short_word = "".join(letters)
    return short_word


if __name__ == "__main__":
    main()
