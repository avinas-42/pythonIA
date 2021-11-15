from recipe import Recipe
from book import Book


def checkInt(text):
    try:
        int(text)
        return True
    except ValueError:
        return False


def get_int():
    choice = input(">>")
    if checkInt(choice):
        return int(choice)
    else:
        return -1


def fill_book(book):
    sandwich = Recipe("sandwich", 4, 5,
                      ["pain", "beur", "cornichon"],
                      "un sandwich quoi...", "lunch")
    sandwich2 = Recipe("sandwich2", 2, 4,
                       ["pain", "beur", "cornichon"],
                       "un sandwich quoi...", "lunch")
    sandwich3 = Recipe("sandwich3", 3, 1,
                       ["pain", "beur"],
                       "un sandwich quoi...", "dessert")
    book.add_recipe(sandwich)
    book.add_recipe(sandwich2)
    book.add_recipe(sandwich3)


def input_a_recipe():
    recipe = input('name of your recipe >> ')
    ingredients = []
    ingre = ''
    time = -1
    cooking_lvl = -1
    while cooking_lvl < 0:
        print('enter cooking level')
        cooking_lvl = get_int()
        if cooking_lvl < 0:
            print('wrong input')
    ingre = input('add one ingredient : ')
    while ingre != 'STOP':
        ingredients.append(ingre)
        print('write : "STOP" to stop adding ingredients')
        ingre = input('add one ingredient : ')
    meal = input('enter your type of meal >> ')
    description = input('enter your description >> ')
    while time < 0:
        print('enter your preparation time')
        time = get_int()
        if time < 0:
            print('wrong input')

    return Recipe(recipe, cooking_lvl, time, ingredients, description, meal)


def main():
    book = Book("cookbook")
    fill_book(book)
    recipes_list = book.get_recipes_by_types("lunch")
    for recipe in recipes_list:
        print(recipe)
    recipe = book.get_recipe_by_name("sandwich3")
    book.add_recipe(input_a_recipe())
    print(book)


if __name__ == "__main__":
    main()
