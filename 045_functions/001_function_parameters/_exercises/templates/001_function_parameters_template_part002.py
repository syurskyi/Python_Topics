# ######################################################################################################################
# Positional Arguments

# ___ my_func a b c
#     print "a_|0|_ b_|1|_ c_|2|".f_ a b c
#
# print()
# ######################################################################################################################
# Default Values

# Note that once a parameter is assigned a default value, all parameters thereafter must be asigned a default value too!

# ___ my_func a b_2 c_3
#     print "a_|0}_ b_|1}_ c_|2|".f_ a b c
#
# my_func(10, 20, 30)
# my_func(10, 20)
# my_func(10)

# Since a does not have a default value, it must be specified:

# print()
# ######################################################################################################################
# Keyword Arguments (named arguments)

# ___ my_func a b_2 c_3
#     print "a_|0|_ b_|1}_ c_|2|".f_ a b c
#
# my_func c_30 b_20 a_10
# my_func 10 c_30 b_20

# Note that once a keyword argument has been used, all arguments thereafter must also be named:
#
# However, if a parameter has a default value, it can be omitted from the argument list, named or not:

# my_func 10 c_30
# my_func a_30 c_10
# my_func c_10, a_30
#
# print()
# ######################################################################################################################
#  arbitrary numbers of positional parameters/arguments:
#
# ___ func1 a b _args
#     print a
#     print b
#     print args
#
# func1 1 2 'a' 'b'

# A few things to note:
# Unlike iterable unpacking, *args will be a tuple, not a list.
# The name of the parameter args can be anything you prefer
# You cannot specify positional arguments after the *args parameter - this does something different that we'll cover in the next lecture.

# print()
# ######################################################################################################################
# how we might use this to calculate the average of an arbitrary number of parameters.

# ___ avg _args
#     count _ len_ args
#     total _ s_ args
#     r_ t_/c_
#
# avg 2 2 4 4
#
# avg() # error
#
# ___ avg _args
#     count _ l_ args
#     total _ s_ args
#     __ count __ 0
#         r_ 0
#     ___:
#         r_ t_/c_
#
# avg 2 2 4 4
# avg()

# But we may not want to allow specifying zero arguments, in which case we can split our parameters into a required (non-defaulted) positional argument, and the rest:

# ___ avg a _args
#     count _ l_(args) + 1
#     total _ a + s_ args
#     r_ t_/c_
#
# avg 2 2 4 4
# avg()
#
# print()
# ######################################################################################################################
# Unpacking an iterable into positional arguments

# ___ func1 a b c
#     print a
#     print b
#     print c
#
# l = [10, 20, 30]
#
# # The function expects three positional arguments, but we only supplied a single one (albeit a list).
# # But we could unpack the list, and then pass it to as the function arguments:
#
# func1 _l
#
# print()
# ######################################################################################################################
# To make the keyword argument optional, we just need to specify a default value in the function definition:

# ___ func1 _args d_'n/a'
#     print args
#     print d
#
# func1 1 2 3
# func1()
#
# print()
# ######################################################################################################################
# Sometimes we want only keyword arguments, in which case we still have to exhaust the positional arguments first -
# but we can use the following syntax if we do not want any positional parameters passed in:

# ___ func1 _, d_'hello'
#     print(d)
#
# func1 10  d_bye
# func1 d_ bye
#
# print()
# ######################################################################################################################
# We can also include positional non-defaulted (first), positional defaulted (after positional non-defaulted)
# followed lastly (after exhausting positional arguments) by keyword args (defaulted or non-defaulted in any order)

# ___ func1 a b_20 _args d_0 e_'n/a'
#     print a b args d e
#
# func1 5 4 3 2 1 d_0 e_ all engines running
# func1 0 600 d_ goooood morning e_ python!
# func1 11 'm/s' 24 mph d_ unladen e_ swallow
#
# print()
# ######################################################################################################################
# **kwargs

# ___ func __kwargs
#     print kwargs
#
# func x_100 y_200
#
# print()
# # ######################################################################################################################
# *args **kwargs

# ___ func _args __kwargs
#     print args
#     print kwargs
#
# func 1 2 a_100 b_200
#
# print()
# ######################################################################################################################
# If you want to specify both specific keyword-only arguments and **kwargs you will need to first get to a point
# where you can define a keyword-only argument (i.e. exhaust the positional arguments, using either *args or just *)

# ___ func _ d __kwargs
#     print d
#     print kwargs
#
# func d_1 x_100 y_200
#
# print()
# ######################################################################################################################
# Positionals Only: no extra positionals, no defaults (all positionals required)

# ___ func a b
#     print a b
#
# func hello _ world
# func b_ world _ a_ hello
#
# print()
# ######################################################################################################################
# Positionals Only: no extra positionals, defaults (some positionals optional)

# ___ func a b_ world  c_10
#     print a b c
#
# func hello
# func hello c='!'
#
# print()
# ######################################################################################################################
# Positionals Only: extra positionals, no defaults (all positionals required)

# ___ func a b _args
#     print a b args
#
# func 1 2 'x' 'y' 'z'
#
# print()
# ######################################################################################################################
# Keywords Only: no positionals, no defaults (all keyword args required)
#
# ___ func _ a b
#     print a b
#
# func a_1 b_2
#
# print()
# ######################################################################################################################
# Keywords Only: no positionals, some defaults (not all keyword args required)

# ___ func _ a_1 b
#     print a b
#
# func a_10 b_20
# func b_2
#
# print()
# ######################################################################################################################
# Keywords and Positionals: some positionals (no defaults), keywords (no defaults)

# ___ func a b _ c d
#     print a b c d
#
# func 1 2 c_3 d_4
# func 1 2 d_4 c_3
# func 1 c_3 d_4 b_2
#
# print()
# ######################################################################################################################
# Keywords and Positionals: some positional defaults

# ___ func a b_2 _, c d_4
#     print a b c d
#
# func 1 c_3
# func c_3 a_1
# func 1 2 c_3 d_4
# func c_3 a_1 b_2 d_4
#
# print()
# ######################################################################################################################
# Keywords and Positionals: extra positionals

# ___ func a b=2 _args c_3 d
#     print a b args c d
#
# func 1 2 'x' 'y' 'z' c_3, d_4
#
# # Note that if we are going to use the extra arguments, then we cannot actually use a default value for b:
#
# func 1 'x' 'y' 'z' c_3 d_4
#
# print()
# ######################################################################################################################
# Keywords and Positionals: no extra positionals, extra keywords
#
# ___ func a b _, c d_4 __kwargs
#     print a b c d kwargs
#
# func 1 2 c_3 x_100 y_200 z=300
# func x_100 y_200 z_300 c_3 b_2 a_1
#
# print()
# ######################################################################################################################
# Keywords and Positionals: extra positionals, extra keywords

# ___ func a b _args c d_4 __kwargs
#     print a b args c d kwargs
#
# func 1 2 'x' 'y' 'z' c_3, d_5 x_100_ y_200 z_300
#
# print()
# ######################################################################################################################
# Keywords and Positionals: only extra positionals and extra keywords

# ___ func _args __kwargs
#     print args kwargs
#
# func 1 2 3 x_100 y_200 z_300
#
# print()
# ######################################################################################################################
# Another Use Case
# log_to_console

# ___ calc_hi_lo_avg _args log_to_console_F_
#     hi _ i_ b_ a_ ___ m_a_
#     lo _ i_ b_ a_ a_ m_ args
#     avg _ (hi + lo)/2
#     __ log_to_console
#         print high_|0| low_|1| avg_|2|".f_ hi lo avg
#     r_ avg
#
# avg _ calc_hi_lo_avg 1 2 3 4 5
# print avg
#
# avg _ calc_hi_lo_avg 1 2 3 4 5 log_to_console_T_
# print avg
#
# print()
# ######################################################################################################################
# A Simple Function Timer

# i_ t_
#
# ___ time_it fn _args rep_5 __kwargs
#     start _ t.p__c_
#     ___ i __ r_ rep
#         fn _args __kwargs
#     end _ t__.p__c__()
#     r_ (end - start) / rep
#
# ___ compute_powers_1 n _, start_1 end
#     # using a for loop
#     results = __
#     ___ i __ r_ start end
#         r_.a_ n**i
#     r_ results
#
# ___ compute_powers_2 n _ start_1, end
#     # using a list comprehension
#     r_ |n**i ___ i __ r_ start end
#
# ___ compute_powers_3 n _ start_1 end
#     # using a generator expression
#     r_ |n**i ___ i __ r_ start end
#
# compute_powers_1 2 end_5
# compute_powers_2 2 end_5
# l_(compute_powers_3 2 e_-5
#
# time_it compute_powers_1 n_2 end_20000 rep_4
# time_it compute_powers_2 2 end_20000 rep_4
# time_it compute_powers_3 2 end_20000 rep_4
#
# print()
# ######################################################################################################################
# We can define such help using docstrings

# ___ my_func a b
#     'Returns the product of a and b'
#     r_ a*b
#
# help my_func
#
# print()
# ######################################################################################################################
# Docstrings can span multiple lines using a multi-line string literal:

# ___ fact n
#     '''Calculates n! (factorial function)
#     Inputs:
#         n: non-negative integer
#     Returns:
#         the factorial of n
#     '''
#
#     __ n < 0
#         '''Note that this is not part of the docstring!'''
#         r_ 1
#     ____
#         r_ n * fact(n - 1)
#
# help fact
#
# # Docstrings, when found, are simply attached to the function in the __doc__ property:
#
#
# fact.__d_
#
# print()
# # ######################################################################################################################
# Annotations

# ___ my_func a: 'annotation for a'
#             b: 'annotation for b') __ 'annotation for return':
#     r_ a * b
#
# help my_func
#
# print()
# ######################################################################################################################
# The annotations can be any expression, not just strings:

# x = 3
# y = 5
# ___ my_func a| s_ __ 'a repeated ' + s_(m_(3, 5)) + ' times':
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
# ___ my_func a| s_ __ 'a repeated ' + s_(m_(3, 5)) + ' times':
# 	r_ a*max x y
#
# my_func.__a_
#
# print()
# ######################################################################################################################
# Annotations will work with default parameters too: just specify the default after the annotation

# ___ my_func a|str_'a' b|int_1)__s_
#     r_ a*b
#
# help my_func
# my_func()
# my_func abc 3
#
# ___ my_func a|i_-0 _args|additional args
#     print a args
#
# my_func.__a_
#
# help my_func
#
# print()

# ######################################################################################################################
# Suppose we want to find the maximum value in a list:
#
# First we define a function that returns the maximum of two arguments:

# l = [5, 8, 6, 10, 9]
#
# _max = l_ a_ b| a __ a > b e_ b
#
# ___ max_sequence sequence
#     result _ sequence[0]
#     ___ x __ sequence[1:]:
#         result = _max(result, x)
#     r_ result
#
# max_sequence l
#
# print()
# ######################################################################################################################
# To calculate the minimum, all we need to do is to change the function that is repeatedly applied
#
# l = [5, 8, 6, 10, 9]
#
# _min = l_ a_ b| a __ a < b e_ b
#
# ___ min_sequence sequence
#     result _ sequence|0|
#     ___ x __ sequence|1_|
#         result _ _m_ re__ x
#     r_ result
#
# print l
# print min_sequence l
#
# print()