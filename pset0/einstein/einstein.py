def einstein():
    """Calculates energy using E=mc^2"""
    # Takes in user input
    mass = int(input("m: "))

    # Calculates energy using E=mc^2
    energy = mass * (300000000 ** 2)

    # Prints the calculated energy
    print(f"E: {energy}")

# The main function


def main():
    """Calls einstein"""
    einstein()


main()
