# ______ ___
# ____ os ______ pa__
#
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
#
#
# c_ MainWindow ?.?MW..
#
#     ___  -
#         """MainWindow constructor.
#
#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         s_. -
#         # Main UI code goes here
#
#         form _ ?.?W..
#         sCW.. ?
#         form.sL.. ?.?VBL..
#         filename _ ?.?LE..
#         filecontent _ ?.?TE..
#         savebutton _ ?.?PB..
#             'Save'
#             c___s.s..
#         )
#
#         f__.la__ .aW.. f..
#         f__.la__ .aW.. f..
#         f__.la__ .aW.. s..
#
#         # End main UI code
#         s..
#
#     ___ save
#         filename _ ?.t__
#         error _ ''
#         __ no. ?
#             error _ 'Filename empty'
#         ____ pa__.e.. ?
#             error _ _*Will not overwrite ?
#         ____
#             ___
#                 w__ o.. ? _ __ fh
#                     ?.w.. f__.tPT..
#             _____ E.. __ e
#                 error _ _*Cannot write file: ?
#         __ ?
#             ?.?MB...c.. N.. 'Error' ?
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
