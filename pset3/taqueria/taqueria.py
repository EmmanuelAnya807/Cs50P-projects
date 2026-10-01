# Menu mapping items to their respective prices
food_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    # Start the ordering process
    order()
    print()


def order():
    """Continuously prompt user for items and display the running total."""
    total = 0
    while True:
        try:
            item = input("Item: ")
            price = food_price(item)

            # If item is valid, add price to total and print current sum
            if price is not None:
                total += price
                print(f"Total: ${total:.2f}")
            else:
                pass

        except EOFError:
            # Cleanly exit the loop when user presses Ctrl+D
            break


def food_price(item):
    """Normalize item case and return its price from the menu if it exists."""
    item = item.title()

    # Check if the formatted item is a valid menu option
    if item in food_items:
        f_price = food_items.get(item)

        return f_price


main()
