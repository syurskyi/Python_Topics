# _______ p__
#
# ____ k.. _______ g..
#
#
# ___ test_no_arguments
#     ... ? __ 'julian is a programmer'
#
#
# ___ test_one_positional_arg
#     w__ p__.r.. T..
#         ? julian
#
#
# ___ test_wrong_single_kw
#     w__ p__.r.. T..
#         ? test=T..
#
#
# ___ test_wrong_additional_kw
#     w__ p__.r.. T..
#         ? name='bob', profession='software developer',
#                     another_flag=F..
#
#
# ___ test_correct_kw_second_default
#     ... ? name='bob' __ 'bob is a programmer'
#
#
# ___ test_two_correct_kws
#     ret = ?(name='bob', profession='software developer')
#     ... ? __ 'bob is a software developer'