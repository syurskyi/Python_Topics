# c_ Subject o..       #Represents what is being 'observed'
#
# 	___ -
# 		_observers    # list # This where references to all the observers are being kept
# 							 # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers
#
# 	___ attach  observer
# 		__ ? no. __ _o... #If the observer is not already in the observers list
# 			_o___s.a.. ? # append the observer to the list
#
# 	___ detach  observer #Simply remove the observer
# 		___
# 			_o___.re.. ?
# 		______ V...
# 			p..
#
# 	___ notify modifier_N..
# 		___ o.. __ _o... # For all the observers in the list
# 			__ m... !_ o... # Don't notify the observer who is actually updating the temperature
# 				o___.up..  # Alert the observers!
#
# c_ Core S.. #Inherits from the Subject class
#
# 	___ -  name_""
# 		S__. -
# 		_n..  ? #Set the name of the core
# 		_temp _ 0 #Initialize the temperature of the core
#
# 	?? #Getter that gets the core temperature
# 	___ temp
# 		r_ _temp
#
# 	??.? #Setter that sets the core temperature
# 	___ temp  temp
# 		_?  ?
# 		no.. #Notify the observers whenever somebody changes the core temperature
#
# c_ TempViewer
#
# 	___ update subject #Alert method that is invoked when the notify() method in a concrete subject is invoked
# 		print("Temperature Viewer: @ has Temperature @".f__ s__._n.. s__._t..
#
# #Let's create our subjects
# c1 = C__("Core 1")
# c2 = C__("Core 2")
#
# #Let's create our observers
# v1 = T..
# v2 = T..
#
# #Let's attach our observers to the first core
# _1.a.. v1
# _1.a.. v2
#
# #Let's change the temperature of our first core
# c1.temp = 80
# c1.temp = 90
#
