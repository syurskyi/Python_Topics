#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


FTP_SERVER_URL _ 'ftp.ed.ac.uk'

______ ftplib
____ ftplib ______ FTP

___ test_ftp_connection(path, username, email):
    #Open ftp connection
    ftp _ ftplib.FTP(path, username, email)
    
   #List the files in the /pub directory
    ftp.cwd("/pub")
    print ("File list at @:" path)
    files _ ftp.dir()
    print (files)

    ftp.quit()

__ _______ __ ______
    test_ftp_connection(path_FTP_SERVER_URL, username_'anonymous', 
                        email_'nobody@nourl.com', 
                        )
