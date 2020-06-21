# # Creating Enumerations Programmatically
# # In some cases, it is more convenient to create enumerations programmatically, rather than hard-coding them in
# # a class definition. For those situations, Enum also supports passing the member names and values to the class
# # constructor.
# #
# # enum_programmatic_create.py
#
# ______ ____
#
# BugStatus = ____.E..(
#     value='BugStatus',
#     names=('fix_released fix_committed in_progress '
#            'wont_fix invalid incomplete new'),
# )
#
# print('Member: @'.f.. ?.n..
#
# print('\nAll members:')
# ___ status __ ?
#     print('@15 = @'.f.. ?.n.. ?.v..
#
# # The value argument is the name of the enumeration, which is used to build the representation of members.
# # The names argument lists the members of the enumeration. When a single string is passed, it is split on whitespace
# # and commas, and the resulting tokens are used as names for the members, which are automatically assigned values
# # starting with 1.
# #
# # $ python3 enum_programmatic_create.py
# #
# # Member: BugStatus.new
# #
# # All members:
# # fix_released    = 1
# # fix_committed   = 2
# # in_progress     = 3
# # wont_fix        = 4
# # invalid         = 5
# # incomplete      = 6
# # new             = 7