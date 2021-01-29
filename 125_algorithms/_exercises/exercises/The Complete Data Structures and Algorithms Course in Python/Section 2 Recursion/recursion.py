# #### Russian Doll recursive function ###
#
# ___ openRussianDoll doll
#     __ ? __ 1
#         print("All dolls are opened")
#     ____
#         ? ?-1
#
#
# ? 4
#
#
# # ___ recursionMethod(parameters):
# #     if  exit from condition satisfied:
# #         return some value
# #     else:
# #         recursionMethod(modified parameters)
#
#
# ___ firstMethod
#     secondMethod
#     print("I am the first Method")
#
# ___ secondMethod
#     thirdMethod
#     print("I am the second Method")
#
# ___ thirdMethod
#     fourthMethod
#     print("I am the third Method")
#
# ___ fourthMethod
#     print("I am the fourth Method")
#
#
# firstMethod()
#
#
# ___ recursiveMethod n
#     __ ?<1
#         print("n is less than 1")
#     ____
#         ? ?-1
#         print ?
#
# recursiveMethod 4
#  ## Recursion vs Iterarion###
#
# ___ powerOfTwo n
#     __ ? __ 0
#          r_ 1
#     ____
#         power _ ? ?-1
#         r_ ? * 2
#
# print(powerOfTwo 3
#
# ___ powerOfTwoIt n
#     i _ 0
#     power _ 1
#     w__ i < ?
#         ? _ ? * 2
#         i _ i + 1
#     r_ ?
#
#
# print(powerOfTwoIt(4))
#
#  ## Factorial###
#
#
# ___ factorial n
#     a__ ? >_ 0 a__ in. ? __ ? 'The number must be positive integer only!'
#     __ ? __  0,1
#         r_ 1
#     ____
#         r_ ? * ? ?- 1
#
#
#  ## Fibonacci###
#
# ___ fibonacci n
#     a__ ? >_0 a__ in. ? __ ? 'Fibonacci number cannot be negative number or non integer.'
#     __ ? __ 0,1
#         r_ ?
#     ____
#         r_ ? ? - 1 + ? ? - 2
#
# print ?7
