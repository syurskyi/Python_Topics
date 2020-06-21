# # Iteration
# # Iterating over the enum class produces the individual members of the enumeration.
#
# # enum_iterate.py
#
# ______ ____
#
# c_ BugStatus ____.E..
#
#     new = 7
#     incomplete = 6
#     invalid = 5
#     wont_fix = 4
#     in_progress = 3
#     fix_committed = 2
#     fix_released = 1
#
#
# ___ status __ ?
#     print('@15 = @'.f.. ?.n.. ?.v..
#
# # The members are produced in the order they are declared in the class definition. The names and values are not used to sort them in any way.
#
# # $ python3 enum_iterate.py
#
# # new             = 7
# # incomplete      = 6
# # invalid         = 5
# # wont_fix        = 4
# # in_progress     = 3
# # fix_committed   = 2
# # fix_released    = 1