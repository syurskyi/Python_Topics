# ____ d.. _______ D..
#
# _______ p__
#
# ____ ? _______ ?
#
#
# ?p__.f..
# ___ list1
#     r.. ? 1, 3, 5
#
#
# ?p__.f..
# ___ list2
#     r.. ? 2, 3, 4, 5, 7
#
#
# ___ test_mean_median_start_first_instance list1
#     ... ?.m.. __ 3
#     ... ?.m.. __ 3
#
#
# ___ test_append_and_new_stats_first_instance list1
#     ?.a..(7)
#     ... ?.m.. __ 4
#     ... ?.m.. __ 4
#
#
# ___ test_mean_median_start_second_instance list2
#     ... ?.m.. __ 4.2
#     ... ?.m.. __ 4
#
#
# ___ test_append_and_new_stats_second_instance list2
#     ?.a..(9.0)  # float ok too
#     ?.a.. D.. 11  # decimal ok too
#     ... r.. ?.m.. 2) __ 5.86
#     ... ?.m.. __ 5
#
#
# ?p__.m__.p. "arg",  'a',  'a' , {'a': 1}])
# ___ test_cannot_append_non_int_values list1 list2 arg
#     ___ instance __ ? ?
#         w__ p__.r.. T..
#             ?.a.. ?
#
#
# ___ test_cannot_append_non_int_values_via_overloading list1
#     w__ p__.r.. T..
#         ? +  'a'
#
#
# ___ test_cannot_append_non_int_values_via_inplace_overloading list2
#     w__ p__.r.. T..
#         ? +_  'a'
#
#
# ___ test_can_append_list_of_ints list1
#     ___
#         ? +_ 1, 2, 3
#     ______ E.. __ exc
#         p__.f.. ?
#     ... ? __ 1, 3, 5, 1, 2, 3