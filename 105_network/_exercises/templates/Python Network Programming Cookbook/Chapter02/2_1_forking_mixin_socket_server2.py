# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 2
# # This program is optimized for Python 3.5.2.
# # It may run on any other version with/without modifications.
# #
# # Need some modifications to make it run on Python 2.7.x:
# # For the start, replace "socketserver" with "SocketServer" throughout the program.
# # Progress accordingly addressing the API changes between the versions.
# #
# # See more: http://docs.python.org/2/library/socketserver.html
# # See more: http://docs.python.org/3/library/socketserver.html
#
# ______ __
# ______ ?
# ______ th..
# ______ s_s
#
#
# SERVER_HOST _ 'localhost'
# SERVER_PORT _ 0 # tells the kernel to pickup a port dynamically
# BUF_SIZE _ 1024
# ECHO_MSG _ 'Hello echo server!'
#
#
# c_ ForkedClient
#     """ A client to test forking server"""
#     ___ -  ip port
#         # Create a socket
#         sock _ ?.? ?.A.. ?.S..
#         # Connect to the server
#         ?.c.. ? ?
#
#     ___ run
#         """ Client playing with the server"""
#         # Send the data to server
#         current_process_id _ __.g_p..
#         print ('PID @ Sending echo message to the server : "@"' ? E..
#
#         sent_data_length _ ?.s.. by.. E.. 'utf-8'
#
#         print ("Sent: d characters, so far..." ?
#
#         # Display server response
#         response _ ?.r.. B..
#         print ("PID @ received: @"  c_p_i. ? 5;
#
#     ___ shutdown
#         """ Cleanup the client socket """
#         ?.c..
#
#
# c_ FSRH.. ?.BRH..
#     ___ handle
#         # Send the echo back to the client
#
#         #received = st..(sock.recv(1024), "utf-8")
#         data _ st.. r__.r.. B.. 'utf-8'
#
#         current_process_id _ __.g_p..
#         response _ '@: @'  c_p_i. d..
#         print ("Server sending response [current_process_id: data] = [@]" ?
#         r__.s.. by.. ? 'utf-8'
#         r_
#
#
# c_ ForkingServer(?.FMI..
#                     ?.T_S..
#
#     """Nothing to add here, inherited everything necessary from parents"""
#     p..
#
#
# ___ main
#     # Launch the server
#     server _ ? S_H.. S_P.. FSRH..
#     ip, port _ ?.s_a.. # Retrieve the port number
#     server_thread _ ?.T.. t_s_.s_f..
#     ?.sD. T.. # don't hang on exit
#     ?.s..
#     print ('Server loop running PID: @' __.g_p..
#
#     # Launch the client(s)
#
#     client1 _  ? ip port
#     ?.r..
#
#     print("First client running")
#
#     client2 _  ? ip port
#     ?.r..
#
#     print("Second client running")
#
#     # Clean them up
#     ?.s..
#     _1.s..
#     _2.s..
#     ?.?.c..
#
#
# __ _______ __ ______
#     ?
