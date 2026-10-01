import re
import sys


def main():
    try:
        convert(input("Hours: "))

    except ValueError:
        sys.exit("Invalid 12 hour time format.")


def convert(s):
    pattern = r'^(0?\d{1,2})(:[0-5]\d)?(\s[AP]M)(\sto\s)(0?\d{1,2})(:[0-5]\d)?(\s[AP]M)$'
    match = re.search(pattern, s, re.IGNORECASE)

    if match:
        hour1 = int(match.group(1))
        hour2 = int(match.group(5))
        if hour1 < 12 and hour1 > 0:
            if match.group(3) == " AM":
                updated_hr1 = hour1

            elif match.group(3) == " PM":
                updated_hr1 = hour1 + 12

        elif hour1 == 12:
            if match.group(3) == " AM":
                updated_hr1 = 0

            elif match.group(3) == " PM":
                updated_hr1 = hour1

        else:
            raise ValueError

        if hour2 < 12 and hour2 > 0:
            if match.group(7) == " AM":
                updated_hr2 = hour2

            elif match.group(7) == " PM":
                updated_hr2 = hour2 + 12

        elif hour2 == 12:
            if match.group(7) == " AM":
                updated_hr2 = 0

            elif match.group(7) == " PM":
                updated_hr2 = hour2

        else:
            raise ValueError

        if match.group(2) is None:
            new_format1 = f"{updated_hr1:02}" + ":00"

        else:
            new_format1 = f"{updated_hr1:02}" + match.group(2)

        if match.group(6) is None:
            new_format2 = f"{updated_hr2:02}" + ":00"

        else:
            new_format2 = f"{updated_hr2:02}" + match.group(6)

        updated_format = new_format1 + match.group(4) + new_format2

        print(match.groups())

        print(updated_format)

    else:
        raise ValueError

...


if __name__ == "__main__":
    main()
