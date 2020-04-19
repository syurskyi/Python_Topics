# # signal_threads.py
#
# ______ s..
# ______ th..
# ______ __
# ______ ti..
#
#
# ___ signal_handler num stack
#     print('Received signal @ in @'.f.. |
#         ? ?.cT__ .n..
#
#
# s__.s__(s__.S_1 ?
#
#
# ___ wait_for_signal
#     print('Waiting for signal in',
#           ?.cT.. .n..
#     s__.pa..
#     print('Done waiting')
#
#
# # Start a thread that will not receive the signal
# receiver _ ?.T..|
#     t.._w..
#     n.._'receiver',
# )
# ?.st..
# t__.sl.. 0.1
#
#
# ___ send_signal
#     print('Sending s__ in', ?.cT.. .n..
#     __.k.. __.g_p.. s__.S_1
#
#
# sender _ ?.T.. t.._s.. name_'sender'
# ?.st..
# ?.jo..
#
# # Wait for the thread to see the signal (not going to happen!)
# print('Waiting for', r__.n..
# s__.al.. 2
# r__.j..
#
# # $ python3 signal_threads.py
# #
# # Waiting for signal in receiver
# # Sending signal in sender
# # Received signal 30 in MainThread
# # Waiting for receiver
# # Alarm clock

