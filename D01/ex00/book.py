from recipe import Recipe
import datetime


class Book:
    def __init__(self, name):
        self.name = name
        now = datetime.datetime.now()
        self.last_update = now
        self.creation_date = now
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name text{name} and returns the instance"""
        for recipe in self.recipes_list["starter"]:
            if recipe.name == name:
                print(recipe)
                return recipe
        for recipe in self.recipes_list["dessert"]:
            if recipe.name == name:
                print(recipe)
                return recipe
        for recipe in self.recipes_list["lunch"]:
            if recipe.name == name:
                print(recipe)
                return recipe
        print('this recipe does not Exist')

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list:
            return self.recipes_list[recipe_type]
        print("wrong recipe type")
        quit()

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("not a valide recipe")
            quit()
        meal = recipe.get_recipe_type()
        self.recipes_list[meal].append(recipe)
        self.last_update = datetime.datetime.now()

    def get_name(self):
        return self.name

    def get_last_update(self):
        return self.last_update

    def get_creation_date(self):
        return self.creation_date

    def get_recipes_list(self):
        return self.recipes_list

    def __str__(self):
        ret = "name: " + self.name + " , " + "last_update: " + \
            str(self.last_update) + " , " + "creation_date: " + \
            str(self.creation_date) + " , " + "recipes_list:\n"
        for meal_type in self.recipes_list:
            for recipe in self.recipes_list[meal_type]:
                ret += str(recipe)
        return ret
