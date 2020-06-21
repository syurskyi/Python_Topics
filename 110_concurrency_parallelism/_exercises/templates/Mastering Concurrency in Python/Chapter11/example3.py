# # ch11/example3.py
#
# ______ a..
#
# c_ EchoServerClientProtocol ?.P..
#     ___ connection_made transport
#         peername _ ?.g_e_i..('peername')
#         print('Connection from @'.f.. ?
#         ? ?
#
#     ___ data_received data
#         message _ data.d..
#         print('Data received: @'.f.. ?
#
#         t__.w.. 'Echoed back: @'.f.. ? .e..
#
#         print('Close the client socket')
#         t__.c..
#
# loop _ ?.g_e_l..
# coro _ ?.c_s..(?, '127.0.0.1' 8888
# server _ l__.r_u_c.. ?
#
# # Serve requests until Ctrl+C is pressed
# print('Serving on @'.f.. s__.s.. 0 .g_s_n..
# ___
#     l__.r_f..
# ______ K..
#     p..
#
# # Close the server
# s__.c..
# l__.r_u_c.. s__.w_c..
# l__.c..
