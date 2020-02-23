# c_ Dog
# 	"""One of the objects to be returned"""
#
# 	___ speak
# 		r_ "Woof!"
#
# 	___ -s
# 		r_ "Dog"
#
#
# c_ DogFactory
# 	"""Concrete Factory"""
#
# 	___ get_pet
# 		"""Returns a Dog object"""
# 		r_ D..
#
# 	___ get_food
# 		"""Returns a Dog Food object"""
# 		r_ "Dog Food!"
#
#
# c_ PetStore
# 	""" PetStore houses our Abstract Factory """
#
# 	___ - pet_factory_N..
# 		""" pet_factory is our Abstract Factory """
#
# 		_?  ?
#
#
# 	___ show_pet
# 		""" Utility method to display the details of the objects retured by the DogFactory """
#
# 		pet = _p__.g..
# 		pet_food = ._p__.g_f_
#
# 		print("Our pet is '@'!".f.. ?
# 		print("Our pet says hello by '@'".f.. ?.s..
# 		print("Its food is '@'!".f.. ?
#
#
# #Create a Concrete Factory
# factory = D..
#
# #Create a pet store housing our Abstract Factory
# shop = P.. ?
#
# #Invoke the utility method to show the details of our pet
# ?.s..
# 
