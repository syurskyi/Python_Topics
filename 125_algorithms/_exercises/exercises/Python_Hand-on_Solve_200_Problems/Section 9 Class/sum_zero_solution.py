# # To add a new cell, type '# %%'
# # To add a new markdown cell, type '# %% [markdown]'
# # %%
# # Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
# # Input
# # [-25, -10, -7, -3, 2, 4, 8, 10]
# # Output
# # [[-10, 2, 8], [-7, -3, 10]]
#
# c_ py_solution
#  ___ threeSum  nums
#         n.. result, i _ s.. ?   # list, 0
#         w___ i < le. ? - 2
#             j, k _ ? + 1, le. ? - 1
#             w___ j < k
#                 __ ? ? + ? ? + ? ? < 0
#                     j +_ 1
#                 ____ ? ? + ? ? + ? ? > 0
#                     k -_ 1
#                 ____
#                     ?.ap.. ? ? ? ? ? ?
#                     j, k _ ? + 1, ? - 1
#                     w___ j < k an. ? ? __ ? ? - 1
#                         ? +_ 1
#                     w___ j < k an. ? ? __ ? ? + 1
#                         k -_ 1
#             ? +_ 1
#             w___ i < le. ? - 2 an. ? ? __ ? ? - 1
#                 ? +_ 1
#         r_ ?
#
# print ?.? -25, -10, -7, -3, 2, 4, 8, 10
#
#
