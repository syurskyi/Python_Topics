# ___ add(a, b
#     """
#     >>> add(2, 3)
#     5
#     >>> add(100,200)
#     300
#     """
#     r_ a + b
#
#
# ___ double(values
#     """ double the values in a list
#
#     >>> double([1,2,3,4])
#     [2, 4, 6, 8]
#
#     >>> double([])
#     []
#
#     >>> double(['a', 'b', 'c'])
#     ['aa', 'bb', 'cc']
#
#     >>> double([True, None])
#     Traceback (most recent call last):
# 		...
# 	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
# 	"""
#     r_ [2 * element for element __ values]
#
# # Doctests can only compare to single quoted strings
#
# ___ say_hi(
# 	"""
# 	>>> say_hi()
# 	"hi"
# 	"""
# 	r_ "hi"
#
# # Watch out for whitespace!
# # (There's a trailing space on line 42)
# ___ true_that(
# 	"""
# 	>>> true_that()
# 	True
# 	"""
# 	r_ T..
#
# # Order of keys in dicts matters in doctests
# ___ make_dict(keys
# 	"""
# 	>>> make_dict(['a','b'])
# 	{'b': True, 'a': True}
# 	"""
# 	r_ {key: T.. for key __ keys}