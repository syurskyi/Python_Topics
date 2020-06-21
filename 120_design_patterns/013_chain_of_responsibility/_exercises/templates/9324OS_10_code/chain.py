# c_ Event
#     ___ - name
#         ?  ?
#
#     ___ -s
#         r_ n..
#
# c_ Widget:
#     ___ - parent_N..
#         ?  ?
#
#     ___ handle event
#         handler _ 'handle_@'.f.. ?
#         __ ha..  ?
#             method _ g..  ?
#             ? ?
#         ____ parent
#             ?.h___ e..
#         ____ ha..  'handle_default'
#             h_d.. e..
#
# c_ MainWindow W..
#     ___ handle_close  event
#         print('MainWindow: @'.f.. ?
#
#     ___ handle_default  event
#         print('MainWindow Default: @'.f.. ?
#
# c_ SendDialog W..
#     ___ handle_paint  event
#         print('SendDialog: @'.f.. ?
#
# c_ MsgText W..
#     ___ handle_down  event
#         print('MsgText: @'.f.. ?
#
# ___ main(
#     mw _ M..
#     sd _ S..
#     msg _ M..
#
#     ___ e __ ('down', 'paint', 'unhandled', 'close')
#         evt _ E.. ?
#         print('\nSending event -@- to MainWindow'.f.. ?
#         m_.h.. ?
#         print('Sending event -@- to SendDialog'.f.. ?
#         s_.h.. ?
#         print('Sending event -@- to MsgText'.f.. ?
#         ms_.h.. ?
#
# __ _______ __ ______
#     ?
