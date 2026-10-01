def convert():
    """Converts emoticons to Unicode characters"""
    # Takes in user input
    emoticon = input("")

    # Replace emoticons with corresponding Unicode characters
    faces = emoticon.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")

    # Print the converted emoticon
    print(faces)

# The main function


def main():
    """Calls convert"""
    convert()


main()
