from inflect import engine
p = engine()


def main():
    name_list = []

    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break

    print()
    print(f"Adieu, adieu, to {p.join(name_list)}")


main()
