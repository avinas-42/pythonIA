from recipe import Recipe
import datetime

class book:
	def __init__(self, name):
		self.name = name
		now = datetime.datetime.now()
		self.last_update = now
		self.creation_date = now
		self.recipes_list = {}
		
	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name text{name} and returns the instance"""
		if name in self.recipes_list:
			print(self.recipes_list[name])
			return self.recipes_list[name]
		else:
			print('this recipe does not Exist')


	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		self.recipe
		pass
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		self.recipes_list[recipe.get_name()] = recipe
		self.last_update = datetime.datetime.now()

	def get_name(self):
		return self.name

	def get_last_update(self):
		return self.last_update

	def get_creation_date(self):
		return self.creation_date

	def get_recipes_list(self):
		return self.recipes_list

	def __str__():
 		return "name: " + name + " , " + "last_update: " + last_update + " , " + "creation_date: " + creation_date + " , " + "recipes_list: " + recipes_list
