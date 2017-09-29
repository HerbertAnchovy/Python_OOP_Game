"""

Created by HerbertAnchovy in September 2017 as part of the 'Object-oriented Programming in Python'
FutureLearn course from the Raspberry Pi Foundation.
See https://www.futurelearn.com/courses/object-oriented-principles for details

"""

class Room():
	"	""A class to create a room"""

	# Constructor method used to create a Room object
	def __init__(self, room_name):
		"""Initialise the room with name, description, linked_rooms dict and character attributes"""
		self.name = room_name
		self.description = None
		self.linked_rooms = {}
		self.character = None # What character, if any, is present in room

	def set_description(self, room_description):
		"""Set a description of the room"""
		self.description = room_description

	def get_description(self):
		"""Return a description of the room"""
		return self.description

	def set_name(self, new_name):
		"""Set room name"""
		self.name = new_name

	def get_name(self):
		"""Return room name"""
		return self.name

	def describe(self):
		"""Describe the room"""
		print(self.description)

    # This method takes three parameters: 
    # the object itself (which we can ignore when we use the method),
    # the room object to link to, and the relative direction of this object.
	def link_room(self, room_to_link, direction):
		"""Link this room to another one by direction"""
		self.linked_rooms[direction] = room_to_link # 'direction' holds key for dict self.linked_rooms 
													# values
		# print(">>" + self.name + " linked rooms :" + repr(self.linked_rooms)) # Info on dict self.linked_rooms 

    # This method loops through the dictionary self.linked_rooms and,
    # for every defined direction, prints out that direction and the
    # name of the room in that direction.
	def get_details(self):
		"""Print details of this room"""	
		print("\n" + self.name + ": " + self. get_description())
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			print( "The " + room.get_name() + " is " + direction)

    # move() method below takes a parameter for the direction in which the player would like to move. 
    # If this direction is one of the directions linked to, the method returns the room object that is in that direction.
    # If there is no room in the dictionary in that direction, the method returns self – i.e. the player is linked back
    # to the room they were already in!
	def move(self, direction):
		"""Move, if direction is valid, from this room to another"""
		if direction in self.linked_rooms:
			return(self.linked_rooms[direction])
		else:
			return(self)
        
    # the getter for a character within a room:
	def get_character(self):
		"""Return the character in the room or None"""
		return self.character
		
    # the setter for putting a character within a room:
	def set_character(self, character):
		"""Set character in the room"""
		self.character = character

    # the getter for an item within a room:
	def get_item(self):
		"""Return the item in this room or None"""
		return self.item

    # the setter for putting an item into a room:
	def set_item(self, item):
		"""Set the item in this room"""
		self.item = item
