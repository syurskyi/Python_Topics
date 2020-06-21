# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 6
# # This program is optimized for Python 3.5.2.
# # It may run on any other version with/without modifications.
# # To make it run on Python 2.7.x, needs some changes due to API differences.
# # Follow the comments inline to make the program work with Python 2.
#
#
# ______ a_p..
# ______ g_p_
# ______ pa..
#
# RECV_BYTES _ 4096
# COMMAND _ 'cat /proc/cpuinfo'
#
# ___ print_remote_cpu_info hostname  port  username password
#     client _ ?.T.. ? ?
#     ?.c.. u.._u..  p.._p..
#
#     stdout_data _ # list
#     stderr_data _ # list
#     session _ c__.o_c.. k.._'session'
#     ?.e_c.. C..
#     w__ T..
#         __ ?.r_r..
#             s_d_.ap.. ?.r.. R..
#         __ ?.r_s_r..
#             s_d_.ap.. ?.r_s.. R..
#         __ ?.e_s_r..
#             b..
#
#     print ('exit status: ' ?.r_e_s..
#     print _''.j.. s_d..
#     print _''.j.. s_d..
#
#     ?.c..
#     c__.c..
#
# __ _______ __ ______
#     parser _ ?.AP..(d.._'Remote file copy')
#     ?.a_a..('--host'  a.._"store"  d.._"host"  d.._'localhost')
#     ?.a_a..('--port'  a.._"store"  d.._"port"  d.._22  ty.._in.)
#     given_args _ ?.p_a..
#     hostname  port _  ?.h..  ?.p..
#
#     user _ in..("Enter your remote account: ")
#     # Comment out the above line and uncomment the below line for Python 2.7.
#     # user = raw_input("Enter your remote account: ")
#
#     password _ g_p_.g_p_("Enter password for @: " ?
#     ? h..  p..  u..  p..
#
