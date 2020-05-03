# _____ _3, ___
# ____ ?.?W.. _____ ?D.., ?A..
# ____ _3 _____ E..
#
# ____ demoChangePassword _____ _
#
# c_ MyForm(?D..
#
#     ___  -
#         s__. -
#         ui _ ?
#         ?.sU..
#         ?.pushButtonChangePassword.c___.c.. ?
#         s..
#
#     ___ ChangePassword
#         selectStatement_*S.. EA.., P.. F.. U.. w.. EA.. l.. '"+?.lineEditEmailAddress.t..+"' an. Password like '"+ ?.lineEditOldPassword.t..+"'"
#         ___
#             conn _ _3.c.. "ECommerce.db"
#             cur _ ?.c..
#             ?.e.. sS..
#             row _ ?.f..
#             __ row__None:
#                 ?.lR___.sT..("Sorry, Incorrect email address or password ")
#             ____
#                 __ ?.lENP__.t..__ ?.lERP__.t..
#                     updateStatement_"U.. U.. set Password = '" + ?.lENP__.t..+"' W.. EA.. l.. '"+?.lEEA__.t..+"'"
#                     w__ ?
#                         ?.e.. uS..
#                         ?.lR___.sT.. "Password successfully changed"
#                 ____
#                     ?.lR___.sT.. "The two passwords don't match"
#         _____ E.. __ e
#             ?.lR___.sT.. "Error in accessing row"
#         f..
#             ?.c..
#
# __ _ ____ __ _____
#     app _ ?A..
#     w _ ?
#     ?.s..
#     ___.e.. ?.e
