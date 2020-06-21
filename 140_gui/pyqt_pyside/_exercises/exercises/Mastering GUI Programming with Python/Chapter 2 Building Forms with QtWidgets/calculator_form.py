# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
#
# c_ MainWindow ?.?W..
#
#     ___  -
#         """MainWindow constructor.
#
#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         s_. -
#         # Main UI code goes here
#         sL.. ?.?VBL..
#         lcd _ ?.?LCDN..
#         la__ .aW.. ?
#
#         history _ ?.?LE..  placeholderText_'History'
#         la__ .aW.. ?
#
#         button_texts _ [
#             'Clear', 'BackSpace', 'Mem', 'Mem Clear',
#             '1', '2', '3', '+',
#             '4', '5', '6', '-',
#             '7', '8', '9', '×',
#             '.', '0', '=', '÷'
#         ]
#         button_layout _ ?.?GL..
#         la__ .aL.. ?
#         buttons _   # list
#         ___ num, button_text __ en.. b_t..
#             button _ ?.?PB.. b_t..
#             ?.sSP.. ?.?SP__.E.. ?.?SP__.E..
#             ?.ap.. ?
#             row _ n.. // 4
#             column _ n.. % 4
#             b_l__.aW.. ? ? ?
#         # End main UI code
#         s..
#
#
# __ ______ __ ______
#     app _ ?.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
