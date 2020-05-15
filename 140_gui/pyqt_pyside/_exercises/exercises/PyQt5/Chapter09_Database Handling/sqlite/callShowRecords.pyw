# _____ _3, ___
# ____ ?.?W.. _____ ?D.., ?A..,?TWI..
# ____ _3 _____ E..
#
# ____ demoShowRecords _____ _
#
# rowNo_1
# sqlStatement_"S.. EA.., P.. F.. U.."
# conn _ _3.c.. "ECommerce.db"
# cur _ ?.c..
#
# c_ MyForm ?D..
#
#     ___  -
#         s__. -
#         ui _ ?
#         ?.sU..
#         cur.e.. s..
#         ?.pBF__.c___.c.. SFR..
#         ?.pBP__.c___.c.. SPR..
#         ?.pBN__.c___.c.. SNR..
#         ?.pBL__.c___.c.. SLR..
#         s..
#
#     ___ ShowFirstRow
#         ___
#             ?.e.. ?
#             row_c__.f..
#             __ row:
#                 ?.lEEA__.sT.. r.. 0
#                 ?.lEP__.sT.. r.. 1
#         _____ E.. __ e
#             ?.lR___.sT.. "Error in accessing table"
#
#
#     ___ ShowPreviousRow
#         g.. r..
#         rowNo -_ 1
#         sqlStatement_"S.. EA.., P.. F.. U.. w.. rowid="+st. rN..
#         c__.e.. s..
#         row_c__.f..
#         __ r..
#             ?.lR___.sT.. ""
#             ?.lEEA__.sT.. r.. 0
#             ?.lEP__.sT.. .. 1
#         ____
#             rN. +_ 1
#             ?.lR___.sT.. "This is the first row"
#
#
#     ___ ShowNextRow
#         g.. rowNo
#         rowNo +_ 1
#         sqlStatement_"S.. EA.. P.. F.. U.. w.. rowid="+st. rN.
#         c__.e.. ?
#         row_c__.f..
#         __ ?
#             ?.lR___.sT.. ""
#             ?.lEEA__.sT.. r.. 0
#             ?.lEP__.sT.. r.. 1
#         ____
#             rN. -_ 1
#             ?.lR___.sT.. "This is the last row"
#
#     ___ ShowLastRow
#         c__.e.. s..
#         ___ row __ c__.f..
#             ?.lEEA__.sT.. r.. 0
#             ?.lEP__.sT.. r.. 1
#
#
# __ _ ____ __ _____
#     app _ ?A..
#     w _ ?
#     ?.s..
#     ___.e.. ?.e
