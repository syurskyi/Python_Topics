#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 6
# This program is optimized for Python 3.5.2.
# It may run on any other version with/without modifications.
# To make it run on Python 2.7.x, needs some changes due to API differences.
# Follow the comments inline to make the program work with Python 2.


______ a_p..
______ paramiko
______ g_p_


SOURCE _ '6_2_copy_remote_file_over_sftp.py' 
DESTINATION _'/tmp/6_2_copy_remote_file_over_sftp.py '


___ copy_file(hostname, port, username, password, src, dst):
    client _ paramiko.SSHClient()
    client.load_system_host_keys()
    print (" Connecting to @ \n with username=@... \n" (hostname,username))
    t _ paramiko.Transport(hostname, port)
    t.c..(username_username,password_password)
    sftp _ paramiko.SFTPClient.from_transport(t)
    print ("Copying file: @ to path: @" (src, dst))
    sftp.put(src, dst)
    sftp.c..
    t.c..


__ _______ __ ______
    parser _ ?.AP..(d.._'Remote file copy')
    parser.a_a..('--host', a.._"store", d.._"host", d.._'localhost')
    parser.a_a..('--port', a.._"store", d.._"port", d.._22, ty.._in.)
    parser.a_a..('--src', a.._"store", d.._"src", d.._SOURCE)
    parser.a_a..('--dst', a.._"store", d.._"dst", d.._DESTINATION)
    
    given_args _ parser.parse_args()
    hostname, port _  ?.host, ?.port
    src, dst _ ?.src, ?.dst
    
    user _ input("Enter your remote account: ")
    # Comment out the above line and uncomment the below line for Python 2.7.
    # user = raw_input("Enter your remote account: ")

    password _ g_p_.g_p_("Enter password for @: " user)
    
    copy_file(hostname, port, user, password, src, dst)
