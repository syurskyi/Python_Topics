# ______ ___
# ____ os ______ pa__
#
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
#
#
# c_ Model ?.?O..
#
#     error _ ?.pS.. st.
#
#     ___ save  filename content
#         print save_called
#         error _ ''
#         __ no. f..
#             error _ 'Filename empty'
#         ____ pa__.e.. f..
#             error _ _*Will not overwrite |f..
#         ____
#             ___
#                 w__ o.. f.. _ __ fh
#                     ?.w.. c..
#             _____ E.. __ e
#                 error _ _*Cannot write file: ?
#         __ ?
#             ?.e.. ?
#
#
# c_ View ?.?W..
#
#     submitted _ qtc.pS..(str, str)
#
#     ___  -
#         s_. -
#         sL.. ?.?VBL..
#         filename _ ?.?LE..
#         filecontent _ ?.?TE..
#         savebutton _ ?.?PB..
#             'Save',
#             c___self.s..
#         )
#         la__ .aW.. f..
#         la__ .aW.. f..
#         la__ .aW.. s..
#
#     ___ submit
#         filename _ ?.t__
#         filecontent _ ?.tPT..
#         s__.e.. ? ?
#
#     ___ show_error  error
#         ?.?MB...c.. N.. 'Error' ?
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
#         view _ ?
#         sCW.. ?
#
#         model _ ?
#
#         v__.s__.c.. m__.s..
#         m__.e__.c.. v__.s_e..
#
#         # End main UI code
#         s..
#
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
