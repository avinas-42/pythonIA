

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        bQuit = False
        if not isinstance(name, str) or \
                not isinstance(cooking_lvl, int) or \
                not isinstance(cooking_time, int) or \
                not isinstance(ingredients, list) or \
                not isinstance(description, str) or \
                not isinstance(recipe_type, str):
            print("wrong type ERROR")
            quit()

        if not 1 < cooking_lvl < 5:
            print("ERROR: cooking level range 1 to 5")
            bQuit = True
        if cooking_time < 0:
            print("ERROR: cooking time can't be negative")
            bQuit = True
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print('ERROR: recipe type can be : "starter",\
"lunch" or "dessert".')
            bQuit = True
        if bQuit:
            quit()

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def get_name(self):
        return self.name

    def get_cooking_lvl(self):
        return self.cooking_lvl

    def get_cooking_time(self):
        return self.cooking_time

    def get_ingredients(self):
        return self.ingredients

    def get_description(self):
        return self.description

    def get_recipe_type(self):
        return self.recipe_type

    def __str__(self):
        return '----------------------------------------\n' + \
            'recipe for ' + self.name + ':' +\
            '\nCooking level : ' + str(self.cooking_lvl) + \
            '\nIngredients list : ' + str(self.ingredients) + \
            '\nTakes ' + str(self.cooking_time) + ' minutes of cooking.' + \
            '\nDescription : ' + self.description + \
            '\nTo be eaten for ' + self.recipe_type + '\n'
