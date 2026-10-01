from pyfiglet import Figlet
import sys
from random import choice


def main():

    # Initialize figlet and retrieve all available font names
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Case 1: No command-line arguments; pick a font at random
    if len(sys.argv) == 1:
        selected_font = choice(fonts)

    # Case 2: Exactly two arguments; validate the flag and font name
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        selected_font = sys.argv[2]

    # Case 3: Any other number of arguments is invalid
    else:
        sys.exit("Invalid usage")

    # Get input string from user and render it using the selected font
    text = input("Input: ")
    print("Output: ")
    text_to_fig(text, selected_font)


def text_to_fig(text, selected_font):
    """Render and print the provided text in the selected figlet font."""
    figlet = Figlet()
    figlet.setFont(font=selected_font)
    print(figlet.renderText(text))


main()



https://cdn.cs50.net/web/2020/spring/projects/2/commerce.zip
