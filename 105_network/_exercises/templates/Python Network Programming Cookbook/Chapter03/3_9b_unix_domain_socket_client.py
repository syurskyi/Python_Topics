#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 3.5.2.
# It may run on any other version with/without modifications.
# To make it run on Python 2.7.x, needs some changes due to API differences.
# Follow the comments inline to make the program work with Python 2.


______ ?
______ ___

SERVER_PATH _ "/tmp/python_unix_socket_server"

___ run_unix_domain_socket_client
    """ Run "a Unix domain socket client """
    sock _ ?.?(?.AF_UNIX, ?.S_D..)
    
    # Connect the socket to the path where the server is listening
    server_address _ SERVER_PATH
    print ("connecting to @"  server_address)
    ___
        sock.c..(server_address)
    ______ ?.e.. __ msg:
        print (msg)
        ___.e..(1)
    
    ___
        message _ "This is the message.  This will be echoed back!"
        print  ("Sending [@]" message)

        sock.s_a..(by..(message, 'utf-8'))
        # Comment out the above line and uncomment the below line for Python 2.7.
        # sock.sendall(message)

        amount_received _ 0
        amount_expected _ le.(message)
        
        w__ amount_received < amount_expected:
            data _ sock.r..(16)
            amount_received +_ le.(data)
            print ("Received [@]"  data)
    
    f..
        print ("Closing client")
        sock.c..

__ _______ __ ______
    run_unix_domain_socket_client()
