# # C:\misc> c:\python26\python
# from access import Private
# _P.. 'age'
# c_ Person
#     ___ - ____
#         ____.age = 42
#     ___ -s ____
#         r_ 'Person: ' + st. ____.a..
#     ___ -a ____ yrs
#          ____.a.. +_ y..
# 
# X = ?
# ?.a..                                   # Name validations fail correctly
# # TypeError: private attribute fetch: age
# print(X)                                # __getattr__ => runs Person.__str__
# # Person: 42
# X + 10                                  # __getattr__ => runs Person.__add__
# print(X)                                # __getattr__ => runs Person.__str__
# # Person: 52
# 
# # C:\misc> c:\python30\python
# from access import Private
# _P.. 'age'
# c_ Person
#     ___ - ____
#         ____.a.. _ 42
#     ___ -s ____
#         r_ 'Person: ' + st. ____.a..
#     ___ -a ____ yrs
#         ____.a.. +_ y..
# 
# X = P..                           # Name validations still work
# ?.a..                                   # But 3.0 fails to delegate built-ins!
# # TypeError: private attribute fetch: age
# print(X)
# # <access.onInstance object at 0x025E0790>
# X + 10
# # TypeError: unsupported operand type(s) for +: 'onInstance' and 'int'
# print(X)
# # <access.onInstance object at 0x025E0790>
# 
