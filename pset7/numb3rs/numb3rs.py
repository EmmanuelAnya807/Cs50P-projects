import re


def main():
    # Prompt user for an IPv4 address and display the validation result
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Validate whether an input string is a properly formatted IPv4 address."""
    # Define regex pattern for four dot-separated groups of 1 to 3 digits
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)

    # Return False immediately if the basic structure does not match
    if match is None:
        return False

    # Check each extracted numeric block (octet) against IPv4 rules
    for address in match.groups():

        # Ensure the octet value does not exceed the valid 0-255 range
        if int(address) > 255:
            return False

        # Reject leading zeros by ensuring the string matches its non-padded integer representation
        if address != str(int(address)):
            return False

    return True


if __name__ == "__main__":
    main()
