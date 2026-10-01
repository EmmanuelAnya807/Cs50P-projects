def main():
    # Get text input from the user
    user_input = input("Input: ")
    print("Output: ", end="")

    # Process the text to remove vowels
    omit_vowel(user_input)
    print()


def omit_vowel(user_input):
    # Define the vowels to filter out
	vowels = "aeiou"
	for letter in user_input:
        # If it's a letter, check if it's a consonant
		if letter.isalpha():

            # If its lowercase version isn't a vowel, print it
			if letter.lower() not in vowels:
				print(letter, end="")

        # If it's a symbol, number, or space, print it exactly as it is
		else:
			print(letter, end="")


main()
