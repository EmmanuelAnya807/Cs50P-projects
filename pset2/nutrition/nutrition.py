# Dictionary containing raw fruits and their corresponding calorie counts
calorie_content = {'apple': 130, 'avocado': 50, 'banana': 110,
                   'cantaloupe': 50, 'grapefruit': 60,
                   'grapes': 90, 'honeydew melon': 50,
                   'kiwifruit': 90, 'lemon': 15, 'lime': 20,
                   'nectarine': 60, 'orange': 80, 'peach': 60,
                   'pear': 100, 'pineapple': 50, 'plums': 70,
                   'strawberries': 50, 'sweet cherries': 100,
                   'tangerine': 50, 'watermelon': 80}


def main():
    fruit = input("Item: ")
    fruit_calories = nutrient(fruit, calorie_content)

    if fruit_calories is not None:
        print(fruit_calories)


def nutrient(fruit, calorie_content):

    # Convert the user's input to lowercase to ensure case insensitivity
    fruits = fruit.lower()

# Check if the fruit exists as a key in the dictionary
    if fruits in calorie_content:
        # Retrieve and return the specific calorie value
        return (calorie_content[fruits])


main()
