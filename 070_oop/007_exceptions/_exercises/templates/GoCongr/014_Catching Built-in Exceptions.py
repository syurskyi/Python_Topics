# # Catching Built-in Exceptions
# ___ kaboom x y
#     print(x + y)               # Trigger TypeError
#
# ___
#     ? 0, 1, 2| "spam"
# ____ T...             # Catch and recover here
#     print('Hello world!')
# print('resuming here')         # Continue here if exception or not
