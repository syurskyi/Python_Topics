# c_ Name                             # Use (object) in 2.6
#     "name descriptor docs"
#     ___ -g  ____ instance owner
#         print('fetch...')
#         r_ in___._name
#     ___ -s ____ instance value
#         print('change...')
#         in___._na.. _ va..
#     ___ __delete__ ____ instance
#         print('remove...')
#         del instance._name
#
# c_ Person:                          # Use (object) in 2.6
#     ___ -  ____ name
#         ____._na.. _ n..
#     name _ N..                       # Assign descriptor to attr
#
# bob = P... Bob Smith               # bob has a managed attribute
# print ?.n..                         # Runs Name.__get__
# ?.na.. _ 'Robert Smith'               # Runs Name.__set__
# print ?.na..
# del ?.na..                            # Runs Name.__delete__
#
# print('-'*20)
# sue = P... Sue Jones               # sue inherits descriptor too
# print ?.n..
# print N___. -d                     # Or help(Name)
#
# c_ Super
#     ___ - ____ name
#         ____._name _ name
#     name = N
#
# c_ Person S...                            # Descriptors are inherited
#    p..
#
#
# c_ Person:
#     ___ __init__(____, name):
#         ____._name = name
#
#     c_ Name:                                 # Using a nested c_
#         "name descriptor docs"
#         ___ __get__(____, instance, owner):
#             print('fetch...')
#             return instance._name
#         ___ __set__(____, instance, value):
#             print('change...')
#             instance._name = value
#         ___ __delete__(____, instance):
#             print('remove...')
#             del instance._name
#     name = Name()
#
#
# print(Person.Name.__doc__)     # Differs: not Name.__doc__ outside c_
#
