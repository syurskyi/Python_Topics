# ____ ?.?W.. ______ _
# ____ ?.?G.. ______ ?KS.. ?P.., ?C..
# ____ ?.?C.. ______ __
#
# app _ ?
#
# # Force the style to be the same on all OSs:
# app.setStyle("Fusion")
#
# # Now use a palette to switch to dark colors:
# palette _ ?P..()
# ?.sC.. ?P...Window, ?C.. 53, 53, 53
# ?.sC.. ?P...WT.. __.wh..
# ?.sC.. ?P...B.. ?C.. 25, 25, 25
# ?.sC.. ?P...AB.. ?C.. 53, 53, 53
# ?.sC.. ?P...TTB.. __.wh..
# ?.sC.. ?P...TTT.. __.wh..
# ?.sC.. ?P...T.. __.wh..
# ?.sC.. ?P...B.. ?C.. 53, 53, 53
# ?.sC.. ?P...BT.. __.wh..
# ?.sC.. ?P...BT.. __.re..
# ?.sC.. ?P...L.. ?C.. 42, 130, 218
# ?.sC.. ?P...Hi.. ?C.. 42, 130, 218
# ?.sC.. ?P...HT.. __.bl..
# ?.sP.. ?
#
# # The rest of the code is the same as for the "normal" text editor.
#
# ?.sAN.. Text Editor
#
# text _ ?PTE..
#
# c_ MainWindow ?MW..
#     ___ closeEvent  e
#         __ no. t__.do__ .iM..
#             r_
#         answer _ ?MB...q..
#             w.. N..
#             "You have unsaved changes. Save before closing?",
#             ?MB...S.. _ ?MB...D.. _ ?MB...C..
#
#         __ ? & ?MB...S..
#             sa..
#         ____ ? & ?MB...C..
#             ?.i..
#
# window _ ?
# ?.sCW.. ?
#
# file_path _ N..
#
# menu _ window.mB.. .aM.. &File
# open_action _ ?A.. &Open
# ___ o_f..
#     gl.. f_p..
#     path _ ?FD...gOFN.. w.. Open 0
#     __ ?
#         t__.sPT.. o.. ? .r..
#         file_path _ ?
# o_a_.t__.c.. o_f..
# o_a_.sS.. ?KS...O..
# m__.aA.. o_a..
#
# save_action _ ?A.. &Save
# ___ sa..
#     __ file_path __ N..
#         s_a.
#     ____
#         w__ o.. f_p.. _  __ f
#             f.w.. t__.tPT..
#         t__.d__ .sM.. F..
# s_a_.t__.c.. s..
# s_a_.sS.. ?KS...S..
# m__.aA.. s_a..
#
# save_as_action _ ?A.. Save &As...
# ___ save_as
#     gl.. f_p..
#     path _ ?FD...gSFN.. w.. Save As 0
#     __ ?
#         file_path _ ?
#         sa..
# s_a__a_.t__.c.. s_a.
# m__.aA.. s_a_a..
#
# close _ ?A.. &Close
# ?.t__.c.. w__.cl..
# m__.aA.. ?
#
# help_menu _ w__.mB.. .aM.. &Help
# about_action _ ?A.. &About
# h__.aA.. a_a..
# ___ show_about_dialog
#     text _ "<center>" \
#            "<h1>Text Editor</h1>" \
#            "&#8291;" \
#            "<img src=icon.svg>" \
#            "</center>" \
#            "<p>Version 31.4.159.265358<br/>" \
#            "Copyright &copy; Company Inc.</p>"
#     ?MB...ab.. w.. About Text Editor ?
# a_a_.t__.c.. ?
#
# w__.s..
# ?.e..