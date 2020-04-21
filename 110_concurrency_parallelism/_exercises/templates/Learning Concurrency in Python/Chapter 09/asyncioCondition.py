# ______ a..
#
#
# ? ___ consumer condition n
#     w__ ? condition
#         print('consumer @ is waiting'.f.. ?
#         ? ?.w..
#         print('consumer @ triggered'.f.. ?
#     print('ending consumer @'.f.. ?
#
#
# ? ___ manipulate_condition condition
#     print('starting manipulate_condition')
#
#     # pause to let consumers start
#     ? ?.s.. 0.1
#
#     ___ i in ra.. 1 3
#         w__ ? ?
#             print('notifying @ consumers'.f.. ?
#             ?.n.. n_i
#         ? ?.s.. 0.1
#
#     w__ ? condition
#         print('notifying remaining consumers')
#         ?.n_a..
#
#     print('ending manipulate_condition')
#
#
# ? ___ main loop
#     # Create a condition
#     condition _ ?.C..
#
#     # Set up tasks watching the condition
#     consumers _ |
#         consumer|c.. i
#         ___ i __ ra.. 5
#     |
#
#     # Schedule a task to manipulate the condition variable
#     ?.c_t.. ? c..
#
#     # Wait for the consumers to be done
#     ? ?.w.. ?s
#
#
# event_loop _ ?.g_e_l..
# ___
#     result _ ?.r_u_c.. m.. ?
# f...
#     ?.c..