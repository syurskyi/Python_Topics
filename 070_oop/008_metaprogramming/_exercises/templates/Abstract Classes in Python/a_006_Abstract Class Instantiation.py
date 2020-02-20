# # Abstract Class Instantiation :
# # Abstract classes are incomplete because they have methods which have no body. If python allows creating an object
# # for abstract classes then using that object if anyone calls the abstract method, but there is no actual implementation
# # o invoke. So we use an abstract class as a template and according to the need we extend it and build on it before
# # we can use it. Due to the fact, an abstract class is not a concrete class, it cannot be instantiated.
# # When we create an object for the abstract class it raises an error.
#
# # Python program showing
# # abstract class cannot
# # be an instantiation
# ____ a.. _____ A.. a..
#
#
# c_ Animal A..
#     ??
#     ___ move
#         p..
#
#
# c_ Human ?
#     ___ move
#         print("I can walk and run")
#
#
# c_ Snake ?
#     ___ move
#         print("I can crawl")
#
#
# c_ Dog ?
#     ___ move
#         print("I can bark")
#
#
# c_ Lion ?
#     ___ move
#         print("I can roar")
#
#
# c = A..
#
# # Output:
# #
# # Traceback (most recent call last):
# #   File "/home/ffe4267d930f204512b7f501bb1bc489.py", line 19, in
# #     c=Animal()
# # TypeError: Can't instantiate abstract class Animal with abstract methods move
