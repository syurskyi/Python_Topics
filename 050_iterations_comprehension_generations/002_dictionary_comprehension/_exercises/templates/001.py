# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# # Put all keys of `dict1` in a list and returns the list
# print ?.k..
# # dict_keys(['c', 'd', 'a', 'b'])
#
# # Put all values saved in `dict1` in a list and returns the list
# print(dict1.v..
#
# ?.i..
# # dict_items([('c', 3), ('d', 4), ('a', 1), ('b', 2)])
#
# # dict_variable = {key:value for (key,value) in dictonary.items()}
#
# dict1_keys = k*2| v ___ ? ? __ ?.i..
# print ?
#
# # Why Use Dictionary Comprehension?
# #
# # Dictionary comprehension is a powerful concept and can be used to substitute for loops and lambda functions.
# # However, not all for loop can be written as a dictionary comprehension but all dictionary comprehension
# # can be written with a for loop.
#
# numbers = ra.. 10
# new_dict_for  # dict
#
# # Add values to `new_dict` using for loop
# ___ n __ numbers
#     __ ?%2__0
#         ? ? _ ?**2
#
# print ?
#
# # {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}
#
# # Use dictionary comprehension
# new_dict_comp = n ?**2 ___ ? __ n.. __ ?%2 __ 0
#
# print ?
#
# # {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}
#
# # Alternative to for loops
# #
# # For loops are used to repeat a certain operation or a block of instructions in a program for a given number of times.
# # However, nested for loops (for loop inside another for loop) can get confusing and complex.
# # Dictionary comprehensions are better in such situations and can simplify the readability and your understanding
# # of the code.
#
# # Alternative to lambda functions
# #
# # Lambda functions are a way of creating small anonymous functions. They are functions without a name.
# # These functions are throw-away functions, which are only needed where they have been created.
# # Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
# #
# # Let's look at the lambda function along with the map() function:
#
# # Initialize `fahrenheit` dictionary
# fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
#
# #Get the corresponding `celsius` values
# celsius = l.. m.. l____ x fl__(5)/9)*(?-32) ?.v..
#
# #Create the `celsius` dictionary
# celsius_dict = di__ z__ ?.k.. ?
#
# print ?
# # {'t2': -28.88888888888889, 't3': -23.333333333333336, 't1': -34.44444444444444, 't4': -17.77777777777778}
#
# ########################################################################################################################
# # Initialize the `fahrenheit` dictionary
# fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
#
# # Get the corresponding `celsius` values and create the new dictionary
# celsius = k fl__(5)/9)*(v-32) ___ ? ? __ ?.i..
#
# print ?
#
# # {'t2': -28.88888888888889, 't3': -23.333333333333336, 't1': -34.44444444444444, 't4': -17.77777777777778}
#
# # Adding Conditionals to Dictionary Comprehension
#
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# # Check for items greater than 2
# dict1_cond =  k v ___ ? ? __ ?.i.. __ ?>2
#
# print ?
# # {'e': 5, 'c': 3, 'd': 4}
#
# # Multiple If Conditions
#
# dict1_doubleCond = k v ___ ? ? __ ?.i.. __ ?>2 __ ?%2 __ 0
# print ?
# # {'d': 4}
#
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
# dict1_tripleCond = k v ___ ? ? __ ?.i.. __ ?>2 __ ?%2 __ 0 __ ?%3 __ 0
# print ?
# # {'f': 6}
#
# # In a for loop, this will correspond to:
#
# dict1_tripleCond   # dict
#
# ___ k v __ ?.i..
#     __  ?>_2 a.. ?%2 __ 0 a.. ?%3 __ 0
#             ? ? _ ?
#
# print ?
# # {'f': 6}
#
# # If-Else Conditions
#
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
#
# # Identify odd and even entries
# dict1_tripleCond = k *even __ ?%2__0 ____ *odd ___ ? ? __ ?.i..
#
# print ?
# # {'f': 'even', 'c': 'odd', 'b': 'even', 'd': 'even', 'e': 'odd', 'a': 'odd'}
#
# # Nested Dictionary Comprehension
# nested_dict = *first *a 1 *second *b 2
# float_dict = outer_k fl__ inner_v ___ (inner_k, inner_v) __ outer_v.i..} ___ (outer_k, outer_v) __ ?.i..
# print ?
# # {'first': {1.0}, 'second': {2.0}}
#
#
# nested_dict = {'first':{'a':1}, 'second':{'b':2}}
#
# ___ outer_k outer_v __ ?.i..
#     ___ inner_k inner_v __ outer_v.i..
#         outer_v.up.. inner_k fl__ inner_v
# ?.up.. outer_k outer_v
#
# print ?
# # {'first': {'a': 1.0}, 'second': {'b': 2.0}}