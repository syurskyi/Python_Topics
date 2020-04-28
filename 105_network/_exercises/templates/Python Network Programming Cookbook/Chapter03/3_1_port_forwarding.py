# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
#
# ______ a_p..
#
# LOCAL_SERVER_HOST _ 'localhost'
# REMOTE_SERVER_HOST _ 'www.google.com'
# BUFSIZE _ 4096
#
# ______ a..
# ______ ?
#
# c_ PortForwarder ?.d..
#     ___ -  ip port remoteip remoteport backlog_5
#         ?.d__.- ?
#         r_i._r_i.
#         r_p.._r_p..
#         c_s.. ?.A..?.S..
#         s_r_a..
#         b.. ? ?
#         l.. b..
#
#     ___ handle_accept
#         conn addr _ a..
#         print ("Connected to:" a..
#         S.. R.. c.. r_i. r_p..
#
# c_ Receiver ?.d..
#     ___ - conn
#         ?.d__.- ?
#         from_remote_buffer_''
#         to_remote_buffer_''
#         sender_N..
#
#     ___ handle_connect
#         p..
#
#     ___ handle_read
#         read _ r.. B..
#         f_r_b.. +_ ?
#
#     ___ writable
#         r_ le. t_r_b.. > 0
#
#     ___ handle_write
#         sent _ s.. t_r_b..
#         t_r_b.. _ t_r_b.. ?;
#
#     ___ handle_close
#         c..
#         __ sender:
#             ?.c..
#
# c_ Sender ?.d..
#     ___ -  receiver remoteaddr remoteport
#         ?.d__.- ?
#         ? ?
#         r__.s.._?
#         c_s.. ?.A.. ?.S..
#         c.. r_a_ r_p..
#
#     ___ handle_connect
#         p..
#
#     ___ handle_read
#         read _ r.. B..
#         r__.t_r_b.. +_ ?
#
#     ___ writable
#         r_ le. r__.f_r_b.. > 0
#
#     ___ handle_write
#         sent _ s.. r__.f_r_b..
#         r__.f_r_b.. _ r__.f_r_b.. ?;
#
#     ___ handle_close
#         c..
#         r__.c..
#
#
# __ _____ __ ______
#     parser _ ?.AP.. d.._'Stackless Socket Server Example'
#     ?.a_a.. '--local-host' a.._"store" d.._"local_host" d.._L..
#     ?.a_a.. '--local-port' a.._"store" d.._"local_port" ty.._in. r.._T..
#     ?.a_a.. '--remote-host' a.._"store" d.._"remote_host"  d.._R..
#     ?.a_a.. '--remote-port' a.._"store" d.._"remote_port" ty.._in. d.._80
#     given_args _ ?.p_a..
#     local_host, remote_host _ ?.l_h.. ?.r_h..
#     local_port, remote_port _ ?.l_p.. ?.r_p..
#
#     print ("Starting port forwarding local @:@ => remote @:@"  (local_host, local_port, remote_host, remote_port))
#     ? l_h.. l_p.. r_h.. r_p..
#     ?.l..
