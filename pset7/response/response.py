from validator_collection import checkers


def main():
    # Prompt the user for an email address and validate it
    email = input("What is your email address? ")
    email_checked = email_checker(email)

    # Output validation result based on the boolean check
    if email_checked:
        print('Valid')

    else:
        print('Invalid')


def email_checker(email):
    """Check if the provided string is a valid email address using validator_collection."""
    return checkers.is_email(email)


main()
