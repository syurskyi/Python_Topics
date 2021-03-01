# # genevents.py
# #
# # A very simplistic example of generating events on a set of sockets
#
# ______ select
# ___ gen_events socks
#     w____ T..
#         rdr,wrt,err _ ?.s.. ? ? ? 0.1
# # r
#         ___ ? __ ?
#             y... *read ?
# # Another
#         ___ ? __ ?
#             y... *write ?
# #  Another
#         ___ ? __ ?
#             y... *error ?
#
# # Example use
# # Use telnet to port 12000 to test this
#
# __ __name__ __ '__main__':
#     ______ s__
#     f.. genreceive ______ _
#
#     addr _ ("",12000)
#     clientset _  # list
#     ___ acceptor soc.. a..
#         ___ c,a __ receive_connections a..
#             ?.ap.. ?
#
#     ______ t___
#     acc_thr _ t___.T...(t.._acceptor,
#                                args _ (c.. a..
#     ?.d.. _ T..
#     ?.s..
#
#     ___ evt, s __ ? cl..
#         __ ? __ 'read'
#             data _ ?.r.. 1024
#             __ no. ?
#                 print("Closing" ?
#                 ?.c..
#                 cl__.r.. ?
#             ____
#                 print ? ?
#
#
#
#
