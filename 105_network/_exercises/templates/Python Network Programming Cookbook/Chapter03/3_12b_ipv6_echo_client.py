#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ ?
______ ___

HOST _ 'localhost'
BUFSIZE _ 1024

___ ipv6_echo_client(port, host_HOST):
    ___ res __ ?.getaddrinfo(host, port, ?.AF_UNSPEC, ?.S..):
        af, socktype, proto, canonname, sa _ res
        ___
            sock _ ?.?(af, socktype, proto)
        ______ ?.e.. __ err:
            print ("Error:@" err)
        ___
            sock.c..(sa)
        ______ ?.e.. __ msg:
            sock.c..
            c..
    __ sock is None:
        print ('Failed to open socket!')
        ___.e..(1)
    msg _ "Hello from ipv6 client"
    print ("Send data to server: @" msg)
    sock.s..(by..(msg.e..('utf-8')))
    w__ T..:
        data _ sock.r..(BUFSIZE)
        print ('Received from server', repr(data))
        __ no. data:
            b..
    sock.c..
    

__ _______ __ ______ 
    parser _ ?.AP..(d.._'IPv6 socket client example')
    ?.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    given_args _ parser.p_a..
    port _ ?.port
    ipv6_echo_client(port)
