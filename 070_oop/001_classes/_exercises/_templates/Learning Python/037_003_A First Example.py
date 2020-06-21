# c_ Person                      # Use (object) in 2.6
#     ___ - ____ name
#         ____._? _ ?
#     ___ getName ____
#         print('fetch...')
#         r_ ____._?
#     ___ setName ____ value
#         print('change...')
#         ____._name _ ?
#     ___ delName ____
#         print('remove...')
#         del ____._?
#     name _ p.. ? ? ? "name property docs"
#
# bob = ? ('Bob Smith')           # bob has a managed attribute
# print(?.n..                     # Runs getName
# ?.n.. _ 'Robert Smith'           # Runs setName
# print(?.n..
# del ?.n..                        # Runs delName
#
# print('-'*20)
# sue = ?('Sue Jones')           # sue inherits property too
# print(?.n..)
# print(?.n__. -d          # Or help(Person.name)
#
#
# print('#' * 82)
# print('#' * 82)
# print('#' * 82)
#
# c_ Super:
#     ___ - ____ name
#         ____._? ?
#     ___ getName ____
#         print('fetch...')
#         r_ ____._?
#     ___ setName ____ value
#         print('change...')
#         ____._? _ v..
#     ___ delName ____
#         print('remove...')
#         del ____._?
#     name = p.. ? ? ? 'name property docs')
#
# c_ Person ?
#     pass                            # Properties are inherited
#
# bob = ?('Bob Smith')
# print(?.n..)                     # Runs getName
# ?.n.. = 'Robert Smith'           # Runs setName
# print(?.n..)
# del ?.n..                        # Runs delName
#
# print('-'*20)
# sue = ?('Sue Jones')           # sue inherits property too
# print(?.n..)
# print(P__.n__. -d          # Or help(Person.name)
