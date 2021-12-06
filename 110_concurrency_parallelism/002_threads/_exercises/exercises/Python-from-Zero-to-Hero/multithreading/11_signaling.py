# _______ r__
# _______ _
# _______ t___
# ____ e.. _______ E..
#
#
# c_ Event
#     ___  -
#         __handlers _ # List
#
#     ___ -c.. $ $$
#         ___ f __ ?
#             ? $ $$
#
#     ___ -i.. handler
#         ?.a.. ?
#         r_
#
#     ___ -i.. handler
#         ?.r.. ?
#         r_
#
#
# c_ O__ E..
#     FINISHED = 0
#     FAULTED = 1
#
#
# c_ Protocol
#
#     ___ -  ip_address
#         ? = ?
#         ? = ?
#
#         message_received = ?
#
#         s..
#
#     ___ set_ip_port
#         # calling 3rd party lib passing port and ip
#         print('set ip and port once')
#         t___.s.. 0.2
#         r_
#
#     ___ send op_code param
#         ___ process_sending
#             print _* Operation is in action with param= ?
#             result = p.. ? ?
#             m.. ?
#
#         t = _.T.. t.._?
#         ?>.s..
#
#     ___ process op_code param
#         print _*processing operation= ? with param= ?
#         t___.s.. 3
#
#         # 3rd party lib response:
#         finished = r__.r..(0, 1) __ 1
#         r_ O__.F.. __ ? ____ O__.F...
#
#
#
# c_ BankTerminal
#     ___ - port ip_address
#         ? = ?
#         ? = ?
#         protocol = ? ? ?
#         ?.m.. += o..
#
#         operation_signal = _.E..
#
#     ___ on_message_received status
#         print _*Signaling for event: ?
#         o__.s..
#
#     ___ purchase amount
#         ___ process_purchase
#             purchase_op_code = 1
#             p__.s.. ? ?
#
#             o__.c..
#             print('\nWaiting for signal')
#             o__.w..
#             print('Purchase finished')
#
#         t = _.T..(t.._p..
#         ?.s..
#
#         r_ t
#
#
# __ _____ __ _____
#     bt = ? 10, '192.168.0.1')
#     t = ?.p.. 20
#     print('Main decided to wait for purchase 1')
#     ?.j...
#     t = ?.p.. 30
#     print('Main decided to wait for purchase 2')
#     ?.j...
#     print('End of Main')
