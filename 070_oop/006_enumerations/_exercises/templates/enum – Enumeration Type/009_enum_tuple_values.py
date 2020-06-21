# # Non-integer Member Values
# # Enum member values are not restricted to integers. In fact, any type of object can be associated with a member.
# # If the value is a tuple, the members are passed as individual arguments to __init__().
# #
# # enum_tuple_values.py
#
# ______ ____
#
# c_ BugStatus ____.E..
#
#     new = (7, ['incomplete',
#                'invalid',
#                'wont_fix',
#                'in_progress'])
#     incomplete = (6, ['new', 'wont_fix'])
#     invalid = (5, ['new'])
#     wont_fix = (4, ['new'])
#     in_progress = (3, ['new', 'fix_committed'])
#     fix_committed = (2, ['in_progress', 'fix_released'])
#     fix_released = (1, ['new'])
#
#     ___  - ____, num transitions
#         ____.?  ?
#         ____.?  ?
#
#     ___ can_transition ____ new_state
#         r_ ?.n.. __ ____.t..
#
#
# print('Name:', ?.i..
# print('Value:', ?.i__.v..
# print('Custom attribute:', ?.i__.t..
# print('Using attribute:', ?.i__.c_t ?.n..
#
#
# # In this example, each member value is a tuple containing the numerical ID (such as might be stored in a database)
# # and a list of valid transitions away from the current state.
# #
# # $ python3 enum_tuple_values.py
# #
# # Name: BugStatus.in_progress
# # Value: (3, ['new', 'fix_committed'])
# # Custom attribute: ['new', 'fix_committed']
# # Using attribute: True
