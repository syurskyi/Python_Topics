# f___ pr.. _____ P_ P_E_
# f___ u___ _______ T...
#
#
# c_ TestPrinter ?
#     ___ setUp
#         printer _ Pr__ pages_per_s=2.0, capacity=300
#
#     ___ test_print_within_capacity
#         ?.print(25)
#
#     ___ test_print_outside_capacity
#         w___ ____.aR_ P..
#             ?.print(301)
#
#     ___ test_print_exact_capacity
#         ?.print ?._capacity
#
#     ___ test_printer_speed
#         pages _ 10
#         expected _ 'Printed 10 pages in 5.00 seconds.'
#
#         result _ ?.print p..
#         assertEqual ? ex..
#
#     ___ test_speed_always_two_decimals
#         fast_printer _ Pr__ pages_per_s=3.0, capacity=300
#         pages _ 11
#         expected _ 'Printed 11 pages in 3.67 seconds.'
#
#         result _ f_p_.print p..
#         aE_ ? e...
#
#     ___ test_multiple_print_runs
#         ?.print 25
#         ?.print 50
#         ?.print 225
#
#     ___ test_multiple_runs_end_up_error
#         ?.print 25
#         ?.print 50
#         ?.print 225
#
#         w___ aR_  P...
#             ?.print(1)