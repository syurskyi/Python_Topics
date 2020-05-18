# ____ ? _____ pool
#
#
# c_ Database
#
#     __c.. _ w..
#
#     ??
#     ___ initialise $$
#         D__.__c.. _ p_.SCP.. 1 10 $$
#
#     ??
#     ___ get_connection
#         r_ ?.__c__.g..
#
#     ??
#     ___ return_connection connection
#         ?.__c__.p.. ?
#
#     ??
#     ___ close_all_connections(
#         ?.__c__.c..
#
# c_ CursorFromConnectionPool
#     ___ -
#         conn _ w..
#         cursor _ w..
#
#     ___ -e
#         co.. _ ?.g_c..
#         cu.. _ co__.c..
#         r_ cu..
#
#     ___ -e  exception_type exception_value, exception_traceback):
#         __ e_v..  # This is equivalent to `if exception_value is not None`
#             co__.r..
#         ____
#             cu__.c..
#             co__.c..
#         ?.r_c.. co..
