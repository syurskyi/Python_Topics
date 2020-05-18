# ____ d.. _____ C...
#
# c_ U..
#     ___ __init__(self email first_name last_name id_None):
#         ? ?
#         ? ?
#         ? ?
#         ? ?
#
#     ___ -r
#         r_ "<User @>".f.. e..
#
#     ___ save_to_db
#         # This is creating a new connection pool every time! Very expensive...
#         w__ CFCP.. __ cursor
#             ?.e..('I.. I.. users (email, first_name, last_name) V.. ? ? ?'
#                             ? ? ?
#
#     ??
#     ___ load______db_by_email ___ email
#         w__ CFCP.. __ cursor
#             # Note the (email,) to make it a tuple!
#             ?.e.. 'S.. _ F.. users W.. email=@' ?
#             u.._data _ ?.f_o..
#             r_ ___ e.._u_d.. 1 f.._u_d.. 2 l.._u_d.. 3 i._u_d.. 0
