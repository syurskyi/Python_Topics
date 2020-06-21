# c_ House o.. #The class being visited
# 	___ accept visitor
# 		"""Interface to accept a visitor"""
# 		?.v... ____ #Triggers the visiting operation!
#
# 	___ work_on_hvac  hvac_specialist):
# 		print ? "worked on by" ? #Note that we now have a reference to the HVAC specialist object in the house object!
#
# 	___ work_on_electricity  electrician
# 		print ? "worked on by" ?    #Note that we now have a reference to the electrician object in the house object!
#
# 	___ -s
# 		"""Simply return the class name when the House object is printed"""
# 		r_ se -c. -n
#
#
# c_ Visitor o..
# 	"""Abstract visitor"""
# 	___ -s
# 		"""Simply return the class name when the Visitor object is printed"""
# 		r_ self. -c. -n
#
#
# c_ HvacSpecialist V.. #Inherits from the parent class, Visitor
# 	"""Concrete visitor: HVAC specialist"""
# 	___ visit  house
# 		?.w_h.. ____ #Note that the visitor now has a reference to the house object
#
#
# c_ Electrician V.. #Inherits from the parent class, Visitor
# 	"""Concrete visitor: electrician"""
# 	___ visit  house
# 		?.w_e.. ____ #Note that the visitor now has a reference to the house object
#
# #Create an HVAC specialist
# hv = H...
# #Create an electrician
# e = E..
#
# #Create a house
# home = H..
#
# #Let the house accept the HVAC specialist and work on the house by invoking the visit() method
# ?.ac.. hv
#
# #Let the house accept the electrician and work on the house by invoking the visit() method
# ?.ac.. e
#
#
