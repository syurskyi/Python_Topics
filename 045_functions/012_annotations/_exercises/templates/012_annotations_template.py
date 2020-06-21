# # ######################################################################################################################
# Annotations

# ___ my_func a 'annotation for a'
#             b 'annotation for b'  'annotation for return'
#     r_ a * b
#
# help my_func
#
# print()
# ######################################################################################################################
# The annotations can be any expression, not just strings:

# x = 3
# y = 5
# ___ my_func a s_ __ 'a repeated ' + s_(m_(3, 5)) + ' times'
# 	r_ a*max x y
#
# help my_func
#
# print()
# ######################################################################################################################
# Just like docstrings are stored in the __doc__ property, annotations are stored in the __annotations__ property -
# a dictionary whose keys are the parameter names, and values are the annotation.

# x = 3
# y = 5
# ___ my_func a s_ __ 'a repeated ' + s_(m_(3, 5)) + ' times'
# 	r_ a*max x y
#
# my_func. -a
#
# print()
# ######################################################################################################################
# Annotations will work with default parameters too: just specify the default after the annotation

# ___ my_func a st._'a' b in._1 __ s_
#     r_ a*b
#
# help my_func
# ?
# ? abc 3
#
# ___ my_func a i_-0 $ 'additional args'
#     print a args
#
# ?. -a
#
# help my_func
#
# print()
