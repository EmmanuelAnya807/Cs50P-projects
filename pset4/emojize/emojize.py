import emoji


def main():
    text = input("Input: ")
    emo = convert_to_emoji(text)

    if emo is not None:
        print(f"Output: {emo}")


def convert_to_emoji(text):
    emoji_pic = emoji.emojize(text, language='alias')
    return emoji_pic


main()
