# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 5
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ __
# ______ a_p..
# ______ ft..
# ______ getpass
#
# LOCAL_FTP_SERVER _ 'localhost'
# LOCAL_FILE _ 'readme.txt'
#
# ___ ftp_upload ftp_server username password file_name
#     print ("Connecting to FTP server: @" ?
#     ftp _ ?.F.. ?
#     print ("Login to FTP server: user=@" u..
#     ?.l.. u.. p..
#     ext _ __.pa__.s.. f_n.. 1
#     __ ? __ ".txt" ".htm" ".html"
#         ?.s_l.. "STOR " + f_n.. o.. f_n..
#     ____
#         ?.s_b..("STOR " + f_n.. o.. f_n.. __ 1024
#     print ("Uploaded file: @" f_n..
#
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'FTP Server Upload Example'
#     ?.a_a.. '--ftp-server' a.._"store" d.._"ftp_server" d.._L..
#     ?.a_a.. '--file-name' a.._"store" d.._"file_name" d.._L..
#     ?.a_a.. '--username' a.._"store" d.._"username" d.._g_p_.g_u..
#     given_args _ ?.p_a..
#     ftp_server f_n.. u.. _ ?.f_s.. ?.f_n.. ?.u..
#     password _ g_p_.g_p_ p.._"Enter you FTP password: "
#     ? f_s.. u.. p.. f_n..
#
