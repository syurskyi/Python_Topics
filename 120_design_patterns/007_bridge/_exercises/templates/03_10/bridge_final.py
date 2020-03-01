# c_ DrawingAPIOne o..
# 	"""Implementation-specific abstraction: concrete class one"""
# 	___ draw_circle x y radius
# 		print("API 1 drawing a circle at (@, @ with radius @!)".f.. ?  ?  ?
#
#
# c_ DrawingAPITwo o...
# 	"""Implementation-specific abstraction: concrete class two"""
# 	___ draw_circle x y radius
# 		print("API 2 drawing a circle at (@, @ with radius @!)".f.. ?  ?  ?
#
# c_ Circle o..
# 	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""
#
# 	___ - x y radius drawing_api
# 		"""Initialize the necessary attributes"""
# 		_?  ?
# 		_?  ?
# 		_?  ?
# 		_?  ?
#
# 	___ draw
# 		"""Implementation-specific abstraction taken care of by another class: DrawingAPI"""
# 		_drawing_api.draw_circle _x _y, _r..
#
# 	___ scale percent
# 		"""Implementation-independent"""
# 		_r.. *_ ?
#
#
# #Build the first Circle object using API One
# circle1 = C___(1, 2, 3, D__O.
# #Draw a circle
# ?.d..
#
# #Build the second Circle object using API Two
# circle2 = C___(2, 3, 4, D__T
# #Draw a circle
# ?.d..
#
#
