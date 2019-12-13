# f___ f... ______ di..  mu..
# f___ u____ ______ T....
#
#
# c_ TestFunctions T..
#     ___ test_divide_result ____
#         dividend _ 15
#         divisor _ 3
#         expected_result _ 5.0
#         ____.aAE_  di..  d__d d__r  e._r. delta_0.0001
#
#     ___ test_divide_negative ____
#         d__d _ 15
#         d__r _ -3
#         e._r. _ -5.0
#         ____.aAE_  di..  d__d d__r  e._r. delta_0.0001
#
#     ___ test_divide_dividend_zero ____
#         d__d _ 0
#         d__r _ 5
#         e._r. _ 0
#         ____.aE_  di..  d__d d__r  e._r.
#
#     ___ test_divide_error_on_zero ____
#         w__ ____.aR_  V...
#             di..  25 0
#
#     ___ test_multiply_empty ____
#         w___ ____.aR_  V...
#             mu..
#
#     ___ test_multiply_single_value ____
#         expected _ 15
#         ____.aE_  mu..  ex..  ex..
#
#     ___ test_multiply_zero ____
#         ex.. _ 0
#         ____.aE_  mu..  ex..  ex..
#
#     ___ test_multiply_result ____
#         inputs _  3 5
#         ex.. _ 15
#         ____.aE_  mu..  0i..  ex..
#
#     ___ test_multiply_results_with_zero ____
#         inputs _  3 5 0
#         ex.. _ 0
#         ____.aE_  mu..  0i..  ex..
#
#     ___ test_multiply_negative ____
#         inputs _  3 -5 2
#         ex.. _ -30
#         ____.aE_  mu..  0i..  ex..
#
#     ___ test_multiply_floats ____
#         inputs _  3.0 2
#         ex.. _ 6.0
#         ____.aE_  mu..  0i..  ex..
