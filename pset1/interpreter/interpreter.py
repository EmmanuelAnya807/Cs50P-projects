def main():
    """ Collects mathematical expression and calls interpret function"""

    math_exp = input("Expression: ")
    interpret(math_exp)


def interpret(math):
    """ Calculates and prints the result of the mathematical expression"""

    # Removes leading and trailing whitespace
    math = math.strip()

    # Extracts the numbers and operators from user input
    math = math.split()

    # Assigns every character in user input to a value
    a = float(math[0])
    b = float(math[-1])
    operator = math[1]

    # Calculates and prints the result of mathematical expression
    if operator == '+':
        print(a + b)

    elif operator == '-':
        print(a - b)

    elif operator == '*':
        print(a * b)

    elif operator == '/':
        if b != 0:
            print(a / b)

        else:
            print("A number can't be divided by zero")


main()
