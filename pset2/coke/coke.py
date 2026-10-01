def main():
	amount_due = 50

    # Loop continuously as long as the user still owes money
	while amount_due > 0:

        # Display the current balance to the user
		print("Amount Due: {}".format(amount_due))

        # Accept coin input from the user (returns a string)
		paid = input("Insert Coin: ")

        # Call the helper function to process the coin and update the remaining balance
		amount_due = coke_amount(amount_due, paid)

    # Once amount_due hits 0 or drops below (overpaid), calculate and issue change
	if amount_due <= 0:

        # Use abs() to convert a negative balance into a positive change amount
		change = abs(amount_due)
		print("Change owed: {}".format(change))


def coke_amount(amount_due, paid):
    # Safety Check: Only convert to an integer if the string contains only digits
	if paid.isdigit():
		paid = int(paid)

    # Valid Coin Check: Only accept nickels (5), dimes (10), or quarters (25)
	if paid == 5 or paid == 10 or paid == 25:

        # Subtract the valid coin's value from the current balance
		amount_due = amount_due - paid

	return amount_due

main()
