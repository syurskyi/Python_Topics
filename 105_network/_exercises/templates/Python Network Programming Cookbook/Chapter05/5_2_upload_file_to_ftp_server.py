#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ __
______ a_p..
______ ftplib
______ getpass 

LOCAL_FTP_SERVER _ 'localhost'
LOCAL_FILE _ 'readme.txt'

___ ftp_upload(ftp_server, username, password, file_name):
    print ("Connecting to FTP server: @" ftp_server)
    ftp _ ftplib.FTP(ftp_server)
    print ("Login to FTP server: user=@" username)
    ftp.login(username, password)
    ext _ __.pa__.splitext(file_name)[1]
    __ ext __ (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file_name, open(file_name))
    ____
        ftp.storbinary("STOR " + file_name, open(file_name, "rb"), 1024)
    print ("Uploaded file: @" file_name)


__ _______ __ ______
    parser _ ?.AP..(d.._'FTP Server Upload Example')
    ?.a_a..('--ftp-server', a.._"store", d.._"ftp_server", default_LOCAL_FTP_SERVER)
    ?.a_a..('--file-name', a.._"store", d.._"file_name", default_LOCAL_FILE)
    ?.a_a..('--username', a.._"store", d.._"username", default_getpass.getuser())
    given_args _ ?.parse_args()
    ftp_server, file_name, username _ ?.ftp_server, ?.file_name, ?.username
    password _ getpass.getpass(prompt_"Enter you FTP password: ")
    ftp_upload(ftp_server, username, password, file_name)

