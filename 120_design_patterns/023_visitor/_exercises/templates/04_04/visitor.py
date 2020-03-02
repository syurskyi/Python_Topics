# c_ House o.. #The class being visited
# 	___ accept visitor
# 		"""Interface to accept a visitor"""
# 		#Triggers the visiting operation!
#
# 	___ work_on_hvac  hvac_specialist
# 		print _____ "worked on by" ? #Note that we now have a reference to the HVAC specialist object in the house object!
#
# 	___ work_on_electricity  electrician
# 		#Note that we now have a reference to the electrician object in the house object!
#
# 	___ -s
# 		"""Simply r_ the class name when the House object is printed"""
# 		r_  -c. n
#
#
# c_ Visitor o..
# 	"""Abstract visitor"""
# 	___ -s
# 		"""Simply r_ the class name when the Visitor object is printed"""
# 		r_  -c. n
#
#
# c_ HvacSpecialist V.. #Inherits from the parent class, Visitor
# 	"""Concrete visitor: HVAC specialist"""
# 	___ visit  house
# 		h___.w_h.. ____ #Note that the visitor now has a reference to the house object
#
#
# c_ Electrician V.. #Inherits from the parent class, Visitor
# 	"""Concrete visitor: electrician"""
# 	___ visit house
# 		#Note that the visitor now has a reference to the house object
#
# #Create an HVAC specialist
#
# #Create an electrician
#
#
# #Create a house
#
#
# #Let the house accept the HVAC specialist and work on the house by invoking the visit() method
#
#
# #Let the house accept the electrician and work on the house by invoking the visit() method
#
#
#
