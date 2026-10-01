from random import randrange


def main():
    # 1. Get the game difficulty level from the user
    level = get_level()
    correct = 0

    # 2. Main game loop running exactly 10 addition problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        # Give the player up to 3 attempts per math problem
        for attempt in range(3):

            try:
                math_prob = input(f"{x} + {y} = ")

                if int(math_prob) == answer:
                    correct += 1
                    break   # Correct answer; break out of the attempts loop

                else:
                    print("EEE")

            except ValueError:
                # Handle non-integer text inputs as an incorrect attempt
                print("EEE")

        else:
            # If all 3 attempts fail without breaking, display the solution
            print(f"{x} + {y} = {answer}")

    # 3. Print the final score out of 10
    print(f"Score: {correct}")


def get_level():
    """Prompt the user until a valid level (1, 2, or 3) is selected."""
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    """Return a single randomly generated integer based on the digit length."""

    if level == 1:
        rand_no = randrange(0, 10)

    elif level == 2:
        rand_no = randrange(10, 100)

    elif level == 3:
        rand_no = randrange(100, 1000)

    else:
        raise ValueError

    return rand_no


if __name__ == "__main__":
    main()
