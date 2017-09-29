"""

Created by HerbertAnchovy in September 2017 as part of the 'Object-oriented Programming in Python'
FutureLearn course from the Raspberry Pi Foundation.
See https://www.futurelearn.com/courses/object-oriented-principles for details.

"""

class Character():
	"""A class to create a character"""
	
    # Constructor method used to create a Character object
	def __init__(self, char_name, char_description):
		"""Initialise a character with a name and description"""
		self.name = char_name
		self.description = char_description
		self.conversation = None
		
	# Describe the character
	def describe(self):
		"""Describe this character"""
		print(self.name + " is here!")
		print(self.name + " " + self.description)
		
    # Set what the character will say when talked to
	def set_conversation(self, conversation):
		"""Returns what the character says"""
		self.conversation = conversation
		
    # Talk to this character
	def talk(self):
		"""Talk to the character"""
		if self.conversation is not None:
			print("[" + self.name + " says]: " + self.conversation)
		else:
			print(self.name + " doesn't want to talk to you")

    # Fight with this character
	def fight(self, combat_item):
		"""Fight with the character"""
		print(self.name + " doesn't want to fight with you")
		return True

class Enemy(Character):
	"""A class to create an enemy as a superclass of Character"""  

	# Class variables, shared between all objects of the Enemy class
	defeated = 0
	remaining = 0

	def __init__(self, char_name, char_description):
		"""Initialise an enemy with a name and description as a superclass of Character"""
		super().__init__(char_name, char_description)
		self.weakness = None
		self.__class__.remaining+=1 # Count total enemies as their objects are created.
		
    # The setter for the weakness of an enemy
	def set_weakness(self, enemy_weakness):
		"""Set a weakness for this character"""
		self.weakness = enemy_weakness

    # The getter for the weakness of an enemy
	def get_weakness(self):
		"""Return this character's weakness"""
		return self.weakness

	def fight(self, combat_item):
		"""Fight with this character. Returns True if the player has won, False otherwise"""
		if combat_item == self.weakness:
			print("You defeat " + self.name + " with the " + combat_item + "!")
			return True
		else:
			print("The " + combat_item + " has little affect on " + self.name + ".")
			print(self.name + " retaliates, squishing you with relative ease.")
			return False

	def defeat(self):
		"""When an enemy defeat occurs, update enemy defeated and enemy remaining class variables"""
		# Increment defeated class variable
		Enemy.defeated += 1
		# Decrement remaining class variable
		Enemy.remaining -= 1

	def get_defeated(self):
		"""Returns number of enemies defeated"""
		return Enemy.defeated

	def get_status(self):
		"""Display number of enemies defeated and enemies remaining"""
		if Enemy.defeated == 1:
			print(str(Enemy.defeated) + " enemy defeated, ", end="")
		else:
			print(str(Enemy.defeated) + " enemies defeated, ", end="")
        
		if Enemy.remaining == 1:
			print(str(Enemy.remaining) + " enemy remains.") # total enemies in game
		else:
			print(str(Enemy.remaining) + " enemies remain.")

class Friend(Character):
	"""A class to create a friend as a superclass of Character"""

	def __init__(self, char_name, char_description):
		"""Initialise a friend with a name and description as a super class of Character"""
		super().__init__(char_name, char_description)
		self.emotion = None

    # The setter for the emotion of a friend 
	def set_emotion(self, friend_emotion):
		"""The setter for the emotion of a friend - Unused"""
		self.emotion = friend_emotion

    # The getter for the emotions of a friend
	def get_emotion(self):
		"""The getter for the emotion of a friend - Unused"""
		return self.emotion

	def hug(self):
		"""Display confirmation of hug event!"""
		print("You hug " + self.name + ". " + self.name + " reciprocates.")
		return False

  