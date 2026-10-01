def playback():
    """Plays back user input, replacing whitespace with ellipses"""
    # Takes in user input
    text = input("")

    # Prints the input as is, but if the input is only whitespace, prints "..." instead
    for i in range(len(text)):
        if text[i].isspace():
            print("...", end="")

        else:
            print(text[i], end="")

    # Print a newline at the end
    print()

# The main function


def main():
    """Calls playback"""
    playback()


main()
