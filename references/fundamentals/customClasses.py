'''Custom classes'''

# class declaration Syntax:
class  Things():
	pass
class  Animate(Things):
	pass

class  Animal(Animate):
	def __init__ (self, spots):		# __init__  function notice the two underscore characters on each side - This is a special type of function in Python classes and must use this name - the init function is a way to set the properties for an object when the object is first created, and Python will automatically call this function when we create a new object - also needs to have (self) as the first parameter.
		self.hasSpots = spots
	# class functions
	def  breathe(self):
		pass
	def  move(self):
		return 'I moved'
	def  eat_food(self):
		print("I ate")

# Creating a new instance of the object
kuei = Animal(True)
# Retrieve a property of the object
print(kuei.hasSpots)
# Using object functions
kuei.eat_food()
kuei.move()

# why use classes and objects at all, when you could just write normal functions?

# Using objects and classes, we can tell Python exactly which giraffe we’re talking about when we want to run the move  function.

"""
Using  named  Parameters

Sometimes functions have a lot of parameters, and we may not always need
to provide a value for every parameter. Named parameters are a way we can
provide values for only the parameters that we need to give values.
"""
def person(width, height):
    print('I am %s feet wide, %s feet high' % (width, height))
# prints person(4, 3) I am 4 feet wide, 3 feet high
