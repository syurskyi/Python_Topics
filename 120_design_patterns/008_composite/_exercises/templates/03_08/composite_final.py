# c_ Component o..
# 	"""Abstract class"""
#
# 	___  -  $  $$
# 		pass
#
# 	___ component_function(
# 		pass
#
# c_ Child C.. #Inherits from the abstract class, Component
# 	"""Concrete class"""
#
# 	___  -  $  $$
# 		C___. -  $  $$
#
# 		#This is where we store the name of your child item!
# 		name _ ar.. 0
#
# 	___ component_function
# 		#Print the name of your child item here!
# 		print("@".f... n..
#
# c_ Composite C___ #Inherits from the abstract class, Component
# 	"""Concrete class and maintains the tree recursive structure"""
#
# 	___  -  $  $$
# 		C___. -  $ $$
#
# 		#This is where we store the name of the composite object
# 		self.name _ ar.. 0
#
# 		#This is where we keep our child items
# 		self.children _    # list
#
# 	___ append_child child
# 		"""Method to add a new child item"""
# 		c___.ap... ?
#
# 	___ remove_child child
# 		"""Method to remove a child item"""
# 		c___.r.. ?
#
# 	___ component_function
#
# 		#Print the name of the composite object
# 		print("@".f.. n..
#
# 		#Iterate through the child objects and invoke their component function printing their names
# 		___ i __ c___
# 			?.c_f..
#
# #Build a composite submenu 1
# sub1 _ C.. "submenu1"
#
# #Create a new child sub_submenu 11
# sub11 _ Ch.. "sub_submenu 11"
# #Create a new Child sub_submenu 12
# sub12 _ Ch.. "sub_submenu 12"
#
# #Add the sub_submenu 11 to submenu 1
# sub1.a_c.. sub11
# #Add the sub_submenu 12 to submenu 1
# sub1.a_c.. sub12
#
# #Build a top-level composite menu
# top _ C.. "top_menu"
#
# #Build a submenu 2 that is not a composite
# sub2 _ Ch.. "submenu2"
#
# #Add the composite submenu 1 to the top-level composite menu
# top.a_c.. sub1
#
# #Add the plain submenu 2 to the top-level composite menu
# top.a_c..sub2
#
# #Let's test if our Composite pattern works!
# top.c_f_
#
