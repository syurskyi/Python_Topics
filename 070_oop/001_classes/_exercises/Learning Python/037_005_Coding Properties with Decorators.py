# c_ Person
#     ___ - ____ name
#         ____._name _ name
#
#     0p.
#     ___ name ____  # name = property(name)
#         "name property docs"
#         print('fetch...')
#         r_ ____._n.
#
#     0n_.s.
#     ___ name ____ value  # name = name.setter(name)
#         print('change...')
#         ____._n. _ v..
#
#     0n_.d..
#     ___ name ____  # name = name.deleter(name)
#         print('remove...')
#         del ____._n.
#
#
# bob = ? Bob Smith  # bob has a managed attribute
# print(?.name)  # Runs name getter (name 1)
# ?.n.. _ 'Robert Smith'  # Runs name setter (name 2)
# print ?.na..
# del ?.na..  # Runs name deleter (name 3)
#
# print('-' * 20)
# sue = ? Sue Jones  # sue inherits property too
# print ?.na..
# print P__.n__. -d  # Or help(Person.name)
#
