# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
#
#
# c_ InventoryNumberValidator ?.?V..
#     """Validates an inventory number in the format XX-999-9999X
#
#     X is an uppercase letter from A to Z excluding O and I.
#     9 is any digit from 0 to 9.
#     """
#
#     valid_letters _ 'ABCDEFGHJKLMNPQRSTUVWXYZ'
#     ___ validate  string index
#         # one approach is to break the string into segments
#         # and test each segment for proper content
#         state _ ?.?V...A..
#         seg1 _ st.. 0 2
#         dash1 _ st.. 2 3
#         seg2 _ st.. 3 6
#         dash2 _ st.. 6 7
#         seg3 _ st.. 7 11
#         seg4 _ st.. 11 12
#
#         __ no. al. char __ v_l.. ___ ch.. __ _1 + _4
#             state _ ?.?V...I..
#         ____ no. al. ch__.i_d.. ___ ch.. __ _2 + _3
#             state _ ?.?V...I..
#         ____ no. al. ch.. __ '-' ___ ch.. __ d_1 + d_2
#             state _ ?.?V...I..
#         ____ le. st.. > 12
#             state _ ?.?V...I..
#         ____ no. al. _1 _1 _2, _2, _3 _4
#             state _ ?.?V...I..
#
#         r_  s.. s.. i..
#
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
#         inventory_number _ ?.?LE..
#         ?.sV.. INV..
#         l__.aW.. ?
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
