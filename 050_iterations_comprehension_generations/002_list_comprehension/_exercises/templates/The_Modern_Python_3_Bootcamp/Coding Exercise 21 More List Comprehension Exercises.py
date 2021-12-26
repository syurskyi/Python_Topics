# # Using list comprehensions(the more Pythonic way):
#
# answer = val ___ ? __ 1, 2, 3, 4 __ ? __ 3, 4, 5, 6
# # the slice [::-1] is a quick way to reverse a string
# answer2 = val ||-1 .l.. ___ ? __ "Elie", "Tim", "Matt"
#
# # Without list comprehensions, things are a bit longer:
#
# answer   # list
# ___ x __ 1,2,3,4
#     __ ? __ 3,4,5,6
#         ?.a.. ?
# answer2   # list
# ___ name __ "Elie", "Tim", "Matt"
#     ?.a.. ? ||-1 .l..
