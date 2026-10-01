import re


def main():
    # Prompt user for text and print the count of standalone "um"s
    print(count(input("Text: ")))


def count(s):
    """Count occurrences of the word 'um' in a string, case-insensitively."""

    # Match 'um' only as a standalone word (word boundaries prevent matching inside words like 'yummy')
    pattern = r'\bum\b'
    match = re.findall(pattern, s, re.IGNORECASE)

    # Return the total number of matched occurrences
    return len(match)


if __name__ == "__main__":
    main()
