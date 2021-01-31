# ______ ___
# ______ n..
# ______ g..
# ______ uu..
# ______ _______
# ______ d_t_
#
# ____ ?.?G.. ______ _
# ____ ?.?C.. ______ _
# ____ ?.?W.. ______ _
#
# SERVER _ _______.______
# DB _ ? *fxphd
# USER_COLLECTION _ ? *users
# CLIPBOARD_COLLECTION _ ? *clipboards
# SCRIPT_LOCATION _ *c:/clipboard
# CURRENT_USER _ g__.g..
#
# ____ _______ ______ C..
#
#
# c_ ClipboardCore ?
#     ___  -
#         s_ ? ? -
#
#         all_users _ user ___ ? __ U_C_.f..
#         b..
#
#         u__.tC__.c__ b__
#         s_c__.c__.c__ c..
#         s_p__.c__.c__ s_
#         r__.c__.c__ c..
#         p__.c__.c__ p__
#         h___.cCC__.c__ s_n..
#
#         b_h..
#
#     ___ set_note index
#         item _ h___.i.. ?, 0
#         obj _ ?.d.. 32
#         note _ ? *note
#         r___.sPT.. ?
#
#     ___ paste_clipboard
#         row _ h___.cR..
#         item _ h___.i.. ? 0
#         doc _ ?.d.. 32
#         script _ ? *nuke_file
#         n__.nP.. "@/@"   S.. ?
#
#     ___ send_clipboard
#         row_count _ s_l_w__.c..
#         __ no. ?
#             ?MB__.i..  *Warning *No user selected
#             r_
#
#         now _ d_t_.d_t_.n..
#         script _ "@.nk"  u__.u..
#         n__.nC.. *@/@   S.. ?
#         ___ i __ ra__ r_c..
#             obj _ s_l_w__.i.. ?.d.. 32
#             doc _ di..
#             ? *sender _ C_U..
#             ? *submitted_at _ now
#             ? *destination_user _ o.. *login
#             ? *nuke_file _ s..
#             ? *note _ t_n_t_e.tPT..
#             C_C__.s.. ?
#         c..
#
#     ___ build_history
#         query _ C_C_.f.. *destination_user : C_U..||.so.. *submitted_at -1
#         h___.sRC.. ?.c..
#         ___ x, i __ e.. ?
#             sender_query _ U_C__.f_o.. *login : ?|*sender
#             item1 _ ?TWI.. ? *name
#             ?.sD.. 32 ?
#             item2 _ ?TWI.. g_t_d_a_s.. ?|*submitted_at
#             h___.I.. ? 0 _1
#             h__w.sI.. ? 1 _2
#
#     ___ get_time_difference_as_string  date
#         delta _ d_t_.d_t_.t.. - ?
#         __ de__.d..
#             r_ *@ day(s) de__.d..
#         seconds _ de__.s..
#         __ ? < 60:
#             r_ *A few seconds ago
#         ____ ? < 3600
#             r_ *@ minute(s) ago  ? / 60
#         ____ ? < 86400:
#             r_ @ hours(s) ago ? / 3600
#
#     ___ build_user_list_widget
#         u___.c..
#         search_pattern _ u__.t__ .l..
#         ___ user __ all_u..
#             name _ ? *name
#             __ ? __ ?.l..
#                 item _ ?LWI.. ?
#                 ?.sD.. 32 ?
#                 ?.sTT.. g__t.. ?
#                 u____.aI.. ?
#         u___.sI..
#
#     ___ get_user_tooltip  user
#         r_ "Email: @\nLogin: @\nAge: @"  (? *? ? *? ? *?
#
#
# ___ start
#     ?.p.. _ ?
#     ?.p__.s..
#
# # app _ QApplication(___.argv)
# # panel _ ClipboardCore()
# # panel.show()
# # app.exec_()
#
