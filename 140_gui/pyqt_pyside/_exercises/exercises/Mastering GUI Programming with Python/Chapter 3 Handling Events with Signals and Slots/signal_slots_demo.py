# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?C.. __ qtc
#
#
# c_ MainWindow ?.?W..
#
#     ___  -
#         s_. -
#         sL.. ?.?VBL..
#
#         # connecting a signal to a slot
#         quitbutton _ ?.?PB.. Quit
#         ?.c__.c.. cl..
#         la__ .aW.. ?
#
#         # connecting a signal with data to a slot that receives data
#         entry1 _ ?.?LE..
#         entry2 _ ?.?LE..
#         la__ .aW.. ?
#         la__ .aW.. ?
#         _1.tC...c.. _2.sT.
#
#         # connecting a signal to a python callable
#         _2.tC...c.. pr..
#
#         # Connecting a signal to another signal
#         _1.eF__.c.. l___ print editing finished
#         _2.rP__.c.. _1.eF__
#
#         # This call will fail, because the signals have different argument types
#         #self.entry1.textChanged.connect(self.quitbutton.clicked)
#
#         # This won't work, because of signal doesn't send enough args
#         badbutton _ ?.?PB.. Bad
#         la__ .aW.. ?
#         ?.c__.c.. n_a..
#
#         # This will work, even though the signal sends extra args
#         goodbutton _ ?.?PB.. Good
#         la__ .aW.. ?
#         ?.c__.c.. n_a..
#
#
#         s..
#
#     ___ needs_args  arg1, arg2, arg3
#         p..
#
#     ___ no_args
#         print('I need no arguments')
#
# __ ______ __ ______
#     app _ ?.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
