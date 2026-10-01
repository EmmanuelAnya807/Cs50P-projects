from random import randint


def main():

    # Prompt the user until a positive integer level is provided
    while True:
        try:
            number = int(input("Level: "))
            if number > 0:
                break

        except ValueError:
            pass

    # Print the "Just right!" string returned by the game function
    print(game(number))


def game(number):

    # Generate a secret random number between 1 and the chosen level
    rand_no = randint(1, number)

    # Loop indefinitely to process user guesses
    while True:
        try:
            guess = int(input("Guess: "))

            # Check only positive integer guesses
            if guess > 0:
                if guess < rand_no:
                    print("Too small!")
                elif guess > rand_no:
                    print("Too large!")
                elif guess == rand_no:

                    # Return success message to main, breaking the game loop
                    return "Just right!"
                else:
                    pass
            else:
                pass

        except ValueError:
            # Ignore non-integer inputs and prompt again
            pass


main()
