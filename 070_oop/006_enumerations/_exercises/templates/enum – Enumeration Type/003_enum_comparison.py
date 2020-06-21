# # Comparing Enums
# # Because enumeration members are not ordered, they support only comparison by identity and equality.
# # enum_comparison.py
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
# actual_state = ?.w..
# desired_state = ?.f..
#
# print('Equality:',
#       a.. __ d..
#       a.. __ B__.w..
# print('Identity:',
#       a.. __ d..
#       a.. __ B__.w..
# print('Ordered by value:')
# ___
#     print('\n'.j.. '  ' + s.n.. ___ ? __ so.. B..
# e.. T.. __ err:
#     print('  Cannot sort: @'.f.. ?
#
# # The greater-than and less-than comparison operators raise TypeError exceptions.
#
# # $ python3 enum_comparison.py
# #
# # Equality: False True
# # Identity: False True
# # Ordered by value:
# #   Cannot sort: '<' not supported between instances of 'BugStatus
# # ' and 'BugStatus'