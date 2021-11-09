from recipe import Recipe

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
    one = input_a_recipe()
    print(one)

if __name__ == "__main__":
    main()