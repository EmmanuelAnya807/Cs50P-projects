def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """Converts a string in the format $##.## to a float representing the amount in dollars"""
    for i in range(len(d)):
        if d[i] == "$":
            return float(d[i + 1:])


def percent_to_float(p):
    """Converts a string in the format ##% to a float representing the percentage as a decimal"""
    for i in range(len(p)):
        if p[i] == "%":
            return float(p[:i]) / 100
    return float(p)


main()
