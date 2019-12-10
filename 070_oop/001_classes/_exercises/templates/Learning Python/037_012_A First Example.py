# c_ Person:
#     ___ - ____ name               # On [Person()]
#         ____._n.. _ n..                   # Triggers __setattr__!
#
#     ___ -g ____ attr            # On [obj.undefined]
#         i_ a... __ 'name':                  # Intercept name: not stored
#             print('fetch...')
#             r_ ____._na..               # Does not loop: real attr
#         e___                               # Others are errors
#             r___ A.... a..
#
#     ___ -s  ____ attr value     # On [obj.any = value]
#         i_ attr __ 'name'
#             print('change...')
#             a.. _ '_name'                  # Set internal name
#         ____. -d a.. _ v...         # Avoid looping here
#
#     ___ -d  ____ attr            # On [del obj.any]
#         i_ a.. __ 'name'
#             print('remove...')
#             a.. _ '_name'                  # Avoid looping here too
#         del ____. -d a..             # but much less common
#
# bob = P_ Bob Smith           # bob has a managed attribute
# print ?.n..                     # Runs -g
# ?.name _ 'Robert Smith'           # Runs __setattr__
# print ?.n..
# del ?.n..                        # Runs __delattr__
#
# print('-'*20)
# sue = P... Sue Jones           # sue inherits property too
# print ?.n.
# #print(Person.name.__doc__)         # No equivalent here
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
#
#
#     # # Replace -g  with this
#     #
#     # ___ __getattribute__(____, attr):                 # On [obj.any]
#     #     if attr == 'name':                            # Intercept all names
#     #         print('fetch...')
#     #         attr = '_name'                            # Map to internal name
#     #     r_ object.__getattribute__(____, attr)    # Avoid looping here
#
#
# # #######################################################################################
#
# c_ Person
#     ___ - ____ name               # On [Person()]
#         ____._n.. _ n..                   # Triggers __setattr__!
#
#     ___ -g ____ attr                 # On [obj.any]
#         i_ attr __ 'name'                            # Intercept all names
#             print('fetch...')
#             a... _ '_name'                            # Map to internal name
#         r_ obj___. -g____ a..    # Avoid looping here
#
#     ___ -s ____ attr value     # On [obj.any = value]
#         i_ attr __ 'name'
#             print('change...')
#             a.. _ '_name'                  # Set internal name
#         ____. -d a.. _ v..         # Avoid looping here
#
#     ___ -d ____ attr            # On [del obj.any]
#         i_ a.. __ 'name'
#             print('remove...')
#             a.. _ '_name'                  # Avoid looping here too
#         del ____. -d a..             # but much less common
#
# bob = ? Bob Smith           # bob has a managed attribute
# print ?.n..                     # Runs -g
# ?.n.. = 'Robert Smith'           # Runs __setattr__
# print ?.n..
# del ?.n..                        # Runs __delattr__
#
# print('-'*20)
# sue = ? Sue Jones           # sue inherits property too
# print ?.n.
# #print(Person.name.__doc__)         # No equivalent here
