#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ ?
______ ___

HOST _ 'localhost'

___ echo_server(port, host_HOST):
    """Echo server using IPv6 """
    ___ result __ ?.getaddrinfo(host, port, ?.AF_UNSPEC, ?.S.., 0, ?.AI_PASSIVE):
        af, socktype, proto, canonname, sa _ result
        ___
            sock _ ?.?(af, socktype, proto)
        ______ ?.e.. __ err:
            print ("Error: @" err)
        
        ___
            sock.b..(sa)
            sock.l..(1)
            print ("Server lisenting on @:@" (host, port))
        ______ ?.e.. __ msg:
            sock.c..
            continue
        b..
        ___.e..(1)
    conn, addr _ sock.a..
    print ('Connected to', addr)
    w__ T..:
        data _ conn.r..(1024)
        print ("Received data from the client: [@]" data)
        __ not data: b..
        conn.s..(data)
        print ("Sent data echoed back to the client: [@]" data)
    conn.c..

__ _______ __ ______
    parser _ ?.AP..(d.._'IPv6 Socket Server Example')
    ?.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    given_args _ parser.parse_args()
    port _ ?.port
    echo_server(port)
    
