# ### file: spam.py
#
# c_ Spam
#     numInstances = 0
#     ___ - ____
#         ?.? _ ?.? + 1
#
#     ___ printNumInstances ____
#         print("Number of instances created: " ?.?
#
# # from spam import Spam
# a = ?                   # Cannot call unbound class methods in 2.6
# b = ?                   # Methods expect a self object by default
# c = ?
#
# # Spam.printNumInstances()
# # TypeError: unbound method printNumInstances() must be called with Spam instance
# # as first argument (got nothing instead)
# # a.printNumInstances()
# # TypeError: printNumInstances() takes no arguments (1 given)
#
# # from spam import Spam
# # a = Spam()                       # Can call functions in class in 3.0
# # b = Spam()                       # Calls through instances still pass a self
# # c = Spam()
#
# # Spam.printNumInstances()         # Differs in 3.0
# # Number of instances created:  3
# # a.printNumInstances()
# # TypeError: printNumInstances() takes no arguments (1 given)
#
# # Spam.printNumInstances()             # Fails in 2.6, works in 3.0
# # instance.printNumInstances()         # Fails in both 2.6 and 3.0
