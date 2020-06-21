# c_ Korean
# 	"""Korean speaker"""
# 	___  -
# 		name _ "Korean"
#
# 	___ speak_korean
# 		r_ "An-neyong?"
#
# c_ British
# 	"""English speaker"""
# 	___  -
# 		name _ "British"
#
# 	#Note the different method name here!
# 	___ speak_english
# 		r_ "Hello!"
#
# c_ Adapter
# 	"""This changes the generic method name to individualized method names"""
#
# 	___  -  object $$adapted_method
# 		"""Change the name of the method"""
# 		_?  ?
#
# 		#Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
# 		#For example, speak() will be translated to speak_korean() if the mapping says so
# 		. - .update a...
#
# 	___ -g attr
# 		"""Simply r_ the rest of attributes!"""
# 		r_ ge.. _o.. ?
#
# #List to store speaker objects
# objects _     # list
#
# #Create a Korean object
# korean _ K..
#
# #Create a British object
# british _ B...
#
# #Append the objects to the objects list
# o___.ap..  A.. k.. s_k_.s_k..
# o___.ap..  A.. b.. s_b_.s_e..
#
#
# ___ obj in o___
# 	print("@ says '@'\n".f.. ?.n.. ?.s..
#
