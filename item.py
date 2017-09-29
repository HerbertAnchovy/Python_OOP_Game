"""

Created by HerbertAnchovy in September 2017 as part of the 'Object-oriented Programming in Python'
FutureLearn course from the Raspberry Pi Foundation.
See https://www.futurelearn.com/courses/object-oriented-principles for details.

"""

class Item():
	"""A class to create an item"""

	# Constructor method used to create an Item object
	def __init__(self, item_name, item_description):
		"""Initialise an item object with name and description attributes"""
		self.name = item_name
		self.description = item_description
			
	# Getters for the name and description of the item:
		
	def get_name(self):
		"""Returns the name of the item"""
		return self.name

	def get_description(self):
		"""Returns the item description"""
		return self.description

	# Setters for the name and description of the item:

	def set_name(self, item_name):
		"""Sets the name of the item"""
		self.name = item_name

	def set_description(self, item_description):
		"""Sets the description of the item"""
		self.description = item_description

	# Output info on item
	def describe(self): 
		"""Describes the item"""
		print("In this room is " + self.description + "\n")
