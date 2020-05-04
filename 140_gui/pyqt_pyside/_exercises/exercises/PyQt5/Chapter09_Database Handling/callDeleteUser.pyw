# _____ _3, ___
# ____ ?.?W.. _____ ?D.., ?A..
# ____ _3 _____ E..
#
# ____ demoDeleteUser _____ _
#
# c_ MyForm(?D..
#
#     ___  -
#         s__. -
#         ui _ ?
#         ?.sU..
#         ?.pBD__.c___.c.. D..
#         ?.pBY__.c___.c.. C..
#         ?.lS__.h..
#         ?.pBY__.h..
#         ?.pBN_.h..
#         s..
#
#     ___ DeleteUser
#         selectStatement_"S.. _ F.. U.. w.. EAd.. l.. '"+?.lEEA__.t..+"' and Password like '"+ ?.lEP__.t..+"'"
#         ___
#             conn _ _3.c.. "ECommerce.db"
#             cur _ ?.c..
#             ?.e.. sSt..
#             row _ cur.f..
#             __ row__None:
#                 ?.lS__.h..
#                 ?.pBY__.h..
#                 ?.pBN_.h..
#                 ?.lR___.sT..("Sorry, Incorrect email address or password ")
#             ____
#                 ?.lS__.s..
#                 ?.pBYes.s..
#                 ?.pushBN_.s..
#                 ?.lR___.sT.. ""
#         _____ E.. __ e
#             ?.lR___.sT.. "Error in accessing user account"
#         f..
#             conn.c..
#
#     ___ ConfirmDelete
#         deleteStatement_"D.. F.. U.. w.. EA.. l.. '"+?.lEEA__.t..+"' and Password like '"+ ?.lEP__.t..+"'"
#         ___
#             conn _ _3.c.. "ECommerce.db"
#             cur _ ?.c..
#             w__ ?
#                 ?.e.. dS..
#                 ?.lR___.sT.. "User successfully deleted"
#         _____ E.. __ e
#             ?.lR___.sT.. "Error in deleting user account"
#         f..
#             ?.c..
#
# __ _ ____ __ _____
#     app _ ?A..
#     w _ ?
#     ?.s..
#     ___.e.. ?.e
