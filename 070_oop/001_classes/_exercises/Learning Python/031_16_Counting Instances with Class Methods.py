# c_ Spam:
#     numInstances = 0                         # Use class method instead of static
#     ___ - ____
#         S_.n... += 1
#     ___ printNumInstances ___
#         print("Number of instances:", ___.n....
#     p... _ cl... p..
#
#
# a, b = S.. S..
# a.p...                   # Passes class to first argument
# S__.p..                 # Also passes class to first argument
#
# c_ Spam
#     numInstances = 0                         # Trace class passed in
#     ___ -  ____
#         S_.n.. += 1
#     ___ printNumInstances ___
#         print("Number of instances:", ___.n... ___
#     printNumInstances _ cl... p..
#
# c_ Sub S..
#     ___ printNumInstances ___              # Override a class method
#         print("Extra stuff...", ___         # But call back to original
#         S__.p...
#     printNumInstances _ cl... p..
#
# c_ Other S.. p..                      # Inherit class method verbatim
#
#
#
# x, y = Sub(), Spam()
# x.p...                    # Call from subclass instance
# Sub.p...                  # Call from subclass itself
# y.p...
#
# z = Other()
# ?.p..
