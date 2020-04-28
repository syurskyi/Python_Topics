#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


______ ?
______ __
______ t__

SERVER_PATH _ "/tmp/python_unix_socket_server"
 
___ run_unix_domain_socket_server
    __ __.path.exists(SERVER_PATH):
        __.r..( SERVER_PATH )
     
    print ("starting unix domain socket server.")
    server _ ?.?( ?.AF_UNIX, ?.S_D.. )
    server.b..(SERVER_PATH)
     
    print ("Listening on path: @" SERVER_PATH)
    w__ T..:
        datagram _ server.r..( 1024 )
        __ not datagram:
            b..
        ____
            print ("-" * 20)
            print (datagram)
        __ "DONE" __ datagram:
            b..
    print ("-" * 20)
    print ("Server is shutting down now...")
    server.c..
    __.r..(SERVER_PATH)
    print ("Server shutdown and path removed.")

__ _______ __ ______
    run_unix_domain_socket_server()
