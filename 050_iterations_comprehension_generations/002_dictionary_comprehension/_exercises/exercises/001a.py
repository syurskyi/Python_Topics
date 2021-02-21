# # Example 1: Dictionary Comprehension
#
# # Consider the following code:
#
# # num
# square_dict _ di__
# ___ ? __ ra.. 1 11
#     ? ? _ ?*?
# print>
#
# # Now, let's create the dictionary in the above program using dictionary comprehension.
#
# # num
# # dictionary comprehension example
# square_dict = ? ?*? ___ ? __ ra.. 1 11
# print(square_dict)
#
# # The output of both programs will be the same.
#
# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
#
#
# #item price in dollars
# old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
#
# dollar_to_pound = 0.76
# # item, value
# new_price _ {? ?*? ___ ? ? __ ?.i..
# print ?
# # {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}
#
# # Conditionals in Dictionary Comprehension
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
#
# # k, v
# even_dict _ ? ? ___ ? ? __ ?.i.. __ ? % 2 __ 0
# print ?
# # {'jack': 38, 'michael': 48}
#
# # Example 5: Multiple if Conditional Dictionary Comprehension
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
#
# # k, v
# new_dict = ? ? ___ ? ? __ ? ?.i.. __ ? % 2 !_ 0 __ ? < 40
# print ?
# # {'john': 33}
#
# # Example 6: if-else Conditional Dictionary Comprehension
#
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
#
# # k
# new_dict_1 _ ? |*old __ ? > 40 ____ *young
#     ___ ? ? __ ?.i..
# print(new_dict_1)
# # {'jack': 'young', 'michael': 'old', 'guido': 'old', 'john': 'young'}
#
# # Example 7: Nested Dictionary with Two Dictionary Comprehensions
# # k1, k2
# dictionary _
#     ? ? ? * ? ___ ? __ ra.. 1 6 ___ ? __ ra.. 2 5
#
# print ?
#
# # {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
# # 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
# # 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}
#
# # As you can see, we have constructed a multiplication table in a nested dictionary, for numbers from 2 to 4.
# # Whenever nested dictionary comprehension is used, Python first starts from the outer loop and then goes
# # to the inner one.
# # So, the above code would be equivalent to:
#
# # k1, k2
# dictionary _ di__
# ___ ? __ ra.. 11 16
#     ? ? _ ? ?*? ___ ? __ ra.. 1 6
# print ?
#
# # k1, k2
# dictionary _ di__
# ___ ? __ ra.. 11 16
#     ? ? _ di__
#     ___ ? __ ra.. 1 6)
#         ? ? ? _ ?*?
# print ?
#
# # Warnings on Using Dictionary Comprehension
# # Even though dictionary comprehensions are great for writing elegant code that is easy to read,
# # they are not always the right choice.
# #
# # We must be careful while using them as :
# #
# #     They can sometimes make the code run slower and consume more memory.
# #     They can also decrease the readability of the code.
# #
# # We must not try to fit a difficult logic or a large number of dictionary comprehension inside them just
# # for the sake of making the code single lined. In these cases, It is better to choose other alternatives like loops.