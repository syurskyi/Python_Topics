# # For more control over the values associated with members, the names string can be replaced with a sequence
# # of two-part tuples or a dictionary mapping names to values.
#
# # enum_programmatic_mapping.py
#
# ______ ____
#
# BugStatus = ____.E..(
#     value='BugStatus',
#     names=[
#         ('new', 7),
#         ('incomplete', 6),
#         ('invalid', 5),
#         ('wont_fix', 4),
#         ('in_progress', 3),
#         ('fix_committed', 2),
#         ('fix_released', 1),
#     ],
# )
#
# print('All members:')
# ___ status __ ?
#     print('@15 = @'.f.. ?.n.. ?.v..
#
#
# # In this example, a list of two-part tuples is given instead of a single string containing only the member names.
# # This makes it possible to reconstruct the BugStatus enumeration with the members in the same order as
# # the version defined in enum_create.py.
# #
# # $ python3 enum_programmatic_mapping.py
# #
# # All members:
# # new             = 7
# # incomplete      = 6
# # invalid         = 5
# # wont_fix        = 4
# # in_progress     = 3
# # fix_committed   = 2
# # fix_released    = 1