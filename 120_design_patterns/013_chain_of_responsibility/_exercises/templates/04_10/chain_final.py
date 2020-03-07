# c_ Handler   # Abstract handler
# 	"""Abstract Handler"""
# 	___ - successor
# 		_?  ? # ___ine who is the next handler
#
# 	___ handle request
# 			handled = _h.. ? #If handled, stop here
#
# 			#Otherwise, keep going
# 			__ no. h..
# 				_s___.h.. ?
#
# 	___ _handle request
# 		r_ N...('Must provide implementation in subc_!')
#
# c_ ConcreteHandler1 Handler # Inherits from the abstract handler
# 	"""Concrete handler 1"""
# 	___ _handle request
# 		__ 0 < ? <_ 10 # Provide a condition for handling
# 			print("Request @ handled in handler 1".f.. ?
# 			r_ T.. # Indicates that the request has been handled
#
# c_ ___aultHandler H.. # Inherits from the abstract handler
# 	"""___ault handler"""
#
# 	___ _handle request
# 		"""If there is no handler available"""
# 		#No condition checking since this is a ___ault handler
# 		print("End of chain, no handler for {}".f.. ?
# 		r_ T.. # Indicates that the request has been handled
#
# c_ Client: # Using handlers
# 	___ -
# 		handler _ C_1 ___aH.. N..  # Create handlers and use them in a sequence you want
# 		                                                      # Note that the ___ault handler has no successor
#
# 	___ delegate ? requests # Send your requests one at a time for handlers to handle
# 		___ request __ ?
# 				h___.h.. ?
#
# # Create a client
# c = C..
#
# # Create requests
# requests = [2, 5, 30]
#
# # Send the requests
# ?.d.. ?
#
#
