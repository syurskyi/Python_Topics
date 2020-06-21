# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
#
#
# c_ AutoCloseDialog ?.QDialog
#
#     ___  -   parent title message timeout
#         s_. - ?
#         setModal F..
#         sWT.. t..
#         sL.. ?.?VBL..
#         la__ .aW..(?.?L.. m..
#         timeout _ timeout
#
#     ___ show
#         s_.s..
#         # Wrong:
#         #from time import sleep
#         #sleep(self.timeout)
#         #self.hide()
#         # Right:
#         ?.?T...sS.. t.. * 1000 h..
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
#         # Using a singleshot timer
#         dialog _ ?
#
#             "Self-destructing message"
#             "This message will self-destruct in 10 seconds"
#             10
#
#         ?.s..
#
#
#         # Using an interval timer
#         interval_seconds _ 10
#         timer _ ?.?T..
#         ?.sI.. ? * 1000
#
#         interval_dialog _ ?
#              "It's time again",
#             _*It has been |?| seconds
#             "since this dialog was last shown.", 2000
#         t__.t__.c.. ?.s..
#         t__.s..
#         toolbar _ aTB.. 'Tools'
#         ?.aA.. 'Stop Bugging Me', t__.s..
#         ?.aA.. 'Start Bugging Me', t__.s..
#
#         # Getting data from a timer
#         timer2 _ ?.?T..
#         ?.sI.. 1000
#         ?.t__.c.. u_s..
#         ?.s..
#         #self.show()
#         #return
#
#         # Does a blocking call in a timer block the UI?
#
#         # create timer
#         #qtc.QTimer.singleShot(1, self.long_blocking_callback)
#         # Yes, yes it does.
#
#         # End main UI code
#
#         s..
#
#     ___ update_status
#         __ t__.iA..
#             time_left _ t__.rT.. // 1000) + 1
#             sB.. .sM..
#                 _*Next dialog will be shown in |? seconds.")
#         ____
#             sB.. .sM.. 'Dialogs are off.'
#
#     ___ long_blocking_callback
#         ____ time ______ sl..
#         sB.. .sM.. 'Beginning a long blocking function.'
#         sl.. 30
#         sB.. .sM..('Ending a long blocking function.')
#
# __ ______ __ ______
#     app _ ?.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
