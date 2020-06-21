# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 6
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
#
# ____ g_p_ ______ g_p_
# ____ fabric.api ______ local  run  env  get  put  p..  open_shell
#
# ___ remote_server
#     e__.h.. _ ['127.0.0.1']
#     e__.p.. _ g_p_('Enter your system password: ')
#     e__.h_f.. _ '/tmp'
#
# ___ login
#     o_s.. c.._"cd @" e__.h_f..
#
#
# ___ download_file
#     print ("Checking local disk space...")
#     l.. "df -h"
#     remote_path _ p..("Enter the remote file path:")
#     local_path _ p..("Enter the local file path:")
#     g.. r.._r..  l.._l..
#     lo.. "ls @" l..
#
#
# ___ upload_file
#     print ("Checking remote disk space...")
#     r.. "df -h"
#     local_path _ p..("Enter the local file path:")
#     remote_path _ p..("Enter the remote file path:")
#     p.. r.._r.. l.._l..
#     run("ls @" r..
#
#
