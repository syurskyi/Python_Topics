# ____ c.. _______ C..
# ____ d__ _______ d__
# ____ ?.m.. _______ p.., M..
#
# _______ p__
#
# _______ m..
# ____ ? _______ t.. A..
#
#
# ?p__.f..
# ___ clean_cache
#     """Make sure each test starts with a clean cache dict"""
#     ?.v.. C..
#
#
# $p.. ?.t.. M.. s.._ 0, 2
# ___ test_one_operation_within_time clean_cache capfd
#     """1 operation took 2 seconds = ok"""
#     w__ ?
#         p..
#     output ?.r .. 0
#     ... n.. ?
#
#
# $p.. ?.t.. M.. s.._ 0, 2, 0, 3
# ___ test_two_operations_one_too_long clean_cache capfd
#     """2 operations, 1 took >= 3 seconds = still ok"""
#     w__ ?
#         p..
#     # this one took too long
#     w__ ?
#         p..
#     output ?.r .. 0
#     ... n.. ?
#
#
# $p.. ?.t.. M.. s.._ 0, 2, 0, 3, 0, 4
# ___ test_three_operations_two_too_long clean_cache capfd
#     """3 operations, 2 took >= 3 seconds = still ok"""
#     # Note that each timeit call takes the next 2 elements of side_effect
#     # = mocked start/end times in seconds
#     w__ ?
#         p..
#     w__ ?
#         p..
#     w__ ?
#         p..
#     output ?.r .. 0
#     ... n.. ?
#
#
# $p.. ?.t.. M.. s.._ 0, 2, 0, 3, 0, 4, 0, 5
# ___ test_four_operations_three_took_too_long clean_cache capfd
#     """4 operations, 3 tooks >= 3 seconds = NOT ok, prints ALERT"""
#     w__ ?
#         p..
#     w__ ?
#         p..
#     w__ ?
#         p..
#     w__ ?
#         p..
#     output ?.r .. 0
#     ... ?.s.. __ A..
#
#
# $p.. ?.t.. M..
#     s.._ 0, 2.3, 0, 3.3, 0, 2.1, 0, 2.21
#
# ___ test_four_operations_three_took_too_long_using_floats clean_cache capfd
#
#     """4 operations, 3 tooks > 2.2 seconds = NOT ok, prints ALERT"""
#     w__ ?
#         p..
#     w__ ?
#         p..
#     w__ ?
#         p..
#     w__ ?
#         p..
#     output ?.r .. 0
#     ... ?.s.. __ A..
#
#
# $p.. ?.t.. M.. s.._ 0, 3, 0, 3, 0, 4, 0, 5
# ___ test_four_operations_took_too_long_but_on_two_days clean_cache capfd
#     """4 tooks >= 3 seconds, but spread over 2 days = ok / no alert"""
#     # 2 violations yesterday
#     w__ patch ?.g.. r.._d.. 2018, 5, 1
#         w__ ?
#             p..
#         w__ ?
#             p..
#     # 2 violations today
#     w__ patch ?.g.. r.._d.. 2018, 5, 2
#         w__ ?
#             p..
#         w__ ?
#             p..
#     output ?.r .. 0
#     ... n.. ?
