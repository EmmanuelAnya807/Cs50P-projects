def main():
    # Execute the grocery tracking program
    grocery_input()


def grocery_input():
    """Collect grocery inputs from the user and print the sorted frequency count."""
    grocery_dict = {}

    while True:
        try:
            grocery = input("")
            # Update the count for the entered item
            grocery_list(grocery, grocery_dict)

        except EOFError:
            # End input collection on Ctrl+D
            break

    print()
    # Iterate through items alphabetically and print their counts
    for key in sorted(grocery_dict):
        value = grocery_dict.get(key)
        print(f"{value} {key.upper()}")


def grocery_list(grocery, grocery_dict):
    """Increment item count if it exists, otherwise initialize it at 1."""
    if grocery in grocery_dict:
        grocery_dict[grocery] += 1

    else:
        grocery_dict[grocery] = 1

    return grocery_dict


main()
